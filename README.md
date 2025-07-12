
# Deck Automation Suite

Deck Automation Suite is an end-to-end solution for automating the creation of professional presentation decks, applying custom themes, and generating high-quality visuals and infographics using state-of-the-art AI models.

---

## Features

### 1. Automated Deck Generation
- Instantly generate PowerPoint presentations on any topic using advanced GPT models.
- Example:
  ```sh
  python deck_generator.py --prompt "Create a presentation about AI in healthcare" --output presentation.pptx
  ```

### 2. Template Application
- Seamlessly apply custom themes and templates to your generated presentations for a polished, branded look.
- Example:
    ```sh
    python apply_template.py --input "presentation.pptx" --template "custom_theme.pptx" --output "themed_presentation.pptx"
    ```

### 3. Visual & Infographic Generation
- Automatically create relevant visuals, infographics, diagrams, and conceptual illustrations for each slide using text-to-image models (e.g., Stable Diffusion via Hugging Face).
- Example:
  ```sh
  python deck_image_generator.py --input "presentation.pptx" --output "output_folder" --hf_token "<your_hf_token>" --model "<model_name>"
  ```

  Output structure:
  ```
  output_folder/
  ├── slide_1/
  │   ├── image_1.png  # Infographic
  │   ├── image_2.png  # Diagram/Chart
  │   └── image_3.png  # Conceptual Illustration
  ├── slide_2/
  │   ├── image_1.png
  │   └── ...
  └── ...
  ```

---

## Supported Hugging Face Models
Recommended models for image generation:

- `stabilityai/stable-diffusion-xl-base-1.0` (default)
- `runwayml/stable-diffusion-v1-5`
- `stabilityai/stable-diffusion-2-1`
- `CompVis/stable-diffusion-v1-4`
- `prompthero/openjourney`

---

## Utility Scripts

- `test_huggingface_connection.py`: Test Hugging Face API connectivity.
- `test_image_generator.py`: Test image generation with multiple models and identify compatible ones.
- `huggingface_image_generator.py`: Standalone module for robust image generation functions.

---

## Resources

1. [Prompt and Image Attribute Guide](https://cloud.google.com/vertex-ai/generative-ai/docs/image/img-gen-prompt-guide)
2. [Top AI Tools Directory](https://topai.tools/)
3. [AI Image Generation Notes](https://github.com/swyxio/ai-notes/blob/main/IMAGE_GEN.md)
4. [How to Run Stable Diffusion](https://www.datacamp.com/tutorial/how-to-run-stable-diffusion) | [GFG: Text-to-Image using Stable Diffusion](https://www.geeksforgeeks.org/artificial-intelligence/text-to-image-using-stable-diffusion-huggingface-model/)
5. [Generative AI Prompt Samples](https://cloud.google.com/vertex-ai/generative-ai/docs/prompt-gallery)
6. [Prompt Engineering for Copilot](https://code.visualstudio.com/docs/copilot/chat/prompt-crafting)
7. [How to Write Better AI Prompts](https://leaddev.com/velocity/how-write-better-ai-prompts)
8. [Prompt Chaining in ChatGPT](https://github.com/MIATECHPARTNERS/PromptChains)
9. [Image Generator using Various Models](https://github.com/SikamikanikoBG/ImageGenerator)

---

## Getting Started

1. Clone the repository and install dependencies as required.
2. Obtain a Hugging Face API token for image generation features.
3. Follow the usage examples above to generate decks and visuals.

For detailed documentation, refer to the code comments and scripts in each module.

```

python deck_image_generator.py --input "presentation.pptx" --output "output_folder" --hf_token  "..." --model "..."

├── slide_1/
│   ├── image_1.png  (infographic)
│   ├── image_2.png  (diagram/chart)
│   └── image_3.png  (conceptual illustration)
├── slide_2/
│   ├── image_1.png
│   └── ...
└── ...
```
### Available Hugging Face Models
Some recommended models for image generation:

stabilityai/stable-diffusion-xl-base-1.0 (default)
runwayml/stable-diffusion-v1-5
stabilityai/stable-diffusion-2-1
CompVis/stable-diffusion-v1-4
prompthero/openjourney

```
test_huggingface_connection.py - A simple script to test basic Hugging Face API connectivity

test_image_generation.py - A script that tests image generation with multiple models and identifies which ones work for you
huggingface_image_generator.py - A standalone module with the robust image generation function
```



