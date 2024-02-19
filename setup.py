from setuptools import setup, find_packages

setup(
    name="profiler",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'profiler=profiler.profiler:main',
        ],
    },
    author="Waleed Alasad",
    description="A simple profiler tool.",
    install_requires=[
        "line_profiler",
    ],
)
