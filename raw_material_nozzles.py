""" RAW MATERIAL FOR NOZZLES 
"""
import math

def raw_material_nozzles(dnzs, dnzt, lnz, schedule40_table):
    
    number_pipes_nozzles = 2
    return number_pipes_heads


def scrap_material_nozzles_shell(density_steel, dnzs, lnz, schedule40_table):
    for tubes in schedule40_table:
        if tubes["Outside diameter"] - 2*tubes["Wall thickness"]<dnzs:
            continue
        else:
            scrap_material_nozzles_shell = density_steel * (math.pi/4) * (
                    (dnzs + 2*tnzs)**2 - dnzs**2
                    ) * (tubes["Length"] - 2*lnz)

    return scrap_material_nozzles_shell
     
    

def scrap_material_nozzles_tubes(density_steel, dnzt, lnz, schedule40_table):
    for tubes in schedule40_table:
        if tubes["Outside diameter"] - 2*tubes["Wall thickness"]<dnzt:
            continue
        else:
            scrap_material_nozzles_tubes = density_steel * (math.pi/4) * (
                    (dnzt + 2*tnzs)**2 - dnz**2
                    ) * (tubes["Length"] - 2*lnz)

    return scrap_material_nozzles_tubes
