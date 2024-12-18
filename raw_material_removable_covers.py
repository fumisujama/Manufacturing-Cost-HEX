""" RAW MATERIAL REMOVABLE COVERS
"""
import math


def raw_material_removable_covers(trc, diameter_removable_covers, plates_table):
    for plates in plates_table:
        if plates["Thickness"]==trc:
            number_plates_removable_covers = math.ceil(
                    (2 * diameter_removable_covers + 3 * ec)
                    / (plates["Length"])
                )
        else:
            continue
   
    return number_plates_removable_covers

def scrap_material_removable_covers(density_steel, plates_table, diameter_removable_covers, number_plates_removable_covers):
    for plates in plates_table:
        if plates["Thickness"]==trc:
            scrap_material_removable_covers = density_steel * plates["Thickness"] * (number_plates_removable_covers * plates["Length"] * plates["Width"] - (math.pi/2) * diameter_removable_covers**2)
        else:
            continue

    return scrap_material_removable_covers
