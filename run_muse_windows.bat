@echo off
REM Windows batch script to run MUSE experiments
cd /d "c:\Users\debra\Desktop\RULE-Unlearn"

echo Starting MUSE experiment for RULE...
echo This will run the Refusal Boundary Optimization approach
echo.

REM Note: You need to update the MODEL_PATH in the experiment script to point to your local model
echo IMPORTANT: Please edit the MODEL_PATH in the experiment scripts to point to your local model files
echo Current script expects: /mnt/usercache/zhangchenlong/RL-Unlearning/LLaMA-Factory/saves/...
echo.

bash examples/exp_target/MUSE/run_llama_bs32_kl1e-2_forget_bf16_two_stage_reject_ref_rollout8_withformat_with_neighbor_abs_lr2e-6_train_icl.sh
