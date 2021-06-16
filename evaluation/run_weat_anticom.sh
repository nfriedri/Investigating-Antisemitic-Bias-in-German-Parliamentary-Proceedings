for slice in kaiserreich_1 kaiserreich_2 weimar; do \
    for att in sentiment political propaganda; \
      do python weat.py \
          --test_number 5 \
          --protocol_type RT \
          --permutation_number 12870 \
          --lower False \
          --sem_domain $att \
          --is_vec_format False \
          --embedding_vectors ${slice}.vectors.npy \
          --embedding_vocab ${slice}.json \
          --output_file weat5_${att}_${slice}.txt \
          --area anticom
    done;
done;

for slice in cdu_1 spd_1 cdu_2 spd_2 cdu_3; do \
    for att in sentiment political propaganda; \
      do python weat.py \
          --test_number 5 \
          --protocol_type BRD \
          --permutation_number 12870 \
          --lower False \
          --sem_domain $att \
          --is_vec_format False \
          --embedding_vectors ${slice}.vectors.npy \
          --embedding_vocab ${slice}.json \
          --output_file weat5_${att}_${slice}.txt \
          --area anticom
    done;
done;