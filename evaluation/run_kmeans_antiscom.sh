for slice in kaiserreich_1 kaiserreich_2 weimar; do \
  python kmeans_test.py \
    --vocab_file ${slice}.json \
    --protocol_type RT \
    --vector_file ${slice}.vectors.npy \
    --area anticom
done

for slice in cdu_1 spd_1 cdu_2 spd_2 cdu_3; do \
python kmeans_test.py \
	--vocab_file ${slice}.json \
	--protocol_type BRD \
	--vector_file ${slice}.vectors.npy \
	--area anticom
done

