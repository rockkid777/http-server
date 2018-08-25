from setuptools import setup

setup(name='http-server',
      version='0.1',
      description='Simple naive implementation for a REST HTTP server',
      url='https://github.com/rockkid777/http-server',
      author='Adam Revesz',
      author_email='reveszadam@gmail.com',
      license='MIT',
      packages=['http-server'],
      test_suite='nose.collector',
      tests_require=['nose'])
