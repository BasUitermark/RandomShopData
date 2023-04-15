from setuptools import find_packages, setup


setup(
    name="RandomShopData",
    version='0.1',
    author='Bas Uitermark',
    description='A small program that creates randomized shop data for TRPG',
    py_modules=['RandomShopData', 'rsdLibrary'],
    python_requires='>=3.10',
    install_requires=[
        'pandas',
        'termcolor',
        'simple-term-menu',
        'scipy',
    ],
    entry_points='''
        [console_scripts]
        RandomShopData=RandomShopData:rsd
    ''',
)
