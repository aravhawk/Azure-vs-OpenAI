# GPT-4o Comparison Tool

This project compares the performance of two GPT-4o services:
- **Azure** (using the `azure-ai-inference` library)
- **OpenAI** (using the `openai` library)

It sends a user-provided prompt to both services, measures response times, calculates output tokens per second, and prints a comparison of the results.

## Features

- **Measure Performance:** Records response time and tokens-per-second for each service.
- **Direct Comparison:** Compares Azure and OpenAI responses to indicate which service is faster.
- **Simple User Interface:** Enter your prompt and view detailed performance metrics.

## Prerequisites

- Python 3.8 or later

## Installation

1. **Clone or download the repository.**

2. **Install the required libraries:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Set the following environment variables with your API credentials before running the script:

- `AZURE_ENDPOINT`: The endpoint URL for your Azure AI service.
- `AZURE_API_KEY`: Your Azure API key.
- `OPENAI_API_KEY`: Your OpenAI API key.

For example, on Unix-based systems:

```bash
export AZURE_ENDPOINT="your_azure_endpoint"
export AZURE_API_KEY="your_azure_api_key"
export OPENAI_API_KEY="your_openai_api_key"
```

## Usage

Run the script with Python:

```bash
python script_name.py
```

When prompted, enter your text prompt for GPT-4o. The script will then:
1. Run the prompt through the Azure service.
2. Run the prompt through the OpenAI service.
3. Compare the response times and output tokens per second, displaying which service performed faster.

## Files

- **script_name.py**: Main Python script that performs the comparison.
- **requirements.txt**: Lists the required libraries.

## License

This project is open source and available under the [MIT License](LICENSE).
