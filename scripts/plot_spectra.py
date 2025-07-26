import pandas as pd
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import Draw
import numpy as np


def generate_molecular_structure(smiles: str, save_img_path: str):
    molecule = Chem.MolFromSmiles(smiles)

    if molecule:
        img = Draw.MolToImage(molecule, size=(300, 300))
        img.save(save_img_path)
    else:
        print("Fail to generate molecular structure,")


def generate_spectra_comparison(
    wavenumbers: list, lines: list, save_img_path: str, start=50, interval=250
):
    plt.figure(figsize=(12, 4))
    for line in lines:
        plt.plot(
            wavenumbers,
            line["absorbance"],
            label=line["label"],
            color=line.get("color", "gray"),
            linestyle=line.get("linestyle", "-"),
            linewidth=line.get("linewidth", 2),
        )

    xticks = wavenumbers[start::interval]
    plt.xticks(xticks, fontname="sans serif", fontweight="bold")
    plt.xlim(0, 1800)
    plt.gca().invert_xaxis()
    plt.gca().set_yticks([])

    plt.xlabel(
        "Wavenumbers (cm⁻¹)", fontname="sans serif", fontsize=12, fontweight="bold"
    )
    plt.ylabel(
        "Absorbance (a.u.)", fontname="sans serif", fontsize=12, fontweight="bold"
    )
    plt.title("IR Spectrum Comparison for Match Case", fontname="sans serif", fontweight="bold")
    plt.legend(frameon=False, loc='upper left')
    plt.grid(False)

    output_file = save_img_path
    plt.savefig(output_file, dpi=300)
    plt.close()

def generate_spectra_comparison_norm(
    wavenumbers: list, lines: list, save_img_path: str, start=50, interval=250
):
    
    plt.figure(figsize=(12, 4))
    for line in lines:
        x = np.array(wavenumbers, dtype=float) 
        y = np.array(line["absorbance"], dtype=float)
        mask = ~np.isnan(y)
        x_plot = x[mask]
        y_plot = y[mask]

        plt.plot(
            x_plot,
            y_plot,
            label=line["label"],
            color=line.get("color", "gray"),
            linestyle=line.get("linestyle", "-"),
            linewidth=line.get("linewidth", 2),
        )
    xticks = x[start::interval]
    plt.xticks(xticks, fontname="sans serif", fontweight="bold")
    plt.xlim(x[0], x[-1])
    plt.gca().invert_xaxis()
    plt.gca().set_yticks([])

    plt.xlabel(
        "Wavenumbers (cm⁻¹)", fontname="sans serif", fontsize=12, fontweight="bold"
    )
    plt.ylabel(
        "Absorbance (a.u.)", fontname="sans serif", fontsize=12, fontweight="bold"
    )
    plt.title("IR Spectrum Comparison for Mismatch Case", fontname="sans serif", fontweight="bold")
    plt.legend(frameon=False, loc='upper left')
    plt.grid(False)

    output_file = save_img_path
    plt.savefig(output_file, dpi=300)
    plt.close()


def normalize(series: pd.Series) -> pd.Series:
    total = series.sum(skipna=True)
    if total == 0:
        return series.fillna(0.0)
    return series.fillna(0.0) / total

# example
file_path_1 = "./data/research_data/test_full.csv"
# file_path_1 = "./data/research_data/experiment/test_full.csv"
df_1 = pd.read_csv(file_path_1)

file_path_2 = "./output/model/qh2_2100_layer3/fold_0/qh2_2100_layer3.csv"
# file_path_2 = "./output/model/qnn_pretrained/fold_0/qnn_pretrained.csv"
df_2 = pd.read_csv(file_path_2)

wavenumbers = [col for col in df_1.columns if col != "smiles" and col != "epi_unc"]

lines = [
    {"absorbance": normalize(df_1.loc[4740, wavenumbers]), "label": "Ground Truth"},
    {
        "absorbance": normalize(df_2.loc[4740, wavenumbers]),
        "label": "Model Prediction",
        "color": "blue",
        "linestyle": (0, (2, 2)),
        "linewidth": 1.5,
    },
    # {
    #     "absorbance": normalize(df_1.loc[229, wavenumbers]),
    #     "label": "Top Match",
    #     "color": "red",
    #     "linestyle": (0, (2, 2)),
    #     "linewidth": 1.5,
    # },
]

# Backward query figure
# 239 match
# 10, 655, CCCCCC(C)(C)C, CCCCCC(C)(C)CC
# 570, 229 OCCCCCCCCBr,OCCCCCCCCCl


smiles1 = df_1.loc[4740, 'smiles']
print(f"Selected SMILES: {smiles1}")
# smiles2 = df_2.loc[655, 'smiles']
# print(f"Selected SMILES: {smiles2}")


# diff_ex1 = 'CC#CC1(O)CCCC(OCCN(C(C)C)C(C)C)C1'
# diff_ex2 = 'c1cnc2ccc(C3CCC3CNC3CC3)cc2c1'
# diff_ensemble_ex1 = 'CCC1=C(C)CCC1'
generate_spectra_comparison(wavenumbers, lines, "./Q3.png")
generate_molecular_structure('CCOC(=O)c1ccc(O)c([N+](=O)[O-])c1', './Q3_mol.png')
# generate_molecular_structure('OCCCCCCCCBr', './test2.png')
# generate_molecular_structure('OCCCCCCCCCl', './test3.png')
# generate_molecular_structure('CCCCCC(C)(C)C', './for.png')
# generate_molecular_structure('CCCCCC(C)(C)CC', './god.png')
# generate_molecular_structure('BrCCCCCCCCCCCCBr', './Match_mol.png')
