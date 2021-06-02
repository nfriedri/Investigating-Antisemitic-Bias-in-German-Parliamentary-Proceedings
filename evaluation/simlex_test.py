# -*- coding: utf-8 -*-
import sys
from utils import load_vocab, load_vectors
import os
from eval import eval_simlex
import argparse
import environment as env

sys.path.append('./..')


# Get simlex pairs
with open(os.path.join(env.ROOT_DIR, 'MSimLex999_German.csv'), encoding='utf-8') as f:
    text = f.readlines()
    simlex_pairs = []
    for line in text:
        elements = line.split(',')
        simlex_pair = [elements[0], elements[1], elements[-1].strip()]
        simlex_pairs.append(simlex_pair)

simlex_pairs.pop(0)


def main():
    parser = argparse.ArgumentParser(description="Running Simlex test")
    parser.add_argument("--vocab_file_pattern", type=str, default=None,
                        help="vocab path file or file pattern in case of multiple files", required=True)
    parser.add_argument("--vector_file_pattern", type=str, default=None,
                        help="vector path file or file pattern in case of multiple files", required=True)
    parser.add_argument("--output_file", type=str, default=None, help="file to write output to", required=True)
    parser.add_argument("--area", nargs="?", choices=["antisem", "anticom"])

    args = parser.parse_args()
    if args.area is not None:
        env.set_area(args.area)
    output_file, vocab_files, vector_files = "", "", ""
    if env.AREA == "antisem":
        vocab_files = f'{env.VOCAB_ANTISEM_DIR}/{args.vocab_file_pattern}'
        vector_files = f'{env.VECTOR_ANTISEM_DIR}/{args.vector_file_pattern}'
    if env.AREA == "anticom":
        vocab_files = f'{env.VOCAB_ANTICOM_DIR}/{args.vocab_file_pattern}'
        vector_files = f'{env.VECTOR_ANTICOM_DIR}/{args.vector_file_pattern}'

    with open(f'{env.SIMLEX_OUTPUTS}/{args.output_file}', 'w') as f:
        for voc, vec in zip(vocab_files, vector_files):
            file_name = os.path.splitext(os.path.basename(voc))[0][4:]
            vocab = load_vocab(voc)
            vectors = load_vectors(vec)
            simlex_score = eval_simlex(simlex_pairs, vocab, vectors)
            f.write('{}: {}'.format(file_name, simlex_score))
            f.write('\n')
        f.close()


if __name__ == '__main__':
    main()
