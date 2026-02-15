# ChatGPT Image Generation API Workshop

> **Build a visual startup brand in minutes using the GPT Image API.**

This repository is a hands-on workshop demonstrating how to use OpenAI's `gpt-image-1` model to rapidly prototype branding and visual assets for a startup — logo, hero image, and product mockup — all from simple text prompts.

Whether you're at a hackathon with 10 minutes to spare or validating a new idea over the weekend, this workflow shows how generative AI lets you skip the design phase and go straight from concept to polished visuals.

---

## What You'll Build

| Asset | Script | Output |
|---|---|---|
| Startup Logo | `generate_logo.py` | `outputs/logo.png` |
| Landing Page Hero | `generate_hero.py` | `outputs/hero.png` |
| Product Mockup | `generate_mockup.py` | `outputs/mockup.png` |
| Prompt Variations | `iterate_prompt.py` | `outputs/variation_*.png` |
| All-in-One | `build_startup_assets.py` | All of the above |

---

## Prerequisites

- Python 3.9+
- An OpenAI API key with access to `gpt-image-1`

## Quick Start

```bash
# 1. Clone the repo
git clone <this-repo-url>
cd image-gen-api-workshop

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your API key
export OPENAI_API_KEY="sk-..."

# 4. Generate all assets in one shot
python build_startup_assets.py
```

---

## Project Structure

```
image-gen-api-workshop/
├── README.md
├── requirements.txt
├── utils.py                  # Shared helper: save base64 → PNG
├── generate_logo.py          # Section 3: Logo generation
├── generate_hero.py          # Section 4: Hero image generation
├── generate_mockup.py        # Section 5: Product mockup generation
├── iterate_prompt.py         # Section 6: Prompt variation demo
├── build_startup_assets.py   # Section 8: Run-all entry script
├── edit_image.py             # Section 9: Advanced image editing
└── outputs/                  # Generated images land here
```

---

## Section Walkthrough

### 1. Project Setup (`utils.py`)

The shared utility module initializes the OpenAI client from the `OPENAI_API_KEY` environment variable and provides a `save_image()` helper that decodes base64 image data and writes it to a PNG file.

### 2. Logo Generation (`generate_logo.py`)

Generates a clean, modern startup logo using a structured prompt focused on simplicity, iconography, and brand identity.

### 3. Hero Image (`generate_hero.py`)

Creates a cinematic, SaaS-style marketing hero image suitable for a landing page above-the-fold section.

### 4. Product Mockup (`generate_mockup.py`)

Produces a realistic product screenshot or dashboard mockup that could be dropped into a pitch deck or landing page.

### 5. Prompt Iteration (`iterate_prompt.py`)

Takes a single base prompt and generates 3 stylistic variations — **minimal**, **premium**, and **cyberpunk** — to demonstrate how quickly you can explore different brand positionings.

### 6. Run-All Script (`build_startup_assets.py`)

A single entry point that sequentially generates the logo, hero image, and mockup to simulate the full "idea → visual startup" pipeline.

### 7. Advanced: Image Editing (`edit_image.py`)

Demonstrates using `client.images.edit()` to modify an existing generated asset — for example, converting a daytime hero image into a cyberpunk night version.

---

## Why This Matters for Startups

Generative image APIs fundamentally change the economics of early-stage product development:

- **Rapid MVP Validation** — Test whether a concept resonates visually before writing a single line of product code. Generate landing page assets in minutes, ship a Carrd or Framer site, and measure signup conversion the same day.

- **A/B Testing at Zero Marginal Cost** — Traditional A/B testing of visual assets requires a designer for each variant. With prompt iteration, you can generate dozens of brand directions and let real user data pick the winner.

- **Branding Iteration Without a Design Team** — Early-stage founders can explore logo styles, color palettes, and visual identity on their own. When it's time to hire a designer, you already have a concrete reference point instead of vague descriptions.

- **Reduced Startup Burn Rate** — Design agency retainers or freelance contracts for branding packages typically start at $2K–$10K. API-generated assets cost pennies per image, letting you defer that spend until product-market fit is established.

- **Hackathon Superpower** — In a time-boxed environment, visuals make the difference between a demo that looks like a prototype and one that looks like a product. This workflow gives your team polished assets without pulling anyone off engineering.

---

## API Reference

This workshop uses the [OpenAI Image Generation API](https://platform.openai.com/docs/guides/image-generation) with the `gpt-image-1` model.

Key parameters used across scripts:

| Parameter | Values | Description |
|---|---|---|
| `model` | `"gpt-image-1"` | The image generation model |
| `prompt` | string | Detailed text description of the desired image |
| `size` | `"1024x1024"`, `"1536x1024"`, `"1024x1536"`, `"auto"` | Output dimensions |
| `quality` | `"low"`, `"medium"`, `"high"`, `"auto"` | Rendering quality |
| `output_format` | `"png"`, `"jpeg"`, `"webp"` | Output image format |
| `output_compression` | `0`–`100` | Compression level (for `jpeg` and `webp` formats) |

---
