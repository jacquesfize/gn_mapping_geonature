import setuptools
from pathlib import Path


root_dir = Path(__file__).absolute().parent
with (root_dir / "VERSION").open() as f:
    version = f.read()
with (root_dir / "README.md").open() as f:
    long_description = f.read()
with (root_dir / "requirements.in").open() as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name="MappingGeoNature",
    version=version,
    description="A module to map users/organisms which uses GeoNature",
    long_description=long_description,
    long_description_content_type="text/markdown",
    maintainer="PNE",
    maintainer_email="geonature@ecrins-parcnational.fr",
    url="https://github.com/PnX-SI/gn_mapping_geonature",
    packages=setuptools.find_packages("backend"),
    package_dir={"": "backend"},
    package_data={"gn_mapping_geonature.migrations": ["data/*.sql"]},
    install_requires=requirements,
    zip_safe=False,
    entry_points={
        "gn_module": [
            "code = gn_mapping_geonature:MODULE_CODE",
            "picto = gn_mapping_geonature:MODULE_PICTO",
            "blueprint = gn_mapping_geonature.blueprint:blueprint",
            "config_schema = gn_mapping_geonature.conf_schema_toml:GnModuleSchemaConf",
            "migrations = gn_mapping_geonature:migrations",
        ],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
)
