 
def imputeCategoricalVarible(df):
    col_to_impute = ['collision_type','property_damage','police_report_available']
    def zeroone(x):
        if x is np.nan:
            return 1
        return 0
    for col in col_to_impute:
        df['imputed'+col] = df[col].apply(zeroone)
        val_to_impute =df[col].value_counts().index[0]
        df[col]=df[col].fillna(val_to_impute)
    return df

def preprocessing(data):
    drop_col = ['_c39','policy_number','policy_bind_date','policy_state','insured_zip','incident_location','incident_date','incident_state','incident_city','insured_hobbies','auto_make','auto_model','auto_year']
    data = data.drop(columns=drop_col)
    data = data.replace('?',np.nan)
    data = imputeCategoricalVarible(data)
    categorical_df = data.select_dtypes(include=['object']).copy()
    encoder = OneHotEncoder(categories='auto',drop=None,sparse=False)
    onehot_df = pd.DataFrame(encoder.fit_transform(categorical_df))
    onehot_col = list(encoder.get_feature_names())
    onehot_df.columns = onehot_col
    numerical_df = data.select_dtypes(exclude=['object']).copy()
    standerdiser = StandardScaler()
    standerdiser_df = pd.DataFrame(standerdiser.fit_transform(numerical_df))
    standerdiser_df.columns=numerical_df.columns
    final_onehot_df = pd.concat([onehot_df,standerdiser_df],axis=1)
    return final_onehot_df
