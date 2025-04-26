""" RAW MATERIAL FOR PASS PARTITIONS
"""



def cost_raw_material_pass_partitions(tpp, plates_table):
    for plates in plates_table:
        if plates["Thickness"]<tpp:
            continue
        else:
            number_plates_pass_partitions = 1
            cost_raw_material_pass_partitions = number_plates_pass_partitions * plates["Price"]

            return cost_raw_material_pass_partitions, number_plates_pass_partitions


def scrap_material_pass_partitions(tpp, wpp, lpp, number_passes, plates_table):
    density_steel = 7850/1000000000
    number_passes = float(number_passes.value)
    for plates in plates_table:
        if plates["Thickness"]<tpp:
            continue
        else:
            scrap_material_pass_partitions = density_steel * plates["Thickness"] * (plates["Width"] * plates["Length"] - (number_passes -1) * wpp * lpp)
            return scrap_material_pass_partitions
