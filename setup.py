import setuptools

setuptools.setup(
    name="amo-blocklist",
    version="0.1.0",
    url="https://github.com/mozilla-services/amo-blocklist",

    author="Mathieu Agopian",
    author_email="magopian@mozilla.com",

    description="A kinto plugin to generate and serve XML blocklist files for Firefox et al.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
