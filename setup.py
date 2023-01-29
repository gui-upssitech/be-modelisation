import setuptools

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(name='be_modelisation',
                 packages=['be_modelisation'],
                 install_requires=install_requires)

