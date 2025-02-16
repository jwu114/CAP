# Mitigating Hallucinations in Multimodal Spatial Relations through Constraint-Aware Prompting
This repository contains the code for "Mitigating Hallucinations in Multimodal Spatial Relations through Constraint-Aware Prompting," NAACL Findings 2025. You can access the paper <a href="https://arxiv.org/abs/2502.08317" target="_blank">here<a> 

## How to Run

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
