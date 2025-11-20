#!/usr/bin/env python3
"""
Graph-RULE Automated Setup Script
=================================
Automated installation and configuration for Graph-RULE thesis project
Author: Debraj Das (21ME3AI31)
"""

import os
import sys
import subprocess
import platform
import venv
from pathlib import Path
import argparse

class GraphRuleSetup:
    def __init__(self):
        self.project_dir = Path(__file__).parent
        self.venv_dir = self.project_dir / ".venv"
        self.system = platform.system().lower()
        self.python_cmd = self._get_python_command()
        
    def _get_python_command(self):
        """Get the appropriate Python command for this system"""
        try:
            # Try python3 first
            subprocess.run([sys.executable, "--version"], check=True, capture_output=True)
            return sys.executable
        except:
            # Fall back to python
            return "python"
    
    def _run_command(self, command, description, check=True, shell=None):
        """Run a system command with error handling"""
        print(f"🔧 {description}...")
        
        # Determine shell behavior based on system
        if shell is None:
            shell = self.system == "windows"
        
        try:
            if isinstance(command, list):
                result = subprocess.run(command, check=check, shell=shell, 
                                      capture_output=True, text=True)
            else:
                result = subprocess.run(command, check=check, shell=True, 
                                      capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ {description} completed successfully")
                return True
            else:
                print(f"❌ {description} failed: {result.stderr}")
                return False
                
        except subprocess.CalledProcessError as e:
            print(f"❌ {description} failed: {e}")
            print(f"   Error output: {e.stderr}")
            return False
        except Exception as e:
            print(f"❌ {description} failed with exception: {e}")
            return False
    
    def check_python_version(self):
        """Check if Python version is compatible"""
        print("🐍 Checking Python version...")
        
        version = sys.version_info
        if version.major < 3 or (version.major == 3 and version.minor < 8):
            print(f"❌ Python {version.major}.{version.minor} is not supported")
            print("   Please install Python 3.8 or higher")
            return False
        
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
        return True
    
    def check_system_requirements(self):
        """Check system-specific requirements"""
        print("💻 Checking system requirements...")
        
        # Check available space
        total, used, free = os.statvfs(self.project_dir) if hasattr(os, 'statvfs') else (0, 0, 5*1024**3)
        free_gb = free * os.statvfs(self.project_dir).f_frsize / (1024**3) if hasattr(os, 'statvfs') else 5
        
        if free_gb < 2:
            print(f"⚠️  Warning: Only {free_gb:.1f}GB free space available")
            print("   Recommended: 5GB+ for complete installation")
        else:
            print(f"✅ Sufficient disk space: {free_gb:.1f}GB available")
        
        # Check for Git (optional)
        git_available = self._run_command("git --version", "Checking Git availability", check=False)
        if not git_available:
            print("ℹ️  Git not found - version control features will be limited")
        
        return True
    
    def create_virtual_environment(self):
        """Create Python virtual environment"""
        if self.venv_dir.exists():
            print(f"📦 Virtual environment already exists at {self.venv_dir}")
            return True
        
        print("📦 Creating virtual environment...")
        try:
            venv.create(self.venv_dir, with_pip=True)
            print("✅ Virtual environment created successfully")
            return True
        except Exception as e:
            print(f"❌ Failed to create virtual environment: {e}")
            return False
    
    def get_activation_command(self):
        """Get the command to activate virtual environment"""
        if self.system == "windows":
            return str(self.venv_dir / "Scripts" / "activate.bat")
        else:
            return f"source {self.venv_dir}/bin/activate"
    
    def get_python_executable(self):
        """Get path to Python executable in virtual environment"""
        if self.system == "windows":
            return self.venv_dir / "Scripts" / "python.exe"
        else:
            return self.venv_dir / "bin" / "python"
    
    def install_requirements(self, gpu_support=False):
        """Install Python requirements"""
        python_exe = self.get_python_executable()
        
        # Upgrade pip first
        upgrade_cmd = [str(python_exe), "-m", "pip", "install", "--upgrade", "pip"]
        if not self._run_command(upgrade_cmd, "Upgrading pip"):
            return False
        
        # Install PyTorch with appropriate backend
        if gpu_support:
            print("🚀 Installing PyTorch with GPU support...")
            torch_cmd = [
                str(python_exe), "-m", "pip", "install", 
                "torch", "torchvision", "torchaudio", 
                "--index-url", "https://download.pytorch.org/whl/cu118"
            ]
            if not self._run_command(torch_cmd, "Installing PyTorch (GPU)"):
                print("⚠️  GPU installation failed, falling back to CPU version")
                gpu_support = False
        
        if not gpu_support:
            print("💻 Installing PyTorch (CPU version)...")
            torch_cmd = [str(python_exe), "-m", "pip", "install", "torch", "torchvision", "torchaudio"]
            if not self._run_command(torch_cmd, "Installing PyTorch (CPU)"):
                return False
        
        # Install all other requirements
        requirements_file = self.project_dir / "requirements.txt"
        if requirements_file.exists():
            install_cmd = [str(python_exe), "-m", "pip", "install", "-r", str(requirements_file)]
            return self._run_command(install_cmd, "Installing project requirements")
        else:
            print("❌ requirements.txt not found")
            return False
    
    def verify_installation(self):
        """Verify that installation was successful"""
        python_exe = self.get_python_executable()
        
        print("🧪 Verifying installation...")
        
        # Test basic imports
        test_imports = [
            ("torch", "PyTorch"),
            ("numpy", "NumPy"),
            ("pandas", "Pandas"),
            ("matplotlib", "Matplotlib"),
            ("networkx", "NetworkX"),
            ("sklearn", "Scikit-learn")
        ]
        
        for module, name in test_imports:
            test_cmd = [str(python_exe), "-c", f"import {module}; print('✅ {name} imported successfully')"]
            if not self._run_command(test_cmd, f"Testing {name} import", check=False):
                print(f"⚠️  Warning: {name} import failed")
        
        # Test GPU availability if relevant
        gpu_test_cmd = [
            str(python_exe), "-c", 
            "import torch; print(f'CUDA available: {torch.cuda.is_available()}'); print(f'Device count: {torch.cuda.device_count()}')"
        ]
        self._run_command(gpu_test_cmd, "Checking GPU availability", check=False)
        
        return True
    
    def create_quick_start_script(self):
        """Create a quick start script for the project"""
        if self.system == "windows":
            script_content = f"""@echo off
echo 🎓 Graph-RULE Quick Start
echo ========================

echo Activating virtual environment...
call "{self.venv_dir}\\Scripts\\activate.bat"

echo Running thesis validation...
python final_thesis_validation.py

echo.
echo ✅ Setup complete! Your Graph-RULE environment is ready.
echo.
echo To generate thesis defense curves, run:
echo python generate_thesis_defense_curves.py
echo.
echo To run the full experimental pipeline, run:
echo python graph_rule_experimental_pipeline.py

pause
"""
            script_path = self.project_dir / "quick_start.bat"
        else:
            script_content = f"""#!/bin/bash
echo "🎓 Graph-RULE Quick Start"
echo "========================"

echo "Activating virtual environment..."
source "{self.venv_dir}/bin/activate"

echo "Running thesis validation..."
python final_thesis_validation.py

echo ""
echo "✅ Setup complete! Your Graph-RULE environment is ready."
echo ""
echo "To generate thesis defense curves, run:"
echo "python generate_thesis_defense_curves.py"
echo ""
echo "To run the full experimental pipeline, run:"
echo "python graph_rule_experimental_pipeline.py"
"""
            script_path = self.project_dir / "quick_start.sh"
        
        try:
            with open(script_path, 'w') as f:
                f.write(script_content)
            
            if self.system != "windows":
                os.chmod(script_path, 0o755)
            
            print(f"📝 Quick start script created: {script_path}")
            return True
        except Exception as e:
            print(f"❌ Failed to create quick start script: {e}")
            return False
    
    def run_setup(self, gpu_support=False, skip_verification=False):
        """Run the complete setup process"""
        print("🎓 GRAPH-RULE THESIS PROJECT SETUP")
        print("=" * 50)
        print(f"Project directory: {self.project_dir}")
        print(f"System: {platform.system()} {platform.release()}")
        print(f"Python: {sys.version}")
        print("=" * 50)
        
        # Check prerequisites
        if not self.check_python_version():
            return False
        
        if not self.check_system_requirements():
            print("⚠️  System requirements check failed, continuing anyway...")
        
        # Create virtual environment
        if not self.create_virtual_environment():
            return False
        
        # Install requirements
        if not self.install_requirements(gpu_support):
            return False
        
        # Verify installation
        if not skip_verification:
            if not self.verify_installation():
                print("⚠️  Installation verification had issues, but setup may still work")
        
        # Create quick start script
        self.create_quick_start_script()
        
        print("\n" + "=" * 50)
        print("🎉 SETUP COMPLETED SUCCESSFULLY!")
        print("=" * 50)
        
        print(f"\nTo activate your environment:")
        if self.system == "windows":
            print(f"   {self.venv_dir}\\Scripts\\activate.bat")
        else:
            print(f"   source {self.venv_dir}/bin/activate")
        
        print("\nTo test your installation:")
        print("   python final_thesis_validation.py")
        
        print("\nTo generate thesis defense curves:")
        print("   python generate_thesis_defense_curves.py")
        
        print("\n🎯 Your Graph-RULE thesis project is ready!")
        
        return True

def main():
    parser = argparse.ArgumentParser(description="Graph-RULE Setup Script")
    parser.add_argument("--gpu", action="store_true", help="Install GPU support (CUDA)")
    parser.add_argument("--skip-verification", action="store_true", help="Skip installation verification")
    parser.add_argument("--force", action="store_true", help="Force reinstallation")
    
    args = parser.parse_args()
    
    setup = GraphRuleSetup()
    
    if args.force and setup.venv_dir.exists():
        print("🗑️  Removing existing virtual environment...")
        import shutil
        shutil.rmtree(setup.venv_dir)
    
    success = setup.run_setup(
        gpu_support=args.gpu,
        skip_verification=args.skip_verification
    )
    
    if not success:
        print("\n❌ Setup failed! Please check error messages above.")
        sys.exit(1)
    else:
        print("\n✅ Setup completed successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
