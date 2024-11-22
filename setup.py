from setuptools import setup, find_packages

setup(
    name="math_tools",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)