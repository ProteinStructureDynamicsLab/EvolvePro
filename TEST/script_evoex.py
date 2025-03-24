from evolvepro.src.evolve import evolve_experimental, evolve_experimental_multi
from evolvepro.src.data import create_csv
import os

iteration = 10
protein_name = 'GPR68'
embeddings_base_path = '/home/tigem/a.valente/develop/EvolvePro/TEST/GPRTEST/embeddings'
embeddings_file_name = 'GPR68_esm1b_t33_650M_UR50S.csv'
round_base_path = '/home/tigem/a.valente/develop/EvolvePro/TEST/GPRTEST/rounds'
wt_fasta_path = '/home/tigem/a.valente/develop/EvolvePro/TEST/GPRTEST/fasta/GPR68_WT.fasta'
number_of_variants = 10
output_dir = '/home/tigem/a.valente/develop/EvolvePro/TEST/GPRTEST/output'
reference_file = 'gpr68_ref.csv'
first_round_file = 'GPR68_Round1.csv'
round_file_names = []

for i in range(0, iteration):

    if i == 0 :
        round_name = 'Round1'
        round_file_names.append(first_round_file)

        rename_WT = False

    else:

		# Single variant
        round_name = f'Round{i+1}'
        rename_WT = False

    evolve_experimental(
	    protein_name,
	    round_name,
	    embeddings_base_path,
	   embeddings_file_name,
	    round_base_path,
	    round_file_names,
	    wt_fasta_path,
	    rename_WT,
	    number_of_variants,
	    output_dir
	)
    
    path_to_output = os.path.join(output_dir, protein_name, round_name , 'df_test.csv' )
    print(path_to_output)    

    next_file_name = f'{protein_name}_Round{i+2}.csv'
    print(next_file_name)

    create_csv(path_to_output , reference_file , number_of_variants , round_file_names , next_file_name , round_base_path)

    round_file_names.append(next_file_name)
