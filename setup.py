from setuptools import Extension, setup
from Cython.Build import cythonize


ext_modules = [
    Extension(
        "cdelta",
        include_dirs=["src"],
        sources=["src/cdeltamodule.c", "src/bind.c"]
    ),
    Extension("integrate", sources=["src/integrate.pyx"]),
]


if __name__ == '__main__':
    setup(
        name="cmarie",
        version="0.1.0",
        description="Python interface for the fputs C library function",
        author="<your name>",
        author_email="your_email@gmail.com",
        ext_modules=cythonize(ext_modules),
        install_requires=[
            "Cython==3.0.10",
            "scipy==1.13.1",
            "setuptools==70.0.0"
        ]
    )
