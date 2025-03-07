"""
🔹 gcloud_nlp.py
---------------------------------
Natural Language → Google Cloud CLI Execution using Ollama (LLaMA 3)
- Converts natural language commands to valid `gcloud` CLI commands.
- Executes the generated commands and measures performance.
- Fully offline execution using Ollama LLM.

Author: Santhosh T K
"""

import subprocess
import time
from utils import clean_command
from execute_gcloud import execute_gcloud_command

def process_command(user_input):
    """
    Converts a natural language command into a valid `gcloud` CLI command using Ollama.

    Args:
        user_input (str): The natural language input from the user.

    Returns:
        tuple: (cleaned_gcloud_command, conversion_time)
    """
    prompt = f"""
    Convert the following natural language request into a valid Google Cloud CLI command:
    
    User: "{user_input}"

    Output only the correct command without any explanation.
    """

    start_time = time.time()  # Start timing the conversion

    # ✅ Run Ollama to get CLI command from LLaMA 3
    result = subprocess.run(
        ["ollama", "run", "llama3"],  
        input=prompt,
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="ignore"
    )

    conversion_time = time.time() - start_time  # Time taken for LLM conversion

    raw_output = result.stdout.strip()  # Raw output from Ollama
    cleaned_command = clean_command(raw_output)  # Remove backticks, unwanted spaces

    return cleaned_command, conversion_time

if __name__ == "__main__":
    while True:
        user_input = input("\n📝 Enter a TPU command (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("👋 Exiting CLI tool.")
            break

        gcloud_command, T_conversion = process_command(user_input)
        print(f"🖥️ Generated Command: {gcloud_command}")
        print(f"⏳ Time taken for conversion: {T_conversion:.2f} seconds")

        T_execution = execute_gcloud_command(gcloud_command)
        print(f"🚀 Total Latency (T_total): {T_conversion + T_execution:.2f} seconds\n")
