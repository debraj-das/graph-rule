# RULE Model Configuration Guide

## Quick Start with Hugging Face Models

### For RWKU Experiments:
The scripts expect Llama-3-8B or Llama-3.1-8B models. You can:

1. **Download models locally**: 
   ```bash
   # Install git-lfs if not already installed
   git lfs install
   
   # Clone Llama-3-8B-Instruct
   git clone https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
   ```

2. **Use directly from Hugging Face**: 
   Update MODEL_PATH in the scripts to:
   ```bash
   MODEL_PATH="meta-llama/Meta-Llama-3-8B-Instruct"
   ```

### For MUSE Experiments:
The scripts expect Llama-2-7B models:

1. **Download models locally**:
   ```bash
   git clone https://huggingface.co/meta-llama/Llama-2-7b-chat-hf
   ```

2. **Use directly from Hugging Face**:
   ```bash
   MODEL_PATH="meta-llama/Llama-2-7b-chat-hf"
   ```

## Current Script Paths (Need to be Updated)

The scripts currently expect models at:
- `/mnt/usercache/zhangchenlong/RL-Unlearning/LLaMA-Factory/saves/...`

These are the author's local paths and need to be changed to your model locations.

## How to Update Scripts

1. Edit the experiment script you want to run
2. Find the line with `MODEL_PATH=...`
3. Replace with your model path or HuggingFace model ID
4. Save and run the script

## Example Script Update

**Before (in RWKU script):**
```bash
MODEL_PATH=/mnt/usercache/zhangchenlong/RL-Unlearning/LLaMA-Factory/saves/RWKU/Target/${name}/rt_target_full/llama3_8b_instruct_bf16/checkpoint-${checkpint}
```

**After (using HuggingFace directly):**
```bash
MODEL_PATH="meta-llama/Meta-Llama-3-8B-Instruct"
```

**Or using local path:**
```bash
MODEL_PATH="C:/Users/debra/models/Meta-Llama-3-8B-Instruct"
```

## Note on Hardware Requirements

- **GPU Memory**: The experiments require substantial GPU memory (recommended 16GB+ for 7B models)
- **Storage**: Each model is several GBs (Llama-3-8B is ~16GB, Llama-2-7B is ~13GB)
- **Internet**: If using HuggingFace directly, models will be downloaded on first use
