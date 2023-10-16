The 'petab' directory contains files for  generating petab files in each case.
The files in this directory create the first model, which can then be used as
a template for generating other models.


The SBML file was generated using the https://sys-bio.github.io/makesbml/ tool.
-------------------------------------------------------------------------------
# Reactions
-----------
R1: EGF -> Raf;  r0*EGF # if Egf is the stimulus

R1: NGF -> Raf;  r0*EGF # if Ngf is the stimulus

R2: Raf -> Mek; r1*Raf

R3: Mek -> Raf; r_1*Mek

R4: Mek -> Erk; r2*Mek

R5: Erk -> Mek; r_2*Erk

R6: Raf -> Erk; r3*Raf

R7:Erk -> Raf; r_3*Erk

R8: Erk ->  ; d*Erk 


# initial concentrations
------------------------
EGF = 100 # if Egf is the stimulus

NGF = 50  # if Ngf is the stimulus

Raf = 0

Mek = 0

Erk = 0


# rate constants
----------------
r0 = 1

r1 = 1.11

r2 = 1

r3 = 0.09

r_1 = -0.10

r_2 = -0.35

r_3 = -0.53

d = 1

sigma = 1     
