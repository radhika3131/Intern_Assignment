import os
import time
from transformers import AutoModelForCausalLM, AutoTokenizer, logging
import torch

# Set logging verbosity to INFO
logging.set_verbosity_info()

# Set the HF_HOME environment variable to a new directory with sufficient space
os.environ['HF_HOME'] = 'D:/huggingface_cache'  # Replace with your desired path

# Disable symlinks warning
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'

# Verify the environment variables are set
print("HF_HOME is set to:", os.environ['HF_HOME'])
print("HF_HUB_DISABLE_SYMLINKS_WARNING is set to:", os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'])

# Use the specified model name
model_name = "openbmb/MiniCPM-Llama3-V-2_5"

# Load the model and tokenizer with detailed debugging
print("Loading tokenizer...")
start_time = time.time()
try:
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    print("Tokenizer loaded successfully.")
except Exception as e:
    print(f"Error loading tokenizer: {e}")
    exit(1)
print(f"Tokenizer loading time: {time.time() - start_time:.2f} seconds")

print("Loading model...")
start_time = time.time()
try:
    model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)
print(f"Model loading time: {time.time() - start_time:.2f} seconds")

# Ensure the pad_token_id is set correctly
pad_token_id = tokenizer.eos_token_id if tokenizer.eos_token_id is not None else tokenizer.pad_token_id

# Check for GPU availability
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("CUDA is available. Using GPU.")
else:
    device = torch.device("cpu")
    print("CUDA is not available. Using CPU.")
model.to(device)
print("Model moved to device.")

# Function to generate a response
def generate_response(input_text, max_length=200):
    print(f"Generating response for input: {input_text}")
    inputs = tokenizer(input_text, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(inputs["input_ids"], max_length=max_length, pad_token_id=pad_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"Response: {response}")
    return response

# Test inference to ensure everything is working
test_input = "Hello, how are you?"
print(f"Running test inference with input: {test_input}")
test_response = generate_response(test_input, max_length=50)
print(f"Test response: {test_response}")

# Infinite chat loop
print("Chat with Llama-3! Type 'exit' to end the conversation.")
while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chat ended.")
            break
        response = generate_response(user_input, max_length=150)  # Adjust max_length as needed
        print(f"Llama-3: {response}")
    except Exception as e:
        print(f"Error during chat loop: {e}")
        break
