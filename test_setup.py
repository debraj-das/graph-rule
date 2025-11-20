#!/usr/bin/env python3
"""
Simple test script to verify RULE setup is working correctly
"""

import torch
import os
import sys

def test_basic_imports():
    """Test if core dependencies can be imported"""
    print("🔍 Testing basic imports...")
    
    try:
        import transformers
        print(f"✅ transformers: {transformers.__version__}")
    except ImportError:
        print("❌ transformers not found")
        return False
    
    try:
        import torch
        print(f"✅ torch: {torch.__version__}")
        print(f"   CUDA available: {torch.cuda.is_available()}")
        if torch.cuda.is_available():
            print(f"   GPU count: {torch.cuda.device_count()}")
    except ImportError:
        print("❌ torch not found")
        return False
    
    try:
        import datasets
        print(f"✅ datasets: {datasets.__version__}")
    except ImportError:
        print("❌ datasets not found")
        return False
    
    try:
        import verl
        print(f"✅ verl: {verl.__version__}")
    except ImportError:
        print("❌ verl not found - check if pip install -e . worked")
        return False
    
    return True

def test_data_files():
    """Test if required data files exist"""
    print("\n🔍 Testing data files...")
    
    data_path = "data/RWKU/Target/1_Stephen_King"
    required_files = [
        "rl_rejection_with_fb_neighbor_target.json",
        "rl_rejection_eval_target.json"
    ]
    
    if not os.path.exists(data_path):
        print(f"❌ Data directory not found: {data_path}")
        return False
    
    for file_name in required_files:
        file_path = os.path.join(data_path, file_name)
        if os.path.exists(file_path):
            print(f"✅ Found: {file_name}")
        else:
            print(f"❌ Missing: {file_name}")
            return False
    
    return True

def test_model_loading():
    """Test if a simple model can be loaded"""
    print("\n🔍 Testing model loading...")
    
    try:
        from transformers import AutoTokenizer, AutoModelForCausalLM
        
        # Try to load a small model for testing
        model_name = "microsoft/DialoGPT-small"  # Small model for testing
        print(f"Loading test model: {model_name}")
        
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        # Don't load the full model to save memory, just test tokenizer
        print("✅ Tokenizer loaded successfully")
        
        return True
    except Exception as e:
        print(f"❌ Model loading failed: {e}")
        return False

def test_config_files():
    """Test if configuration files exist"""
    print("\n🔍 Testing configuration files...")
    
    config_files = [
        "examples/grpo_rj_rl.yaml",
        "examples/grpo_rj_rl_muse.yaml"
    ]
    
    for config_file in config_files:
        if os.path.exists(config_file):
            print(f"✅ Found: {config_file}")
        else:
            print(f"❌ Missing: {config_file}")
            return False
    
    return True

def main():
    """Run all tests"""
    print("🚀 RULE Setup Verification")
    print("=" * 50)
    
    # Change to the RULE directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    tests = [
        test_basic_imports,
        test_data_files,
        test_config_files,
        test_model_loading
    ]
    
    passed = 0
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                print("❌ Test failed")
        except Exception as e:
            print(f"❌ Test error: {e}")
    
    print("\n" + "=" * 50)
    print(f"Tests passed: {passed}/{len(tests)}")
    
    if passed == len(tests):
        print("🎉 All tests passed! Your RULE setup is ready.")
        print("\nNext steps:")
        print("1. Update MODEL_PATH in experiment scripts (see MODEL_SETUP_GUIDE.md)")
        print("2. Run experiments with the provided scripts")
        return True
    else:
        print("⚠️  Some tests failed. Please check the issues above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
