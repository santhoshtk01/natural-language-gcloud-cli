"""
🔹 execute_gcloud.py
---------------------------------
Executes the generated `gcloud` command and measures execution latency.
"""

import subprocess
import time

def execute_gcloud_command(command):
    """
    Executes a `gcloud` CLI command.

    Args:
        command (str): The cleaned `gcloud` command.

    Returns:
        float: Execution time taken (T_execution).
    """
    print(f"🚀 Executing: {command}")

    start_time = time.time()

    exec_result = subprocess.run(command, shell=True, capture_output=True, text=True)

    execution_time = time.time() - start_time  # Time taken for command execution

    if exec_result.returncode == 0:
        print("✅ Command executed successfully!\n")
        print(exec_result.stdout)
    else:
        print("❌ Error executing command!")
        print(exec_result.stderr)

    return execution_time
