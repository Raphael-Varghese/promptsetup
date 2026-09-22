from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="promptsetup",
    version="0.1.0",
    author="llmhacker",
    author_email="raphaelcvarghese@gmail.com",
    description="A custom CLI styling and prompt library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Raphael-Varghese/promptsetup",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.6",
)
