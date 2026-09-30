#!/bin/bash

for rate in 0.01 0.05 0.10 0.15
do
    for seed in 1 2 3
    do
        if [ ! -r chr22_mut${rate}_s${seed}.fa ]
        then
            # introduce mutations
            python3 sim_mutations.py -i chr22_orig.fa -o chr22_mut${rate}_s${seed}.fa -m ${rate} -s ${seed}
            nucmer --mum -g 1000 -b 1000 -p chr22_orig_vs_mut${rate}_s${seed} chr22_orig.fa chr22_mut${rate}_s${seed}.fa
            delta-filter -1 chr22_orig_vs_mut${rate}_s${seed}.delta > chr22_orig_vs_mut${rate}_s${seed}.1delta
            show-coords -rcl chr22_orig_vs_mut${rate}_s${seed}.1delta > chr22_orig_vs_mut${rate}_s${seed}.coords
        fi
    done
done

head chr22_orig_vs_mut*.coords