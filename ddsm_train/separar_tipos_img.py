import pandas as pd;
import subprocess
import os

initial_dir = '/home/ulisses/DDSM-all'
metadata = '/home/ulisses/DDSM-all/metadata.csv'
full_img_dir = '/home/ulisses/DDSM-all/CBIS-DDSM-png/full_img_dir'
roi_mask_dir = '/home/ulisses/DDSM-all/CBIS-DDSM-png/roi_mask_dir'
cropped_img_dir = '/home/ulisses/DDSM-all/CBIS-DDSM-png/cropped_img_dir'

def run():
    metadata_df = pd.read_csv(metadata, header=0)
    metadata_df = metadata_df.set_index(['Subject ID', 'Series Description'])
    
    print(metadata_df.head()['File Location'])
    print()
    
    for subj, serie in metadata_df.index:
        # print(subj, serie, metadata_df.loc[subj, serie]['File Location'].values) 
        
        pwd_dicom = initial_dir + '/' + metadata_df.loc[subj, serie]['File Location'].values[0]
        print(pwd_dicom)
        if(serie == 'cropped images'):
            subprocess.run(['dcmj2pnm', '--write-png', '--min-max-window', '--verbose', pwd_dicom + '/1-1.dcm', cropped_img_dir + '/' + subj + '.png'])
        elif(serie == 'full mammogram images'):
            subprocess.run(['dcmj2pnm', '--write-png', '--min-max-window', '--verbose', pwd_dicom + '/1-1.dcm', full_img_dir + '/' + subj + '.png'])
        elif(serie == 'ROI mask images'):
            if  (os.path.exists(pwd_dicom + '/1-2.dcm')):
                subprocess.run(['dcmj2pnm', '--write-png', '--min-max-window', '--verbose', pwd_dicom + '/1-2.dcm', roi_mask_dir + '/' + subj + '.png'])
                subprocess.run(['dcmj2pnm', '--write-png', '--min-max-window', '--verbose', pwd_dicom + '/1-1.dcm', cropped_img_dir + '/' + subj + '.png'])
            else:
                subprocess.run(['dcmj2pnm', '--write-png', '--min-max-window', '--verbose', pwd_dicom + '/1-1.dcm', roi_mask_dir + '/' + subj + '.png'])
            
        

if __name__ == '__main__':
    run()