''' 
###################################################

            PROCESS OF PLASMA CUTING

###################################################
'''
import math

def calculate_cost_plasma_cutting(labor_cost_plasma_cutting, material_cost_plasma_cutting, utility_cost_plasma_cutting, depreciation_cost_plasma_cutting, starting_time_plasma_cutting, manipulation_time_plasma_cutting, spca, tpcs, operation_factor_plasma_cutting, ec, thickness_shell, thickness_flange, thickness_baffles, thickness_pass_partitions, thickness_removable_covers, thickness_heads, thickness_tubesheets, diameter_flange, diameter_shell, width_pass_partitions, length_pass_partitions, number_passes, diameter_removable_covers, diameter_shell, length_heads, number_baffles,  volume_tubesheets, volume_flange, volume_baffles, volume_pass_partitions, volume_removable_covers, volume_shell, volume_heads):
    
    if diameter_shell<=635:
        clearence = 1.5875
    else:
        clearence = 3.175
    #Table 3 for calculating STpc
    table_3 = [
            2 * math.pi * diameter_flange,
            4 * math.pi * diameter_flange,
            4 * math.pi * (diameter_shell + 2*thickness_shell),
            math.pi * number_baffles * (diameter_shell - 2*clearence),
            (2*width_pass_partitions + 2*length_pass_partitions)*(number_passes - 1),
            2 * math.pi * diameter_removable_covers
    Sty = 

