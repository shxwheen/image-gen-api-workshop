"""
Section 3 — Logo Generation Module

Generates a clean, modern startup logo using the GPT Image API
and saves it to outputs/logo.jpeg.
"""

from utils import client, save_image

LOGO_PROMPT = """
Design a modern, minimalist startup logo for a company called "Launchpad AI".

Requirements:
- Clean, geometric icon paired with bold sans-serif wordmark
- Icon should convey speed, innovation, and upward momentum (e.g., abstract rocket, arrow, or rising graph)
- Color palette: electric blue (#0066FF) and white on a transparent background
- Flat design, no gradients or 3D effects
- The icon should work at small sizes (favicon) and large sizes (billboard)
- Professional, Silicon Valley aesthetic
- No photorealistic elements — purely graphic/vector style
"""


def generate_logo():
    """Generate a startup logo and save it to outputs/logo.jpeg."""
    print("\n🎨 Generating startup logo...")

    result = client.images.generate(
        model="gpt-image-1",
        prompt=LOGO_PROMPT,
        size="1024x1024",
        quality="high",
        output_format="jpeg",
        output_compression=100,
    )

    save_image(result.data[0].b64_json, "logo.jpeg")
    print("  Logo generation complete.")


if __name__ == "__main__":
    generate_logo()
