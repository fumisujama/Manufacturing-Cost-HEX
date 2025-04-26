""" RAW MATERIAL FOR BAFFLES
"""
import math


def cost_raw_material_baffles(tb, Nb, ec, Bc, Db, plates_table):
    Nb=float(Nb.value)
    Bc=float(Bc.value)
    ec=float(ec.value)
    for plates in plates_table:
        if plates["Thickness"]<=tb:
            continue
        else:
            number_plates_baffles = math.ceil(
                    (Nb/2) * (Db + ec/2)
                    / (plates["Length"])
                    )
            cost_raw_material_baffles = number_plates_baffles * plates["Price"]
            return cost_raw_material_baffles, number_plates_baffles
           


def scrap_material_baffles(Db, Bc, Nb, tb, number_plates_baffles, plates_table):
    density_steel=7850
    Nb=float(Nb.value)
    Bc=float(Bc.value)
    for plates in plates_table:
        if plates["Thickness"]<=tb:
            continue
        else:
            scrap_material_baffles = density_steel * plates["Thickness"] * (plates["Length"] * plates["Width"] * number_plates_baffles - Nb * (
                (math.pi/4)*Db**2
                - (
                    ((Db**2)/4) * math.acos(1-Bc/50)
                    - (
                        Db/2 - Db*Bc/100
                        ) * (math.sqrt(Db**2 * Bc * (1/100 - Bc/5000)))
                    )
                )
                                                                            )
            return scrap_material_baffles


