for slice in kaiserreich_1 kaiserreich_2 weimar ns ; do \
  for dom in sentiment political propaganda; do \
    python propagate.py \
	    --ppmi ppmi_${slice}.npz \
      --index ${slice}.json \
      --protocol_type RT \
      --semantic_domain $dom \
      --output_file ${slice} \
      --area anticom
  done
done

for slice in cdu_1 spd_1 cdu_2 spd_2 cdu_3; do \
  for dom in sentiment political propaganda; do \
    python propagate.py \
      --ppmi ppmi_${slice}.npz \
      --index ${slice}.json \
      --protocol_type BRD \
      --semantic_domain $dom \
      --output_file ${slice} \
      --area anticom
  done
done
