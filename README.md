Unraveling the Complexity of MAPK Signaling Pathways
------------------------------------------------

This repository  is dedicated to  reproducing the work   presented  in the article titled  " Growth Factor-Induced MAPK  Network Topology  Shapes Erk Response
Determining     PC-12  Cell     Fate " by SilviaD. M. Santos, Peter J. Verveer, and 
Philippe I. H. Bastiaens, originally published in 2007. In our research endeavor,
we aim to replicate the findings and  methodologies outlined in this influential
paper.   Additionally,   we  have  redefined  aspects  of the  signaling  pathway 
studied in this article in various ways and used different tools and  parameter 
estimation methods to determine previously unknown parameters.


Overview
-----------------------------------------------

In this repository, you will find a comprehensive collection of files and resources
related  to our efforts  in reproducing  the study.  Our approach encompasses the 
original methodology,  "Modular Response Analysis (MRA)(a sensitivity analysis 
developed by  Kholodenko et al.)".   In addition, we have employed two different
approaches: one utilizing  "petab"  and  "pypesto"  tools, and the other involving 
gradient-based algorithms implemented in Python."


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
----------------------------------------------------------------------------------------------------------------------------------------------

## Copyright and Permissions

This repository is intended for educational and research purposes. The materials and content provided within 

this  repository  is subject to  copyright and intellectual property rights. The  reproduction  and use  of these 

materials  are governed  by the principles  of fair use  and  applicable  copyright laws.  Users are encouraged 

to  review  and  respect the original  authors' rights  as   specified   in the   referenced   articles   and   papers. 

When   using or referencing the   content within this repository,  proper attribution and citation to the original

sources,    including   the cited articles and authors,   is essential.    Any commercial   or for-profit   use of the 

materials   in this repository   may require additional   permissions or licensing from the respective copyright

holders. The repository   maintainers do not assume liability  for any misuse or violation of copyright laws by

users. For questions or inquiries regarding copyright, permissions, or licensing, please contact the respective

copyright holders or authors as indicated in the original sources.



