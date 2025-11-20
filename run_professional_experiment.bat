@echo off
REM Professional Windows batch script for RULE reproduction
cd /d "c:\Users\debra\Desktop\RULE-Unlearn"

echo.
echo ===============================================
echo   RULE: Reinforcement UnLEarning Reproduction
echo   Professional Experiment Execution
echo ===============================================
echo.

echo [INFO] Starting RULE experiment reproduction...
echo [INFO] Method: Refusal Boundary Optimization (ReBO)
echo [INFO] Dataset: RWKU (Real-World Knowledge Unlearning)
echo [INFO] Target: Stephen King (Celebrity Forgetting)
echo.

echo [SETUP] Checking environment...
python -c "import torch, transformers, verl; print('[OK] All dependencies available')" || (
    echo [ERROR] Missing dependencies. Please run: pip install -r requirements.txt
    pause
    exit /b 1
)

echo [SETUP] Checking data files...
if not exist "data\RWKU\Target\1_Stephen_King\rl_rejection_with_fb_neighbor_target.json" (
    echo [ERROR] Training data not found
    pause
    exit /b 1
)

if not exist "data\RWKU\Target\1_Stephen_King\rl_rejection_eval_target.json" (
    echo [ERROR] Evaluation data not found  
    pause
    exit /b 1
)

echo [OK] Data files verified
echo.

echo [EXECUTION] Running RULE experiment...
echo [CONFIG] Using accessible model for demonstration
echo [CONFIG] Reduced parameters for quick execution
echo [CONFIG] Results will be saved in ./log/ directory
echo.

bash run_demo_experiment.sh

echo.
echo ===============================================
echo   Experiment Execution Complete
echo ===============================================
echo.
echo [RESULTS] Check the log directory for outputs:
echo   - Training logs: ./log/RWKU/demo/
echo   - Model checkpoints: ./saves/RWKU/Target/
echo.
echo [NEXT] Run report generation: python generate_report.py
echo.
pause
