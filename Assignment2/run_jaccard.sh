#!/bin/bash

for rate in 0.01 0.05 0.10 0.15
do
    for seed in 1 2 3
    do
        if [ ! -r jaccard_mut${rate}_s${seed}.txt ]
        then
            python compute_jaccard.py -a chr22_orig.fa -b chr22_mut${rate}_s${seed}.fa -k 21 > jaccard_mut${rate}_s${seed}.txt
        fi
    done
done

head jaccard_mut*.txt