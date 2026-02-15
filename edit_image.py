"""
Section 9 — Advanced Extension: Image Editing

Demonstrates using client.images.edit() to modify an existing generated asset.
This example takes the hero image (outputs/hero.png) and transforms it into
a cyberpunk night version.

Prerequisites:
    Run generate_hero.py first to create outputs/hero.png.

Usage:
    python edit_image.py
"""

import base64
from pathlib import Path

from utils import client, save_image, OUTPUTS_DIR

EDIT_PROMPT = """
Transform this image into a cyberpunk night scene. Keep the same composition
and subjects, but change the lighting to neon magenta and cyan. Make it nighttime
with rain. Add holographic advertisements and glitch effects in the background.
The overall mood should shift from corporate daytime to Blade Runner night.
"""


def edit_hero_image():
    """Edit the existing hero image into a cyberpunk night version."""
    hero_path = OUTPUTS_DIR / "hero.png"

    if not hero_path.exists():
        print("  ERROR: outputs/hero.png not found.")
        print("  Run generate_hero.py first to create the base image.")
        return

    print("\n🌃 Editing hero image → cyberpunk night version...")

    # Read the existing hero image as bytes for the edit endpoint
    hero_bytes = hero_path.read_bytes()

    result = client.images.edit(
        model="gpt-image-1",
        image=hero_bytes,
        prompt=EDIT_PROMPT,
        size="1536x1024",
    )

    save_image(result.data[0].b64_json, "hero_cyberpunk.png")
    print("  Image editing complete. Compare hero.png and hero_cyberpunk.png")


if __name__ == "__main__":
    edit_hero_image()
