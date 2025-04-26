""" RAW MATERIAL REMOVABLE COVERS
"""
import math


def cost_raw_material_removable_covers(trc, ec, diameter_removable_covers, plates_table):
    ec=float(ec.value)
    for plates in plates_table:
        if plates["Thickness"]>=trc:
            number_plates_removable_covers = math.ceil(
                    (2 * diameter_removable_covers + 3 * ec)
                    / (plates["Length"])
                )
            cost_raw_material_removable_covers = number_plates_removable_covers * plates["Price"]
            return cost_raw_material_removable_covers, number_plates_removable_covers

        else:
            continue


def scrap_material_removable_covers(trc, plates_table, diameter_removable_covers, number_plates_removable_covers):
    density_steel = 7850/1000000000
    for plates in plates_table:
        if plates["Thickness"]>=trc:
            scrap_material_removable_covers = density_steel * plates["Thickness"] * (number_plates_removable_covers * plates["Length"] * plates["Width"] - (math.pi/2) * diameter_removable_covers**2)
            return scrap_material_removable_covers
        else:
            continue

