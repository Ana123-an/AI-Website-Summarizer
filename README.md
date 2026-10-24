# AI Website Summarizer

## Overview

AI Website Summarizer is a Python-based application that extracts readable text from a website and uses a locally running Large Language Model (LLM) through Ollama to generate a concise summary.

## Features

* Fetches content from publicly accessible websites.
* Extracts readable text using BeautifulSoup.
* Removes unnecessary HTML elements.
* Generates summaries using the Mistral model through Ollama.
* Runs locally on your computer.

## Tech Stack

* Python
* Requests
* BeautifulSoup
* Ollama
* Mistral LLM

## Prerequisites

* Python 3
* Ollama installed and running
* Mistral model downloaded through Ollama

## Installation

1. Clone this repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd GENAI8
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment on Windows:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

5. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

6. Download the Mistral model:

   ```bash
   ollama pull mistral
   ```

7. Run the application:

   ```bash
   python app.py
   ```

## Usage

Enter a publicly accessible website URL when prompted. The application fetches the website content and generates a summary using Ollama.

Type `exit` to quit the application.

## Limitations

* Some websites block automated requests.
* JavaScript-heavy websites may not expose their content through simple HTTP requests.
* Authentication-protected pages may not be accessible.
* Summary generation requires Ollama and the Mistral model to be available locally.

## License

This project is available for educational and personal use.
