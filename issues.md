"""Processing gpr68_ph55_esmrank - Round1
Embeddings loaded: (7092, 20)
Loaded experimental data for Round1.csv: (10, 3)
iteration shape: (10, 2)
Labels shape: (7092, 5)
Embeddings and labels are aligned
(7082,)
/home/tigem/a.valente/EvolvePro/evolvepro/src/model.py:198: FutureWarning: The behavior of DataFrame concatenation with empty or all-NA entries is deprecated. In a future version, this will no longer exclude empty or all-NA columns when determining the result dtypes. To retain the old behavior, exclude the relevant entries before the concat operation.
  df_all = pd.concat([df_train, df_test])
/home/tigem/a.valente/miniconda3/envs/evolvepro/lib/python3.11/site-packages/numpy/lib/nanfunctions.py:1215: RuntimeWarning: Mean of empty slice
  return np.nanmean(a, axis, out=out, keepdims=keepdims)
Traceback (most recent call last):
  File "/home/tigem/a.valente/EvolvePro/iterative_evolve_experimental.py", line 49, in <module>
    evolve_experimental(
  File "/home/tigem/a.valente/EvolvePro/evolvepro/src/evolve.py", line 403, in evolve_experimental
    this_round_variants, df_test, df_sorted_all, model  = top_layer(
                                                          ^^^^^^^^^^
  File "/home/tigem/a.valente/EvolvePro/evolvepro/src/model.py", line 208, in top_layer
    top_variant = df_sorted_all.loc[df_sorted_all['y_actual_scaled'] == top_activity_scaled, 'variant'].values[0]
                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^
IndexError: index 0 is out of bounds for axis 0 with size 0"""


This error happened when i tried to use EvolvePro pipeline with ESMRank embeddings. Apparently, it is triggered by setting the "n_estimator" RandomForest parameter in the "top_layer"
function that lies in the "model.py" sheet.
This happens because the line "top_activity_scaled = df_sorted_all.loc[:final_round, 'y_actual_scaled'].max()" where "final_round" equals to 10, if there are no variants in the top 10 
gives back a NaN value that raises the previous error.

To solve this i commented the lines 206 to 211  in "model.py": those are additional metrics that are out of our scopes and needings.
