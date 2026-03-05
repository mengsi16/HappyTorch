"""Prepare notebooks directory for HappyTorch practice.

This script creates the notebooks directory and copies templates/solutions.
Works on Windows, macOS, and Linux.
"""

import shutil
import sys
from pathlib import Path


def prepare_notebooks():
    """Create notebooks directory and copy templates/solutions."""
    root = Path(__file__).parent
    notebooks_dir = root / "notebooks"
    templates_dir = root / "templates"
    solutions_dir = root / "solutions"

    # Create notebooks directory
    notebooks_dir.mkdir(exist_ok=True)
    print(f"✓ Created directory: {notebooks_dir}")

    # Copy templates
    if templates_dir.exists():
        for file in templates_dir.glob("*.ipynb"):
            dest = notebooks_dir / file.name
            shutil.copy2(file, dest)
        print(f"✓ Copied templates to notebooks/")
    else:
        print(f"⚠ Templates directory not found: {templates_dir}")

    # Copy solutions
    if solutions_dir.exists():
        for file in solutions_dir.glob("*.ipynb"):
            dest = notebooks_dir / file.name
            shutil.copy2(file, dest)
        print(f"✓ Copied solutions to notebooks/")
    else:
        print(f"⚠ Solutions directory not found: {solutions_dir}")

    print("\n🎉 Notebooks ready! You can now start practicing.")


if __name__ == "__main__":
    prepare_notebooks()
