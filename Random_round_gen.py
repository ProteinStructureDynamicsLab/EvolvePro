#!/usr/bin/env python
# coding: utf-8

# ## Random round file generator

# In[9]:


import io
import sys
from evolvepro.src.process import suggest_initial_mutants
import pandas as pd
import os

for i in range(1, 31):

    file_name = f'random{i}.csv'
    path_to_file = os.path.join('randomized_iter' , file_name)
    
    #converting buffer to string
    buffer = io.StringIO()

    #redirecting output to buffer
    sys.stdout = buffer
    
    #variant randomizer (prints on screen)
    suggest_initial_mutants( 'suggested_mutants/GPR68_mut2.fasta', num_mutants=10 )
    
    #capture buffer output
    file = buffer.getvalue()

    #parse file line
    file = [line.split()[-1] for line in file.split('\n')[2:] if line.strip()]

    #convert 'file' to dataframe
    df = pd.DataFrame({'variant': file})

    #load df and reference df
    df1 = df
    df_ref = pd.read_csv('gpr68_ref.csv')

    #select top 10 found (skippable, prolly)
    top_10_variants = df1['variant'].head(11)
    
    # Search to obtain scores in reference dataframe
    merged_df = df_ref[df_ref['hgvs_pro'].isin(top_10_variants)]
    
    # Create new dataframe with 'variant' and 'score' columns
    df1['score'] = df1['variant'].map(merged_df.set_index('hgvs_pro')['score'])
    df1 = df1.rename(columns={'variant': 'Variant' , 'score': 'activity'})
    
    #slice first letter of the variant column
    df1['Variant'] = df1['Variant'].str[1:]
    
    #save csv in folder
    df1[['Variant', 'activity']].to_csv(path_to_file , index=False)


# In[13]:





# In[ ]:




