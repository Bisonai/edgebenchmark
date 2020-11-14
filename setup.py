import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="edgebenchmark",
    version="0.0.1",
    author="Martin Kersner",
    author_email="martin@bisonai.com",
    description="Tool to benchmark speed of machine learning models on real mobile devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bisonai/edgebenchmark",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points='''
        [console_scripts]
        edgebenchmark=edgebenchmark_cli:cli
    ''',
)
