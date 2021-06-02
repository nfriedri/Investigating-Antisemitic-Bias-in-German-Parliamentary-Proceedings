# -*- coding: utf-8 -*-
from gensim.utils import save_as_line_sentence
from text_preprocessing import *
import logging
import codecs
from environment import DATA_DIR

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

lemmatizer = GermanLemmatizer()
logging.info('Lemmatizer loaded.')

os.chdir(DATA_DIR)

class ProcessProtocols(object):
    def __init__(self, input):
        self.input = input
    def process_and_save(self):
        logging.info('Start processing of file.')
        try:
             text = codecs.open(os.path.join(DATA_DIR, self.input),'r', encoding='utf-8', errors='ignore').readlines()
             text = remove_punctuation(text)
             text = remove_double_spaces(text)
             text = remove_noisy_digits(text)
             text = remove_dash_and_minus_signs(text)
             text = replace_digits(text)
             text = remove_double_spaces(text)
             text = reduce_numerical_sequences(text)
             text = filter_doc(text)
             text = [remove_german_chainwords(line) for line in text]
             logging.info('Chainword splitting finished')
             text = [remove_hyphens(line) for line in text]
             text = [lemmatizer.lemmatize(line) for line in text]
             logging.info('Lemmatizing finished')
             text = [lowercase(line) for line in text]
             text = [remove_umlauts(line) for line in text]
             text = [harmonizeSpelling(line) for line in text_preprocessing]
             if self.input.endswith('.txt'):
                save_as_line_sentence(text, f'{self.input[:-4]}_processed.txt')
             else:
                save_as_line_sentence(text, f'{self.input}_processed.txt')
             logging.info('Processing finished')

        except FileNotFoundError:
            print(f'File was not found.')

if __name__ == "__main__":
  try:
    filename = sys.argv[1]
  except IndexError as e:
    print(e)

    ProcessProtocols(filename).process_and_save()


