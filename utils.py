"""
Shared utilities for the Image Gen API Workshop.

Initializes the OpenAI client and provides a helper for saving
base64-encoded image responses to files.
"""

import base64
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Initialize the client from the OPENAI_API_KEY environment variable.
# The SDK reads it automatically, but we keep this explicit for clarity.
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Ensure the outputs directory exists
OUTPUTS_DIR = Path(__file__).parent / "outputs"
OUTPUTS_DIR.mkdir(exist_ok=True)


def save_image(base64_data: str, filename: str) -> Path:
    """Decode a base64 image string and save it to a file.

    Args:
        base64_data: The base64-encoded image data from the API response.
        filename: The output filename (e.g. "logo.jpeg"). Saved into outputs/.

    Returns:
        The full path to the saved file.
    """
    filepath = OUTPUTS_DIR / filename
    image_bytes = base64.b64decode(base64_data)
    filepath.write_bytes(image_bytes)
    print(f"  Saved {filepath}")
    return filepath
