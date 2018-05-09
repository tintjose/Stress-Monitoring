from distutils.core import setup

setup(name='Savoring',
      version='1.0',
      description='Python Distribution Utilities',
      author='Sina Labbaf',
      author_email='slabbaf@uci.edu',
      url='',
      packages=['server'],
      install_requires=[
          'flask',
          'flask_security',
          'flask_mongoengine',
          'flask_cors'
          ],
     )
