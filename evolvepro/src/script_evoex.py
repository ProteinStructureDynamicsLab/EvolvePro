from evolvepro.src.evolve import evolve_experimental, evolve_experimental_multi
from evolvepro.src.data import create_csv

iteration = 'number of iterations(int)'
protein_name = 'protein_name'
embeddings_base_path = 'path/to/embd'
embeddings_file_name = 'embd_file_name'
round_base_path = 'path_to_rounds'
wt_fasta_path = 'path/to/wt/fasta'
number_of_variants = 'variants_per_round(int)'
output_dir = 'path/to/output/'
reference_file = 'path/to/file'
first_round_file = 'protein_name_Round1.csv file (user-defined)'

for i in range(0, iteration):

	if i == 0 :
	    round_name = 'Round1'
	    round_file_names = [first_round_file]
	
	    rename_WT = False
	
	else:

	    # Single variant
	    round_name = f'Round{i+1}'
	    round_file_names = []

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

	path_to_output = os.path.join((output_dir, protein_name, round_name , 'df_test.csv'))

	next_file_name = f'{protein_name}_Round{i+2}'

    create_csv(path_to_output , reference_file , number_of_variants , round_file_names , next_file_name)

    round_file_names.append(next_file_name + '.csv')
