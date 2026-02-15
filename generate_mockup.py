"""
Section 5 — Product Mockup Module

Generates a realistic product dashboard mockup image
and saves it to outputs/mockup.jpeg.
"""

from utils import client, save_image

MOCKUP_PROMPT = """
Create a realistic product screenshot mockup of a modern SaaS analytics dashboard
called "Launchpad AI" displayed on a MacBook Pro.

The dashboard should include:
- A left sidebar with navigation icons (Home, Analytics, Users, Settings)
- A top bar showing "Launchpad AI" branding with a search bar and user avatar
- Main content area with:
  - A large line chart showing "Monthly Active Users" trending upward
  - Three KPI cards: "Revenue $142K" (up 23%), "Users 12.4K" (up 18%), "NPS 72" (up 5)
  - A small bar chart showing "Signups by Channel"
  - A recent activity feed with user avatars and action descriptions

Style: Clean, modern UI with a white background, subtle gray borders, and the brand's
electric blue (#0066FF) as the accent color. The MacBook should be shown at a slight
3/4 angle on a minimal desk surface with soft studio lighting.

The overall feel should be "this product already exists and is thriving."
"""


def generate_mockup():
    """Generate a product mockup image and save it to outputs/mockup.jpeg."""
    print("\nGenerating product mockup...")

    result = client.images.generate(
        model="gpt-image-1",
        prompt=MOCKUP_PROMPT,
        size="1536x1024",
        quality="high",
        output_format="jpeg",
        output_compression=100,
    )

    save_image(result.data[0].b64_json, "mockup.jpeg")
    print("  Product mockup generation complete.")


if __name__ == "__main__":
    generate_mockup()
