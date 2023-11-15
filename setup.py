from setuptools import setup

with open("README.md") as readme:
    long_description = readme.read()

setup(
    name="meshtools",
    version="0.2.0",
    packages=["meshtools"],
    license="MIT",
    python_requires=">=3.6",
    platforms=["any"],
    description="Mesh Tools for 3D Computer Graphics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Szabolcs Dombi",
    author_email="szabolcs@szabolcsdombi.com",
    url="https://github.com/szabolcsdombi/meshtools/",
    project_urls={
        "Source": "https://github.com/szabolcsdombi/meshtools/",
        "Bug Tracker": "https://github.com/szabolcsdombi/meshtools/issues/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Graphics :: 3D Modeling",
        "Topic :: Multimedia :: Graphics :: Editors",
        "Topic :: Multimedia :: Graphics :: Editors :: Vector-Based",
        "Topic :: Scientific/Engineering :: Visualization",
        "Development Status :: 1 - Planning",
    ],
    keywords=[
        "mesh",
        "tools",
        "editor",
        "geometry",
        "subdivide",
        "shapes",
        "quads",
        "load",
        "obj",
    ],
)
