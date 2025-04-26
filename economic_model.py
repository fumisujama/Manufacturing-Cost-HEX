""" ECONOMIC MODEL """

import math

def cost_heat_exchanger_FOB(raw_material,
                            cost_plasma_cutting, 
                            cost_drilling, cost_lathe, 
                            cost_root_pass_welding, 
                            cost_welding, 
                            cost_blade_saw_cutting, 
                            cost_assembly, 
                            kg_price):
    kg_price = float(kg_price.value)
    cost_raw_material = 0
    for items in raw_material:
        print(items)
        cost_raw_material += items["Cost"]-float(items["K scrap factor"].value) * kg_price *items["Scrap"]

    cost_manufacturing = cost_plasma_cutting + cost_drilling + cost_lathe + cost_root_pass_welding + cost_welding + cost_blade_saw_cutting
    
    total_cost_heat_exchanger_FOB = cost_raw_material + cost_manufacturing + cost_assembly
    return total_cost_heat_exchanger_FOB



def cost_heat_exchanger_installed(raw_material, 
                                  cost_plasma_cutting, 
                                  cost_drilling, cost_lathe, 
                                  cost_root_pass_welding, 
                                  cost_welding, 
                                  cost_blade_saw_cutting, 
                                  kg_price, cost_assembly, 
                                  cost_shipping, 
                                  km, 
                                  cost_foundation, 
                                  Ds, 
                                  Ls, 
                                  Lh, 
                                  LCphLAP, 
                                  STt, 
                                  STh, 
                                  VHEX):

    cost_raw_material = 0
    for i in raw_material:
        cost_raw_material += raw_material["Cost"]-k_factor * kg_price * raw_material["Scrap"]

    cost_manufacturing = cost_plasma_cutting + cost_drilling + cost_lathe + cost_root_pass_welding + cost_welding + cost_blade_saw_cutting
    
    cost_lift_alignment_positioning = LCphLAP * (STt + STh*VHEX)

    total_cost_heat_exchanger_installed = cost_raw_material + cost_manufacturing + cost_assembly + cost_shipping*km + cost_foundation * 1.2 * Ds * (Ls + 2*Lh) + cost_lift_alignment_positioning

    return total_cost_heat_exchanger_installed 

