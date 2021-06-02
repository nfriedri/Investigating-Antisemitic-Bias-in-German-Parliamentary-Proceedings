for slice in kaiserreich_1_processed kaiserreich_2_processed weimar_processed; do \
python simlex_test.py \
	--vocab_file_pattern ${slice}.json \
	--vector_file_pattern ${slice}.vectors.npy \
	--output_file ${slice}.txt \
	--area antisem
done

for slice in cdu_1 spd_1 cdu_2 spd_2 cdu_3; do \
python simlex_test.py \
	--vocab_file_pattern ${slice}.json \
	--vector_file_pattern ${slice}.vectors.npy \
	--output_file ${slice}.txt \
	--area antisem
done