#!/bin/bash
#SBATCH --job-name=epro_iter        # Nome del job
#SBATCH --output=iter.out      # File di output
#SBATCH --error=iter.err       # File di errore
#SBATCH --ntasks=8                       # Numero di task
#SBATCH --cpus-per-task=1               # Numero di CPU per task
#SBATCH --mem=32G                        # Memoria da assegnare al job
#SBATCH --gres=gpu:1                     # Numero di GPU richieste
#SBATCH --time=24:00:00                  # Tempo massimo di esecuzione
#SBATCH --partition=test           # Partizione su cui eseguire il job
#SBATCH --nodelist=biocluster7     # Nodo su cui eseguire il job

srun conda run -n evolvepro python ../evoex_mk2.py
