""" RAW MATERIAL CALCULATION FOR TUBESHEETS
"""
import math


def cost_raw_material_tubesheets(tts, 
                                 diameter_tubesheets, 
                                 plates_table,
                                 ec):
    ec=float(ec.value)
    for plates in plates_table:
        if plates["Thickness"]<tts:
            continue
        else:
            number_plates_tubesheets = math.ceil(
                    (2 * diameter_tubesheets + 3 * ec)
                    / (plates["Length"])
                )
            cost_raw_material_tubesheets = number_plates_tubesheets * plates["Price"]
            print(f"\n Number of plates for tubesheets is: {number_plates_tubesheets}")
            print(f"\n Plates price is: ${plates["Price"]}")
            return cost_raw_material_tubesheets,number_plates_tubesheets




def scrap_material_tubesheets(plates_table,tubesheets_thickness, diameter_tubesheets, number_plates_tubesheets):
    density_steel = 7850/1000000000
    for plates in plates_table:
        if plates["Thickness"]>=tubesheets_thickness:
            scrap_material_tubesheets = density_steel * plates["Thickness"] * (number_plates_tubesheets * plates["Length"] * plates["Width"] - (math.pi/2) * diameter_tubesheets**2)
            return scrap_material_tubesheets

        else:
            continue

