import setuptools
with open('./requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Thaispoon", # Replace with your own username
    version="0.0.1",
    author="Deduq",
    author_email="niti08@gmail.com",
    description="A small package for thai Spoonerism",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=install_requires,
)