# Graph-RULE: Master Thesis Project Setup
# Author: Debraj Das (21ME3AI31)
# Project: Graph Neural Network Unlearning with Reinforcement Learning
# Supervisor: Dr. Plaban Bhowmick
#
# Licensed under the MIT License

import os
import re

from setuptools import find_packages, setup


def get_version() -> str:
    with open(os.path.join("verl", "__init__.py"), encoding="utf-8") as f:
        file_content = f.read()
        pattern = r"__version__\W*=\W*\"([^\"]+)\""
        (version,) = re.findall(pattern, file_content)
        return version


import os
import re
from pathlib import Path
from setuptools import find_packages, setup


def get_version() -> str:
    """Get version from package"""
    try:
        with open("verl/__init__.py", encoding="utf-8") as f:
            version = re.search(r'__version__ = "(.*?)"', f.read())
            return version.group(1) if version else "1.0.0"
    except FileNotFoundError:
        return "1.0.0"


def get_long_description() -> str:
    """Get long description from README"""
    try:
        with open("README.md", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Graph-RULE: Revolutionary Graph Neural Network Unlearning Framework"


def get_requires() -> list[str]:
    """Parse requirements.txt"""
    requirements = []
    try:
        with open("requirements.txt", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                # Skip comments, empty lines, and lines with #
                if line and not line.startswith("#") and "#" not in line:
                    requirements.append(line)
    except FileNotFoundError:
        # Fallback minimal requirements
        requirements = [
            "torch>=2.0.0",
            "numpy>=1.24.0",
            "networkx>=3.0",
            "matplotlib>=3.7.0",
            "pandas>=2.0.0",
            "scikit-learn>=1.3.0"
        ]
    return requirements


# Development and optional dependencies
extra_require = {
    "dev": [
        "pre-commit",
        "black",
        "flake8", 
        "mypy",
        "pytest",
        "pytest-cov"
    ],
    "gpu": [
        "torch-geometric",
        "dgl",
    ],
    "visualization": [
        "plotly>=5.15.0",
        "seaborn>=0.12.0",
        "bokeh>=3.1.0"
    ],
    "notebook": [
        "jupyter",
        "ipykernel",
        "ipywidgets"
    ]
}


def main():
    """Main setup function"""
    setup(
        name="graph-rule",
        version=get_version(),
        description="Graph-RULE: Reinforcement Learning-based Graph Neural Network Unlearning Framework",
        long_description=get_long_description(),
        long_description_content_type="text/markdown",
        author="Debraj Das",
        author_email="debraj.das@student.university.edu",
        maintainer="Debraj Das",
        license="MIT License", 
        url="https://github.com/debrajdas/graph-rule",
        project_urls={
            "Documentation": "https://github.com/debrajdas/graph-rule/blob/main/README.md",
            "Source Code": "https://github.com/debrajdas/graph-rule",
            "Thesis Report": "https://github.com/debrajdas/graph-rule/blob/main/MTECH_MTP_FINAL_REPORT_COMPREHENSIVE.md"
        },
        package_dir={"": "."},
        packages=find_packages(where="."),
        python_requires=">=3.8.0",
        install_requires=get_requires(),
        extras_require=extra_require,
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Science/Research",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9", 
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        keywords=[
            "graph neural networks",
            "machine unlearning", 
            "reinforcement learning",
            "privacy preserving ai",
            "graph algorithms",
            "deep learning"
        ],
        entry_points={
            "console_scripts": [
                "graph-rule=graph_rule_experimental_pipeline:main",
                "graph-rule-curves=generate_thesis_defense_curves:main",
                "graph-rule-validate=final_thesis_validation:main"
            ],
        },
        include_package_data=True,
        zip_safe=False,
    )


if __name__ == "__main__":
    main()
