from setuptools import setup

setup(name='text_extraction',
      version='0.1',
      description='some text processing',
      url='https://github.com/MatthewMong/text_extraction',
      author='Matthew Mong',
      author_email='matthew.mong1999@gmail.com',
      license='MIT',
      install_requires=[
          'flask', 'biopython', 'spacy'
      ],
      zip_safe=False)