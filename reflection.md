# Lab 5 Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

**Easiest:**
- Adding blank lines between functions (E302, E305)
- Removing unused imports
- Renaming functions to snake_case
These were simple find-and-replace operations with no logic changes.

**Hardest:**
- **Mutable default argument (logs=[]):** Required understanding Python's object model and how default arguments are evaluated once at function definition, not at each call.
- **Refactoring file operations:** Needed to understand context managers and restructure code to use `with` statements properly.

## 2. Did the static analysis tools report any false positives?

No significant false positives were encountered. The `global` statement warning (W0603) could be considered debatable since it's sometimes necessary for simple scripts, but the warning is valid as it's generally better practice to avoid globals.

## 3. How would you integrate static analysis tools into your actual software development workflow?

**Local Development:**
- Run tools before each commit using pre-commit hooks
- Configure IDE to show warnings in real-time

**CI/CD Pipeline:**
- Add automated checks in GitHub Actions/GitLab CI
- Fail builds if critical issues are found (Bandit security issues)
- Generate reports for code review

**Example GitHub Actions workflow:**
```yaml
- name: Run Pylint
  run: pylint --fail-under=8.0 *.py
```

## 4. What tangible improvements did you observe in code quality, readability, or potential robustness?

**Security:** Eliminated 2 critical vulnerabilities (eval usage, bare except)
**Reliability:** Proper file handling with context managers prevents resource leaks
**Readability:** Consistent naming (snake_case), proper spacing, f-strings make code clearer
**Maintainability:** Docstrings help future developers understand function purposes
**Score:** Improved from 4.80/10 to 9.64/10 on Pylint

The code went from "potentially buggy and insecure" to "production-ready" quality.