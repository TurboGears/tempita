from setuptools import setup

version = '0.6.0'

setup(name='Tempita',
      version=version,
      description="A very small text templating language",
      long_description="""\
Tempita is a small templating language for text substitution.

This isn't meant to be the Next Big Thing in templating; it's just a
handy little templating language for when your project outgrows
``string.Template`` or ``%`` substitution.  It's small, it embeds
Python in strings, and it doesn't do much else.

You can read about the Language and the Interface at
https://github.com/TurboGears/tempita/blob/main/README.rst,
and there's nothing more to learn about it.
""",
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Topic :: Text Processing',
          'Programming Language :: Python :: 3',
      ],
      keywords='templating template language html',
      author='Ian Bicking',
      author_email='ianb@colorstudy.com',
      url='https://github.com/TurboGears/tempita',
      license='MIT',
      packages=['tempita'],
      include_package_data=True,
      zip_safe=True)
