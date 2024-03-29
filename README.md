# Unraveling the Complexity of MAPK Signaling Pathway


![abstract](https://github.com/LoqmanSamani/mapk_pathway/blob/systembiology/article/appendix/abstract.png)
<sub>**Graphical abstract of the project**</sub>

![Static Badge](https://img.shields.io/badge/MIT_License-red)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/scipy)
![Static Badge](https://img.shields.io/badge/NumPy-1.25-darkgreen)
![Static Badge](https://img.shields.io/badge/pandas-2.1-darkblue)
![Static Badge](https://img.shields.io/badge/matplotlib-3.8-lightblue?color=blue)
![Static Badge](https://img.shields.io/badge/PEtaB-0.2.7-yellow)
![Static Badge](https://img.shields.io/badge/pyPESTO-0.4-red)

This repository  is dedicated to  reproducing the work   presented  in the article titled  [Growth Factor-Induced MAPK Network Topology Shapes Erk Response
Determining PC-12  Cell Fate](https://www.nature.com/articles/ncb1543) by SilviaD. M. Santos, Peter J. Verveer, and 
Philippe I. H. Bastiaens, originally published in 2007. In our research endeavor,
we aim to replicate the findings and  methodologies outlined in this influential
paper.   Additionally,   we  have  redefined  aspects  of the  signaling  pathway 
studied in this article in various ways and used different tools and  parameter 
estimation methods to determine previously unknown parameters.

## Acknowledgments
-----------------------------------------------------------------

We ( Ines Schneider and Loghman Samani ) would like to express our gratitude to the following individuals who played a crucial role in this project:

- [Prof. Dr. Nicole Radde](https://www.isa.uni-stuttgart.de/institut/team/Radde-00003/): Our esteemed professor, whose guidance and support were instrumental throughout the project. The project was conducted as part of her [Systems Theory in Systems Biology](https://www.ist.uni-stuttgart.de/teaching/lectures/2022ss/stsb/) course.

- [M.Sc. Amatus Beyer](https://www.isa.uni-stuttgart.de/institut/team/Beyer-00005/): our project supervisor, whose expertise and feedback significantly contributed to the development and improvement of our work. We appreciate his valuable insights and continuous support.


Overview
-----------------------------------------------

In this repository, you will find a comprehensive collection of files and resources
related  to our efforts  in reproducing  the study.  Our approach encompasses the 
original methodology,  [Modular Response Analysis](https://www.pnas.org/doi/abs/10.1073/pnas.192442699). In addition, we have employed two
different approaches: one utilizing  [petab](https://petab.readthedocs.io/en/latest/) and [pypesto](https://pypesto.readthedocs.io/en/latest/) tools, and the other involving 
gradient-based algorithms implemented in Python. 


Folder Structure
------------------------------------------------

`replica_work` 

Contains files and materials related to the replication of the original study using 
the MRA  approach.  (some results may not match those of the study  due to the 
use of different statistical methods)


`petab_&_pypesto` 

This folder is dedicated to one of the new approaches, which utilizes the "petab"
and "pypesto" tools.  We have  developed  Python  code to  replicate the study's 
findings using this modern framework.


`file_collection` 

a collection  of different datasets for  both stimuli (NGF and EGF) ,  each  with all 
necessary files (.tsv & .yaml) that can be used to estimate unknown parameters
with the pypesto package.


`params_estimation` 

Within  this directory,   you  will find  various  Python  programs  that  serve as
algorithms for estimating the unknown parameters defined within the system.


`article` 

Contained within this directory are both the comprehensive report (article) and the accompanying appendix files, detailing the project.


| Folder Structure    | Description                                                                                                         |
|---------------------|---------------------------------------------------------------------------------------------------------------------|
| `replica_work`      | This folder contains files that reproduce the same work as the original paper.                                      |
| └── `CI`            | Subfolder containing files related to calculation intensity.                                                        |
| └── `GRC`           | Subfolder containing files related to the Global Response Coefficients.                                             |
| └── `LRC`           | Subfolder containing files related to the Local Response Coefficients.                                              |
| └── `MC`            | Subfolder containing files related to monte carlo simulation.                                                       |
|                     |                                                                                                                     |
| `petab_&_pypesto`   | This folder contains PEtab and PyPESTO-related files.                                                               |
| └── `petab`         | Subfolder containing code that can be used to create petab files.                                                   |
| └──  `pypesto`      | Subfolder containing code that can be used to create a pypesto problem.                                             |
|                     |                                                                                                                     |
| `file_collection`   | This folder contains a collection of datasets, which can be used to estimate unknown parameters                     |
| └── `ngf`           | Subfolder containing NGF-related files.                                                                             |
| └── `egf`           | Subfolder containing EGF-related files.                                                                             |
|                     |                                                                                                                     |
| `params_estimation` | This folder contains files for estimating unknown parameters in various cases using the gradient descent algorithm. |
| └── `data`          | Subfolder contains the outcomes (numerical and plots) of the simulations.                                           |
| `article`           | This folder contains a report on our work.                                                                          |
----------------------------------------------------------------------------------------------------------------------------------------------


## Copyright and Permissions

This repository is governed by the terms of the [MIT License](https://github.com/LoqmanSamani/mapk_pathway/blob/systembiology/LICENSE) 





