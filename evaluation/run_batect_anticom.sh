for slice in kaiserreich_1 kaiserreich_2 weimar; do \
  python ect_and_bat.py \
    --test_type ECT \
    --protocol_type RT \
    --output_file ${slice}_score \
    --vocab_file ${slice}.json \
    --vector_file ${slice}.vectors.npy \
    --area anticom
done;

for slice in cdu_1 spd_1 cdu_2 spd_2 cdu_3; do \
  python ect_and_bat.py \
    --test_type ECT \
    --protocol_type BRD \
    --output_file ${slice}_score \
    --vocab_file ${slice}.json \
    --vector_file ${slice}.vectors.npy \
    --area anticom
done;


