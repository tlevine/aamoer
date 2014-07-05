from distutils.core import setup

from aamoer import __version__, __author__

setup(name='aamoer',
      author=__author__,
      author_email='_@thomaslevine.com',
      description='Run statistics on data tables.',
      url='https://github.com/tlevine/aamoer',
      packages=['aamoer'],
      tests_require = ['nose'],
      version=__version__,
      license='AGPL',
)
