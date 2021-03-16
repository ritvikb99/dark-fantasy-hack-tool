from setuptools import setup, find_packages

# Change version to desired version number
setup(name='dark-fantasy-hack-tool',
      packages=find_packages(),
      version="0.1.0",
      install_requires=['html2text'],
      zip_safe=False)
