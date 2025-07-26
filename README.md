# Spectral Prediction
This repository contains hybrid quantum neural networks for spectral predictions. The architecture is an extension of `chemprop-IR` described in the paper [Message Passing Neural Networks for Infrared Spectral Predictions](https://pubs.acs.org/doi/full/10.1021/acs.jcim.1c00055) and available in the [Chemprop-IR GiHub repository](https://github.com/gfm-collab/chemprop-IR).


## Docker

Docker provides a nice way to isolate the code and environment. To install and run our code in a Docker container, follow these steps:

1. Install Docker from [https://docs.docker.com/install/](https://docs.docker.com/install/)
2. `cd /path/to/project`
3. `docker build -t hqnn .`
4. `docker run -it --gpus all -v $(pwd):/project hqnn /bin/bash`

Note:
To enable GPU support, you must use a CUDA-enabled base image in the Dockerfile. You can replace the default line with a CUDA/cuDNN/Ubuntu base image that matches your environment. You can find options at [https://hub.docker.com/r/nvidia/cuda/tags](https://hub.docker.com/r/nvidia/cuda/tags). Make sure the CUDA version also matches the PyTorch version you are using. You can refer to the compatibility chart here: [https://pytorch.org/get-started/previous-versions/](https://pytorch.org/get-started/previous-versions/)



## Training

To train a model, run:
```
cd /path/to/project/
python ./chempropIRZenodo/chempropIR/train.py --data_path <path> --dataset_type spectra --checkpoint_path <checkpoint> --save_dir <dir>
```
where `<path>` is the path to a CSV file containing a spectral dataset,`dataset_type` is set to `spectra`. `<checkpoint>` is the path to a pretrained model file (e.g., `model.pt`). This argument is used when you want to **fine-tune** an existing model instead of training from scratch, and `<dir>` is the directory where model checkpoints will be saved.

The example spectral dataset format in a CSV file:
```
smiles,400,402,404,...,3996,3998,4000
OCc1cc(F)cc(F)c1,0.000423112823390177,0.0004251490935022775,...,0.0004340529928113568
```


We recommend using the training configuration provided in `/path/to/project/recommended_config.json`. You can specify a config file using `--config_path <config>`. We also suggest using a GPU, which can be selected using the `--gpu <index>` where `<index>` indicates the GPU device ID to use (if available).

To use the HQNN (Hybrid Quantum Neural Network) model, you must include the `--qnn` flag.  
This enables quantum layers in the network. You can also control the number of quantum hidden layers using the `--qnn_layer <int>` argument. If the `--qnn` flag is not specified, a standard FFNN (Feedforward Neural Network) model will be used instead.

An example script for training is provided at: `/path/to/project/scripts/run_train.sh`
To use it, run the following commands:
```
cd /path/to/project
./scripts/run_train.sh
```


## Predicting

To load a trained model and make predictions, run `chempropIRZenodo/chempropIR/predict.py` and specify:
* `--test_path <path>` Path to the data to predict on. Format this file as a `.csv` file with only a single column, with the header row with the entry `smiles` and every subsequent row entered with the SMILES you would like to predict.
* `--checkpoint_path <path>` Path to a model checkpoint file (`.pt` file).
* `--preds_path` Path where a CSV file containing the predictions will be saved.
* `--qnn` If the model checkpoint is HQNN model.
An example script for training is provided at: `/path/to/project/scripts/run_pred.sh`
To use it, run the following commands:
```
cd /path/to/project
./scripts/run_predict.sh
```

We suggest using a GPU, which can be selected using the `--gpu <index>` where `<index>` indicates the GPU device ID to use (if available).
