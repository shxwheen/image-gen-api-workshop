"""
Section 8 — Run-All Script

Sequentially generates logo, hero image, and product mockup to simulate
the full "idea → visual startup in minutes" pipeline.

Usage:
    python build_startup_assets.py
"""

from generate_logo import generate_logo
from generate_hero import generate_hero
from generate_mockup import generate_mockup


def main():
    print("=" * 60)
    print("  LAUNCHPAD AI — Startup Asset Generator")
    print("  From idea to visual brand in one script.")
    print("=" * 60)

    generate_logo()
    generate_hero()
    generate_mockup()

    print("\n" + "=" * 60)
    print("  All assets generated! Check the outputs/ directory.")
    print("=" * 60)


if __name__ == "__main__":
    main()
