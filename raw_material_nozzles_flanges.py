""" RAW MATERIALS FLANGES FOR NOZZLES
"""
#Probably will be removed in the future this module, replaced for a more robust selection of raw materials from vendors

def cost_raw_material_nozzles_flanges(flanges_nozzles_table,
                                 shell_nozzles_inside_diameter,
                                 tubes_nozzles_inside_diameter):
    cost_raw_material_nozzles_flanges = 0 
    for flanges in flanges_nozzles_table:

        if flanges["Inside diameter"]>=shell_nozzles_inside_diameter:
            number_flanges_shell = 2
            cost_raw_material_nozzles_flanges += number_flanges_shell * flanges["Price"]
            break
        else:
            if flanges["Price"] == 428.48:
                cost_raw_material_nozzles_flanges += 2 * 428.48 #just for a moment, it is the last price of the flanges nozzles table
            else:
                continue

    for flanges in flanges_nozzles_table:

        if flanges["Inside diameter"]>=tubes_nozzles_inside_diameter:
            number_flanges_tubes = 2
            cost_raw_material_nozzles_flanges += number_flanges_tubes * flanges["Price"]
            break
        else:
            if flanges["Price"] == 428.48:
                cost_raw_material_nozzles_flanges += 2 * 428.48 #just for a moment, it is the last price of the flanges nozzles table
            else:
                continue

    number_flanges = 4
    return cost_raw_material_nozzles_flanges, number_flanges

#Fix later, there is no flange that fits needs, maybe add more flanges for nozzles or change how diameter of nozzles is calculated?

