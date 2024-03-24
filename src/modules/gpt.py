from transformers import GPT2LMHeadModel, GPT2Tokenizer, pipeline
import os

# Directory where models will be saved
MODEL_DIR = 'models/'

def download_and_save_model(model_name='gpt2', save_dir=MODEL_DIR):
    """
    Downloads the model and tokenizer for a given model name and saves it to the specified directory.
    """
    # Ensure the save directory exists
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Initialize tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    
    # Save tokenizer and model
    tokenizer.save_pretrained(os.path.join(save_dir, model_name))
    model.save_pretrained(os.path.join(save_dir, model_name))
    print(f"Model and tokenizer for '{model_name}' saved to '{save_dir}{model_name}'")

def load_model_from_dir(model_name='gpt2', model_dir=MODEL_DIR):
    """
    Loads the model and tokenizer from a specified directory.
    """
    model_path = os.path.join(model_dir, model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_path)
    model = GPT2LMHeadModel.from_pretrained(model_path)
    return pipeline('text-generation', model=model, tokenizer=tokenizer)

def generate_text(prompt, max_length=280, model_name='gpt2', model_dir=MODEL_DIR):
    """
    Generates text using the GPT model loaded from a specified directory.
    """
    generator = load_model_from_dir(model_name=model_name, model_dir=model_dir)
    results = generator(prompt, max_length=max_length, num_return_sequences=1)
    return results[0]['generated_text']
