#!/bin/bash
ROI_MASK_PATH_FILE="/home/ulisses/DDSM-all/roi_mask_path.csv"
PAT_TRAIN_LIST_FILE="/home/ulisses/DDSM-all/pat_train_list.csv"
ROI_MASK_DIR="/home/ulisses/DDSM-all/CBIS-DDSM-png/roi_mask_dir"
FULL_IMG_DIR="/home/ulisses/DDSM-all/CBIS-DDSM-png/full_img_dir"
TRAIN_OUT_DIR="/home/ulisses/DDSM-all/patchesbkg/test_out"
VAL_OUT_DIR="/home/ulisses/DDSM-all/patchesbkg/val_out"

python sample_patches_combined.py \
    --target-height 1152 \
    --target-width 896 \
    --patch-size 224 \
    --segment-breast \
    --nb-bkg 0 \
    --nb-abn 1 \
    --nb-hns 1 \
    --pos-cutoff 0.75 \
    --neg-cutoff 0.35 \
    --val-size 0 \
    --bkg-dir background \
    --calc-pos-dir calc_mal \
    --calc-neg-dir calc_ben \
    --mass-pos-dir mass_mal \
    --mass-neg-dir mass_ben \
    --verbose \
    $ROI_MASK_PATH_FILE $ROI_MASK_DIR $PAT_TRAIN_LIST_FILE $FULL_IMG_DIR $TRAIN_OUT_DIR $VAL_OUT_DIR



# parser.add_argument("roi_mask_path_file", type=str)
# parser.add_argument("roi_mask_dir", type=str)
# parser.add_argument("pat_train_list_file", type=str)
# parser.add_argument("full_img_dir", type=str)
# parser.add_argument("train_out_dir", type=str)
# parser.add_argument("val_out_dir", type=str)
# parser.add_argument("--target-height", dest="target_height", type=int, default=4096)
# parser.add_argument("--target-width", dest="target_width", type=int, default=None)
# parser.add_argument("--no-target-width", dest="target_width", action="store_const", const=None)
# parser.add_argument("--segment-breast", dest="segment_breast", action="store_true")
# parser.add_argument("--no-segment-breast", dest="segment_breast", action="store_false")
# parser.set_defaults(segment_breast=True)
# parser.add_argument("--patch-size", dest="patch_size", type=int, default=256)
# parser.add_argument("--nb-bkg", dest="nb_bkg", type=int, default=30)
# parser.add_argument("--nb-abn", dest="nb_abn", type=int, default=30)
# parser.add_argument("--nb-hns", dest="nb_hns", type=int, default=15)
# parser.add_argument("--pos-cutoff", dest="pos_cutoff", type=float, default=.75)
# parser.add_argument("--neg-cutoff", dest="neg_cutoff", type=float, default=.35)
# parser.add_argument("--val-size", dest="val_size", type=float, default=.1)
# parser.add_argument("--bkg-dir", dest="bkg_dir", type=str, default="background")
# parser.add_argument("--calc-pos-dir", dest="calc_pos_dir", type=str, default="calc_mal")
# parser.add_argument("--calc-neg-dir", dest="calc_neg_dir", type=str, default="calc_ben")
# parser.add_argument("--mass-pos-dir", dest="mass_pos_dir", type=str, default="mass_mal")
# parser.add_argument("--mass-neg-dir", dest="mass_neg_dir", type=str, default="mass_ben")
# parser.add_argument("--verbose", dest="verbose", action="store_true")
# parser.add_argument("--no-verbose", dest="verbose", action="store_false")
# parser.set_defaults(verbose=True)