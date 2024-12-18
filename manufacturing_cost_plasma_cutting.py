''' 
###################################################

            PROCESS OF PLASMA CUTING

###################################################
'''
import math

def calculate_cost_plasma_cutting(labor_cost_plasma_cutting, material_cost_plasma_cutting, utility_cost_plasma_cutting, depreciation_cost_plasma_cutting, starting_time_plasma_cutting, manipulation_time_plasma_cutting, spca, tpcs, operation_factor_plasma_cutting, ec, thickness_shell, thickness_flange, thickness_baffles, thickness_pass_partitions, thickness_removable_covers, thickness_heads, thickness_tubesheets, diameter_flange, diameter_shell, width_pass_partitions, length_pass_partitions,thickness_pass_partitions, number_passes, diameter_removable_covers, diameter_shell, diameter_heads, diameter_tubesheets, length_heads, number_baffles,  volume_tubesheets, volume_flange, volume_baffles, volume_pass_partitions, volume_removable_covers, volume_shell, volume_heads):
    
    if diameter_shell<=635:
        clearence = 1.5875
    else:
        clearence = 3.175
    #Table 3 for calculating STpc
    table_3 = [ 
            {"Cutpath length": 2 * math.pi * diameter_tubesheets,"Thickness of the part": thickness_tubesheets, "Manipulated volume": volume_tubesheets},
            {"Cutpath length": 4 * math.pi * diameter_flange, "Thickness of the part": thickness_flange, "Manipulated volume": volume_flange},
            {"Cutpath length": 4 * math.pi * (diameter_shell + 2*thickness_shell), "Thickness of the part": thickness_flange, "Manipulated volume": volume_flange},
            {"Cutpath length": math.pi * number_baffles * (diameter_shell - 2*clearence), "Thickness of the part": thickness_baffles, "Manipulated volume": volume_baffles},
            {"Cutpath length": (2*width_pass_partitions + 2*length_pass_partitions)*(number_passes - 1), "Thickness of the part": thickness_pass_partitions, "Manipulated volume": volume_pass_partitions},
            {"Cutpath length": 2 * math.pi * diameter_removable_covers, "Thickness of the part": thickness_removable_covers, "Manipulated volume": volume_removable_covers}
            ]



    if diameter_shell<=635: 
        a = [
            {"Cutpath length": 2 * math.pi * diameter_heads, "Thickness of the part": thickness_heads, "Manipulated volume": volume_heads},
            {"Cutpath length": 2 * math.pi * diameter_shell, "Thickness of the part": thickness_shell, "Manipulated volume": volume_shell}
             ]
        table_3.append(a)
    else:
        b = [
                {"Cutpath length": 4 * math.pi * diameter_heads+ 4*length_heads, "Thickness of the part": thickness_heads,  "Manipulated volume": volume_heads},
                {"Cutpath length": 2 * length_shell + 2 * math.pi * diameter_shell, "Thickness of the part": thickness_heads,  "Manipulated volume": volume_shell}
                ]
        table_3.append(b)


    for cutpaths in table_3:
        labor_cost = labor_cost_plasma_cutting * (
            (cutpaths["Cutpath length"]*cutpaths["Thickness of the part"] 
            / (spca * tpcs * operation_factor_plasma_cutting) ) 
            + starting_time_plasma_cutting
            + manipulation_time_plasma_cutting*cutpaths["Manipulated volume"]
            )
        material_cost = material_cost_plasma_cutting * (
            (cutpaths["Cutpath length"]*cutpaths["Thickness of the part"] 
            / (spca * tpcs * operation_factor_plasma_cutting) )
            )
        utility_cost = utility_cost_plasma_cutting * (
            (cutpaths["Cutpath length"]*cutpaths["Thickness of the part"] 
            / (spca * tpcs * operation_factor_plasma_cutting) )
            + manipulation_time_plasma_cutting*cutpaths["Manipulated volume"]
            )
        depreciation_cost = depreciation_cost_plasma_cutting * (
            (cutpaths["Cutpath length"]*cutpaths["Thickness of the part"] 
            / (spca * tpcs * operation_factor_plasma_cutting) )
            + manipulation_time_plasma_cutting*cutpaths["Manipulated volume"]
            )

    return labor_cost+material_cost+utility_cost+depreciation_cost


#continue by adding thickness to every part
