""" ECONOMIC MODEL """

import math

def cost_heat_exchanger_FOB(raw_material):
    cost_raw_material = 0
    for i in raw_material:
        cost_raw_material += raw_material["Cost"]-k_factor * kg_price * raw_material["Scrap"]

    cost_manufacturing = 0
   
