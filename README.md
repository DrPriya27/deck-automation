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

python deck_visuals_generator.py --input "presentation.pptx" --output "output_folder" --hf_token  "..." --model "..."

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

### 
test_huggingface_connection.py - A simple script to test basic Hugging Face API connectivity
test_image_generation.py - A script that tests image generation with multiple models and identifies which ones work for you
huggingface_image_generator.py - A standalone module with the robust image generation function



## Prompting guide
By taking this course, you'll learn to:
- Deeply understand generative AI, describing the key steps in a typical LLM-based generative AI lifecycle, from data gathering and model selection, to performance evaluation and deployment
- Describe in detail the transformer architecture that powers LLMs, how they’re trained, and how fine-tuning enables LLMs to be adapted to a variety of specific use cases
- Use empirical scaling laws to optimize the model's objective function across dataset size, compute budget, and inference requirements
- Apply state-of-the art training, tuning, inference, tools, and deployment methods to maximize the performance of models within the specific constraints of your project
- Discuss the challenges and opportunities that generative AI creates for businesses after hearing stories from industry researchers and practitioners





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


5️⃣
