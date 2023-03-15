#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


from setuptools import find_packages, setup

MAIN_REQUIREMENTS = [
    "airbyte-cdk~=0.2"
]

TEST_REQUIREMENTS = [
    "pytest~=6.2",
    "connector-acceptance-test",
    "requests_mock"
]

setup(
    name="source_kobotoolbox",
    description="Source implementation for Kobotoolbox.",
    author="Airbyte",
    author_email="contact@airbyte.io",
    packages=find_packages(),
    install_requires=MAIN_REQUIREMENTS,
    package_data={"": ["*.json", "*.yaml"]},
    extras_require={
        "tests": TEST_REQUIREMENTS,
    },
)
