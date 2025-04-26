""" RAW MATERIAL FOR FLANGES
"""
import math



def cost_raw_material_flanges(dfl, ec, tfl, plates_table):
    ec=float(ec.value)

    for plates in plates_table:
        if plates["Thickness"]>=tfl:
            Nflp = math.floor(plates["Length"] / (dfl + ec))
            print(f"number of flanges per plate: {Nflp}")
            number_plates_flanges = math.ceil(4/Nflp)
            print(f"number of plates for all flanges: {number_plates_flanges}")
            print(f"Price of the plate: ${plates["Price"]}")
            cost_raw_material_flanges = number_plates_flanges * plates["Price"]
            return cost_raw_material_flanges, number_plates_flanges
        else:
            continue



def scrap_material_flanges(dfl, ds, ts, tfl, ec, plates_table, number_plates_flanges):
    ds=float(ds.value)
    ec=float(ec.value)   
    density_steel=7850/1000000000

    for plates in plates_table:

        density_steel=float(density_steel)
        if plates["Thickness"]<tfl:
            continue
        else:
            scrap_material_flanges = density_steel * plates["Thickness"] * (number_plates_flanges * plates["Length"] * plates["Width"] - math.pi * ((dfl+ec/2)**2 - ((ds + 2*ts)/2)**2))

            return scrap_material_flanges





