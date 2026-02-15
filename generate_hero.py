"""
Section 4 — Landing Page Hero Image Module

Generates a cinematic SaaS-style marketing hero image
and saves it to outputs/hero.jpeg.
"""

from utils import client, save_image

HERO_PROMPT = """
Create a cinematic, wide-format hero image for a SaaS startup landing page.

Scene: A futuristic workspace where holographic data dashboards float in mid-air.
A diverse team of professionals collaborates around a glowing central display
showing upward-trending analytics charts. The environment blends a modern
glass office with subtle sci-fi elements — soft neon accent lighting in blue
and purple tones, clean lines, and a city skyline visible through floor-to-ceiling
windows in the background.

Style: Photorealistic with a slight cinematic color grade. Depth of field with
the foreground slightly blurred. Aspirational and premium feel — the kind of
image that makes you want to sign up immediately.

Mood: Innovation, collaboration, momentum, trust.
"""


def generate_hero():
    """Generate a landing page hero image and save it to outputs/hero.jpeg."""
    print("\nGenerating landing page hero image...")

    result = client.images.generate(
        model="gpt-image-1",
        prompt=HERO_PROMPT,
        size="1536x1024",
        quality="high",
        output_format="jpeg",
        output_compression=100,
    )

    save_image(result.data[0].b64_json, "hero.jpeg")
    print("  Hero image generation complete.")


if __name__ == "__main__":
    generate_hero()
