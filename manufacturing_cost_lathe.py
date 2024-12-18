#########################################
#                                       #
#          PROCESS OF LATHE             #
#                                       #
#########################################

import math

def calculate_cost_lathe(labor_cost_lathe, material_cost_lathe, utility_cost_lathe, depreciation_cost_lathe, starting_time_lathe, manipulation_time_lathe,operation_factor_lathe, vcl, apl, fnl, diameter_flange, diameter_shell, thickness_flange, thickness_removable_covers, thickness_tubesheets, volume_tubesheets, volume_flange, volume_removable_covers):
    
    #Table 5 for calculating Vlw
    table_5 = [ 
            {"Removed volume": (((math.pi * (diameter_flange + apl)**2 /4) * (thickness_tubesheets + apl)) - (math.pi * diameter_flange**2 / 4) * tubesheets thickness))}, "Manipulated volume": volume_tubesheets},
            {"Removed volume": ((math.pi * (diameter_flange + apl)**2) / 4)
             * (thickness_flange + apl)
             - (math.pi / 4) * thickness_flange
             + ((math.pi / 4) * diameter_shell**2 * thickness_flange)
             - ((math.pi / 4) * (diameter_shell-apl)**2 * thickness_flange),  "Manipulated volume": volume_flange},
            {"Removed volume": ((((diameter_removable_covers + apl) / 2)**2
             * math.pi * (thickness_removable_covers + apl))
             - ((diameter_removable_covers / 2)**2) * math.pi * thickness_removable_covers), "Manipulated volume": volume_removable_covers}
           ]



    for components in table_5:
        labor_cost = labor_cost_lathe * (
            (components["Removed volume"] / (kl * vcl * apl * fnl)
             ) 
            + starting_time_lathe
            + manipulation_time_lathe*components["Manipulated volume"]
            )
        material_cost = material_cost_lathe * (
            (components["Removed volume"] / (kl * vcl * apl * fnl)
             )
            )
        utility_cost = utility_cost_lathe * (
            (components["Removed volume"] / (kl * vcl * apl * fnl)
             )
            + manipulation_time_lathe*components["Manipulated volume"]
            )
        depreciation_cost = depreciation_cost_lathe * (
            (components["Removed volume"] / (kl * vcl * apl * fnl)
             )
            + manipulation_time_lathe*components["Manipulated volume"]
            )

    return labor_cost+material_cost+utility_cost+depreciation_cost




