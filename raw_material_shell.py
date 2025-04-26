""" RAW MATERIAL CALCULATION FOR SHELL
"""
import math


def cost_raw_material_shell(ds, 
                       schedule40_table, 
                       ls, 
                       ts,
                       plates_table):
    ds=float(ds.value)
    ls=float(ls.value)
    if ds<=609.6:
        for tubes in schedule40_table:
            if (tubes["Outside diameter"] - 2*tubes["Wall thickness"])<ds:
                continue
            else:
                number_pipes_shell = math.ceil(ls/tubes["Length"])
                print(f"\n \n number_pipes_shell is:{number_pipes_shell}")
                print(f"\n price of tubes is: ${tubes["Price"]}")
                cost_raw_material_shell = number_pipes_shell * tubes["Price"]

                return cost_raw_material_shell,0,number_pipes_shell,0


    else:
        for plates in plates_table:
            if plates["Thickness"]>=ts:

                Ntrunks_option_1 = math.ceil(math.pi*ds/plates["Width"])
                Npr_option_1 = math.ceil(ls/plates["Length"])
                Ntrunks_option_2 = math.ceil(math.pi*ds/plates["Length"])
                Npr_option_2 = math.ceil(ls/plates["Width"])

                number_plates_shell = min(Ntrunks_option_1 * Npr_option_1,
                                          Ntrunks_option_2 * Npr_option_2)

                cost_raw_material_shell = number_plates_shell * plates["Price"] 
                if Ntrunks_option_1*Npr_option_1<=Ntrunks_option_2*Npr_option_2:

                    Ntrunks = Ntrunks_option_1
                else:
                    Ntrunks = Ntrunks_option_2

                print(f"\n \n number_plates_shell is:{number_plates_shell}")
                print(f"\n price of plates is: ${plates["Price"]} \n")
                return cost_raw_material_shell,number_plates_shell,0,Ntrunks
            else:
                continue

def scrap_material_shell(plates_table, schedule40_table, ds, ts, ls, number_plates_shell, number_pipes_shell):
    density_steel=7850/1000000000 #density steel in #kg/mm3
    ds=float(ds.value)
    ls=float(ls.value)
    if ds<=609.6:
        for tubes in schedule40_table:
            if (tubes["Outside diameter"] - 2*tubes["Wall thickness"])<=ds:
                continue
            else:
                scrap_material_shell = density_steel * number_pipes_shell * (math.pi/4) * (ds**2-(ds-2*ts)**2) * (tubes["Length"] - ls)

                return scrap_material_shell
    else:
        for plates in plates_table:
            if plates["Thickness"]>=ts:
                scrap_material_shell = density_steel * plates["Thickness"] * (number_plates_shell * plates["Length"] * plates["Width"] - math.pi * ds * ls)
                return scrap_material_shell
            else:
                continue


