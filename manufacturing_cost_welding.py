'''
##################################
#                                #
#       PROCESS OF  WELDING      #
#                                #
##################################
'''

import math

def calculate_cost_welding(labor_cost_welding, material_cost_welding, utility_cost_welding, depreciation_cost_welding, starting_time_welding, manipulation_time_welding, density_root_pass_welding_material, average_deposition_rate , operation_factor_welding, deposition_efficiency,  thickness_shell, thickness_flange, thickness_baffles, thickness_pass_partitions, thickness_removable_covers, thickness_heads, thickness_tubesheets, number_plates_shell, diameter_flange, diameter_shell, width_pass_partitions, length_pass_partitions,thickness_pass_partitions, number_passes, number_tubes_pass, diameter_removable_covers, diameter_shell, diameter_heads, diameter_tubesheets, length_heads, number_baffles, number_trunks_shell, volume_tubesheets, volume_flange, volume_baffles, volume_pass_partitions, volume_removable_covers, volume_shell, volume_heads):
   #Look how to implement the amount of plates in this function, later we change it to be compatible with raw materials 

    #Table 7 for calculating Vrp 
    table_7 = [ 
               {"Volume of welding": 2 * diamenter_nozzles * math.pi * (thickness_nozzles - thickness_welding)**2, "Manipulated volume": volume_nozzles/2 + volume_shell},
               {"Volume of welding": 2 * diamenter_nozzles * math.pi * (thickness_nozzles - thickness_welding)**2, "Manipulated volume": volume_nozzles/2 + volume_nozzles_flanges/2}, #here, nozzles flanges are standard parts
               {"Volume of welding": 2 * diameter_shell * math.pi * (thickness_shell - thickness_welding)**2, "Manipulated volume": volume_tubesshets + volume_shell},
               {"Volume of welding": 2 * diamenter_nozzles * math.pi * (thickness_nozzles - thickness_welding)**2, "Manipulated volume": volume_nozzles/2 + volume_nozzles_flanges/2}, #here is also the volume of the standard part
            {"Volume of welding": 2 * diameter_nozzles * math.pi * (thickness_nozzles - thickness_welding)**2 , "Manipulated volume": volume_nozzles/2 + volume_heads},
            {"Volume of welding": 4 * diameter_shell * math.pi * (thickness_flange - thickness_welding)**2, "Manipulated volume": volume_flange + volume_heads},
            {"Volume of welding": number_tubes_per_pass * number_passes * 2 * tube_outside_diameter * math.pi * (thickness_tubes - thickenss_welding)**2, "Manipulated volume": volume_tubes + volume_tubesheets},
               {"Volume of welding": number_tie_rods * diameter_tie_rods * 2 * math.pi * (thickness_tubesheets - thickness_welding)**2, "Manipulated volume": volume_tie_rods + volume_tubesheets},
               {"Volume of welding": number_baffles * number_tie_rods * diameter_tie_rods * 2 * math.pi * (thickness_baffles - thickness_welding)**2, "Manipulated volume": volume_tie_rods + volume_baffles},
               {"Volume of welding": 4 * (number_passes -1) * length_pass_partitions * 2 * (thickness_pass_partitions - thickness_welding)**2, "Manipulated volume": volume_pass_paritions}
            ]


    if diameter_shell>635: 
        a = [
            {"Volume of welding":  (number_plates_shell-1) * diameter_shell * math.pi * (thickness_shell - thickness_welding)**2, "Manipulated volume": volume_shell},
            {"Volume of welding": (number_trunks_shell-1) * length_shell * (thickness_shell - thickness_welding)**2, "Manipulated volume": volume_shell},
            {"Volume of welding": 2 * length_heads * (thickness_heads - thickness_welding)**2, "Manipulated volume": volume_heads}
             ]
        table_7.append(a)

    if length_tubes>508:   #lenght of tubes is bigger the 20'
        b = [
                {"Volume of welding": number_passes * number_tubes_pass * math.pi * (tubes_outside_diameter - 2 * thickness_tubes) * (thickness_tubes - thickness_welding)**2, "Manipulated volume": volume_tubes}
                ]
        table_7.append(b)



    for components in table_7:
        labor_cost = labor_cost_welding * (
                (components["Volume of welding"] * density_welding_material
                  / (deposition_efficiency * operation_factor_welding * average_deposition_rate))
            + starting_time_welding
            + manipulation_time_welding*components["Manipulated volume"]
            )
        material_cost = material_cost_welding * (
            (components["Volume of welding"]* density_welding_material
                  / (deposition_efficiency * operation_factor_welding * average_deposition_rate)) 
            ))
        utility_cost = utility_cost_welding * (
            (components["Volume of welding"]* density_welding_material
                  / (deposition_efficiency * operation_factor_welding * average_deposition_rate)) 
            + manipulation_time_welding*components["Manipulated volume"]
            )
        depreciation_cost = depreciation_cost_welding * (
            (components["Volume of welding"]* density_welding_material
                  / (deposition_efficiency * operation_factor_welding * average_deposition_rate)) 
            + manipulation_time_welding*components["Manipulated volume"]
            )
    total_manufacturing_cost_welding = labor_cost+material_cost+utility_cost+depreciation_cost
    return total_manufacturing_cost_welding



