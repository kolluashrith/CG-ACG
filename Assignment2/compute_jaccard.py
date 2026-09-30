#compute_jaccard.py

def build_kmer_set(input_file, k_size):

    fastastart = input_file.readline() #throw out first line
    if (not fastastart.startswith(">")):
        input_file.seek(0)

    kmer_set = set()
    prev_k = "" #maintain k-1 previous characters to build kmer

    for line in input_file:
        line = list(line.strip().upper())

        for m in range(len(line)):
            if (line[m] not in ['A', 'C', 'G', 'T']):
                line[m] = 'N'

        line = ''.join(line)

        sequence = prev_k + line

        #Build k-mers and add to dictionary
        for i in range(len(sequence) - k_size + 1):
            kmer = sequence[i:i+k_size]
            kmer_set.add(kmer)

        #Overlap
        prev_k = sequence[-(k_size-1):]

    return kmer_set




import argparse
import math

#Need parser to allow for CLI flags
parser = argparse.ArgumentParser(description="Jaccard.py argument parser")

parser.add_argument('-a', '--sequence1', type=str, help="Sequence 1 to compare")
parser.add_argument('-b', '--sequence2', type=str, help="Sequence 2 to compare")
parser.add_argument('-k', '--kmer_length', type=int, help="length of kmer to compute Jaccard coefficient")

args = parser.parse_args()

k = args.kmer_length

#Open required files
input_file1 = open(args.sequence1)
input_file2 = open(args.sequence2)

#Build kmer index for sequence 1 and sequence 2
kmer_set_1 = build_kmer_set(input_file1, k)
kmer_set_2 = build_kmer_set(input_file2, k)


#Calculate and display outputs
jaccard = len(kmer_set_1.intersection(kmer_set_2)) / len(kmer_set_1.union(kmer_set_2))
ani = ((2*jaccard) / (1 + jaccard)) ** (1/k)
ani_approx = 1 + (1/k)*math.log((2*jaccard)/(1 + jaccard))
print(f"The Jaccard coefficient is {jaccard:.4}.")
print(f"The Average Nucleotide Identity is exactly {ani:.4f}.")
print(f"The Average Nucleotide Identity is approximately {ani_approx:.4f}.")

input_file1.close()
input_file2.close()
