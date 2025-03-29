import time
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential
from openai import OpenAI
import os

azureendpoint = os.getenv("AZURE_ENDPOINT")
azureapikey = os.getenv("AZURE_API_KEY")
openaiapikey = os.getenv("OPENAI_API_KEY")

azureclient = ChatCompletionsClient(
    endpoint=azureendpoint,
    credential=AzureKeyCredential(azureapikey),
)

openaiclient = OpenAI(
    api_key = openaiapikey
)

def runAzureJob(prompt):
    # Record the start time
    start_time = time.perf_counter()

    response = azureclient.complete(
        messages=[
            UserMessage(content=prompt)
        ],
        model="gpt-4o",
        max_tokens=4096,
        temperature=1.0,
        top_p=1.0,
    )

    # Record the end time just before printing the response
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    if isinstance(response.usage, dict):
        completion_tokens = response.usage.get("completion_tokens", 0)
    else:
        completion_tokens = getattr(response.usage, "completion_tokens", 0)

    tokens_per_second = completion_tokens / elapsed_time if elapsed_time > 0 else 0

    print("Azure Response:")
    print(response.choices[0].message.content)
    print("\n---\nResponse time: {:.3f} seconds".format(elapsed_time))
    print("Output tokens per second: {:.2f}".format(tokens_per_second))

    return elapsed_time, tokens_per_second

def runOpenAIJob(prompt):
    # Record the start time
    start_time = time.perf_counter()

    response = openaiclient.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="gpt-4o",
        max_tokens=4096,
        temperature=1.0,
        top_p=1.0,
    )

    # Record the end time just before printing the response
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    if isinstance(response.usage, dict):
        completion_tokens = response.usage.get("completion_tokens", 0)
    else:
        completion_tokens = getattr(response.usage, "completion_tokens", 0)

    tokens_per_second = completion_tokens / elapsed_time if elapsed_time > 0 else 0

    print("OpenAI Response:")
    print(response.choices[0].message.content)
    print("\n---\nResponse time: {:.3f} seconds".format(elapsed_time))
    print("Output tokens per second: {:.2f}".format(tokens_per_second))

    return elapsed_time, tokens_per_second

def compare():
    prompt = input("Prompt for GPT-4o: ")

    print("\nRunning Azure job...")
    azure_elapsed, azure_tps = runAzureJob(prompt)

    print("\nRunning OpenAI job...")
    openai_elapsed, openai_tps = runOpenAIJob(prompt)

    print("\n--- Comparison Results ---")
    if azure_elapsed < openai_elapsed:
        winner = "Azure"
        faster_time = azure_elapsed
        slower_time = openai_elapsed
    elif openai_elapsed < azure_elapsed:
        winner = "OpenAI"
        faster_time = openai_elapsed
        slower_time = azure_elapsed
    else:
        print("Both services performed equally fast!")
        return

    times_faster = slower_time / faster_time
    seconds_faster = slower_time - faster_time

    print(f"{winner} was faster!")
    print(f"It was {times_faster:.2f}x faster, finishing {seconds_faster:.3f} seconds quicker.")

compare()
