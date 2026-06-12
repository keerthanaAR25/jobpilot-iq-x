#!/usr/bin/env python3
"""
Verify that all required packages are installed and importable.
Run this to troubleshoot missing dependencies.
"""

import sys
from pathlib import Path

# Color codes for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def check_import(module_name, package_name=None):
    """Try to import a module and report success/failure."""
    try:
        __import__(module_name)
        print(f"{GREEN}✓{RESET} {module_name}")
        return True
    except ImportError as e:
        print(f"{RED}✗{RESET} {module_name}: {e}")
        if package_name:
            print(f"  {YELLOW}→{RESET} Install with: pip install {package_name}")
        return False

print(f"\n{YELLOW}=== JobPilot IQ X - Dependency Checker ==={RESET}\n")

# List of all required packages
packages = [
    ("streamlit", "streamlit"),
    ("streamlit_extras", "streamlit-extras"),
    ("pandas", "pandas"),
    ("numpy", "numpy"),
    ("plotly", "plotly"),
    ("PyPDF2", "pypdf2"),
    ("pydantic", "pydantic"),
    ("dotenv", "python-dotenv"),
    ("requests", "requests"),
    ("openai", "openai"),
    ("json5", "json5"),
    ("sqlalchemy", "sqlalchemy"),
    ("typing_extensions", "typing-extensions"),
    ("sqlite3", None),  # Built-in, no pip install needed
]

results = []
for module, pip_name in packages:
    results.append(check_import(module, pip_name))

print(f"\n{YELLOW}=== Summary ==={RESET}\n")
passed = sum(results)
total = len(results)
print(f"Passed: {GREEN}{passed}/{total}{RESET}")

if passed == total:
    print(f"\n{GREEN}✓ All dependencies installed successfully!{RESET}\n")
    sys.exit(0)
else:
    print(f"\n{RED}✗ Some dependencies are missing.{RESET}")
    print(f"{YELLOW}Run: pip install -r requirements.txt{RESET}\n")
    sys.exit(1)
