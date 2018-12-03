from setuptools import setup, find_packages
setup(
    name="rainbowgram",
    version="1.0.0",
    packages=find_packages(),
    install_requires = [
        "scipy",
        "numpy",
        "toolz",
        "librosa",
        "matplotlib"
    ]
)
