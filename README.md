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
