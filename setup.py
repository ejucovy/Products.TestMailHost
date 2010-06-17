from setuptools import setup, find_packages
import os

version = '0.8'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

# line breaks are needed after each block so that reST doesn't get mad
long_description = """
%s

%s

%s

Download
========
""" % (read("README"),
       read('docs', 'INSTALL.txt'),
       read('docs', 'HISTORY.txt'))

setup(name='Products.TestMailHost',
      version=version,
      description="A monkey patch to send MailHost messages to text files",
      long_description=long_description,
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='zope debug mailhost',
      author='Ethan Jucovy',
      author_email='ethan.jucovy@gmail.com',
      url='http://github.com/ejucovy/Products.TestMailHost',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
