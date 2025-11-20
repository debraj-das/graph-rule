#!/usr/bin/env python3
"""
Graph-RULE Installation Verification Script
===========================================
Comprehensive testing of Graph-RULE thesis project setup
Author: Debraj Das (21ME3AI31)
"""

import sys
import importlib
import subprocess
import time
import traceback
from pathlib import Path

class InstallationVerifier:
    def __init__(self):
        self.failed_tests = []
        self.passed_tests = []
        self.warnings = []
        self.project_dir = Path(__file__).parent
    
    def test_import(self, module_name, display_name=None, optional=False):
        """Test if a module can be imported"""
        display_name = display_name or module_name
        try:
            importlib.import_module(module_name)
            self.passed_tests.append(f"✅ {display_name}")
            return True
        except ImportError as e:
            if optional:
                self.warnings.append(f"⚠️  {display_name} (optional) - {e}")
            else:
                self.failed_tests.append(f"❌ {display_name} - {e}")
            return False
    
    def test_version(self, module_name, min_version=None):
        """Test module version"""
        try:
            module = importlib.import_module(module_name)
            version = getattr(module, '__version__', 'unknown')
            
            if min_version and hasattr(module, '__version__'):
                from packaging import version as pkg_version
                if pkg_version.parse(version) >= pkg_version.parse(min_version):
                    self.passed_tests.append(f"✅ {module_name} v{version} (>= {min_version})")
                else:
                    self.warnings.append(f"⚠️  {module_name} v{version} (< {min_version} recommended)")
            else:
                self.passed_tests.append(f"✅ {module_name} v{version}")
            return True
        except:
            return False
    
    def test_gpu_availability(self):
        """Test GPU/CUDA availability"""
        try:
            import torch
            if torch.cuda.is_available():
                device_count = torch.cuda.device_count()
                device_name = torch.cuda.get_device_name(0) if device_count > 0 else "Unknown"
                self.passed_tests.append(f"✅ CUDA: {device_count} GPU(s) available ({device_name})")
                return True
            else:
                self.warnings.append("⚠️  CUDA: No GPU detected (CPU-only mode)")
                return False
        except:
            self.warnings.append("⚠️  CUDA: Cannot check GPU status")
            return False
    
    def test_project_files(self):
        """Test if essential project files exist"""
        essential_files = [
            "graph_rule_experimental_pipeline.py",
            "generate_thesis_defense_curves.py", 
            "final_thesis_validation.py",
            "MTECH_MTP_FINAL_REPORT_COMPREHENSIVE.md",
            "requirements.txt"
        ]
        
        for file_path in essential_files:
            full_path = self.project_dir / file_path
            if full_path.exists():
                size = full_path.stat().st_size
                self.passed_tests.append(f"✅ {file_path} ({size:,} bytes)")
            else:
                self.failed_tests.append(f"❌ Missing: {file_path}")
    
    def test_graph_functionality(self):
        """Test basic graph processing functionality"""
        try:
            import networkx as nx
            import torch
            import numpy as np
            
            # Create a simple graph
            G = nx.karate_club_graph()
            
            # Test basic operations
            nodes = G.number_of_nodes()
            edges = G.number_of_edges()
            
            # Test tensor creation
            adj_matrix = nx.adjacency_matrix(G).toarray()
            tensor = torch.FloatTensor(adj_matrix)
            
            self.passed_tests.append(f"✅ Graph processing: {nodes} nodes, {edges} edges")
            return True
            
        except Exception as e:
            self.failed_tests.append(f"❌ Graph processing test failed: {e}")
            return False
    
    def test_ml_functionality(self):
        """Test machine learning functionality"""
        try:
            import torch
            import torch.nn as nn
            import numpy as np
            from sklearn.datasets import make_classification
            
            # Test PyTorch
            x = torch.randn(10, 5)
            model = nn.Linear(5, 1)
            output = model(x)
            
            # Test sklearn
            X, y = make_classification(n_samples=100, n_features=5, n_classes=2, random_state=42)
            
            self.passed_tests.append("✅ Machine learning frameworks working")
            return True
            
        except Exception as e:
            self.failed_tests.append(f"❌ ML functionality test failed: {e}")
            return False
    
    def test_visualization(self):
        """Test visualization capabilities"""
        try:
            import matplotlib
            matplotlib.use('Agg')  # Use non-interactive backend
            import matplotlib.pyplot as plt
            import seaborn as sns
            import numpy as np
            
            # Test basic plot creation
            fig, ax = plt.subplots(figsize=(6, 4))
            x = np.linspace(0, 10, 100)
            ax.plot(x, np.sin(x))
            ax.set_title("Test Plot")
            
            # Save to temporary file
            test_plot_path = self.project_dir / "test_verification_plot.png"
            plt.savefig(test_plot_path, dpi=100, bbox_inches='tight')
            plt.close()
            
            # Clean up
            if test_plot_path.exists():
                test_plot_path.unlink()
            
            self.passed_tests.append("✅ Visualization libraries working")
            return True
            
        except Exception as e:
            self.failed_tests.append(f"❌ Visualization test failed: {e}")
            return False
    
    def run_comprehensive_test(self):
        """Run all verification tests"""
        print("🧪 GRAPH-RULE INSTALLATION VERIFICATION")
        print("=" * 50)
        print(f"Project directory: {self.project_dir}")
        print(f"Python version: {sys.version}")
        print("=" * 50)
        
        print("\n📦 Testing Core Dependencies...")
        
        # Core ML libraries
        self.test_import("torch", "PyTorch")
        self.test_import("numpy", "NumPy") 
        self.test_import("pandas", "Pandas")
        self.test_import("sklearn", "Scikit-learn")
        
        # Graph libraries
        self.test_import("networkx", "NetworkX")
        self.test_import("torch_geometric", "PyTorch Geometric", optional=True)
        self.test_import("dgl", "Deep Graph Library", optional=True)
        
        # Visualization libraries
        self.test_import("matplotlib", "Matplotlib")
        self.test_import("seaborn", "Seaborn")
        self.test_import("plotly", "Plotly", optional=True)
        
        # RL libraries
        self.test_import("gymnasium", "Gymnasium", optional=True)
        
        print("\n🔍 Testing Versions...")
        self.test_version("torch", "2.0.0")
        self.test_version("numpy", "1.24.0")
        self.test_version("pandas", "2.0.0")
        
        print("\n🎯 Testing GPU Availability...")
        self.test_gpu_availability()
        
        print("\n📁 Testing Project Files...")
        self.test_project_files()
        
        print("\n🧠 Testing Functionality...")
        self.test_graph_functionality()
        self.test_ml_functionality()
        self.test_visualization()
        
        print("\n" + "=" * 50)
        print("📊 VERIFICATION SUMMARY")
        print("=" * 50)
        
        print(f"\n✅ Passed: {len(self.passed_tests)}")
        for test in self.passed_tests:
            print(f"  {test}")
        
        if self.warnings:
            print(f"\n⚠️  Warnings: {len(self.warnings)}")
            for warning in self.warnings:
                print(f"  {warning}")
        
        if self.failed_tests:
            print(f"\n❌ Failed: {len(self.failed_tests)}")
            for test in self.failed_tests:
                print(f"  {test}")
        
        # Calculate score
        total_tests = len(self.passed_tests) + len(self.failed_tests)
        if total_tests > 0:
            score = (len(self.passed_tests) / total_tests) * 100
        else:
            score = 0
        
        print(f"\n🎯 Installation Score: {score:.1f}%")
        
        if score >= 90:
            status = "EXCELLENT ✨"
        elif score >= 75:
            status = "GOOD 👍"
        elif score >= 60:
            status = "ACCEPTABLE ⚠️"
        else:
            status = "NEEDS WORK ❌"
        
        print(f"🏆 Status: {status}")
        
        if not self.failed_tests:
            print("\n🎉 All critical tests passed! Your Graph-RULE setup is ready!")
            print("\nNext steps:")
            print("1. Run: python generate_thesis_defense_curves.py")
            print("2. Run: python graph_rule_experimental_pipeline.py")
            print("3. Check: thesis_defense_curves/ directory")
        else:
            print("\n🔧 Please fix the failed tests before proceeding.")
            print("Refer to SETUP_INSTRUCTIONS.md for troubleshooting.")
        
        return len(self.failed_tests) == 0

def main():
    """Main verification function"""
    try:
        verifier = InstallationVerifier()
        success = verifier.run_comprehensive_test()
        
        if success:
            print("\n🎯 Your Graph-RULE thesis project is ready for defense!")
            sys.exit(0)
        else:
            sys.exit(1)
            
    except Exception as e:
        print(f"\n❌ Verification failed with exception: {e}")
        print("Traceback:")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
