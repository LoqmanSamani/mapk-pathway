

"""
The SBML file was generated using the https://sys-bio.github.io/makesbml/ tool.

# Reactions

R1: NGF -> Raf;  r0*NGF
R2: Raf -> Mek; r1*Raf
R3: Mek -> Raf; r_1*Mek
R4: Mek -> Erk; r2*Mek
R5: Erk -> Mek; r_2*Erk
R6: Raf -> Erk; r3*Raf
R7:Erk -> Raf; r_3*Erk
R8: Erk ->  ; d*Erk 

# initial concentrations

NGF = 50
Raf = 0
Mek = 0
Erk = 0

# rate constants

r0 = 1
r1 = 6.18
r2 = 0.63
r3 = 0.96
r_1 = -0.17
r_2 = -3.73
r_3 = 0.40
d = 1
sigma = 1


"""
