import os
from pathlib import Path
from huggingface_hub import InferenceClient
from datetime import datetime

def generate_image(prompt, model="black-forest-labs/FLUX.1-dev", output_folder="output_images"):
    """
    Generate an image using Hugging Face models and save it to the specified output folder
    
    Args:
        prompt (str): The text prompt to generate an image from
        model (str): The Hugging Face model to use
        output_folder (str): The folder to save the image in
    
    Returns:
        Path: The path to the saved image
    """
    # Ensure the output folder exists
    output_path = Path(output_folder)
    output_path.mkdir(exist_ok=True, parents=True)
    
    # Initialize the client with the API key
    print(f"Initializing client with token length: {len(os.environ.get('HF_TOKEN', '')) if os.environ.get('HF_TOKEN') else 'No token found'}")
    
    try:
        client = InferenceClient(
            provider="hf-inference",
            api_key=os.environ["HF_TOKEN"],
        )
        
        print(f"Generating image with prompt: '{prompt}'")
        print(f"Using model: {model}")
        
        # Generate the image
        image = client.text_to_image(
            prompt,
            model=model,
        )
        
        # Create a filename based on the current timestamp and the first few words of the prompt
        clean_prompt = "".join(c if c.isalnum() or c.isspace() else "_" for c in prompt)
        short_prompt = "_".join(clean_prompt.split()[:5])  # First 5 words
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{short_prompt}.png"
        
        # Full path to save the image
        save_path = output_path / filename
        
        # Save the image
        image.save(save_path)
        
        print(f"Image successfully saved to: {save_path}")
        return save_path
        
    except Exception as e:
        print(f"Error generating or saving image: {str(e)}")
        return None

if __name__ == "__main__":
    # Example usage
    prompt = "Astronaut riding a horse"
    output_folder = "output_images"
    
    # Generate and save the image
    image_path = generate_image(prompt=prompt, model="black-forest-labs/FLUX.1-dev", output_folder=output_folder)
    
    if image_path:
        print(f"Image generation successful! Image saved at: {image_path}")
    else:
        print("Image generation failed.")
