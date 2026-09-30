#!/bin/bash

for rate in 0.01 0.05 0.10 0.15
do
    for seed in 1 2 3
    do
        for mod in 100 1000
        do
            if [ ! -r modimizers_mut${rate}_s${seed}_m${mod}.txt ]
            then
                python compute_jaccard_modimizer.py -a chr22_orig.fa -b chr22_mut${rate}_s${seed}.fa -k 21 -m $mod > modimizers_mut${rate}_s${seed}_m${mod}.txt
            fi
        done
    done
done

head -100 modimizers_mut*.txt