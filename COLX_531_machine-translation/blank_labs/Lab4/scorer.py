'''
Python code to evaluate the system outputs using BLEU

usage format:
> python scorer.py <task> <gold-file> <pred_file>

example usage for Machine Translation (Problem 1):
> python scorer.py mt machine_translation/dummy-example-mt-test-gold.tsv machine_translation/dummy-example-mt-test-pred.tsv

example usage for Paraphrase Generation (Problem 2):
> python scorer.py pp paraphrase_generation/dummy-example-pp-test-gold.tsv paraphrase_generation/dummy-example-pp-test-pred.tsv

'''

import os
import sys
from nltk.translate.bleu_score import corpus_bleu


NUM_MT_TEST_EXAMPLES = 4738
NUM_PP_TEST_EXAMPLES = 4692

'''
file utilties
'''
def count_number_of_lines_in_file(f):
  # counts the number of lines in the file
  num_lines = 0
  for line in open(f):
    line = line.strip()
    if len(line) != 0:
      num_lines += 1
  return num_lines

def check_if_header_is_present(f, header):
  # check if the first line has the right header
  r = open(f)
  first_line = r.readline()
  print(first_line)
  return first_line.strip() == header

if __name__ == '__main__':

  # check for 3 command-line arguments
  if len(sys.argv) != 4:
    print('ERROR: usage format: python scorer.py <task> <gold-file> <pred_file>')
    print('ERROR: please provide task (mt or pp), gold file and prediction file')
    sys.exit(0)

  # read command-line arguments
  task = sys.argv[1]
  gold_file = sys.argv[2]
  pred_file = sys.argv[3]

  # check for the file format
  if not os.path.exists(gold_file):
    print('ERROR: File %s does not exist'%gold_file)
    sys.exit(0)
  if not os.path.exists(pred_file):
    print('ERROR: File %s does not exist'%pred_file)
    sys.exit(0)
  num_lines = NUM_MT_TEST_EXAMPLES if task == "mt" else NUM_PP_TEST_EXAMPLES
  if count_number_of_lines_in_file(gold_file) != num_lines + 1:
    print('ERROR: File %s does not contain %d lines in it'%(gold_file, num_lines))
    sys.exit(0)
  if count_number_of_lines_in_file(pred_file) != num_lines + 1:
    print('ERROR: File %s does not contain %d lines in it'%(pred_file, num_lines))
    sys.exit(0)

  # create corpus_bleu inputs
  references = []
  candidates = []
  r_gold = open(gold_file)
  r_pred = open(pred_file)
  r_gold.readline() # skip header
  r_pred.readline() # skip header
  while True:
    reference = r_gold.readline()
    if not reference:
      break
    candidate = r_pred.readline()
    references.append([r.split() for r in reference.split("\t")])
    candidates.append(candidate.split())

  # compute corpus_bleu and print scores
  print('OVERALL SCORES:')
  print('Cumulative 1-gram: %f' % corpus_bleu(references, candidates, weights=(1, 0, 0, 0)))
  print('Cumulative 2-gram: %f' % corpus_bleu(references, candidates, weights=(0.5, 0.5, 0, 0)))
  print('Cumulative 3-gram: %f' % corpus_bleu(references, candidates, weights=(0.33, 0.33, 0.33, 0)))
  print('Cumulative 4-gram: %f' % corpus_bleu(references, candidates, weights=(0.25, 0.25, 0.25, 0.25)))
  print('BLEU (default, that is, Cumulative 4-gram): %f' % corpus_bleu(references, candidates))



