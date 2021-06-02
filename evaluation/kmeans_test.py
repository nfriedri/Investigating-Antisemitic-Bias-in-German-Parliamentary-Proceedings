# -*- coding: utf-8 -*-
import sys

sys.path.append('./..')
from utils import load_vocab, load_vectors
import os
import glob
from eval import eval_k_means
from weat import XWEAT
from pathlib import Path
import argparse
import environment as env

# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# vocab_path = Path((os.path.join(ROOT_DIR, "../data/vocab")))
# models_path = Path((os.path.join(ROOT_DIR, "../models")))

weat_tests_antisem = [XWEAT().weat_1, XWEAT().weat_2, XWEAT().weat_3, XWEAT().weat_4]
DIMENSIONS_antisem = ['sentiment', 'patriotism', 'economic', 'conspiratorial', 'religious', 'racist', 'ethic']
weat_tests_anticom = [XWEAT().weat_5]
DIMENSIONS_anticom = ['sentiment', 'political', 'propaganda']


def main():
    parser = argparse.ArgumentParser(description="Running K-means test")
    parser.add_argument("--vocab_file_pattern", type=str, default=None,
                        help="vocab path file or file pattern in case of multiple files", required=True)
    parser.add_argument("--vector_file_pattern", type=str, default=None,
                        help="vector path file or file pattern in case of multiple files", required=True)
    parser.add_argument("--protocol_type", nargs='?', choices=['RT', 'BRD'],
                        help="Whether to run test for Reichstagsprotokolle (RT) or Bundestagsprotokolle (BRD)",
                        required=True)
    parser.add_argument("--area", nargs="?", choices=["antisem", "anticom"])
    args = parser.parse_args()

    if args.area is not None:
        env.set_area(args.area)

    if env.AREA == "antisem":
        vocab_files = f'{env.VOCAB_ANTISEM_DIR}/{str(args.vocab_file_pattern)}'
        vector_files = f'{env.VECTOR_ANTISEM_DIR}/{str(args.vector_file_pattern)}'
        for voc, vec in zip(vocab_files, vector_files):
            file_name = os.path.splitext(os.path.basename(voc))[0]
            vocab = load_vocab(voc)
            vectors = load_vectors(vec)
            with open(f'{env.KMEANS_OUTPUTS}/antisem/{file_name}.txt', 'w') as f:
                for test in weat_tests_antisem:
                    for dim in DIMENSIONS_antisem:
                        f.write(f'K-means score {test.__name__}: ')
                        targets_1 = test(dim, args.protocol_type, )[0]
                        targets_2 = test(dim, args.protocol_type)[1]
                        k_means_score = eval_k_means(targets_1, targets_2, vectors, vocab)
                        f.write(str(k_means_score))
                        f.write('\n')
            f.close()
    if env.AREA == "anticom":
        vocab_files = f'{env.VOCAB_ANTICOM_DIR}/{str(args.vocab_file_pattern)}'
        vector_files = f'{env.VECTOR_ANTICOM_DIR}/{str(args.vector_file_pattern)}'
        for voc, vec in zip(vocab_files, vector_files):
            file_name = os.path.splitext(os.path.basename(voc))[0]
            vocab = load_vocab(voc)
            vectors = load_vectors(vec)
            with open(f'{env.KMEANS_OUTPUTS}/antisem/{file_name}.txt', 'w') as f:
                for test in weat_tests_antisem:
                    for dim in DIMENSIONS_antisem:
                        f.write(f'K-means score {test.__name__}: ')
                        targets_1 = test(dim, args.protocol_type, )[0]
                        targets_2 = test(dim, args.protocol_type)[1]
                        k_means_score = eval_k_means(targets_1, targets_2, vectors, vocab)
                        f.write(str(k_means_score))
                        f.write('\n')
            f.close()


if __name__ == '__main__':
    main()
