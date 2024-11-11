#!/bin/bash
ROI_MASK_PATH_FILE="/home/ulisses/DDSM-all/roi_mask_path.csv"
PAT_TRAIN_LIST_FILE="/home/ulisses/DDSM-all/full_train.csv"
FULL_IMG_DIR="/home/ulisses/DDSM-all/CBIS-DDSM-png/full_img_dir"
TRAIN_OUT_DIR="/home/ulisses/DDSM-all/full_images/train_out"
VAL_OUT_DIR="/home/ulisses/DDSM-all/full_images/train_out"

python separar_imagens_DDSM.py \
    --target-height 1152 \
    --target-width 896 \
    --val-size 0 \
    --pos-dir mal \
    --neg-dir ben \
    $ROI_MASK_PATH_FILE $PAT_TRAIN_LIST_FILE $FULL_IMG_DIR $TRAIN_OUT_DIR $VAL_OUT_DIR