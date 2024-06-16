# Llama-3 Chatbot Assignment

This repository contains my progress on an assignment to create a chatbot using the Llama-3 model. The task is to set up an infinite loop that enables users to chat with the Llama-3 model. This is part of my learning journey in generative AI, and I'm excited to share what I've accomplished so far.


## Project Structure

llama3-chatbot/
│
├── README.md
├── Assignment.py
├── requirements.txt



## Achievements

### Environment Initialization
- **Objective**: Set up environment variables for caching model files to ensure sufficient space and efficient operation.
- **Progress**: Successfully set up environment variables and disabled symlink warnings to avoid potential issues on Windows.

### Tokenizer Loading
- **Objective**: Load the tokenizer for the Llama-3 model.
- **Progress**: Successfully loaded the tokenizer for the model `openbmb/MiniCPM-Llama3-V-2_5`. Verified that the tokenizer loads successfully with detailed logging, ensuring visibility into the loading process.

### Model Configuration Loading
- **Objective**: Load the configuration for the Llama-3 model.
- **Progress**: Successfully loaded the configuration for the model and verified the process with comprehensive logging.

### Model Weights Loading
- **Objective**: Download and load the model weights.
- **Progress**: Initiated the download and loading of model weights with detailed logging to monitor progress. Successfully loaded the model weights.

### Device Management
- **Objective**: Ensure the model runs on the appropriate device (GPU if available, otherwise CPU).
- **Progress**: Implemented functionality to move the model to the appropriate device to optimize performance.

### Inference and Response Generation
- **Objective**: Develop functions to generate responses using the model and tokenizer.
- **Progress**: Implemented functions to generate responses and conducted test inferences to ensure the model generates responses as expected.

### Chat Loop Implementation
- **Objective**: Create an infinite chat loop for user interaction with the model.
- **Progress**: Implemented a chat loop that allows users to interact with the model. Included a mechanism for users to exit the chat loop by typing 'exit'.

## Issues Encountered

- **Script Termination**: The script appears to load both the tokenizer and the model successfully but terminates without entering the chat loop. This suggests an issue with the script not proceeding beyond the initial setup phase or an early exit due to an unseen error. Detailed logging has been added to identify where the termination occurs and to ensure the script reaches the chat loop.

## Next Steps

1. **Verify Model Weights Loading**: Ensure the model weights load successfully without hanging or taking an unusually long time.
2. **Run Full End-to-End Test**: Verify that the entire script runs smoothly from initialization to the chat loop.
3. **Error Handling and Logging**: Implement additional error handling and logging as needed to capture any issues that might arise during the execution.
4. **Final Review and Cleanup**: Review and clean up the script, ensuring it is well-documented and ready for further development.


## Dependencies
* transformers
* torch
* torchvision
* pillow

## Conclusion
This project is a foundational step in my learning journey with generative AI. Although the current implementation faces an issue with script termination before entering the chat loop, the groundwork has been laid for further development and debugging. I am eager to learn and improve
