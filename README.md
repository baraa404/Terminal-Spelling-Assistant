# 📝 Spelling & Grammar Assistant CLI

<div align="center">

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![PyPI](https://img.shields.io/badge/PyPI-cword-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

*A powerful command-line spelling and grammar assistant powered by AI* ✨

![Showcase GIF](showcasess.gif)

</div>

---

## 🚀 Quick Start

### Prerequisites
- 🐍 **Python 3.7+** ([Download here](https://python.org/downloads/))
- 🌐 Internet connection

### Installation
```bash
# Universal install (works anywhere)
pip install cword

# Or development install
git clone https://github.com/baraa404/Terminal-Spelling-Assistant
cd spelling-cli
pip install .
```

### Get API Key
Get your free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### Start Using
```bash
# Fix spelling mistakes
cword misspeled
# → misspelled

# Fix spelling and grammar in sentences
cword This sentance has some erors in it and grammer mistakes.
# → This sentence has some errors in it and grammar mistakes.
```

---

## 💡 How to Use

### 🔧 First Time Setup
The first time you run the command, you'll be asked for your Google Gemini API key:

```bash
$ cword hello
Gemini API key not found. Please enter your API key.
You can get an API key from: https://makersuite.google.com/app/apikey
Enter your Gemini API key: [paste your key here]
API key saved successfully!
hello
```

### ✨ Basic Usage
```bash
# Fix simple spelling mistakes
cword definately
# → definitely

cword recieve  
# → receive

cword seperate
# → separate

cword accomodate
# → accommodate

# Fix spelling and grammar in sentences (no quotes needed)
cword I have recieved the documnt and it looks grate.
# → I have received the document and it looks great.

cword The commitee will meet on wendsday to discus the propsal.
# → The committee will meet on Wednesday to discuss the proposal.

# Grammar corrections
cword I are going to the store
# → I am going to the store

cword She don't like that movie
# → She doesn't like that movie
```

### 🎯 Smart Suggestions
When there are multiple possible corrections:
```bash
cword reed
# → (read - red - reed)

cword theres
# → (there's - theirs - there is)
```

### 🔄 API Key Management
```bash
# Reset your saved API key
cword --reset-api
# API key reset successfully. You'll be prompted for a new one next time.
```

### 💡 Pro Tips
- **Fast corrections**: Just type `cword` followed by any word or sentence
- **Spelling & Grammar**: Fixes both spelling mistakes and grammar errors automatically
- **Multiple words**: `cword misspelled sentence works perfectly` 
- **No quotes needed**: Works with spaces automatically
- **Secure**: Your API key is stored locally in `~/.config/spelling-cli/config.json`
- **Offline safety**: No data is stored remotely, only sent to Google's API for processing

---

## ✨ Features

- 🤖 **AI-Powered**: Uses Google Gemini for intelligent spelling and grammar correction
- 📝 **Dual Purpose**: Fixes both spelling mistakes and grammar errors
- 🔐 **Secure**: API key stored locally and securely
- ⚡ **Fast**: Instant corrections from the command line
- 🎯 **Smart**: Provides multiple suggestions for ambiguous words
- 🛠️ **Easy Setup**: One-time API key configuration
- 🔄 **Flexible**: Reset API key anytime

---

## 📋 Examples

| Input | Output | Description |
|-------|--------|-------------|
| `cword accomodate` | `accommodate` | Spelling correction |
| `cword occassion` | `occasion` | Double letter fix |
| `cword therefor` | `(therefore - therefor)` | Multiple options |
| `cword reccomend` | `recommend` | Common misspelling |
| `cword This is a grate sentance.` | `This is a great sentence.` | Spelling + grammar |
| `cword I are going home` | `I am going home` | Grammar correction |

---

## 🛠️ Development

### Building from Source

```bash
# Install build tools
pip install build

# Build the package
python -m build

# Install locally for development
pip install -e .
```

### Running Without Installation

```bash
# Run as module
python -m cword --help

# Or directly from source (development)
python src/cword/cli.py --help
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

- 🐛 Report bugs
- 💡 Suggest new features
- 📝 Improve documentation  
- 🔧 Submit pull requests

---

<div align="center">

**Made with ❤️ by Baraa**

⭐ Star this repo if you found it helpful!

</div>
