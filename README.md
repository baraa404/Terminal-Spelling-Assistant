# 📝 Spelling Assistant CLI

<div align="center">

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

*A powerful command-line spelling assistant powered by Google Gemini AI* ✨

</div>

---

## 🚀 Quick Install & Use

Get spelling corrections in 3 simple steps:

### 1️⃣ Install
```bash
git clone https://github.com/baraa404/spelling-cli
cd spelling-cli
pip install .
```

### 2️⃣ Get API Key
Get your free API key from [Google AI Studio](https://makersuite.google.com/app/apikey) (takes 30 seconds)

### 3️⃣ Start Using
```bash
words misspeled
# → misspelled
```

That's it! ✨

---

## 📦 Installation Options

### 🔥 Quick Install (Recommended)
```bash
git clone https://github.com/baraa404/spelling-cli.git
cd spelling-cli
pip install .
```

### 🛠️ Development Install
For developers who want to modify the code:
```bash
git clone https://github.com/baraa404/spelling-cli.git
cd spelling-cli
pip install -e .
```

### 📋 Manual Install
If you downloaded the ZIP file:
```bash
unzip spelling-cli-main.zip
cd spelling-cli-main
pip install .
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
```

### 🎯 Smart Suggestions
When there are multiple possible corrections:
```bash
words reed
# → (read - red - reed)

words there
# → (their - there - they're)
```

### 🔄 API Key Management
```bash
# Reset your saved API key
words --reset-api
# API key reset successfully. You'll be prompted for a new one next time.
```

### 💡 Pro Tips
- **Fast corrections**: Just type `words` followed by any word
- **No quotes needed**: `words misspelled word` works fine
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

## 🛠️ Requirements

- 🐍 Python 3.6 or higher
- 🌐 Internet connection
- 🔑 Google Gemini API key (free)

---

## 📋 Examples

| Input | Output | Description |
|-------|--------|-------------|
| `words accomodate` | `accommodate` | Simple correction |
| `words occassion` | `occasion` | Double letter fix |
| `words therefor` | `(therefore - therefor)` | Multiple options |
| `words reccomend` | `recommend` | Common misspelling |

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
