from setuptools import setup, find_packages


setup(
    name="twpack",
    version="1.0.7",
    url="https://github.com/EllenSshi/otus-qa-course-dz4-api-testing",
    author="Alyona Shishkina",
    author_email="author@example.com",
    description="Test package wheel",
    packages=find_packages(),
    long_description=open('README.md').read(),
    install_requires=["pytest>=5.3.2", "requests>=2.22.0", "jsonschema>=3.2.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)