#Sim_mutations.py

import argparse
import random as rng

#Need parser to allow for CLI flags
parser = argparse.ArgumentParser(description="sim_mutations argument parser")

parser.add_argument('-i', '--input', type=str, help="path to input file")
parser.add_argument('-o', '--output', type=str, help="path to output file")
parser.add_argument('-m', '--mutation', type=float, help="proportion of input bases to change to different base")
parser.add_argument('-s', '--seed', type=int, help="random seed", default=42)

args = parser.parse_args()

#Open required files
input_file = open(args.input)
output_file = open(args.output, 'w')

#Copy over the fasta header line
output_file.write(f"{input_file.readline().strip()}_mutated\n")

sequence = ''.join(line.strip().upper() for line in input_file.readlines())
length = len(sequence)

sequence = list(sequence)
edits = int(args.mutation * length)

rng.seed(args.seed)
bases_to_edit = rng.sample(range(length), edits)

bases = ['A', 'C', 'G', 'T']
#Replacing each base with some mutated one
for index in bases_to_edit: 
    original = sequence[index] 
    
    # Don't mutate N 
    if original == 'N': 
        continue 
    
    # Choose a base different from the original 
    
    possible_bases = [base for base in bases if base != original]
    sequence[index] = rng.choice(possible_bases) 
    

# Convert back to a string 
sequence = ''.join(sequence)

#Write lines 50 characters per line
line_length = 50
output_file.writelines(f"{sequence[p:p + line_length]}\n" for p in range(0, length, line_length))

#Close files at end
input_file.close()
output_file.close()