#!/bin/bash

python chempropIRZenodo/chempropIR/predict.py \
  --qnn \
  --test_path ./data/research_data/experiment/test_smiles.csv \
  --checkpoint_path ./output/model/ffnn_direct/fold_0/model_0/model.pt \
  --preds_path ./output/model/ffnn_direct/fold_0/ffnn_direct.csv
