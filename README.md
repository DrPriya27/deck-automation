# deck-automation

## Module 1
Auto generate deck on any topic with the help of GPT models

```
python deck_generator.py  --prompt "Create a presentation about AI in healthcare" --output presentation.pptx

```



## Module 2
Apply template theme to the generated presentation

## Module 3
Auto generate visuals, infographics on each slide deck using text-to-image model

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




### resources

1️⃣ Prompt and image attribute guide 
🔗 https://cloud.google.com/vertex-ai/generative-ai/docs/image/img-gen-prompt-guide

2️⃣ Find the Best AI Tools for Every Task 
🔗 https://topai.tools/

3️⃣ Detailed notes on image generation 
🔗 https://github.com/swyxio/ai-notes/blob/main/IMAGE_GEN.md

4️⃣ How to Run Stable Diffusion: A Step-by-Step Guide 
🔗 https://www.datacamp.com/tutorial/how-to-run-stable-diffusion
🔗 https://www.geeksforgeeks.org/artificial-intelligence/text-to-image-using-stable-diffusion-huggingface-model/


5️⃣Generative AI prompt sample
🔗 https://cloud.google.com/vertex-ai/generative-ai/docs/prompt-gallery

Prompt engineering for copilot
https://code.visualstudio.com/docs/copilot/chat/prompt-crafting

https://leaddev.com/velocity/how-write-better-ai-prompts

Prompt chaining in ChatGPT
https://github.com/MIATECHPARTNERS/PromptChains

Image generator using various models
https://github.com/SikamikanikoBG/ImageGenerator
