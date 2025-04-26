""" RAW MATERIAL FOR NOZZLES 
"""
import math

def cost_raw_material_nozzles(dnzs, dnzt, schedule40_table):
    
    number_pipes_nozzles = 2
    cost_raw_material_nozzles = 0
    print(f"\n Diameter of shell nozzles: {dnzs}")
    print(f"\n Diameter of tubes nozzles: {dnzt}")
    for tubes in schedule40_table:
        if (tubes["Outside diameter"] - 2*tubes["Wall thickness"])<dnzs:
            continue
        else:
            cost_raw_material_nozzles += tubes["Price"]
            break

    for tubes in schedule40_table:
        if (tubes["Outside diameter"] - 2*tubes["Wall thickness"])<dnzt:
            continue
        else:
            cost_raw_material_nozzles += tubes["Price"]
            break

    return cost_raw_material_nozzles,number_pipes_nozzles


def scrap_material_shell_nozzles(dnzs,tnzs, lnzs, schedule40_table):
    density_steel=7850/1000000000
    for tubes in schedule40_table:
        if (tubes["Outside diameter"] - 2*tubes["Wall thickness"])<dnzs:
            continue
        else:
            scrap_material_nozzles_shell = density_steel * (math.pi/4) * (
                    (dnzs + 2*tnzs)**2 - dnzs**2
                    ) * (tubes["Length"] - 2*lnzs)
            return scrap_material_nozzles_shell
    

def scrap_material_tubes_nozzles(dnzt,tnzs, lnzt, schedule40_table):
    density_steel=7850/1000000000
    for tubes in schedule40_table:
        if (tubes["Outside diameter"] - 2*tubes["Wall thickness"])<dnzt:
            continue
        else:
            scrap_material_nozzles_tubes = density_steel * (math.pi/4) * (
                    (dnzt + 2*tnzs)**2 - dnzt**2
                    ) * (tubes["Length"] - 2*lnzt)
            return scrap_material_nozzles_tubes

