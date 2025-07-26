import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("./analysis/TMSE_detailed_change.csv")

# TMSE log10
df['NegLogTMSE'] = -np.log10(df['TMSE'])

df = df[df['Group'].astype(int) >= 5]
df['Group'] = df['Group'].astype(int).apply(lambda x: f'Group{x}')

plt.figure(figsize=(10, 5))

palette = {
    'FFNN': '#A0A2A3',
    'HQNN': '#009495',
    'Ensemble':'#CC252B'
}

palette = {
    'FFNN': '#0072B2',
    'HQNN': '#D55E00',   
    'Ensemble': '#009E73'
}
ax = sns.boxplot(data=df, x='Group', y='NegLogTMSE', hue='Model', 
            order=['Group5', 'Group6', 'Group7'],showfliers=False, width=0.6, whis=0)

handles, labels = ax.get_legend_handles_labels()

# order = ['Ensemble', 'HQNN', 'FFNN']
order = ['FFNN', 'HQNN', 'Ensemble']
new_handles = [handles[labels.index(label)] for label in order]

plt.legend(new_handles, order, title=None, frameon=False, loc='lower right')

# legend = plt.legend(title=None, frameon=False, loc='lower right')
plt.title("TMSE Distribution of Different Models Across Groups")
plt.ylabel(r"$-\log_{10}(\mathrm{TMSE})$")
plt.xlabel("")
plt.ylim(2.9, 4.2)
plt.tight_layout()
plt.savefig("./output/figures/Format.png", dpi=300)

summary = df.groupby(['Group', 'Model'])['NegLogTMSE'].agg(
    Q1=lambda x: x.quantile(0.25),
    Median=lambda x: x.quantile(0.5),
    Q3=lambda x: x.quantile(0.75),
    Mean='mean'
)
print(summary)
