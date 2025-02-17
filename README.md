# Mitigating Hallucinations in Multimodal Spatial Relations through Constraint-Aware Prompting
This repository contains the code for "Mitigating Hallucinations in Multimodal Spatial Relations through Constraint-Aware Prompting," NAACL Findings 2025. You can access the paper <a href="https://arxiv.org/abs/2502.08317" target="_blank">here<a> 

## How to Run
### Install
1. Clone this repository and navigate to CAP folder
```
git clone https://github.com/jwu114/CAP.git
cd CAP
```
2. Install Dependencies (ignore if you've installed tqdm, sklearn, and openai)
```
conda create -n cap python=3.10 -y
conda activate cap
conda install tqdm scikit-learn openai -y
```
### Prepare Dataset
- Download and put the images of <a href="https://github.com/mertyg/vision-language-models-are-bows" target="_blank">ARO dataset<a> under ./dataset/aro/images/
- Download and put the images of <a href="https://cs.stanford.edu/people/dorarad/gqa/download.html" target="_blank">GQA dataset<a> under ./dataset/gqa/images/
- Download and put the images of <a href="https://github.com/niejiahao1998/MMRel" target="_blank">MMRel dataset<a> under ./dataset/mmrel/images/

### Get OpenAI API Key
You need to get your own API key from <a href="https://openai.com/api/">OpenAI<a>. After obtaining the key, include it in the ./run.sh file.

### Run the Program
After changing to the correct working directory, enter:
```
bash run.sh
```
You can modify the dataset and prompt used in the evaluation. More details about prompts can be found in ./config/para.py

## Code Organization
```
├── config
│   ├── para.py
│   └── path.py
├── dataset
│   ├── aro
│   │   ├── annotation
│   │   │   ├── test.jsonl
│   │   │   └── valid.jsonl
│   │   └── images
│   ├── gqa
│   │   ├── annotation
│   │   │   ├── test.jsonl
│   │   │   └── valid.jsonl
│   │   └── images
│   └── mmrel
│       ├── annotation
│       │   ├── test.jsonl
│       │   └── valid.jsonl
│       └── images       
└── run.py
```

## Citation
If our work is useful for your research, please cite our paper:
```
@misc{wu2025mitigatinghallucinationsmultimodalspatial,
      title={Mitigating Hallucinations in Multimodal Spatial Relations through Constraint-Aware Prompting}, 
      author={Jiarui Wu and Zhuo Liu and Hangfeng He},
      year={2025},
      eprint={2502.08317},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.08317}, 
}
```
