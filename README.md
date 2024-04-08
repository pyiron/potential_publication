# Workflows for "From electrons to phase diagrams with classical and machine learning potentials: automated workflows for materials science with pyiron"

Sarath Menon, Yury Lysogorskiy, Alexander L. M. Knoll, Niklas Leimeroth, Marvin Poul, Minaam Qamar, Jan Janssen, Matous Mrovec, Jochen Rohrer, Karsten Albe, Jörg Behler, Ralf Drautz, Jörg Neugebauer    

[Preprint at http://arxiv.org/abs/2403.05724 (2024)](http://arxiv.org/abs/2403.05724)

This repository contains the workflows for the above publication. 

## Setting up the environment

The computational environment with all the necessary software can be installed using [conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html). First step is to create an environment:

```
conda env create -f binder/environment.yml
```

After the environment is created, it can be activated by

```
conda activate potentials
```

Once the environment is activated, the Tensorpot can be installed:

```
git clone --depth 1 --single-branch https://github.com/ICAMS/TensorPotential
cd TensorPotential
python setup.py install
cd ..
```
after this, jupyter lab can be started with

```
jupyter lab
```

## Setting up pyiron

Create a configuration file called `.pyiron` in your home directory and add the following contents

```
[DEFAULT]
FILE = ~/pyiron.db
PROJECT_PATHS = ~/pyiron/projects
RESOURCE_PATHS = ~/pyiron/resources:~/<path-to-repo>/potential_publication/resources
```

Note that `<path-to-repo>` needs to be replaced with the actual path.

## Interatomic potentials used in this work

The files for the interatomic potentials used in this work is available in the `resources/lammps/potentials` folder.

