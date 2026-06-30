# EraW-Net: Enhance-Refine-Align W-Net for Scene-Associated Driver Attention Estimation

This is the official repository for the paper:

> **EraW-Net: Enhance-Refine-Align W-Net for Scene-Associated Driver Attention Estimation**  
> Jun Zhou, Chunsheng Liu, Faliang Chang, Wenqian Wang, Penghui Hao, Yiming Huang, and Zhiqiang Yang  
> *IEEE Transactions on Multimedia, 2025*  
> [[Paper]](https://ieeexplore.ieee.org/abstract/document/10988653)

## Abstract

Associating driver attention with driving scene across two fields of view is a challenging cross-domain perception problem, which requires comprehensive consideration of cross-view mapping, dynamic driving scene analysis and driver status tracking. Previous methods typically analyze a single view or map attention to the scene through a two-step projection, failing to exploit their implicit connections and establish accurate associations. Moreover, simple fusion modules are inadequate for modeling the complex relationships between the two views, making information integration complicated. To address these issues, we propose EraW-Net, a novel end-to-end framework for scene-associated driver attention estimation by aggregating information from dual views. This method enhances the most discriminative dynamic cues, refines feature representations, and facilitates semantically aligned cross-domain integration through a W-shaped architecture, termed W-Net. Specifically, a Dynamic Adaptive Filter Module (DAF-Module) is proposed to address the challenges of frequently changing driving environments by extracting vital regions. It suppresses the indiscriminately recorded dynamics and highlights crucial ones by innovative joint frequency-spatial analysis, enhancing the model's ability to parse complex dynamics. Additionally, to track driver states during non-fixed facial poses, we propose a Global Context Sharing Module (GCS-Module) to construct refined feature representations by capturing hierarchical features that adapt to various scales of head and eye movements. Finally, W-Net achieves systematic cross-view information integration through its unique two-stage decoding strategy, addressing semantic misalignment in heterogeneous data integration. Experiments demonstrate that the proposed method robustly and accurately estimates scene-associated driver attention on large public datasets. 

## News

- **[Available]** Ground-truth attention maps.
- **[Available]** Dataset split files.
- **[Available]** Evaluation code.

## Ground Truth (GT)

The GT files are organized as follows:
```text
LBW_GT/
├── Subject01_2_data/
│   ├── s_g/       # Gaze-Projected Heatmap
│   └── fix_map/   # Sequential Fixation Heatmap
├── Subject02_2_data/
│   ├── s_g/
│   └── fix_map/
├── Subject03_2_data/
│   ├── s_g/
│   └── fix_map/
└── ...
```

Here, /s_g corresponds to the Gaze-Projected Heatmap, and /fix_map corresponds to the Sequential Fixation Heatmap described in the paper. 

**Download:**

- Baidu Netdisk (optional): **[Baidu Link](https://pan.baidu.com/s/1xz8-5DYuziF5P4QJiCEyVg?pwd=ut13)** (Code: ut13)



## Dataset Split

We provide the official dataset split in JSON format.

```
dataset_split/
├── train_test_spilt_all.json
```

The provided `train_test_spilt_all.json` contains the complete split. Users can reproduce our setting by randomly selecting 20% of the training samples as the validation set.

---

## Evaluation

We provide the evaluation scripts used in our experiments.
- Metric implementation: [`evaluation/metrics.py`](evaluation/metrics.py) Currently supported metrics include:CC, SIM, NSS, KLD. 
- Example usage: [`evaluation/evaluate_example.py`](evaluation/evaluate_example.py)



## Code

The complete implementation will be released in the future.

## Acknowledgements

Our implementation is built upon the official implementation of **Look Both Ways**(https://github.com/Kasai2020/look_both_ways): 

We sincerely thank the authors for making their code publicly available.



## Credits

We would like to acknowledge the authors of the **Look Both Ways** project for providing the open-source implementation that served as the foundation of this work.


## Citation

If you find this work useful, please consider citing:

```bibtex
@article{zhou2025erawnet,
  title={EraW-Net: Enhance-Refine-Align W-Net for Scene-Associated Driver Attention Estimation},
  author={Zhou, Jun and Liu, Chunsheng and Chang, Faliang and Wang, Wenqian and Hao, Penghui and Huang, Yiming and Yang, Zhiqiang},
  journal={IEEE Transactions on Multimedia},
  year={2025}
}
```


---

## License


The released ground-truth maps, dataset splits, and evaluation code are provided for research purposes only.

If you use these resources in your work, please cite our paper.
