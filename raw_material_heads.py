""" RAW MATERIAL FOR HEADS
"""
import math

def cost_raw_material_heads(dh,th, lh, schedule40_table, plates_table):
    if dh<609.6:
        for tubes in schedule40_table:
            if tubes["Outside diameter"]>=dh:
                number_pipes_heads = 1
                cost_raw_material_heads = number_pipes_heads * tubes["Price"]
                print(f"cost of raw material heads is {cost_raw_material_heads}")
                return cost_raw_material_heads,number_pipes_heads,0
            else:
                continue
    else:
        for plates in plates_table:
            if plates["Thickness"]>=th:
                number_plates_heads = 1
                cost_raw_material_heads = number_plates_heads * plates["Price"]
                print(f"cost of raw material heads is {cost_raw_material_heads}")
                return cost_raw_material_heads,0,number_plates_heads
            else:
                continue

def scrap_material_heads(dh, th, lh, schedule40_table, plates_table):
    density_steel=7850/1000000000
    if dh<609.6:
        for tubes in schedule40_table:
            if tubes["Outside diameter"]>=dh:
                scrap_material_heads = density_steel * (math.pi/4) * (dh**2 - (dh-2*th)**2) * (tubes["Length"] - 2*lh)
                return scrap_material_heads
            else:
                continue
    else:
        for plates in plates_table:
            if plates["Thickness"]>=th:
                scrap_material_heads = density_steel * (plates["Length"] * plates["Width"] * plates["Thickness"] - (math.pi/4) * (dh**2 - (dh - 2*th)**2) * 2 * lh)
                return scrap_material_heads

            else:
                continue

    
    

