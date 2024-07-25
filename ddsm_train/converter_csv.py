import pandas as pd;

# python converter_csv.py /home/ulisses/Imagens/descriptive/calc_case_description_train_set.csv /home/ulisses/Imagens/descriptive/metadata.csv

calc_test_description = '/home/ulisses/DDSM-all/calc_case_description_test_set.csv' 
calc_train_description = '/home/ulisses/DDSM-all/calc_case_description_train_set.csv'
mass_train_descriptive = '/home/ulisses/DDSM-all/mass_case_description_train_set.csv'
mass_test_descriptive = '/home/ulisses/DDSM-all/mass_case_description_test_set.csv'
metadata = '/home/ulisses/DDSM-all/metadata.csv'
out_dir = "/home/ulisses/DDSM-all"

def run():
    calc_test_description_df = pd.read_csv(calc_test_description, header=0)
    calc_train_description_df = pd.read_csv(calc_train_description, header=0)
    mass_train_descriptive_df = pd.read_csv(mass_train_descriptive, header=0)
    mass_test_descriptive_df = pd.read_csv(mass_test_descriptive, header=0)
    
    columns = ['patient_id', 'side', 'view', 'abn_num', 'pathology', 'type']
    df = pd.DataFrame(columns=columns)
    
    df['patient_id'] = pd.concat([mass_train_descriptive_df['patient_id'], mass_test_descriptive_df['patient_id'], calc_test_description_df['patient_id'], calc_train_description_df['patient_id']])
    df['side'] = pd.concat([mass_train_descriptive_df['left or right breast'], mass_test_descriptive_df['left or right breast'], calc_test_description_df['left or right breast'], calc_train_description_df['left or right breast']])
    df['view'] = pd.concat([mass_train_descriptive_df['image view'], mass_test_descriptive_df['image view'], calc_test_description_df['image view'], calc_train_description_df['image view']])
    df['abn_num'] = pd.concat([mass_train_descriptive_df['abnormality id'], mass_test_descriptive_df['abnormality id'], calc_test_description_df['abnormality id'], calc_train_description_df['abnormality id']])
    df['pathology'] = pd.concat([mass_train_descriptive_df['pathology'], mass_test_descriptive_df['pathology'], calc_test_description_df['pathology'], calc_train_description_df['pathology']])
    df['type'] = pd.concat([mass_train_descriptive_df['abnormality type'], mass_test_descriptive_df['abnormality type'], calc_test_description_df['abnormality type'].map(lambda s: "calc"), calc_train_description_df['abnormality type'].map(lambda s: "calc")])
    
    df.to_csv(out_dir + '/roi_mask_path.csv', index=False)
    
    print(df)
    
    metadata_df = pd.read_csv(metadata, header=0)
    
    df = pd.DataFrame(columns=['patient_id'])
    lista_pat = []

    
    for subject in metadata_df['Subject ID']:
        subject_split = subject.split('_')
        lista_pat.append('P_' + subject_split[2])
        
    df['patient_id'] = pd.Series(lista_pat).unique()
    
    df.to_csv(out_dir + '/pat_train_list.csv', index=False)
    
    print(df)


if __name__ == '__main__':
    run()