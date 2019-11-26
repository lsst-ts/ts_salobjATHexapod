from setuptools import setup, find_namespace_packages

scm_version_template = """
# Generated by setuptools_scm

__all__ = ["__version__"]

__version__ = "{version}"

"""

setup(
    name="ts_athexapod",
    use_scm_version={"write_to": "python/lsst/ts/ATHexapod/version.py",
                     "write_to_template": scm_version_template},
    package_dir={"": "python"},
    packages=find_namespace_packages(where="python"),
    scripts=["bin/runATHexapodCSC.py"]
)
