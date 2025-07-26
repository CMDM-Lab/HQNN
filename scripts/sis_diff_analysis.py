import re

# 讀檔案
with open("./output/sis/diff_log_7_thesis.txt", "r") as f:
    lines = f.readlines()

diffs = []
for line in lines:
    if line.startswith("#") or not line.strip():
        continue
    matches = re.findall(r"[-+]?\d*\.\d+|\d+", line)
    if matches:
        try:
            diff = float(matches[-1])
            diffs.append(diff)
        except ValueError:
            continue

positive = [d for d in diffs if d > 0]
negative = [d for d in diffs if d < 0]

print("(1) 正的有幾個:", len(positive))
print("(2) 負的有幾個:", len(negative))

print("(3) 正的中 <= 0.1:", len([d for d in positive if d <= 0.1]))
print("(4) 正的中 > 0.1 且 <= 0.15:", len([d for d in positive if 0.1 < d <= 0.15]))
print("(5) 正的中 > 0.15:", len([d for d in positive if d > 0.15]))

print("(6) 負的中 >= -0.1:", len([d for d in negative if d >= -0.1]))
print("(7) 負的中 < -0.1 且 >= -0.15:", len([d for d in negative if -0.15 <= d < -0.1]))
print("(8) 負的中 < -0.15:", len([d for d in negative if d < -0.15]))

