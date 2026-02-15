"""
Section 9 — Advanced Extension: Image Editing

Demonstrates using client.images.edit() to modify any existing image.
The script lists available images in outputs/ and lets you pick which one
to edit and what transformation to apply.

Usage:
    python edit_image.py
"""

import base64
from pathlib import Path

from utils import client, save_image, OUTPUTS_DIR


def get_available_images():
    """Return a sorted list of PNG images in the outputs directory."""
    return sorted(OUTPUTS_DIR.glob("*.png"))


def pick_image(images):
    """Prompt the user to choose an image from the list."""
    print("\nAvailable images:")
    for i, img in enumerate(images, 1):
        print(f"  {i}. {img.name}")

    while True:
        choice = input("\nSelect an image number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(images):
            return images[int(choice) - 1]
        print("  Invalid choice, try again.")


def get_edit_prompt():
    """Ask the user what transformation they want."""
    print("\nDescribe the edit you want to apply.")
    print("(e.g. 'Make it a watercolor painting', 'Change to night scene with neon lights')")
    prompt = input("\nEdit prompt: ").strip()
    if not prompt:
        print("  No prompt entered, using default.")
        prompt = "Transform this image into a cyberpunk night scene with neon lighting and rain."
    return prompt


def edit_image():
    """Pick an image from outputs/, apply a user-defined edit, and save the result."""
    images = get_available_images()

    if not images:
        print("  ERROR: No images found in outputs/.")
        print("  Run one of the generation scripts first (e.g. basic_generation.py).")
        return

    selected = pick_image(images)
    prompt = get_edit_prompt()

    stem = selected.stem
    output_name = f"{stem}_edited.png"

    print(f"\n🎨 Editing {selected.name}...")

    # DALL-E 2 requires a file object with PNG mimetype (not raw bytes)
    with open(selected, "rb") as image_file:
        result = client.images.edit(
            model="dall-e-2",
            image=image_file,
            prompt=prompt,
            size="1024x1024",
        )

    save_image(result.data[0].b64_json, output_name)
    print(f"  Done! Compare {selected.name} and {output_name}")


if __name__ == "__main__":
    edit_image()
