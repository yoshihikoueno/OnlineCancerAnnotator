import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as f:
    install_reqs = [l.rstrip() for l in f.readlines() if not l.startswith('#')]

setuptools.setup(
    name='online_annotator',
    version='0.1.0',
    author='Yoshihiko Ueno',
    description='Web app to conduct cancer annotation with DNN models',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=install_reqs,
    url='https://github.com/yoshihikoueno/OnlineCancerAnnotator',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programmiing Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
    python_requires='>3.7',
)
