from setuptools import setup, find_packages


setup(
   name='scrolls',
   version='0.1.9',
   description='Useful solutions/templates/patterns',
   author='Oleg Dudnik',
   author_email='Oleggelo86@gmail.com',
   packages=find_packages(include=['scrolls', 'scrolls.*']),
   install_requires=[
      'opencv-python',
      'scikit-learn',
      'pillow',
      'matplotlib',
      'numpy'
   ],
)
