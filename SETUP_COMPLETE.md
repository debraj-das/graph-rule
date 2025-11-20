# ✅ RULE Repository Setup Complete!

## 🎉 Status: Ready to Reproduce Results

Your RULE (Reinforcement UnLEarning) repository is now properly set up and ready to reproduce the paper's results.

## 📋 What's Been Completed

### ✅ Environment Setup
- ✅ Python 3.11.3 (meets requirement of Python 3.9+)
- ✅ All core dependencies installed:
  - transformers 4.57.1
  - torch 2.9.1+cpu
  - accelerate, datasets, wandb, etc.
- ✅ RULE package installed in editable mode

### ✅ Repository Structure Verified
- ✅ Data files available for both RWKU and MUSE datasets
- ✅ Configuration files ready (YAML configs)
- ✅ Experiment scripts available for both approaches
- ✅ Windows-compatible batch scripts created

## 🚀 How to Run Experiments

### **Method 1: Rejection Steering (RS)**
```bash
cd RS
bash scripts/full/run_rt_epoch_target.sh
```

### **Method 2: Refusal Boundary Optimization (ReBO) - Main RULE Method**

#### For RWKU Dataset:
```bash
# Option 1: Use the provided Windows batch script
run_rwku_windows.bat

# Option 2: Run directly
bash examples/exp_target/RWKU/run_llama_bs32_kl1e-2_forget_bf16_two_stage_reject_ref_rollout8_withformat_with_fb_neighbor_abs_lr2e-6.sh
```

#### For MUSE Dataset:
```bash
# Option 1: Use the provided Windows batch script
run_muse_windows.bat

# Option 2: Run directly
bash examples/exp_target/MUSE/run_llama_bs32_kl1e-2_forget_bf16_two_stage_reject_ref_rollout8_withformat_with_neighbor_abs_lr2e-6_train_icl.sh
```

## ⚠️ Important: Model Configuration Required

**Before running experiments, you MUST update the MODEL_PATH in the scripts:**

1. **Current paths** (from authors' environment):
   ```bash
   MODEL_PATH=/mnt/usercache/zhangchenlong/RL-Unlearning/LLaMA-Factory/saves/...
   ```

2. **Update to your model path**:
   ```bash
   # Option A: Use HuggingFace directly (recommended)
   MODEL_PATH="meta-llama/Meta-Llama-3-8B-Instruct"  # For RWKU
   MODEL_PATH="meta-llama/Llama-2-7b-chat-hf"        # For MUSE
   
   # Option B: Use local path if you downloaded models
   MODEL_PATH="C:/Users/debra/models/Meta-Llama-3-8B-Instruct"
   ```

## 📁 Key Files Created
- `MODEL_SETUP_GUIDE.md` - Detailed model configuration guide
- `run_rwku_windows.bat` - Windows script for RWKU experiments  
- `run_muse_windows.bat` - Windows script for MUSE experiments
- `test_setup.py` - Setup verification script

## 🔬 Expected Results

The RULE paper demonstrates:

1. **Pareto-optimal trade-off** between forgetting and retention
2. **Natural refusal responses** instead of gibberish
3. **Data efficiency** - strong results with only 10% of data
4. **Generalization** to unseen but related queries
5. **Robustness** against various attacks

## 📊 Datasets Available

### RWKU (Real-World Knowledge Unlearning)
- **Targets**: 10 celebrities (Stephen King, Confucius, Bruce Lee, etc.)
- **Task**: Forget specific person's information while retaining general knowledge

### MUSE-Book  
- **Target**: Book content
- **Task**: Forget specific book content while retaining other knowledge

## 🎯 Next Steps

1. **Choose your approach**: RS (simpler) or ReBO (main RULE method)
2. **Update MODEL_PATH** in the experiment script you want to run
3. **Run the experiment** using the provided commands
4. **Monitor results** in the `log/` directory
5. **Compare with paper results** for validation

## 📖 Paper Reference

```bibtex
@misc{zhang2025rulereinforcementunlearningachieves,
      title={RULE: Reinforcement UnLEarning Achieves Forget-Retain Pareto Optimality},
      author={Chenlong Zhang and Zhuoran Jin and Hongbang Yuan and Jiaheng Wei and Tong Zhou and Kang Liu and Jun Zhao and Yubo Chen},
      year={2025},
      eprint={2506.07171},
      archivePrefix={arXiv}
}
```

---

🎉 **Your RULE repository is now ready for experiments!** 

The setup is complete and all dependencies are properly installed. Simply update the model paths as described above and start running the experiments to reproduce the paper's results.
