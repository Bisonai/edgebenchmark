import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="edgebenchmark",
    version="0.0.11",
    author="Bisonai",
    author_email="contact@bisonai.com",
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
    install_requires=[
        "click>=7.1.2",
        "requests>=2.24.0",
    ],
    include_package_data=True,
    entry_points='''
        [console_scripts]
        edgebenchmark=edgebenchmark.edgebenchmark_cli:cli
    ''',
)
