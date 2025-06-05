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

def get_correction(word):
    api_key = get_api_key()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

    prompt = f"""Act as a helpful spelling assistant. Whenever I type a word that is misspelled, provide the correct spelling of that word. If you are certain about the word I am trying to type, give me the correct spelling. If you are not certain and there are multiple possible corrections, list them in the following format: (word1 - word2 - word3 - etc...). For example, if I type 'tbale', you should respond with 'table'. If I type 'reed', you might respond with '(read - red - reed)'. Do not provide any additional information or explanations, just the correctly spelled word or the list of possible corrections.

Here is my word: {word}"""

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

    response = requests.post(url, headers=headers, json=data)
    
    try:
        reply = response.json()['candidates'][0]['content']['parts'][0]['text'].strip()
        return reply
    except KeyError:
        return "Error: Could not get correction from Gemini."

def run():
    # Check for special commands
    if len(sys.argv) == 2 and sys.argv[1] == "--reset-api":
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
    
    if len(sys.argv) != 2:
        print("Usage: words <misspelled-word>")
        print("       words --reset-api  (to reset your API key)")
        return

    word = sys.argv[1]
    correction = get_correction(word)
    print(correction)

if __name__ == "__main__":
    run()