from setuptools import setup, find_packages

setup(
      name='super ai pets',
      version='0.0.0',
      packages=find_packages(),
      install_requires=[
          "sapai @ git+https://github.com/manny405/sapai.git@main",
          "sapai-gym @ git+https://github.com/alexdriedger/sapai-gym.git",
          "gym~=0.21.0",
          "scikit-learn"
      ]
)