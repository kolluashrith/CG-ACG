#Jaccard.py

import argparse
import random as rng

#Need parser to allow for CLI flags
parser = argparse.ArgumentParser(description="sim_mutations argument parser")

parser.add_argument('-a', '--sequence1', type=str, help="Sequence 1 to compare")
parser.add_argument('-b', '--sequence2', type=str, help="Sequence 2 to compare")
parser.add_argument('-k', '--kmer_length', type=int, help="length of kmer to compute Jaccard coefficient")

args = parser.parse_args()

#Open required files
input_file = open(args.input)
output_file = open(args.output, 'w')

