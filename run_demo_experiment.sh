#!/bin/bash
set -x

export VLLM_ATTENTION_BACKEND=XFORMERS
export VLLM_USE_V1=0

# Updated script for accessible model reproduction
names=(
    '1_Stephen_King'
)

# Use a smaller, accessible model for demonstration
# For full reproduction, replace with appropriate Llama models
BASE_MODEL_PATH="microsoft/DialoGPT-medium"  # Small accessible model for testing
# BASE_MODEL_PATH="meta-llama/Llama-2-7b-chat-hf"  # Use this for full experiments

# Reduced experiment settings for testing/demonstration
checkpoints=(10)  # Reduced from 76 114
max_steps=5       # Reduced from 20 for quick testing

for checkpint in "${checkpoints[@]}"
do
    for name in "${names[@]}"
    do
        echo "Running ${name} with checkpoint-${checkpint}"
        save_dir="./saves/RWKU/Target/${name}"
        mkdir -p ${save_dir}
        
        experiment_name="RWKU/demo/llama_demo_step${checkpint}_bs8_kl1e-2_bf16_two_stage_reject_ref_rollout4_target_lr2e-6"
        MODEL_PATH=${BASE_MODEL_PATH}
        
        log_path="./log/${experiment_name}/$name.log"
        if [ -f ${log_path} ]; then
            echo "Skip existing log file: ${log_path}"
            continue
        fi
        
        mkdir -p "./log/${experiment_name}"
        python3 -m verl.trainer.main \
            config=examples/grpo_rj_rl.yaml \
            worker.actor.model.model_path=${MODEL_PATH} \
            worker.ref.model.model_path=${MODEL_PATH} \
            trainer.save_checkpoint_path=${save_dir}/${experiment_name} \
            trainer.save_freq=-1 \
            trainer.experiment_name=${experiment_name}/$name \
            trainer.n_gpus_per_node=1 \
            worker.rollout.tensor_parallel_size=1 \
            data.train_files=data/RWKU/Target/${name}/rl_rejection_with_fb_neighbor_target.json \
            data.rollout_batch_size=8 \
            worker.actor.global_batch_size=8 \
            worker.actor.micro_batch_size_per_device_for_update=2 \
            worker.actor.micro_batch_size_per_device_for_experience=4 \
            algorithm.kl_coef=1e-2 \
            worker.rollout.n=4 \
            worker.actor.optim.lr=2e-6 \
            trainer.max_steps=${max_steps} \
            trainer.val_freq=1 \
            trainer.total_episodes=1 \
            worker.reward.score_function="forget_two_stage_abs_target" \
            data.val_files=data/RWKU/Target/${name}/rl_rejection_eval_target.json \
             2>&1 | tee ${log_path}
    done
done
