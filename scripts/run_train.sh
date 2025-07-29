#!/bin/bash

python chempropIRZenodo/chempropIR/train.py \
  --qnn \
  --qnn_layer 2 \
  --data_path ./data/research_data/experiment/train_full.csv \
  --separate_val_path ./data/research_data/experiment/val_full.csv \
  --separate_test_path ./data/research_data/experiment/test_full.csv \
  --save_dir ./output/model/test \
  --config_path ./recommended_config.json

# if we don't want to seperate data auto, using the following recommended_config to assign the validation set and test set
# --separate_val_path \
# --separate_test_path \

# If we want to fine-tune on a pretrained model, specify the checkpoint path using:
# --checkpoint_path <path_to_pretrained_model.pt>