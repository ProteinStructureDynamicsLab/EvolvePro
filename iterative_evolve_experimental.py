from evolvepro.src.evolve import evolve_experimental, evolve_experimental_multi
from evolvepro.src.data import create_csv
import os


iteration = 10
protein_name = 'GPR68'
embeddings_base_path = './EvolvePro/TEST/GPRTEST/embeddings'
embeddings_file_name = 'GPR68_esm1b_t33_650M_UR50S.csv'
round_base_path = './EvolvePro/TEST/GPRTEST/rounds'
wt_fasta_path = './EvolvePro/TEST/GPRTEST/fasta/GPR68_WT.fasta'
number_of_variants = 10
output_dir = './EvolvePro/TEST/GPRTEST/output'
reference_file = 'gpr68_ref.csv'
first_round_file = 'GPR68_Round1.csv'
round_file_names = []
'''
    Arguments in function: 
    iteration: number of iterations desired (always an integer)
    protein_name: name of the protein analyzed. Creates a folder with the same name in the path selected for the output data
    embeddings_base_path: folder containing embeddings file
    embeddings_file_name: embeddings file (always a csv)
    round_base_path: folder that will contain round files (always csv). Those file will be used for iterations.
    wt_fasta_path: fasta containing folder path. Be sure to include the file name (path/to/file/filename)
    number_of_variants: number of variants tested per round. This will affect how many proposed variants you will get at the end of the iterations. (always an integer)
    output_dir: folder that will contain output files divided by round.
    reference_file: this is the reference file with experimental scores, parsed to be readable by the program. (always a csv)
    first_round_file: this is the first round file, user-defined and made by hand. in this file you should write the variants suggested in the random step.
    round_file_names: just a list of round file names. Used to automatize iterations. Do not fill.
'''

#this loop uses the user-defined file for the first round, then uses the created files to carry on iterations.

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
    
    #creation of the next round file based on the correspondant df_test.csv confronted with the reference file    
    create_csv(path_to_output , reference_file , number_of_variants , round_file_names , next_file_name , round_base_path)
    
    #round file name appending in list
    round_file_names.append(next_file_name)
