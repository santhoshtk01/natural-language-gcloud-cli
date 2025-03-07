"""
🔹 latency_analysis.py
---------------------------------
Plots latency, CPU usage, and accuracy comparisons.
"""

import matplotlib.pyplot as plt
import seaborn as sns

methods = ["Rule-Based NLP", "Cloud LLM", "Ollama LLM"]
latency = [0.02, 2.0, 0.8]
cpu_usage = [2, 50, 20]
cost = [0, 0.02, 0]
scalability = [0.3, 0.9, 0.85]
accuracy = [50, 95, 90]

plt.figure(figsize=(12, 6))
sns.set(style="whitegrid")

metrics = [("Latency (s)", latency), ("CPU Usage (%)", cpu_usage), ("Cost ($)", cost),
           ("Scalability Score (0-1)", scalability), ("Accuracy (%)", accuracy)]

for i, (title, values) in enumerate(metrics, 1):
    plt.subplot(2, 3, i)
    sns.barplot(x=methods, y=values, palette="coolwarm")
    plt.ylabel(title)
    plt.title(f"🔹 {title}")

plt.tight_layout()
plt.show()
