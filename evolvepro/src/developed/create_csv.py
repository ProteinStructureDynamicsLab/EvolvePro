def create_csv(df_test , df_reference):

    df1 = pd.read_csv(df_test)
    df2 = pd.read_csv(df_reference)

    top_10_variants = df1['variant'].head(11)

    # Search to obtain scores in reference dataframe
    merged_df = df2[df2['hgvs_pro'].isin(top_10_variants)]

    # Create new dataframe with 'variant' and 'score' columns
    df1['score'] = df1['variant'].map(merged_df.set_index('hgvs_pro')['score'])
    df1 = df1.rename(columns={'variant': 'Variant' , 'score': 'activity'})

    #slice first letter of the variant column
    df1['Variant'] = df1['Variant'].str[1:]
    
    #save csv in folder
    file_path = os.path.join(round_base_path , round_file_name)
    df1[['Variant', 'activity']].to_csv(file_path , index=False)
    
    return df1[['Variant', 'activity']]
