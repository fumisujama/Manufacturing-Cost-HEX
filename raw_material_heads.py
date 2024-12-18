""" RAW MATERIAL FOR HEADS
"""
import math

def raw_material_heads(dh, lh, schedule40_table):
    if dh<609.6:
        number_pipes_heads = 1
        return number_pipes_heads
    else:
        number_plates_heads = 1
        return number_plates_heads

def scrap_material_heads(density_steel, dh, th, lh, schedule40_table, plates_table):
    if dh<609.6:
        for tubes in schedule40_table:
            if tubes["Outside diameter"]==dh:
                scrap_material_heads = density_steel * (math.pi/4) * (dh**2 - (dh-2*th)**2) * (tubes["Length"] - 2*lh)
            else:
                continue
    else:
        for plates in plates_table:
            if plates["Thickness"]==th:
                scrap_material_heads = density_steel * (plates["Length"] * plates["Width"] * plates["Thickness"] - (math.pi/4) * (dh**2 - (dh - 2*th)**2) * 2 * lh)

    return scrap_material_heads

    
    

