from setuptools import setup, find_packages

VERSION = "2.0.0"

setup(
    name='ci_output_parser',
    version=VERSION,
    author='Lizann Brooks',
    author_email='brooks.lizann@gmail.com',
    description='CI output log file parser',
    url='https://github.com/lzbrooks/CIOutputParser',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={
          'console_scripts': [
              'ci_output_parser = ci_output_parser.__main__:parse_command_arguments'
          ]
    },
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
