#!/usr/bin/env python3
"""CLI for code-review-pack."""

import shutil
from pathlib import Path

import click
import yaml
from rich.console import Console
from rich.prompt import Confirm, Prompt

console = Console()


def get_packs_dir() -> Path:
    """Get the packs directory, checking multiple possible locations."""
    # First, check if we're in a development environment (repo checkout)
    # Walk up from the module location to find packs/
    module_path = Path(__file__).resolve()
    for parent in module_path.parents:
        packs_candidate = parent / "packs"
        if packs_candidate.is_dir():
            return packs_candidate

    # Fallback: check relative to current working directory
    cwd_packs = Path.cwd() / "packs"
    if cwd_packs.is_dir():
        return cwd_packs

    # If not found, raise an error
    raise FileNotFoundError(
        "Could not find packs directory. "
        "Ensure you're running from the code-review-packs repository."
    )


@click.group()
@click.version_option()
def main() -> None:
    """Code Review Pack CLI."""
    pass


@main.command()
@click.option("--pack", "-p", help="Pack name to initialize")
@click.option("--target", "-t", default=".", help="Target directory")
def init(pack: str | None, target: str) -> None:
    """Initialize a code review pack in a project."""
    target_path = Path(target).resolve()

    if not target_path.exists():
        console.print(f"[red]Target directory does not exist: {target_path}[/red]")
        raise SystemExit(1)

    # Warn if target is outside current directory
    try:
        target_path.relative_to(Path.cwd())
    except ValueError:
        console.print(f"[yellow]Warning: Target is outside current directory: {target_path}[/yellow]")
        if not Confirm.ask("Continue anyway?", default=False):
            raise SystemExit(0)

    packs_dir = get_packs_dir()

    # List available packs (exclude hidden directories)
    available_packs = [
        p.name for p in packs_dir.iterdir() 
        if p.is_dir() and not p.name.startswith(".")
    ]

    if not pack:
        console.print("\n[bold]Available packs:[/bold]")
        for p in available_packs:
            console.print(f"  - {p}")

        pack = Prompt.ask("\nSelect pack", choices=available_packs)

    if pack not in available_packs:
        console.print(f"[red]Unknown pack: {pack}[/red]")
        raise SystemExit(1)

    pack_path = packs_dir / pack

    console.print(f"\n[bold]Initializing {pack} in {target_path}[/bold]\n")

    # Copy Windsurf config
    if Confirm.ask("Install Windsurf rules and workflows?", default=True):
        windsurf_src = pack_path / "windsurf"
        windsurf_dst = target_path / ".windsurf"

        if windsurf_src.exists():
            shutil.copytree(windsurf_src, windsurf_dst, dirs_exist_ok=True)
            console.print("[green]✓[/green] Installed .windsurf/rules/ and .windsurf/workflows/")

    # Copy Cursor config
    if Confirm.ask("Install Cursor rules?", default=True):
        cursor_src = pack_path / "cursor"

        if cursor_src.exists():
            cursorrules_file = cursor_src / "cursorrules"
            agents_file = cursor_src / "AGENTS.md"

            if cursorrules_file.exists():
                shutil.copy(cursorrules_file, target_path / ".cursorrules")
                console.print("[green]✓[/green] Installed .cursorrules")
            else:
                console.print("[yellow]![/yellow] cursorrules not found in pack")

            if agents_file.exists():
                shutil.copy(agents_file, target_path / "AGENTS.md")
                console.print("[green]✓[/green] Installed AGENTS.md")
            else:
                console.print("[yellow]![/yellow] AGENTS.md not found in pack")

    # Copy Claude config
    if Confirm.ask("Install Claude Code config?", default=True):
        claude_src = pack_path / "claude"

        if claude_src.exists():
            claude_md_file = claude_src / "CLAUDE.md"
            settings_file = claude_src / "settings.json"

            if claude_md_file.exists():
                shutil.copy(claude_md_file, target_path / "CLAUDE.md")
                console.print("[green]✓[/green] Installed CLAUDE.md")
            else:
                console.print("[yellow]![/yellow] CLAUDE.md not found in pack")

            if settings_file.exists():
                claude_dst = target_path / ".claude"
                claude_dst.mkdir(exist_ok=True)
                shutil.copy(settings_file, claude_dst / "settings.json")
                console.print("[green]✓[/green] Installed .claude/settings.json")
            else:
                console.print("[yellow]![/yellow] settings.json not found in pack")

    # Copy GitHub Action
    if Confirm.ask("Install GitHub Action for PR reviews?", default=True):
        gh_src = pack_path / "github" / "workflows"
        gh_scripts_src = pack_path / "github" / "scripts"
        gh_dst = target_path / ".github" / "workflows"
        gh_scripts_dst = target_path / ".github" / "scripts"

        if gh_src.exists():
            gh_dst.mkdir(parents=True, exist_ok=True)
            gh_scripts_dst.mkdir(parents=True, exist_ok=True)

            for f in gh_src.iterdir():
                shutil.copy(f, gh_dst / f.name)

            if gh_scripts_src.exists():
                for f in gh_scripts_src.iterdir():
                    shutil.copy(f, gh_scripts_dst / f.name)

            console.print("[green]✓[/green] Installed .github/workflows/ai-code-review.yml")
            console.print("[yellow]![/yellow] Remember to add ANTHROPIC_API_KEY to repository secrets")

    console.print("\n[bold green]Pack initialized successfully![/bold green]")
    console.print("\nNext steps:")
    console.print("  1. Review the installed configuration files")
    console.print("  2. Customize as needed for your project")
    console.print("  3. Add ANTHROPIC_API_KEY to GitHub secrets for CI reviews")


@main.command()
def list_packs() -> None:
    """List available packs."""
    packs_dir = get_packs_dir()

    console.print("\n[bold]Available Code Review Packs:[/bold]\n")

    for pack_dir in packs_dir.iterdir():
        if pack_dir.is_dir() and not pack_dir.name.startswith("."):
            pack_yaml = pack_dir / "pack.yaml"
            if pack_yaml.exists():
                with open(pack_yaml, encoding="utf-8") as f:
                    config = yaml.safe_load(f)

                name = config["pack"]["name"]
                desc = config["pack"]["description"]
                version = config["pack"]["version"]

                console.print(f"[bold]{name}[/bold] v{version}")
                console.print(f"  {desc}\n")


@main.command()
@click.option("--pack", "-p", default="python-azure-ai-agent", help="Pack to use for review context")
@click.option("--staged", is_flag=True, help="Review staged changes only")
def review(pack: str, staged: bool) -> None:
    """Run an AI code review on current changes."""
    # Lazy import to avoid loading anthropic SDK unless review command is used
    from code_review_pack.reviewer import (
        GitError,
        get_staged_diff,
        get_working_diff,
        load_checklists,
        load_overlay,
        review_code,
    )

    packs_dir = get_packs_dir()
    pack_path = packs_dir / pack

    if not pack_path.exists():
        console.print(f"[red]Pack not found: {pack}[/red]")
        raise SystemExit(1)

    console.print(f"\n[bold]Running code review with pack: {pack}[/bold]\n")

    # Get the diff
    try:
        if staged:
            diff = get_staged_diff()
            console.print("[dim]Reviewing staged changes...[/dim]\n")
        else:
            diff = get_working_diff()
            console.print("[dim]Reviewing working directory changes...[/dim]\n")
    except GitError as e:
        console.print(f"[red]Git error: {e}[/red]")
        raise SystemExit(1)

    if not diff.strip():
        console.print("[yellow]No changes to review.[/yellow]")
        return

    # Load pack context
    overlay = load_overlay(pack_path)
    checklists = load_checklists(pack_path)

    console.print("[dim]Sending to Claude for review...[/dim]\n")

    try:
        result = review_code(diff, overlay, checklists)
        console.print(result)
    except ImportError:
        console.print("[red]Error: anthropic package not installed.[/red]")
        console.print("Run: pip install anthropic")
        raise SystemExit(1)
    except ValueError as e:
        # Raised by reviewer.py for diff size limits
        console.print(f"[red]Validation error: {e}[/red]")
        raise SystemExit(1)
    except Exception as e:
        error_name = type(e).__name__
        if "AuthenticationError" in error_name:
            console.print("[red]Authentication failed. Check your ANTHROPIC_API_KEY.[/red]")
        elif "RateLimitError" in error_name:
            console.print("[red]Rate limit exceeded. Please wait and try again.[/red]")
        elif "APIError" in error_name:
            console.print(f"[red]API error: {e}[/red]")
        else:
            console.print(f"[red]Review failed ({error_name}): {e}[/red]")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
