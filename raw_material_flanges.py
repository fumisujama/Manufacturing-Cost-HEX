""" RAW MATERIAL FOR FLANGES
"""
import math


def raw_material_flanges(dfl, ec, tfl, plates_table):
    for plates in plates_table:
        if plates["Thickness"]<tfl:
            continue
        else:
            Nflp = math.floor(plates["Length"] / (Dfl + ec))
            number_plates_flanges = math.ceil(4/Nflp)


    return number_plates_flanges


def scrap_material_flanges(density_steel, dfl, ds, ts, tfl, ec, plates_table):
    for plates in plates_table:
        if plates["Thickness"]<tfl:
            continue
        else:
            scrap_material_flanges = density_steel * plates["Thickness"] * (number_plates_flanges * plates["Length"] * plates["Width"] - math.pi * ((dfl+ec/2)**2 - ((ds + 2*ts)/2)**2))

    return scrap_material_flanges





