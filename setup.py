from setuptools import setup, find_packages

setup(
    name="ml_miniproject",
    version="0.1.0",
    author="Shivani Kasaudhan",
    description="End-to-end Machine Learning mini project",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn",
        "streamlit"
    ],
    python_requires=">=3.8",
)
