import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SQLServerToPandasDataFrame-germanandresjejencortes", # Replace with your own username
    version="0.0.1",
    author="Andres Jejen",
    author_email="gajcam@gmail.com",
    description="Query Data from a Private DataBase and save it in a Pandas DataFrame",
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
)