import setuptools

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(name='be-modelisation',
                 packages=['be-modelisation'],
                 install_requires=install_requires)

