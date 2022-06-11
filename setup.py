from setuptools import setup, find_packages


setup(
    name="smartcrud",
    version="0.0.1",  # Upgrades, Updates, Fixes
    author="Muthupandian",
    author_email="muthu.thangarajan@imdexlimited.com",
    description="Dataset Management",
    packages=["smartcrud"],
    include_package_data=True,
    url="https://github.com/Datacloud/workflow",
    install_requires=[
        "requests",
        "loguru"
    ],
    classifiers=[
                    "Programming Language :: Python :: 3",
                    "License :: OSI Approved :: MIT License",
                    "Operating System :: OS Independent",
                ],
    python_requires='>=3.6',
)
