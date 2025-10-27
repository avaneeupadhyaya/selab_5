# selab_5
SE Lab 5 — Static Code Analysis

Name: Avanee Upadhyaya
SRN: PES2UG23CS108
Overview

A Python Inventory Management System improved using static code analysis tools — Pylint, Flake8, and Bandit.
Focus: fixing code style, readability, and security issues.


Features

Add / remove items

Track and report stock

Save & load data from JSON

Check for low-stock items
Tools Used

 Pylint — Code quality

 Flake8 — PEP 8 checks

 Bandit — Security scan

 | Issue               | Tool   | Fix                            |
| ------------------- | ------ | ------------------------------ |
| Mutable default arg | Pylint | Replaced `logs=[]` with `None` |
| Bare `except`       | Bandit | Used `except KeyError`         |
| `eval()` usage      | Bandit | Removed unsafe eval            |
| Missing `with`      | Pylint | Used context managers          |
| Naming style        | Flake8 | Converted to `snake_case`      |
| Missing docs        | Pylint | Added docstrings               |


Result

 Pylint score: 4.80 → 9.64/10
 Improved readability, security, and maintainability

 Run
pylint inventory_system.py > pylint_report.txt
python inventory_system.py

Summary

Static analysis made the code cleaner, safer, and more professional — a solid example of quality improvement through automation.