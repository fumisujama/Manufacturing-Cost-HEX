""" RAW MATERIAL FOR TUBES
"""
import math


def cost_raw_material_tubes(lt, dte, Ntp, Np, schedule40_table):
    dte= float(dte.value)
    Ntp = float(Ntp.value)
    Np = float(Np.value)
    for tubes in schedule40_table:
        if tubes["Outside diameter"]>=dte:
            if lt<=508:
                Nt_tubes = math.floor(tubes["Length"]/lt)
                Ntt = (Ntp * Np) / Nt_tubes
                cost_raw_material_tubes = Ntt * tubes["Price"]
                print(f"\n Number of tubes is: {Ntt}")
                print(f"\n Price of tubes is : ${tubes["Price"]} \n")

                return cost_raw_material_tubes,Ntt

            else:
                Nt_tubes = math.floor(tubes["Length"]/(lt-508))
                Ntt = Ntp * Np + ((Ntp * Np) / Nt_tubes)
                cost_raw_material_tubes = Ntt * tubes["Price"]
                print(f"\n Number of tubes is: {Ntt}")
                print(f"\n Price of tubes is : ${tubes["Price"]} \n")
                return cost_raw_material_tubes,Ntt
        else:
            continue


def scrap_material_tubes(dte, schedule40_table, Ntt, Ntp, Np, lt):
    density_steel = 7850/1000000000
    dte= float(dte.value)
    Ntp = float(Ntp.value)
    Np = float(Np.value)
    for tubes in schedule40_table:
        if tubes["Outside diameter"]>=dte:
            scrap_material_tubes = density_steel * (math.pi/4) * (dte**2 - (dte - 2 * tubes["Wall thickness"])**2) * (Ntt * tubes["Length"] - Ntp * Np * lt)
            return scrap_material_tubes

        else:
            continue


