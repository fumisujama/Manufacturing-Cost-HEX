""" RAW MATERIAL CALCULATION FOR TUBESHEETS
"""
import math


def raw_material_tubesheets(tts, diameter_tubesheets, plates_table):
    for plates in plates_table:
        if plates["Thickness"]==tts:
            number_plates_tubesheets = math.ceil(
                    (2 * diameter_tubesheets + 3 * ec)
                    / (plates["Length"])
                )
        else:
            continue
   
    return number_plates_tubesheets

def scrap_material_tubesheets(density_steel, plates_table, diameter_tubesheets, number_plates_tubesheets):
    for plates in plates_table:
        if plates["Thickness"]==tts:
            scrap_material_tubesheets = density_steel * plates["Thickness"] * (number_plates_tubesheets * plates["Length"] * plates["Width"] - (math.pi/2) * diameter_tubesheets**2)
        else:
            continue

    return scrap_material_tubesheets
