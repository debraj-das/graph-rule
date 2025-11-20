# Graph-RULE Setup Instructions
## Master Thesis Project: Graph Neural Network Unlearning with Reinforcement Learning

**Author:** Debraj Das (21ME3AI31)  
**Supervisor:** Professor Plaban Bhowmick  
**Project:** Graph-RULE (G-RULE) Framework  

---

## 🚀 Quick Start Guide

### Prerequisites
- **Operating System:** Windows 10/11, macOS 10.15+, or Ubuntu 18.04+
- **Python:** 3.8+ (Recommended: Python 3.11)
- **Memory:** Minimum 8GB RAM (Recommended: 16GB+)
- **Storage:** 5GB free space
- **GPU:** Optional but recommended (CUDA 11.8+ for GPU acceleration)

---

## 📦 Installation Methods

### Method 1: Automated Setup (Recommended)

#### Windows (PowerShell)
```powershell
# Clone or navigate to project directory
Set-Location "c:\Users\debra\Desktop\RULE-Unlearn"

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Upgrade pip
python -m pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Verify installation
python -c "import torch; print('PyTorch version:', torch.__version__)"
python -c "import numpy; print('NumPy version:', numpy.__version__)"
```

#### Linux/macOS (Bash)
```bash
# Navigate to project directory
cd /path/to/RULE-Unlearn

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Verify installation
python -c "import torch; print('PyTorch version:', torch.__version__)"
```

### Method 2: Conda Environment Setup
```bash
# Create conda environment
conda create -n graph-rule python=3.11 -y

# Activate environment
conda activate graph-rule

# Install PyTorch with CUDA support (if available)
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

# Install remaining requirements
pip install -r requirements.txt
```

### Method 3: Docker Setup
```bash
# Build Docker image
docker build -t graph-rule .

# Run container
docker run -it --gpus all -v $(pwd):/workspace graph-rule

# Inside container, install requirements
pip install -r requirements.txt
```

---

## 🧪 Quick Testing

### Test Core Functionality
```bash
# Test basic imports
python -c "from graph_rule_experimental_pipeline import *; print('✅ Core pipeline loaded successfully')"

# Test visualization system
python -c "from generate_thesis_defense_curves import *; print('✅ Visualization system loaded')"

# Run basic validation
python final_thesis_validation.py
```

### Generate Sample Results
```bash
# Generate thesis defense curves (takes 2-3 minutes)
python generate_thesis_defense_curves.py

# Create final defense presentation
python create_final_defense_presentation.py

# Run experimental pipeline (takes 5-10 minutes)
python graph_rule_experimental_pipeline.py
```

---

## 📊 Component Testing

### 1. Data Validation
```python
# Test dataset loading
python -c "
import pandas as pd
import numpy as np
print('✅ Data processing libraries working')
"
```

### 2. Graph Processing
```python
# Test graph libraries
python -c "
import networkx as nx
import torch_geometric
print('✅ Graph processing libraries working')
"
```

### 3. Machine Learning
```python
# Test ML frameworks
python -c "
import torch
import sklearn
print('✅ ML frameworks working')
print(f'PyTorch version: {torch.__version__}')
print(f'CUDA available: {torch.cuda.is_available()}')
"
```

### 4. Visualization
```python
# Test plotting libraries
python -c "
import matplotlib.pyplot as plt
import seaborn as sns
import plotly
print('✅ Visualization libraries working')
"
```

---

## 🔧 Advanced Configuration

### GPU Setup (NVIDIA)
```bash
# Check CUDA installation
nvidia-smi

# Install CUDA-enabled PyTorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Verify GPU access
python -c "import torch; print(f'CUDA devices: {torch.cuda.device_count()}')"
```

### Memory Optimization
```bash
# For large datasets, configure memory settings
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512
export OMP_NUM_THREADS=4
```

### Jupyter Notebook Setup (Optional)
```bash
# Install Jupyter
pip install jupyter ipykernel

# Create kernel for this environment
python -m ipykernel install --user --name=graph-rule --display-name "Graph-RULE"

# Launch Jupyter
jupyter notebook
```

---

## 📁 Project Structure Overview

```
RULE-Unlearn/
├── 📄 Core Files
│   ├── graph_rule_experimental_pipeline.py     # Main experimental framework
│   ├── generate_thesis_defense_curves.py       # Visualization system
│   └── final_thesis_validation.py              # Validation suite
│
├── 📊 Results & Visualizations
│   ├── thesis_defense_curves/                  # 16 critical evaluation curves
│   ├── final_defense_presentation/             # Professional presentation package
│   └── graph_rule_results/                     # Experimental outputs
│
├── 📚 Documentation
│   ├── MTECH_MTP_FINAL_REPORT_COMPREHENSIVE.md # Complete thesis report (67 pages)
│   ├── CRITICAL_EVALUATION_CURVES_GUIDE.md     # Evaluation methodology
│   └── FINAL_THESIS_ACHIEVEMENT_SUMMARY.md     # Achievement overview
│
└── 🔧 Configuration
    ├── requirements.txt                         # Python dependencies
    ├── Dockerfile                              # Container setup
    └── setup.py                               # Package installation
```

---

## 🚨 Troubleshooting

### Common Issues & Solutions

#### 1. **Import Errors**
```bash
# Problem: ModuleNotFoundError
# Solution: Ensure virtual environment is activated
.\.venv\Scripts\Activate.ps1  # Windows
source .venv/bin/activate     # Linux/macOS

# Reinstall requirements
pip install -r requirements.txt --force-reinstall
```

#### 2. **CUDA/GPU Issues**
```bash
# Problem: CUDA not detected
# Solution: Install CUDA-enabled PyTorch
pip uninstall torch torchvision torchaudio
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

#### 3. **Memory Errors**
```bash
# Problem: OutOfMemoryError
# Solution: Reduce batch size or enable memory optimization
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:256
```

#### 4. **Plotting Issues**
```bash
# Problem: Matplotlib backend errors
# Solution: Set backend explicitly
export MPLBACKEND=Agg
```

#### 5. **Permission Errors (Windows)**
```powershell
# Problem: Execution policy restrictions
# Solution: Enable script execution
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📈 Performance Optimization

### For Large Datasets (>100K nodes)
```python
# Optimize memory usage
import torch
torch.backends.cudnn.benchmark = True
torch.backends.cudnn.deterministic = False

# Enable mixed precision
from torch.cuda.amp import autocast, GradScaler
scaler = GradScaler()
```

### For CPU-Only Systems
```python
# Optimize for CPU
import torch
torch.set_num_threads(4)  # Adjust based on your CPU cores
```

---

## 🧪 Running Experiments

### Quick Demo (2-3 minutes)
```bash
# Generate sample results
python -c "
from generate_thesis_defense_curves import main
main()
print('✅ Demo completed successfully')
"
```

### Full Experimental Pipeline (10-15 minutes)
```bash
# Run complete validation
python graph_rule_experimental_pipeline.py

# Generate all visualizations
python generate_thesis_defense_curves.py

# Create defense presentation
python create_final_defense_presentation.py

# Final validation
python final_thesis_validation.py
```

---

## 📞 Support & Documentation

### Getting Help
1. **Check logs:** Look for error messages in terminal output
2. **Review documentation:** Read thesis report and guides
3. **Validate setup:** Run `python final_thesis_validation.py`
4. **Check requirements:** Ensure all dependencies are installed

### Key Documentation Files
- `MTECH_MTP_FINAL_REPORT_COMPREHENSIVE.md` - Complete thesis documentation
- `CRITICAL_EVALUATION_CURVES_GUIDE.md` - Evaluation methodology
- `FINAL_THESIS_ACHIEVEMENT_SUMMARY.md` - Project overview

### Performance Benchmarks
- **Expected Runtime:** 5-15 minutes for full pipeline
- **Memory Usage:** 2-8GB depending on dataset size
- **Disk Usage:** 500MB for results and visualizations

---

## ✅ Verification Checklist

After setup, ensure these work:
- [ ] Python environment activated
- [ ] All requirements installed successfully
- [ ] Core imports work without errors
- [ ] GPU detected (if available)
- [ ] Sample visualizations generate
- [ ] Experimental pipeline runs
- [ ] Final validation passes

---

## 🎓 Ready for Thesis Defense!

Once setup is complete, you'll have:
- ✅ Complete Graph-RULE framework implementation
- ✅ 16 professional thesis defense curves
- ✅ Comprehensive experimental validation
- ✅ Professional presentation package
- ✅ 95%+ thesis completion status

**Your revolutionary Graph-RULE research is ready to change the world of privacy-preserving AI!**

---

*Setup Guide Version: 1.0*  
*Last Updated: November 21, 2025*  
*Contact: Debraj Das (21ME3AI31)*
