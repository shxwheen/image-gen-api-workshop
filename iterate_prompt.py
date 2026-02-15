"""
Section 6 — Prompt Iteration Demonstration

Takes a base prompt and generates 3 stylistic variations to demonstrate
how quickly you can explore different brand positionings.

Variations:
  1. Minimal — clean, Swiss-design inspired
  2. Premium — luxury, dark-mode aesthetic
  3. Cyberpunk — neon, high-energy, futuristic
"""

from utils import client, save_image

BASE_PROMPT = (
    "A startup landing page hero image for an AI-powered analytics platform "
    "called 'Launchpad AI'. The image shows a futuristic control room with "
    "floating data visualizations."
)

VARIATIONS = {
    "minimal": {
        "suffix": (
            " Style: Ultra-minimal, Swiss design inspired. White background, "
            "thin black lines, monospace typography, generous whitespace. "
            "Muted pastel accent colors only. Feels like a Dieter Rams product."
        ),
        "filename": "variation_minimal.png",
    },
    "premium": {
        "suffix": (
            " Style: Premium dark mode. Deep charcoal and matte black surfaces, "
            "gold and warm amber accent lighting, subtle leather and brushed metal "
            "textures. Feels like a luxury car interior — exclusive and refined."
        ),
        "filename": "variation_premium.png",
    },
    "cyberpunk": {
        "suffix": (
            " Style: Cyberpunk / neon. Saturated magenta and cyan neon lighting, "
            "rain-slicked surfaces with reflections, holographic glitch effects, "
            "dense urban environment visible in background. High energy, "
            "Blade Runner meets Tokyo at night."
        ),
        "filename": "variation_cyberpunk.png",
    },
}


def iterate_prompt():
    """Generate 3 stylistic variations of the same base prompt."""
    print("\n🔄 Generating prompt variations...")

    for style_name, config in VARIATIONS.items():
        print(f"\n  [{style_name.upper()}]")
        full_prompt = BASE_PROMPT + config["suffix"]

        result = client.images.generate(
            model="gpt-image-1",
            prompt=full_prompt,
            size="1536x1024",
            quality="medium",
        )

        save_image(result.data[0].b64_json, config["filename"])

    print("\n  Prompt iteration complete — compare the 3 outputs in outputs/")


if __name__ == "__main__":
    iterate_prompt()
