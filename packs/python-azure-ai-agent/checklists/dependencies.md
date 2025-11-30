# Dependencies Checklist

## Necessity
- [ ] Is each new dependency truly necessary?
- [ ] Could standard library functionality be used instead?
- [ ] Is the dependency actively maintained?
- [ ] Is the dependency's scope appropriate (not bloated)?

## Security
- [ ] Are there known vulnerabilities in selected versions?
- [ ] Is the package source trusted (PyPI, not arbitrary URLs)?
- [ ] Are dependency hashes verified (if high security)?
- [ ] Is the dependency's security track record acceptable?

## Versioning
- [ ] Are version constraints appropriate (not too loose, not too tight)?
- [ ] Are breaking change risks understood?
- [ ] Is there a strategy for security updates?
- [ ] Are transitive dependencies considered?

## License Compliance
- [ ] Is the license compatible with project requirements?
- [ ] Are license obligations understood and met?
- [ ] Is license information documented?

## Operational Impact
- [ ] Does the dependency have reasonable performance?
- [ ] Are there deployment size implications?
- [ ] Is the dependency's error behavior understood?
- [ ] Are there platform compatibility concerns?
