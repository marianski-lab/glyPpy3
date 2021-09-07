import math
from . import calc_cp
from . import rmsd, utilities
import numpy as np
import sys, copy
from scipy import interpolate
from scipy.linalg import expm
from optparse import OptionParser

"""
These functions are all genetic algorithm operations. Each operation modifies existing conformer objects.
"""

def modify_glyc(conf, bond):
    """Modifies the angle between the two rings attached by a specified glycosidic bond

    :param conf: a conformer object
    :param bond: (int) index of which edge in the list of edges of the conformer
    """
    edge = conf.graph.edges[bond]
    atoms = len(edge['linker_atoms']) ; angles = [] ; n=0

    while n < atoms-3: 
        angles.append((utilities.draw_random()*360)-180.0)
        n += 1 
    if atoms == 5:
        conf.set_glycosidic(bond, angles[0], angles[1])
    elif atoms== 6:
        conf.set_glycosidic(bond, angles[0], angles[1], angles[2])
    elif atoms == 7: #NAc linkage, set two bonds linear
        angles[1] = (utilities.draw_random_int(top=2)+0.005)*179.0
        angles[2] = (utilities.draw_random_int(top=2)+0.005)*179.0
        #print( angles )
        conf.set_glycosidic(bond, angles[0], angles[1], angles[2], angles[3])

def modify_c6(conf, ring):
    """Modifies the 6th carbon of a ring, randomly draws an integer and edits the dihedral angle

    :param conf: a conformer object
    :param ring: (int) index that specifies which ring of the conformer is being edited 
    """
    node = conf.graph.nodes[ring]
    if 'c6_atoms' in node:
        atoms = node['c6_atoms']
        dih = ((utilities.draw_random_int(top=3)-1)*120.0)+60.0
        conf.set_c6(ring, dih)

def modify_ring(conf, ring, phi, psi):
    """ This does nothing at the moment
    """
    pass

def cross_over(conf1, conf2):
    """Swaps angle measures of two conformers

    :param conf1: the first conformer object
    :param conf2: the second conformer object
    """

    #Compare the edges.
    #if connectivity is identical, compare dihs angles, then exchange the information if different. 
    #if conf1.graph.edges == conf2.graph.edges: 
    #    for e1, e2 in zip(conf1.graph.edges, conf2.graph.edges):
    #        if bond_distance(l1, conf1.graph.edges[e1]['dih'], conf2.graph.edges[e2]['dih'], 'l1') < 5.0:
    #            pass
    #        else:

        


    #exchange glycosidic bond:
    bond = utilities.draw_random_int(len(conf1.dih))
    print("Modifying bond number {0:2d}".format(bond))
    phi1, psi1 = conf1.dih_angels[bond]
    phi2, psi2 = conf2.dih_angels[bond] 

    conf2.set_glycosidic(bond, phi1, psi1)
    conf1.set_glycosidic(bond, phi2, psi2)




