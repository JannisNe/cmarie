from setuptools import Extension, setup, find_packages
from Cython.Build import cythonize


ext_modules = [
    Extension(
        "cmarie.cdelta",
        include_dirs=["extensions/cmarie"],
        sources=["extensions/cmarie/cdeltamodule.c", "extensions/cmarie/bind.c"]
    ),
    Extension("cmarie.integrate", sources=["extensions/cmarie/integrate.pyx"]),
]


if __name__ == '__main__':
    setup(
        name="cmarie",
        version="0.1.0",
        description="Python interface for the fputs C library function",
        author="<your name>",
        author_email="your_email@gmail.com",
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        ext_modules=cythonize(ext_modules),
        install_requires=[
            "Cython==3.0.10",
            "scipy==1.13.1",
            "setuptools==70.0.0"
        ]
    )
