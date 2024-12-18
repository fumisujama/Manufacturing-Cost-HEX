##############################
#                            #
#   PROCESS OF DRILLING      #
#                            #
##############################
import math

def calculate_cost_drilling(labor_cost_drilling, material_cost_drilling, utility_cost_drilling, depreciation_cost_drilling, starting_time_drilling, manipulation_time_drilling, Stm, RPM, Fnd, STdo ,thickness_flange, thickness_baffles,thickness_removable_covers, thickness_tubesheets, number_tubes_per_pass, number_passes, number_baffles, number_tie_rods, volume_tubesheets, volume_flange, volume_baffles, volume_pass_partitions, volume_removable_covers, volume_shell, volume_heads):
    
    #Table 4 for calculating STd
    table_4 = [ 
            {"Drilling time": 2 * number_tubes_per_pass * number_passes * (Stm + (thickness_tubesheets / (RPM*Fnd)) + STdo),"Number of drilling passes": math.ceil(tube_outside_diameter/SDh) , "Manipulated volume": volume_tubesheets},
            {"Drilling time": 2 * number_bolts * (Stm + (thickness_tubesheets / (RPM*Fnd)) + STdo), "Number of drilling passes": math.ceil(diameter_bolts/SDh), "Manipulated volume": volume_tubesheets},
            {"Drilling time": number_tubes_per_pass * number_passes * (Stm + ((thickness_baffles * number_baffles) / (RPM*Fnd)) + STdo) , "Number of drilling passes": math.ceil(tubes_outside_diameter/SDh), "Manipulated volume": volume_baffles},
            {"Drilling time": number_tie_rods * (Stm + ((thickness_baffles * number_baffles)/ (RPM*Fnd)) + STdo), "Number of drilling passes": math.ceil(diameter_tie_rods/SDh), "Manipulated volume": volume_baffles},
            {"Drilling time": 4 * number_bolts * (Stm + (thickness_flange/ (RPM*Fnd)) + STdo), "Number of drilling passes": math.ceil(diameter_bolts/SDh), "Manipulated volume": volume_pass_partitions},
            {"Drilling time": 2 * number_bolts * (Stm + (thickness_removable_covers / (RPM*Fnd)) + STdo), "Number of drilling passes": math.ceil(diameter_bolts/SDh), "Manipulated volume": volume_removable_covers}
            ]



    for components in table_4:
        labor_cost = labor_cost_drilling * (
            (components["Drilling time"]*components["Number of drilling passes"] 
             ) 
            + starting_time_drilling
            + manipulation_time_drilling*components["Manipulated volume"]
            )
        material_cost = material_cost_drilling * (
            (components["Drilling time"]*components["Number of drilling passes"] 
             )
            )
        utility_cost = utility_cost_drilling * (
            (components["Drilling time"]*components["Number of drilling passes"] 
             )
            + manipulation_time_drilling*components["Manipulated volume"]
            )
        depreciation_cost = depreciation_cost_drilling * (
            (components["Drilling time"]*components["Number of drilling passes"] 
             )
            + manipulation_time_drilling*components["Manipulated volume"]
            )

    return labor_cost+material_cost+utility_cost+depreciation_cost



