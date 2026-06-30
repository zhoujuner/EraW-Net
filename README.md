# EraW-Net: Enhance-Refine-Align W-Net for Scene-Associated Driver Attention Estimation

Official repository for **EraW-Net: Enhance-Refine-Align W-Net for Scene-Associated Driver Attention Estimation**.

> 🚧 This repository is under active development.



## News

- **[Available]** Ground-truth attention maps.
- **[Available]** Dataset split files.
- **[Available]** Evaluation code.
- **[Coming Soon]** Training and inference code.


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

The provided `train_test_spilt_all.json` contains the complete split. Users can reproduce our setting by randomly selecting **20% of the training samples as the validation set**.

---

## Evaluation

We provide the evaluation scripts used in our experiments.
- Evaluation script: [`evaluation/evaluate_example.py`](evaluation/evaluate_example.py)
- Metric implementation: [`evaluation/metrics.py`](evaluation/metrics.py)
Currently supported metrics include:CC, SIM, NSS, KLD. 


## Code

The complete implementation will be released in the future.

## Code

Our implementation is built upon the official implementation of **Look Both Ways**:

> https://github.com/Kasai2020/look_both_ways

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


---

## License

This project is released under the MIT License.
