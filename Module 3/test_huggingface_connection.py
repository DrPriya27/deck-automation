import os
import requests
import json
import sys

def test_huggingface_connection():
    """
    Test the connection to Hugging Face API and verify endpoint status.
    """
    print("Testing Hugging Face API Connection...")
    
    # Get API token from environment or input
    api_token = os.environ.get("HF_TOKEN")
    if not api_token:
        api_token = input("Please enter your Hugging Face API token: ")
    
    # Basic API test - check user information
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    
    try:
        # Test basic API connection
        response = requests.get(
            "https://huggingface.co/api/whoami-v2",
            headers=headers
        )
        
        if response.status_code == 200:
            print("✅ Successfully connected to Hugging Face API!")
            print(f"User info: {json.dumps(response.json(), indent=2)}")
        else:
            print(f"❌ Failed to connect to Hugging Face API. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
        print('here')
        
        # Test the specific model endpoint that's being used in the main script
        model_id = "stabilityai/stable-diffusion-xl-base-1.0"
        print(f"\nTesting inference endpoint for model: {model_id}")
        
        # Check if using inference endpoints
        endpoint_url = os.environ.get("HUGGINGFACE_ENDPOINT_URL")
        if endpoint_url:
            endpoint_check_url = f"https://api.endpoints.huggingface.cloud//endpoint//{endpoint_url}"
            endpoint_response = requests.get(endpoint_check_url, headers=headers)
            
            
            if endpoint_response.status_code == 200:
                endpoint_info = endpoint_response.json()
                print(f"✅ Endpoint exists with status: {endpoint_info.get('status', 'unknown')}")
                print(f"Endpoint info: {json.dumps(endpoint_info, indent=2)}")
            else:
                print(f"❌ Endpoint check failed. Status code: {endpoint_response.status_code}")
                print(f"Response: {endpoint_response.text}")
                
        # Test a simple inference request with minimal computation
        test_inference_url = f"https://api-inference.huggingface.co/models/{model_id}"
        test_inference_url = "https://api-inference.huggingface.co/stabilityai/stable-diffusion-xl-base-1.0"
        
        test_payload = {
            "inputs": "A simple test",
            "options": {"wait_for_model": True}
        }
        
        print("\nTesting simple inference request (this may take a moment)...")
        inference_response = requests.post(test_inference_url, headers=headers, json=test_payload)
        
        if inference_response.status_code == 200:
            print("✅ Inference endpoint is responsive!")
            # Don't print the full response as it might be large
            print("Received valid response from inference API")
        else:
            print(f"❌ Inference test failed. Status code: {inference_response.status_code}")
            print(f"Error message: {inference_response.text}")
            
        return True
            
    except Exception as e:
        print(f"❌ Error testing connection: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_huggingface_connection()
    if not success:
        print("\nTroubleshooting tips:")
        print("1. Verify your Hugging Face API token is correct")
        print("2. Check if the model endpoint is available on Hugging Face")
        print("3. Ensure you have an active internet connection")
        print("4. If using an inference endpoint, verify its status on endpoints.huggingface.co")
        sys.exit(1)
    else:
        print("\nConnection test completed successfully.")
