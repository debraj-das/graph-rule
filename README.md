<h1 align="center">
 RULE: Reinforcement UnLEarning Achieves 
 
 Forget–Retain Pareto Optimality
</h1>

<div align="center">

[![arXiv](https://img.shields.io/badge/arXiv-2506.07171-b31b1b.svg?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2506.07171)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)

</div>

> *TL;DR*: RULE is a reinforcement unlearning pipeline that enables the model to explore **when and how** to refuse. RULE achieves a strong **Pareto frontier** between forgetting and retention—without massive datasets.


## 📰 News

* 🎉 [2025.09] Our paper has been **accepted to NeurIPS 2025**!


---

## ✨ Overview

![RULE Overview](img/overview.png)


We propose RULE, which views model unlearning as refusal-policy optimization and introduces an online RL–based refusal fine-tuning approach. This brings three key benefits:

- Natural, safe responses:
Prior methods often yield unnatural outputs after fine-tuning. By designing appropriate rewards, RULE induces refusal behavior on forget data, producing fluent and safe replies.

- Generalization beyond the forget/retain sets:
We introduce a simple, effective data synthesis strategy and leverage RL’s exploration on a boundary set. The model implicitly learns a refusal policy from rewards, improving generalization to unseen but related queries.

- A better forget–retain trade-off:
Because RL samples on-policy from the model’s own distribution, RULE better preserves the model’s knowledge while unlearning targeted content.

Empirically, on RWKU and MUSE-Book, RULE achieves a Pareto-optimal forget–retain frontier using only 10% of the forget and retain sets, while maintaining naturalness and general utility. Additional experiments show robustness to both black-box and white-box attacks, and compatibility with multiple reward designs and online RL algorithms.


---


## 📈 Key Findings
![img/exp.png](img/exp.png)

* **Natural refusals** on forget-related queries without collapsing helpfulness.
* **Data-efficient**: strong results with a **small fraction** of forget data + synthetic boundary data.
* **Pareto-optimal** trade-off between forgetting and retention.
* **Generalization** to unseen but semantically related queries.

![img/tradeoff.png](img/tradeoff.png)

> See the paper for full quantitative results, attack robustness, and ablations.

---


## 🚀 Installation

We recommend Python **3.9+**.

```bash
# Option A: editable install
pip install -e .

# Install dependencies
pip install -r requirements.txt
```

> If you use conda:

```bash
conda create -n rule python=3.9 -y
conda activate rule
pip install -e .
pip install -r requirements.txt
```

---


## 🗂️ Repository Structure

```
log/            # Training and evaluation logs
# For Rejection Steering:
RS/             # Rejection Steering (RS) implementation
    scripts/    # Scripts for running RS experiments
    models/     # RS model implementations
    utils/      # Utility functions for RS
# For Refusal Boundary Optimization:
examples/       # Example experiment configs (YAML + runnable bash)
data/           # Datasets and metadata
verl/           # Core source code (models, training, evaluation, utils)
run_muse.sh     # Script to run MUSE-Book experiments for ReBO
run_rwku.sh     # Script to run RWKU experiments for ReBO
requirements.txt
setup.py
```

---


## 🧪 Quick Start

### 1) Rejection Steering (RS)

```bash
cd RS && bash scripts/full/run_rt_epoch_target.sh
```

### 2) Refusal Boundary Optimization (ReBO)

```bash
bash examples/exp_target/RWKU/run_llama_bs32_kl1e-2_forget_bf16_two_stage_reject_ref_rollout8_withformat_with_fb_neighbor_abs_lr2e-6.sh
```

> **Tips**
>
> * Edit the RS runner at: `RS/scripts/full/run_rt_epoch_target.sh`.
> * Edit ReBO YAMLs under `examples/` for models, rewards, data paths, and hyperparameters.

---

## 🧰 Configuration

* **RS:**

  * Set the forget targets, reward weights, and sampler options in the runner script above.
* **ReBO:**

  * Control boundary synthesis, rollout length, reward shaping, and evaluation suites in `examples/**.yaml`.

---

## 🙏 Acknowledgements

This project builds on:

* **EasyR1** (preference-based RL training utilities)
* **RWKU** (real-world knowledge unlearning benchmark)

We also evaluate on **MUSE-Books** where appropriate.

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 📚 Citation

If you find RULE useful, please cite our paper:

```bibtex
@misc{zhang2025rulereinforcementunlearningachieves,
      title={RULE: Reinforcement UnLEarning Achieves Forget-Retain Pareto Optimality},
      author={Chenlong Zhang and Zhuoran Jin and Hongbang Yuan and Jiaheng Wei and Tong Zhou and Kang Liu and Jun Zhao and Yubo Chen},
      year={2025},
      eprint={2506.07171},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2506.07171}
}
```
