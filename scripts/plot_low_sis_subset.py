from collections import Counter
import matplotlib.pyplot as plt

bins = {
    "0 ~ 0.1": lambda x: 0 < x < 0.1,
    "-0.1 ~ 0": lambda x: -0.1 < x < 0,
    ">= 0.1": lambda x: x >= 0.1,
    "<= -0.1": lambda x: x <= -0.1,
}

counter = Counter()
pos_values = []
neg_values = [] 

with open("./output/sis/diff_log_7_thesis.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#') or 'Line' in line or 'Mean' in line:
            continue

        parts = line.split()
        try:
            diff = float(parts[-1])

            for label, cond in bins.items():
                if cond(diff):
                    counter[label] += 1
                    break

            if diff > 0:
                pos_values.append(diff)
            elif diff < 0:
                neg_values.append(diff)

        except ValueError:
            continue

pos_mean = sum(pos_values) / len(pos_values) if pos_values else 0
neg_mean = sum(neg_values) / len(neg_values) if neg_values else 0

print(f"Positive Δ avg: {pos_mean:.4f}")
print(f"Negative Δ avg: {neg_mean:.4f}")

blue = "#90d3f4"     
pink = "#f4a0a0"     


ordered_labels = ["0 ~ 0.1", "-0.1 ~ 0", ">= 0.1", "<= -0.1"]
counts = [counter[label] for label in ordered_labels]
colors = ['#950E2E' if '>=' in label or '0 ~' in label else 'gray' for label in ordered_labels]

print("\nBin counts:")
for label in ordered_labels:
    print(f"{label}: {counter[label]}")

plt.figure(figsize=(8, 6))
plt.bar(ordered_labels, counts, color=colors)
plt.title("Distribution of ΔSIS (Hybrid - Classical)")
plt.ylabel("Number of Molecules")
plt.xlabel("ΔSIS Interval (Hybrid - Classical)")
plt.xticks(rotation=30)
plt.grid(False)
plt.tight_layout()
plt.savefig("./sis_dis.png", dpi=300)

