"""Tests for the reviewer module."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from code_review_pack.reviewer import (
    MAX_DIFF_SIZE,
    GitError,
    get_staged_diff,
    get_working_diff,
    load_checklists,
    load_overlay,
    review_code,
)


class TestGitDiffFunctions:
    """Tests for git diff functions."""

    def test_get_staged_diff_success(self) -> None:
        """Should return diff output on success."""
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = "diff --git a/file.py b/file.py\n+new line"

        with patch("code_review_pack.reviewer.subprocess.run", return_value=mock_result):
            result = get_staged_diff()
            assert result == mock_result.stdout

    def test_get_staged_diff_failure(self) -> None:
        """Should raise GitError on failure."""
        mock_result = MagicMock()
        mock_result.returncode = 1
        mock_result.stderr = "fatal: not a git repository"

        with patch("code_review_pack.reviewer.subprocess.run", return_value=mock_result):
            with pytest.raises(GitError, match="git diff --cached failed"):
                get_staged_diff()

    def test_get_working_diff_success(self) -> None:
        """Should return diff output on success."""
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = "diff --git a/file.py b/file.py\n-old line"

        with patch("code_review_pack.reviewer.subprocess.run", return_value=mock_result):
            result = get_working_diff()
            assert result == mock_result.stdout

    def test_get_working_diff_failure(self) -> None:
        """Should raise GitError on failure."""
        mock_result = MagicMock()
        mock_result.returncode = 128
        mock_result.stderr = "error: something went wrong"

        with patch("code_review_pack.reviewer.subprocess.run", return_value=mock_result):
            with pytest.raises(GitError, match="git diff failed"):
                get_working_diff()


class TestLoadOverlay:
    """Tests for load_overlay function."""

    def test_load_existing_overlay(self, tmp_path: Path) -> None:
        """Should load overlay content when file exists."""
        overlay_content = "# Test Overlay\n\nThis is test content."
        overlay_file = tmp_path / "overlay.md"
        overlay_file.write_text(overlay_content, encoding="utf-8")

        result = load_overlay(tmp_path)
        assert result == overlay_content

    def test_load_missing_overlay(self, tmp_path: Path) -> None:
        """Should return empty string when overlay doesn't exist."""
        result = load_overlay(tmp_path)
        assert result == ""


class TestLoadChecklists:
    """Tests for load_checklists function."""

    def test_load_checklists(self, tmp_path: Path) -> None:
        """Should load all markdown checklists."""
        checklists_dir = tmp_path / "checklists"
        checklists_dir.mkdir()

        (checklists_dir / "security.md").write_text("# Security\n- Check 1", encoding="utf-8")
        (checklists_dir / "tests.md").write_text("# Tests\n- Check 2", encoding="utf-8")
        (checklists_dir / "not_a_checklist.txt").write_text("ignored", encoding="utf-8")

        result = load_checklists(tmp_path)

        assert "## security" in result
        assert "# Security" in result
        assert "## tests" in result
        assert "# Tests" in result
        assert "ignored" not in result

    def test_load_missing_checklists_dir(self, tmp_path: Path) -> None:
        """Should return empty string when checklists dir doesn't exist."""
        result = load_checklists(tmp_path)
        assert result == ""


class TestReviewCode:
    """Tests for review_code function."""

    def test_diff_size_limit(self) -> None:
        """Should raise ValueError when diff exceeds MAX_DIFF_SIZE."""
        large_diff = "x" * (MAX_DIFF_SIZE + 1)

        with pytest.raises(ValueError, match="Diff too large"):
            review_code(large_diff)

    def test_diff_at_limit(self) -> None:
        """Should accept diff exactly at MAX_DIFF_SIZE."""
        exact_diff = "x" * MAX_DIFF_SIZE

        # Mock the Anthropic client
        mock_message = MagicMock()
        mock_message.content = [MagicMock(text="Review result")]

        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_message

        with patch("code_review_pack.reviewer.Anthropic", return_value=mock_client):
            result = review_code(exact_diff)
            assert result == "Review result"

    def test_review_code_calls_api(self) -> None:
        """Should call Anthropic API with correct parameters."""
        diff = "diff --git a/test.py b/test.py\n+new code"
        overlay = "Test overlay"
        checklists = "Test checklists"

        mock_message = MagicMock()
        mock_message.content = [MagicMock(text="LGTM")]

        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_message

        with patch("code_review_pack.reviewer.Anthropic", return_value=mock_client):
            result = review_code(diff, overlay, checklists)

            # Verify API was called
            mock_client.messages.create.assert_called_once()
            call_kwargs = mock_client.messages.create.call_args.kwargs

            assert call_kwargs["model"] == "claude-opus-4-5-20250514"
            assert call_kwargs["max_tokens"] == 8192
            assert "timeout" in call_kwargs
            assert diff in call_kwargs["messages"][0]["content"]
            assert overlay in call_kwargs["messages"][0]["content"]
            assert checklists in call_kwargs["messages"][0]["content"]

            assert result == "LGTM"
