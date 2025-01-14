""" RAW MATERIAL FOR PASS PARTITIONS
"""



def raw_material_pass_partitions(tpp, plates_table):
    for plates in plates_table:
        if plates["Thickness"]<tpp:
            continue
        else:
            number_plates_pass_partitions = 1

    return number_plates_pass_partitions


def scrap_material_pass_partitions(tpp, wpp, lpp, density_steel, number_passes, plates_table):
    for plates in plates_table:
        if plates["Thickness"]<tpp:
            continue
        else:
            scrap_material_pass_partitions = density_steel * plates["Thickness"] * (plates["Width"] * plates["Length"] - (number_passes -1) * wpp * lpp)

    return scrap_material_pass_partitions
