
import matplotlib.pyplot as plt
import numpy as np

values = []

with open("./iso_ref.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            last_value = float(line.split(",")[-1])
            if last_value != 0:
                values.append(last_value)
        except ValueError:
            continue

q1 = np.percentile(values, 25)
median = np.percentile(values, 50)
q3 = np.percentile(values, 75)


plt.figure(figsize=(8, 5))
plt.hist(values, bins=50, cumulative=True, color="#90d3f4", edgecolor='black')
plt.xlabel("SIS Score")
plt.ylabel("Cumulative Count")
plt.title("Cumulative Histogram of SIS Scores for Most Similar Isomers in Reference Database")
plt.grid(False)

for val, label in zip([q1, median, q3], ["Q1", "Median", "Q3"]):
    plt.axvline(val, color="gray", linestyle="--", linewidth=1)
    plt.text(val, plt.ylim()[1]*0.95, f'{label}\n{val:.4f}', 
             rotation=90, verticalalignment='top', horizontalalignment='right', color="gray")

plt.tight_layout()
plt.savefig("./sis_hist_1.png")

