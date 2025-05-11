import sys
import subprocess
import pkg_resources

# List of required packages
REQUIRED_PACKAGES = [
    'gradio',
    'torch',  # PyTorch
    'numpy',  # Often a dependency
    # Add others as needed (e.g., 'transformers', 'pandas')
]

def check_python_version():
    """Ensure Python version is >= 3.7 (Gradio requires 3.7+)"""
    if sys.version_info < (3, 7):
        raise RuntimeError(f"Python 3.7+ required. Detected: {sys.version}")

def check_packages():
    """Check if required packages are installed"""
    missing_packages = []
    for package in REQUIRED_PACKAGES:
        try:
            pkg_resources.get_distribution(package)
        except pkg_resources.DistributionNotFound:
            missing_packages.append(package)
    
    if missing_packages:
        raise ImportError(
            f"Missing packages: {missing_packages}. "
            f"Install with: `pip install {' '.join(missing_packages)}`"
        )

def check_cuda():
    """Verify PyTorch can detect CUDA (if GPU is expected)"""
    import torch
    if not torch.cuda.is_available():
        print("⚠️ Warning: CUDA not available. PyTorch will use CPU.")

if __name__ == "__main__":
    try:
        check_python_version()
        check_packages()
        check_cuda()
        print("✅ All requirements are satisfied.")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)  # Exit with error code (useful for CI/CD)