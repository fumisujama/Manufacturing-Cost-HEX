""" RAW MATERIALS FOR TIE RODS
"""
import math


def cost_raw_material_tie_rods(Ntr, ltr, dtr, rods_table):
    for rods in rods_table:
        if rods["Outside diameter"]<dtr:
            continue
        else:
            Ntrd = math.floor(rods["Length"]/ltr)
            number_rods_tie_rods = math.ceil(Ntr/Ntrd)
            cost_raw_material_tie_rods = number_rods_tie_rods * rods["Price"]
            return cost_raw_material_tie_rods, number_rods_tie_rods


def scrap_material_tie_rods(number_rods_tie_rods, ltr, Ntr, dtr, rods_table):
    density_steel = 7850/1000000000
    for rods in rods_table:
        if rods["Outside diameter"]<dtr:
            continue
        else:
            scrap_material_tie_rods = density_steel * (math.pi/4) * dtr**2 * (number_rods_tie_rods * rods["Length"] - Ntr*ltr)
            return scrap_material_tie_rods


