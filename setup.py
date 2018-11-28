from setuptools import setup


setup(
    name='cashconvert',
    version='1.0',
    py_modules=['cashconvert'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        cashconvert=cli:cli
    ''',
)