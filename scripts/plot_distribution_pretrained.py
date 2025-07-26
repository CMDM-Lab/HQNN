import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("./analysis/direct_pretrained_ensemble.csv")

df = df[df['Model'].isin(['Pretrained', 'Direct'])]

plt.figure(figsize=(8, 5))

# palette = {
#     'FFNN': '#0072B2',
#     'HQNN': '#D55E00',
#     'Ensemble': '#009E73',
# }

ax = sns.boxplot(data=df, x='Group', y='SIS', hue='Model', hue_order=['Direct', 'Pretrained'], showfliers=False, width=0.6, whis=0)

# plt.title("SIS Score Distribution of Direct and Pretrained Models")
#
#
# # plt.title("SIS Score Distribuition of Different Models")
# legend = plt.legend(title=None, frameon=False, loc='lower right')
# ax.set_xticks([])
# plt.ylabel("Spectral Information Similarity (SIS)")
# plt.xlabel("")
# plt.ylim(0.65, 0.92)
# plt.yticks(np.arange(0.65, 0.921, 0.05))
# plt.tight_layout()
# plt.savefig("./output/figures/Format.png", dpi=300)


summary = df.groupby(['Group', 'Model'])['SIS'].agg(
    Q1=lambda x: x.quantile(0.25),
    Median=lambda x: x.quantile(0.5),
    Q3=lambda x: x.quantile(0.75),
    Mean='mean'
)
print(summary)
