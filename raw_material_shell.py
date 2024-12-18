""" RAW MATERIAL CALCULATION FOR SHELL
"""
import math


def raw_material_shell(ds, schedule40_table, ls, ts):
    if ds<=609.6:
        for tubes in schedule40_table:
            if (tubes["Outside diameter"] - 2*tubes["Wall thickness"])<=ds:
                continue
            else:
                number_pipes_shell = math.ceil(ls/tubes["Length"])
                return number_pipes_shell
    else:
        for plates in plates_table:
            if plates["Thickness"]==ts:
                Ntrunks_option_1 = math.ceil(math.pi*ds/plates["Width"])
                Npr_option_1 = math.ceil(ls/plates["Length"])
                Ntrunks_option_2 = math.ceil(math.pi*ds/plates["Length"])
                Npr_option_2 = math.ceil(ls/plates["Width"])

                number_plates_shell = min(Ntrunks_option_1 * Npr_option_1,
                                          Ntrunks_option_2 * Npr_option_2)

                return number_plates_shell
            else:
                continue

def scrap_material_shell(ds, ts, ls, number_plates_shell, number_pipes_shell, density_steel):
    if ds<=609.6:
        for tubes in schedule40_table:
            if (tubes["Outside diameter"] - 2*tubes["Wall thickness"])<=ds:
                continue
            else:
                scrap_material_shell = density_steel * number_pipes_shell * (math.pi/4) * (ds**2-(ds-2*ts)**2) * (tubes["Length"] - ls)

                return scrap_material_shell
    else:
        for plates in plates_table:
            if plates["Thickness"]==ts:
                scrap_material_shell = density_steel * plates["Thickness"] * (number_plates_shell * plates["Length"] * plates["Width"] - math.pi * ds * ls)

                return scrap_material_shell


