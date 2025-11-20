#!/bin/bash
# Graph-RULE Automated Setup for Linux/macOS
# Author: Debraj Das (21ME3AI31)
# Master Thesis Project: Graph Neural Network Unlearning

echo ""
echo "========================================"
echo "🎓 GRAPH-RULE THESIS PROJECT SETUP"
echo "========================================"
echo "Project: Graph Neural Network Unlearning"
echo "Author: Debraj Das (21ME3AI31)"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "❌ Python is not installed or not in PATH"
    echo "Please install Python 3.8+ using your package manager:"
    echo ""
    echo "Ubuntu/Debian: sudo apt update && sudo apt install python3 python3-pip python3-venv"
    echo "macOS: brew install python"
    echo "CentOS/RHEL: sudo yum install python3 python3-pip"
    echo ""
    exit 1
fi

# Determine Python command
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
fi

echo "✅ Python detected"
$PYTHON_CMD --version

# Ask user for GPU support
echo ""
read -p "Do you want GPU support (CUDA)? [y/N]: " gpu_choice
if [[ $gpu_choice =~ ^[Yy]$ ]]; then
    GPU_FLAG="--gpu"
    echo "🚀 GPU support will be installed"
else
    GPU_FLAG=""
    echo "💻 CPU-only installation selected"
fi

echo ""
echo "🔧 Starting automated setup..."
echo "This may take 5-10 minutes depending on your internet connection."
echo ""

# Run the Python setup script
$PYTHON_CMD setup_graph_rule.py $GPU_FLAG

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Setup failed! Please check the error messages above."
    echo ""
    echo "Common solutions:"
    echo "1. Ensure you have Python 3.8+ installed"
    echo "2. Check your internet connection"
    echo "3. Install system dependencies:"
    echo "   Ubuntu: sudo apt install build-essential python3-dev"
    echo "   macOS: xcode-select --install"
    echo "4. Update pip: python3 -m pip install --upgrade pip"
    echo ""
    exit 1
fi

echo ""
echo "========================================"
echo "🎉 SETUP COMPLETED SUCCESSFULLY!"
echo "========================================"
echo ""
echo "Your Graph-RULE thesis project is now ready!"
echo ""
echo "To activate your environment and start working:"
echo "1. Run: source .venv/bin/activate"
echo "2. Test: python final_thesis_validation.py"
echo "3. Generate curves: python generate_thesis_defense_curves.py"
echo ""
echo "Or simply run: ./quick_start.sh"
echo ""
echo "🎯 Ready for your thesis defense!"
echo ""
