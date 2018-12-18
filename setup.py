import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="supremacy1914_wrapper",
    version="0.1.2",
    author="Joost Sijm",
    author_email="joostsijm@gmail.com",
    description="Supremacy1914 API wrapper in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joostsijm/supremacy1914_wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
