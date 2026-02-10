from setuptools import setup

setup(
    name='pycrafter6500',
    version='0.1.0',
    description='Local editable version of Pycrafter6500',
    # This tells pip to include the specific .py files found in the root directory
    py_modules=['pycrafter6500', 'erle'], 
    install_requires=['numpy', 'pyusb'],
)