from setuptools import setup

# Read README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="words-cli",
    version="0.1.0",
    description="A CLI spelling assistant powered by Google Gemini",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Baraa",
    author_email="baraa0email@gmail.com",
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "words=main:run"
        ]
    },
    install_requires=[
        "requests"
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
