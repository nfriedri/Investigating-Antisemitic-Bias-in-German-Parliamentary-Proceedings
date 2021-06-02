for slice in kaiserreich_1 kaiserreich_2 ns weimar; do \
  python create_ppmi_mat.py \
    --protocols reichstag/${slice}_processed \
    --protocol_type RT \
    --min_count 10 \
    --window_size 2 \
    --output_file ${slice} \
    --area antisem
done

for slice in cdu_1 spd_1 cdu_2 spd_2 cdu_3; do \
  python create_ppmi_mat.py \
    --protocols bundestag/${slice} \
    --protocol_type BRD \
    --min_count 10 \
    --window_size 2 \
    --output_file ${slice} \
    --area antisem
done