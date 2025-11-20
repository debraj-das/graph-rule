@echo off
REM Graph-RULE Automated Setup for Windows
REM Author: Debraj Das (21ME3AI31)
REM Master Thesis Project: Graph Neural Network Unlearning

echo.
echo ========================================
echo 🎓 GRAPH-RULE THESIS PROJECT SETUP
echo ========================================
echo Project: Graph Neural Network Unlearning
echo Author: Debraj Das (21ME3AI31)
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo ✅ Python detected
python --version

REM Ask user for GPU support
echo.
set /p gpu_choice="Do you want GPU support (CUDA)? [y/N]: "
if /i "%gpu_choice%"=="y" (
    set GPU_FLAG=--gpu
    echo 🚀 GPU support will be installed
) else (
    set GPU_FLAG=
    echo 💻 CPU-only installation selected
)

echo.
echo 🔧 Starting automated setup...
echo This may take 5-10 minutes depending on your internet connection.
echo.

REM Run the Python setup script
python setup_graph_rule.py %GPU_FLAG%

if errorlevel 1 (
    echo.
    echo ❌ Setup failed! Please check the error messages above.
    echo.
    echo Common solutions:
    echo 1. Ensure you have Python 3.8+ installed
    echo 2. Check your internet connection
    echo 3. Try running as administrator
    echo 4. Disable antivirus temporarily during installation
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo 🎉 SETUP COMPLETED SUCCESSFULLY!
echo ========================================
echo.
echo Your Graph-RULE thesis project is now ready!
echo.
echo To activate your environment and start working:
echo 1. Run: .venv\Scripts\activate.bat
echo 2. Test: python final_thesis_validation.py
echo 3. Generate curves: python generate_thesis_defense_curves.py
echo.
echo Or simply run: quick_start.bat
echo.
echo 🎯 Ready for your thesis defense!
echo.
pause
