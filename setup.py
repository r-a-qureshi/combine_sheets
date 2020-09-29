from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='combine_sheets',
    version='0.1',
    description="""Combine multiple excel files with a single worksheet into"""\
        """ a single excel file with multiple worksheets. Output file must"""\
        """ be in a different directory than the input files.""",
    url='https://github.com/r-a-qureshi/combine_sheets/',
    author='Rehman Qureshi',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts":["combine_sheets = combine_sheets.combine_sheets:main"]
    },
    keywords="Excel, combining worksheets",
    zip_safe=False,
)