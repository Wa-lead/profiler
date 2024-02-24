from setuptools import setup, find_packages
import profiler
setup(
    name="profiler",
    version="0.2",
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
        "inquirer",
    ],
)
