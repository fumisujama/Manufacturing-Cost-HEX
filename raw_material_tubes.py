""" RAW MATERIAL FOR TUBES
"""
import math


def raw_material_tubes(lt, dte, Ntp, Np, schedule40_table):
    for tubes in schedule40_table:
        if tubes["Outside diameter"]==dte:
            if lt<=508:
                Nt_tubes = math.floor(tubes["Length"]/lt)
                Ntt = (Ntp * Np) / Nt_tubes

            else:
                Nt_tubes = math.floor(tubes["Length"]/(lt-508))
                Ntt = Ntp * Np + ((Ntp * Np) / Nt_tubes)
        else:
            continue
    return Ntt

def scrap_material_tubes(density_steel, dte, schedule40_table, Ntt, Ntp, Np):
    for tubes in schedule40_table:
        if tubes["Outside diameter"]==dte:
            scrap_material_tubes = density_steel * (math.pi/4) * (dte**2 - (dte - 2 * tubes["Wall thickness"])**2) * (Ntt * tubes["Length"] - Ntp * Np * Lt)
        else:
            continue

    return scrap_material_tubes

