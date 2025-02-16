#!/bin/bash

datasets=("aro" "mmrel" "gqa")
prompts=(0 1 5 6 10)

for dataset in "${datasets[@]}"; do
    for prompt in "${prompts[@]}"; do
        python3 --dataset "$dataset" --prompt "$prompt"
    done
done
