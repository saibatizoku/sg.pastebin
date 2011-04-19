from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='sg.pastebin',
      version=version,
      description="Allows for snippets of source code to be added as a content type for Plone 4>",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='plone dexterity pastebin',
      author='Joaquín Rosales'
      'collective.autopermission',,
      author_email='globojorro@gmail.com',
      url='https://github.com/saibatizoku/sg.pastebin',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sg'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'Plone',
          'plone.app.dexterity',
          'collective.autopermission',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
            target = plone
      """,
      )
