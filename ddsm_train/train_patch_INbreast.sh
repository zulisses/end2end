#!/bin/bash

TRAIN_DIR="/home/ulisses/INbreast/patches_2/train_out"
VAL_DIR="/home/ulisses/INbreast/patches_2/val_out"
TEST_DIR="/home/ulisses/INbreast/patches_2/test_out"
#RESUME_FROM="Combined_patches_im4096_256_v3/3cls_best_model3.h5"
BEST_MODEL="/home/ulisses/INbreast/patches_2/best_model.h5"
#FINAL_MODEL="Combined_patches_im4096_256_v3/3cls_final_model4.h5"
FINAL_MODEL="/home/ulisses/INbreast/patches_2/finalmodel.h5"

export NUM_CPU_CORES=12

python patch_clf_train.py \
	--img-size 224 224 \
    --img-scale 224.0 \
	--featurewise-center \
    --featurewise-mean 44.33 \
    --equalize-hist \
	--batch-size 32 \
    --train-bs-multiplier 1 \
	--augmentation \
	--class-list background mal ben \
	--nb-epoch 3 \
    --top-layer-epochs 13 \
    --all-layer-epochs 35 \
    --no-load-val-ram \
    --no-load-train-ram \
    --net resnet50 \
    --optimizer adam \
    --use-pretrained \
    --top-layer-nb 46 \
    --weight-decay 0.001 \
    --weight-decay2 0.01 \
    --hidden-dropout 0.4 \
    --hidden-dropout2 0.5 \
    --init-learningrate 0.001 \
    --top-layer-multiplier 0.1 \
    --all-layer-multiplier 0.01 \
	--lr-patience 2 \
	--es-patience 8 \
	--no-resume-from \
	--auto-batch-balance \
    --pos-cls-weight 1.24458 \
	--neg-cls-weight 0.83576\
    --nb-init-filter 64 \
    --init-filter-size 7 \
    --init-conv-stride 2 \
    --max-pooling-size 3 \
    --max-pooling-stride 2 \
    --alpha 0.0001 \
    --l1-ratio 0.0 \
    --inp-dropout 0.0 \
	--best-model $BEST_MODEL \
	--final-model $FINAL_MODEL \
	$TRAIN_DIR $VAL_DIR $TEST_DIR	
