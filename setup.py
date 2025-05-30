from setuptools import setup, find_packages

setup(
    name='finops-prompts',
    version='0.1.0',
    description='Prompt library for FinOps AI Agents',
    author='Your Name',
    packages=find_packages(),
    package_data={"finops_prompts": ["prompts.json"]},
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.7",
)
