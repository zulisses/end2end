import pandas as pd
import os, sys, argparse
from dm_image import read_resize_img
import imageio
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#### Define some functions to use ####
def const_filename(pat, side, view, directory, itype=None, abn=None):
    token_list = [pat, side, view]
    if itype is not None:
        token_list.insert(0, ('Calc' if itype == 'calc' else 'Mass') + '-Test') #-Training ou -Test
        token_list.append(str(abn))
    fn = "_".join(token_list) + ".png"
    return os.path.join(directory, fn)

def run(roi_mask_path_file, pat_train_list_file, full_img_dir, 
        train_out_dir, val_out_dir,
        target_height=4096, target_width=None, val_size=.1,
        pos_dir='mal', neg_dir='ben'):

    # Print info for book-keeping.
    print ("Pathology file=", roi_mask_path_file)
    print ("Patient train list=", pat_train_list_file)
    print ("Full image dir=", full_img_dir)
    print ("Train out dir=", train_out_dir)
    print ("Val out dir=", val_out_dir)
    print ("===")
    sys.stdout.flush()

    # Read ROI mask table with pathology.
    roi_mask_path_df = pd.read_csv(roi_mask_path_file, header=0)
    roi_mask_path_df = roi_mask_path_df.set_index(['patient_id', 'side', 'view'])
    roi_mask_path_df.sort_index(inplace=True)
    # Read train set patient IDs and subset the table.
    pat_train = pd.read_csv(pat_train_list_file, header=0)
    pat_train = pat_train.values.ravel()
    if len(pat_train) > 1:
        path_df = roi_mask_path_df.loc[pat_train.tolist()]
    else:
        locs = roi_mask_path_df.index.get_loc(pat_train[0])
        path_df = roi_mask_path_df.iloc[locs]
    # Determine the labels for patients.
    pat_labs = []
    for pat in pat_train:
        pathology = path_df.loc[pat]['pathology']
        malignant = 0
        for path in pathology:
            if path.startswith('MALIGNANT'):
                malignant = 1
                break
        pat_labs.append(malignant)
    # Split patient list into train and val lists.
    def write_pat_list(fn, pat_list):
        with open(fn, 'w') as f:
            for pat in pat_list:
                f.write(str(pat) + "\n")
            f.close()
    if val_size > 0:
        # import pdb; pdb.set_trace()
        pat_train, pat_val, labs_train, labs_val = train_test_split(
            pat_train, pat_labs, stratify=pat_labs, test_size=val_size,
            random_state=12345)
        if len(pat_val) > 1:
            val_df = roi_mask_path_df.loc[pat_val.tolist()]
        else:
            locs = roi_mask_path_df.index.get_loc(pat_val[0])
            val_df = roi_mask_path_df.iloc[locs]
        write_pat_list(os.path.join(val_out_dir, 'pat_lst.txt'), pat_val.tolist())
    if len(pat_train) > 1:
        train_df = roi_mask_path_df.loc[pat_train.tolist()]
    else:
        locs = roi_mask_path_df.index.get_loc(pat_train[0])
        train_df = roi_mask_path_df.iloc[locs]
    write_pat_list(os.path.join(train_out_dir, 'pat_lst.txt'), pat_train.tolist())

    #### Define a functin to sample patches.
    def do_sampling(pat_df, out_dir):
        for pat,side,view in pat_df.index.unique():
            full_fn = const_filename(pat, side, view, full_img_dir)
            # import pdb; pdb.set_trace()
            try:
                if target_width is None:
                    full_img = read_resize_img(full_fn, target_height=target_height)
                else:
                    full_img = read_resize_img(full_fn, target_size=(target_height, target_width))
                    
                # plt.imshow(full_img, cmap='gray')
                # plt.axis('off')
                # plt.show()


                # Read mask image(s).
                abn_path = roi_mask_path_df.loc[pat].loc[side].loc[view]
                if isinstance(abn_path, pd.Series):
                    pathology = [abn_path['pathology']]
                else:
                    pathology = abn_path['pathology']
                    
                pos = False
                for path in pathology:
                    if(path.startswith('MALIGNANT')):
                        pos = True
                    
                if pos:
                    roi_out = os.path.join(out_dir, pos_dir)
                else:
                    roi_out = os.path.join(out_dir, neg_dir)
                
                filename = pat + "_" + side + "_" + view + ".png"
                fullname = os.path.join(roi_out, filename)
                
                patch_img = imageio.core.util.Array(full_img.astype('int32'))
                imageio.imwrite(fullname, patch_img)
                
            except AttributeError:
                print ("Read image error: %s" % (full_fn))
            except ValueError:
                print ("Error sampling from ROI mask image: %s" % ())

    #####
    print ("Sampling for train set")
    sys.stdout.flush()
    do_sampling(train_df, train_out_dir)
    print ("Done.")
    #####
    if val_size > 0.:
        print ("Sampling for val set")
        sys.stdout.flush()
        do_sampling(val_df, val_out_dir)
        print ("Done.")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Sample patches for DDSM images")
    parser.add_argument("roi_mask_path_file", type=str)
    parser.add_argument("pat_train_list_file", type=str)
    parser.add_argument("full_img_dir", type=str)
    parser.add_argument("train_out_dir", type=str)
    parser.add_argument("val_out_dir", type=str)
    parser.add_argument("--target-height", dest="target_height", type=int, default=4096)
    parser.add_argument("--target-width", dest="target_width", type=int, default=None)
    parser.add_argument("--no-target-width", dest="target_width", action="store_const", const=None)
    parser.add_argument("--val-size", dest="val_size", type=float, default=.1)
    parser.add_argument("--pos-dir", dest="pos_dir", type=str, default="mal")
    parser.add_argument("--neg-dir", dest="neg_dir", type=str, default="ben")
    parser.set_defaults(verbose=True)

    args = parser.parse_args()
    run_opts = dict(
        target_height=args.target_height,
        target_width=args.target_width,
        val_size=args.val_size,
        pos_dir=args.pos_dir,
        neg_dir=args.neg_dir,
    )
    print ("\n>>> Model training options: <<<\n", run_opts, "\n")
    run(args.roi_mask_path_file, args.pat_train_list_file,
        args.full_img_dir, args.train_out_dir, args.val_out_dir, **run_opts)