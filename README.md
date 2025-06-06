# 📝 Spelling Assistant CLI

<div align="center">

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

*A powerful command-line spelling assistant powered by Google Gemini AI* ✨

![Showcase GIF](https://github.com/baraa404/Terminal-Spelling-Assistant-/blob/main/showcases.gif)

</div>

---

## 🚀 Quick Start

### Prerequisites
- 🐍 **Python 3.6+** ([Download here](https://python.org/downloads/))
- 🌐 Internet connection

### Installation
```bash
# Quick install (recommended)
pip install git+https://github.com/baraa404/Terminal-Spelling-Assistant

# Or clone and install
git clone https://github.com/baraa404/Terminal-Spelling-Assistant
cd spelling-cli
pip install .
```

### Get API Key
Get your free API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### Start Using
```bash
# Single word correction
words misspeled
# → misspelled

# Sentence correction (use quotes)
words "This sentance has some erors in it."
# → This sentence has some errors in it.
```

---

## 💡 How to Use

### 🔧 First Time Setup
The first time you run the command, you'll be asked for your Google Gemini API key:

```bash
$ words hello
Gemini API key not found. Please enter your API key.
You can get an API key from: https://makersuite.google.com/app/apikey
Enter your Gemini API key: [paste your key here]
API key saved successfully!
hello
```

### ✨ Basic Usage
```bash
# Fix simple spelling mistakes
words definately
# → definitely

words recieve  
# → receive

words seperate
# → separate

words accomodate
# → accommodate

# Correct entire sentences (use double quotes)
words "I have recieved the documnt and it looks grate."
# → I have received the document and it looks great.

words "The commitee will meet on wendsday to discus the propsal."
# → The committee will meet on Wednesday to discuss the proposal.
```

### 🎯 Smart Suggestions
When there are multiple possible corrections:
```bash
words reed
# → (read - red - reed)

words theres
# → (there's - theirs - there is)
```

### 🔄 API Key Management
```bash
# Reset your saved API key
words --reset-api
# API key reset successfully. You'll be prompted for a new one next time.
```

### 💡 Pro Tips
- **Fast corrections**: Just type `words` followed by any word
- **Sentence corrections**: Use double quotes for full sentences
- **No extra quotes needed**: `words misspelled word` works for multiple words
- **Secure**: Your API key is stored locally in `~/.config/spelling-cli/config.json`
- **Offline safety**: No data is stored remotely, only sent to Google's API for processing

---

## ✨ Features

- 🤖 **AI-Powered**: Uses Google Gemini for intelligent spelling correction
- 🔐 **Secure**: API key stored locally and securely
- ⚡ **Fast**: Instant corrections from the command line
- 🎯 **Smart**: Provides multiple suggestions for ambiguous words
- 🛠️ **Easy Setup**: One-time API key configuration
- 🔄 **Flexible**: Reset API key anytime

---

## 📋 Examples

| Input | Output | Description |
|-------|--------|-------------|
| `words accomodate` | `accommodate` | Simple correction |
| `words occassion` | `occasion` | Double letter fix |
| `words therefor` | `(therefore - therefor)` | Multiple options |
| `words reccomend` | `recommend` | Common misspelling |
| `words "This is a grate sentance."` | `This is a great sentence.` | Sentence correction |

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- ✨ Suggest new features
- 🔧 Submit pull requests

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

<div align="center">

**Made with ❤️ by Baraa**

⭐ Star this repo if you found it helpful!

</div>
