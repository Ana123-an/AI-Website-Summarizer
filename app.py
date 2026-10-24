
import requests
from bs4 import BeautifulSoup

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"


# Fetch website content
def get_web(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unnecessary HTML elements
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()

        text = soup.get_text(separator=" ", strip=True)

        if not text:
            return "ERROR: No readable text found on the website."

        return text[:5000]

    except requests.exceptions.RequestException as e:
        return f"ERROR FETCHING WEBSITE: {e}"


# Summarize website content using Ollama
def sum_web(context):
    if context.startswith("ERROR"):
        return context

    prompt = f"""
You are an AI website analyzer.

Analyze the website content and provide:
1. A short summary.
2. The main topics discussed.
3. Important information.
4. Key takeaways.

Use simple and clear language.

Website content:
{context}
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        data = response.json()
        return data.get("response", "ERROR: No response received from Ollama.")

    except requests.exceptions.RequestException as e:
        return f"ERROR CONNECTING TO OLLAMA: {e}"

    except ValueError:
        return "ERROR: Ollama returned an invalid JSON response."


# Main function
def main():
    print("AI Website Summarizer")
    print("Enter 'exit' to quit.\n")

    while True:
        url = input("Enter Website URL: ").strip()

        if url.lower() == "exit":
            break

        if not url.startswith(("http://", "https://")):
            print("Please enter a valid URL beginning with http:// or https://\n")
            continue

        print("\nFetching website content...")

        content = get_web(url)
        print("\nDEBUG - Website content:")
        print(content[:500])

        if content.startswith("ERROR"):
            print(content, "\n")
            continue

        print("Generating summary...\n")

        result = sum_web(content)

        print("Website Summary:")
        print("-" * 50)
        print(result)
        print("-" * 50, "\n")


if __name__ == "__main__":
    main()


    