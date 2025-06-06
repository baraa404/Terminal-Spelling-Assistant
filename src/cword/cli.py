#!/usr/bin/env python3
"""
cword CLI - A command-line spelling and grammar assistant powered by AI
"""

import sys
import requests
import os
import json
from pathlib import Path

CONFIG_DIR = Path.home() / ".config" / "spelling-cli"
CONFIG_FILE = CONFIG_DIR / "config.json"

def load_config():
    """Load configuration from file."""
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}

def save_config(config):
    """Save configuration to file."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=2)
        return True
    except IOError:
        print("Error: Could not save configuration.")
        return False

def get_api_key():
    """Get API key from config or prompt user to enter it."""
    config = load_config()
    
    if "gemini_api_key" in config and config["gemini_api_key"]:
        return config["gemini_api_key"]
    
    print("Gemini API key not found. Please enter your API key.")
    print("You can get an API key from: https://makersuite.google.com/app/apikey")
    
    while True:
        api_key = input("Enter your Gemini API key: ").strip()
        if api_key:
            config["gemini_api_key"] = api_key
            if save_config(config):
                print("API key saved successfully!")
                return api_key
            else:
                print("Warning: Could not save API key. You'll need to enter it again next time.")
                return api_key
        else:
            print("API key cannot be empty. Please try again.")

def get_correction(text):
    """Get spelling/grammar correction from Google Gemini AI."""
    api_key = get_api_key()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

    # Determine if it's a word or sentence based on content
    is_sentence = len(text.split()) > 1 or any(char in text for char in '.!?,:;')
    
    if is_sentence:
        prompt = f"""Act as a helpful spelling and grammar assistant. I will provide you with a sentence that may contain spelling or grammar errors. Please correct any mistakes and return the corrected sentence. If the sentence is already correct, return it unchanged. Do not provide any additional information or explanations, just the corrected sentence.

Here is my sentence: {text}"""
    else:
        prompt = f"""Act as a helpful spelling assistant. Whenever I type a word that is misspelled, provide the correct spelling of that word. If you are certain about the word I am trying to type, give me the correct spelling. If you are not certain and there are multiple possible corrections, list them in the following format: (word1 - word2 - word3 - etc...). For example, if I type 'tbale', you should respond with 'table'. If I type 'reed', you might respond with '(read - red - reed)'. Do not provide any additional information or explanations, just the correctly spelled word or the list of possible corrections.

Here is my word: {text}"""

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [{"text": prompt}],
                "role": "user"
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        reply = response.json()['candidates'][0]['content']['parts'][0]['text'].strip()
        return reply
    except requests.exceptions.RequestException as e:
        return f"Error: Network request failed - {str(e)}"
    except (KeyError, IndexError) as e:
        return "Error: Could not get correction from Gemini. Please check your API key."
    except Exception as e:
        return f"Error: Unexpected error - {str(e)}"

def show_help():
    """Display help information."""
    print("""
cword - A CLI spelling and grammar assistant powered by  AI

Usage:
    cword <word>                   Check spelling of a single word
    cword <sentence to check>      Check and correct spelling and grammar
    cword --reset-api             Reset your API key
    cword --help                  Show this help message

Examples:
    cword teh                     → the
    cword I are writting a leter  → I am writing a letter
    cword --reset-api             → Resets stored API key

Get your Gemini API key from: https://makersuite.google.com/app/apikey
""")

def main():
    """Main entry point for the cword CLI."""
    # Handle special commands
    if len(sys.argv) == 2:
        if sys.argv[1] in ["--help", "-h", "help"]:
            show_help()
            return
        elif sys.argv[1] == "--reset-api":
            config = load_config()
            if "gemini_api_key" in config:
                del config["gemini_api_key"]
                if save_config(config):
                    print("API key reset successfully. You'll be prompted for a new one next time.")
                else:
                    print("Error: Could not reset API key.")
            else:
                print("No API key found to reset.")
            return
    
    if len(sys.argv) < 2:
        print("Usage: cword <word-or-sentence>")
        print("       cword <sentence to check and correct>")
        print("       cword --reset-api  (to reset your API key)")
        print("       cword --help      (for detailed help)")
        return

    # Join all arguments to handle sentences with spaces
    input_text = " ".join(sys.argv[1:])
    
    # Check if the input is enclosed in double quotes (optional)
    if input_text.startswith('"') and input_text.endswith('"'):
        # Remove the quotes for processing
        input_text = input_text[1:-1]
    
    correction = get_correction(input_text)
    print(correction)

if __name__ == "__main__":
    main()
