def load_experimental_csv(base_path: str, round_file_name: str, wt_fasta_path: str, single_mutant: bool = True) -> pd.DataFrame:
    """
    MODDED:
    Originariamente "load_experimental_data"
    
    
    Load experimental data from file and process variants.

    Args:
        base_path (str): Base path to the data directory.
        round_file_name (str): Name of the round file.
        wt_fasta_path (str): Path to the wild-type FASTA file.
        single_mutant (bool, optional): Flag for single mutant processing. Defaults to True.

    Returns:
        pd.DataFrame: Processed experimental data.
    """
    # Load experimental data
    file_path = os.path.join(base_path, round_file_name)
    #file_path = round_file_name
    
    #cambiato tipo file in lettura
    df1 = pd.read_csv(file_path)
    
    
    # Load wild-type sequence
    WT_sequence = str(SeqIO.read(wt_fasta_path, "fasta").seq)

    # Process variants
    if single_mutant:
        df1['updated_variant'] = df1['Variant'].apply(lambda x: process_variant(x, WT_sequence))
        
    else:
        df1.rename(columns={'Variant': 'updated_variant'}, inplace=True)
    
    df1.head()
    return df1
