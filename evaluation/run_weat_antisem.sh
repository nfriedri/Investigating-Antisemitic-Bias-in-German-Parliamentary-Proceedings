for slice in kaiserreich_1_processed kaiserreich_2_processed weimar_processed; do \
  for i in 1; do \
    for att in sentiment patriotism economic conspiratorial religious racist ethic; \
      do python weat.py \
          --test_number $i \
          --protocol_type RT \
          --permutation_number 12870 \
          --lower False \
          --sem_domain $att \
          --is_vec_format False \
          --embedding_vectors ${slice}.vectors.npy \
          --embedding_vocab ${slice}.json \
          --output_file weat${i}_${att}_${slice}.txt \
          --area antisem
    done;
  done;
done;

for slice in cdu_1 spd_1 cdu_2 spd_2 cdu_3; do \
  for i in 1; do \
    for att in sentiment patriotism economic conspiratorial religious racist ethic; \
      do python weat.py \
          --test_number $i \
          --protocol_type BRD \
          --permutation_number 12870 \
          --lower False \
          --sem_domain $att \
          --is_vec_format False \
          --embedding_vectors ${slice}.vectors.npy \
          --embedding_vocab ${slice}.json \
          --output_file weat${i}_${att}_${slice}.txt \
          --area antisem
    done;
  done;
done;