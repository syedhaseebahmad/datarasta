"""Setup script for datarasta package."""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Read version from package
version = {}
version_file = this_directory / "datarasta" / "__init__.py"
exec(version_file.read_text(), version)

setup(
    name="datarasta",
    version=version["__version__"],
    author="DataRasta Contributors",
    author_email="",
    description="A Python library for data quality testing with comprehensive metrics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/syedhaseebahmad/datarasta",
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.20.0",
        "scipy>=1.7.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.910",
        ],
    },
    keywords="data quality, data validation, data testing, data profiling, metrics",
    project_urls={
        "Bug Reports": "https://github.com/syedhaseebahmad/datarasta/issues",
        "Source": "https://github.com/syedhaseebahmad/datarasta",
        "Documentation": "https://github.com/syedhaseebahmad/datarasta#readme",
    },
)

