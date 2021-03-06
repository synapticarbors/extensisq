import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="extensisq",
    version="0.0.1",
    author="W.R. Kampinga",
    author_email="wrkampi@tuta.io",
    description="extend solve_ivp of scipy.integrate with OdeSolver objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WRKampi/extensisq",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy>=1.4.0",
        "scipy>=1.0.0",
    ],
    keywords = ['ode', 'ode-solver', 'ivp', 'ivp-methods', 'scipy', 
        'scipy-integrate', 'runge-kutta', 'differential-equations'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    tests_require=['pytest']
)