for slice in kaiserreich_1 kaiserreich_2 weimar; do \
  python train_embeddings.py --protocols reichstag/${slice}_processed \
						--format gensim \
						--model_path ${slice} \
						--threads 1 \
						--model_architecture word2vec \
						--sg 0 \
						--vocab_path ${slice} \
						--min_count 2 \
						--area anticom
done

for slice in cdu_1 spd_1 cdu_2 spd_2 cdu_3; do \
  python train_embeddings.py --protocols reichstag/${slice}_processed \
						--format gensim \
						--model_path ${slice} \
						--threads 1 \
						--model_architecture word2vec \
						--sg 0 \
						--vocab_path ${slice} \
						--min_count 2 \
						--area anticom
done

