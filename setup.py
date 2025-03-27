from setuptools import setup, find_packages

setup(
    name="texttools",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Lazer Kat",
    author_email="lazerkato.o@gmail.com",
    description="A cool lil' package for text utilities",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lazerkatsweirdstuff/texttools/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
