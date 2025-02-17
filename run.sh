#!/bin/bash

datasets=("aro" "mmrel" "gqa")
prompts=(0 1 5 6 10)
openai_key="" # add your OpenAI API key here

for dataset in "${datasets[@]}"; do
    for prompt in "${prompts[@]}"; do
        python3 main.py --dataset "$dataset" --prompt "$prompt" --key "$openai_key"
    done
done
