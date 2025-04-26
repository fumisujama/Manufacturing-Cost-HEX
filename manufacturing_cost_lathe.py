#########################################
#                                       #
#          PROCESS OF LATHE             #
#                                       #
#########################################

import math

def calculate_cost_lathe(labor_cost_lathe,
                         material_cost_lathe,
                         utility_cost_lathe,
                         depreciation_cost_lathe,
                         starting_time_lathe,
                         manipulation_time_lathe,
                         operation_factor_lathe,
                         vcl,
                         apl, 
                         fnl, 
                         diameter_flange, 
                         diameter_shell, 
                         diameter_tubesheets,
                         thickness_flange, 
                         thickness_removable_covers, 
                         thickness_tubesheets, 
                         volume_tubesheets, 
                         volume_flange,
                         volume_removable_covers,
                         diameter_removable_covers,
                         ts):

       #Consistency of data entered
    labor_cost_lathe = float(labor_cost_lathe.value)
    material_cost_lathe = float(material_cost_lathe.value)
    utility_cost_lathe = float(utility_cost_lathe.value)
    depreciation_cost_lathe = float(depreciation_cost_lathe.value)
    starting_time_lathe = float(starting_time_lathe.value)
    manipulation_time_lathe = float(manipulation_time_lathe.value) 
    kl= float(operation_factor_lathe.value)
    vcl = float(vcl.value)
    apl = float(apl.value)
    fnl = float(fnl.value)
    diameter_shell = float(diameter_shell.value)


    first_removed_volume = ((math.pi/4) * ((diameter_flange + apl)**2)) * (thickness_tubesheets + apl) - (math.pi * (diameter_flange**2) / 4) * thickness_tubesheets

    second_removed_volume = (math.pi * ((diameter_flange + apl)**2) / 4) * (thickness_flange + apl) - (math.pi/4)* (diameter_flange**2) * thickness_flange+ (math.pi/4)* thickness_flange * ((diameter_shell+2*ts)**2) - (math.pi/4)* thickness_flange * ((diameter_shell+2*ts-apl)**2)


    third_removed_volume = ((((diameter_removable_covers + apl) / 2)**2) * math.pi * (thickness_removable_covers + apl)) - ((diameter_removable_covers / 2)**2) * math.pi * thickness_removable_covers


    #Table 5 for calculating Vlw
    table_5 = [
            {"Removed volume": first_removed_volume,
             "Manipulated volume": volume_tubesheets},

            {"Removed volume": second_removed_volume,
             "Manipulated volume": volume_flange},

            {"Removed volume": third_removed_volume,
             "Manipulated volume": volume_removable_covers}
            ]

    labor_cost=0
    material_cost=0
    utility_cost=0
    depreciation_cost=0


    for components in table_5:
        labor_cost += (labor_cost_lathe/60) * (
            (components["Removed volume"] / (kl * vcl * apl * fnl)
             ) 
            + (starting_time_lathe*60)
            + (manipulation_time_lathe*60)*components["Manipulated volume"]
            )
        print(f"\n\nLabor cost lathe: ${labor_cost}")
        material_cost += (material_cost_lathe/60) * (
            (components["Removed volume"] / (kl * vcl * apl * fnl)
             )
            )
        print(f"\n material cost lathe: ${material_cost}")
        utility_cost += (utility_cost_lathe/60) * (
            (components["Removed volume"] / (kl * vcl * apl * fnl)
             )
            + (manipulation_time_lathe*60)*components["Manipulated volume"]
            )
        print(f"\n utility cost lathe: ${utility_cost}")
        depreciation_cost += (depreciation_cost_lathe/60) * (
            (components["Removed volume"] / (kl * vcl * apl * fnl)
             )
            + (manipulation_time_lathe*60)*components["Manipulated volume"]
            )
        print(f"\n depreciation cost lathe: ${depreciation_cost}")

    return labor_cost+material_cost+utility_cost+depreciation_cost




