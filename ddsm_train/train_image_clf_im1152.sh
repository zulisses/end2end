#!/bin/bash

TRAIN_DIR="/home/ulisses/DDSM-all/full_images/train_out"
VAL_DIR="/home/ulisses/DDSM-all/full_images/val_out"
TEST_DIR="/home/ulisses/DDSM-all/full_images/test_out"
PATCH_STATE="/home/ulisses/DDSM-all/patch-models/s10_resnet50.h5"
BEST_MODEL="/home/ulisses/DDSM-all/Results_full/best_model_resnet50_s10_512-512-1024x2.h5"
FINAL_MODEL="/home/ulisses/DDSM-all/Results_full/final_model_resnet50_s10_512-512-1024x2.h5"

export NUM_CPU_CORES=12

# 255/65535 = 0.003891.
python image_clf_train.py \
	--patch-model-state $PATCH_STATE \
	--no-resume-from \
    --img-size 1152 896 \
    --no-img-scale \
    --rescale-factor 0.003891 \
	--featurewise-center \
    --featurewise-mean 52.18 \
    --no-equalize-hist \
    --top-depths 512 512 \
    --top-repetitions 3 3 \
    --batch-size 2 \
    --train-bs-multiplier 1 \
	--augmentation \
	--class-list ben mal \
	--nb-epoch 3 \
    --all-layer-epochs 5 \
    --no-load-val-ram \
    --no-load-train-ram \
    --optimizer adam \
    --weight-decay 0.0001 \
    --weight-decay2 0.001 \
    --hidden-dropout 0.1 \
    --hidden-dropout2 0.1 \
    --init-learningrate 0.0001 \
    --all-layer-multiplier 0.1 \
	--lr-patience 2 \
	--es-patience 10 \
	--auto-batch-balance \
    --pos-cls-weight 1.0 \
	--neg-cls-weight 1.0 \
	--best-model $BEST_MODEL \
	--final-model $FINAL_MODEL \
	$TRAIN_DIR $VAL_DIR $TEST_DIR	
