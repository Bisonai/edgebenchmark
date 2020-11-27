import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="edgebenchmark",
    version="0.0.3",
    author="Martin Kersner",
    author_email="martin@bisonai.com",
    description="Tool to benchmark speed of machine learning models on real mobile devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bisonai/edgebenchmark",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    entry_points='''
        [console_scripts]
        edgebenchmark=edgebenchmark.edgebenchmark_cli:cli
    ''',
)
