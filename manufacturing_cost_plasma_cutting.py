''' 
###################################################

            PROCESS OF PLASMA CUTING

###################################################
'''
import math

def calculate_cost_plasma_cutting(labor_cost_plasma_cutting, 
                                  material_cost_plasma_cutting, 
                                  utility_cost_plasma_cutting, 
                                  depreciation_cost_plasma_cutting, 
                                  starting_time_plasma_cutting, 
                                  manipulation_time_plasma_cutting, 
                                  spca, 
                                  tpcs, 
                                  operation_factor_plasma_cutting, 
                                  ec, 
                                  thickness_shell, 
                                  thickness_flange, 
                                  thickness_baffles, 
                                  thickness_pass_partitions, 
                                  thickness_removable_covers, 
                                  thickness_heads, 
                                  thickness_tubesheets, 
                                  diameter_flange, 
                                  diameter_shell, 
                                  width_pass_partitions, 
                                  length_pass_partitions, 
                                  number_passes, 
                                  diameter_removable_covers, 
                                  diameter_heads, 
                                  diameter_tubesheets, 
                                  length_heads, 
                                  number_baffles,  
                                  volume_tubesheets, 
                                  volume_flange, 
                                  volume_baffles, 
                                  volume_pass_partitions, 
                                  volume_removable_covers, 
                                  volume_shell, 
                                  volume_heads,
                                  length_shell):


    #Consistency of data entered
    labor_cost_plasma_cutting = float(labor_cost_plasma_cutting.value)
    material_cost_plasma_cutting = float(material_cost_plasma_cutting.value)
    utility_cost_plasma_cutting = float(utility_cost_plasma_cutting.value)
    depreciation_cost_plasma_cutting = float(depreciation_cost_plasma_cutting.value)
    starting_time_plasma_cutting = float(starting_time_plasma_cutting.value)
    manipulation_time_plasma_cutting = float(manipulation_time_plasma_cutting.value)
    spca = float(spca.value)
    tpcs = float(tpcs.value)
    operation_factor_plasma_cutting = float(operation_factor_plasma_cutting.value)
    diameter_shell = float(diameter_shell.value)
    number_passes = float(number_passes.value)
    number_baffles = float(number_baffles.value)
    length_shell = float(length_shell.value)

    
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
        for i in a:
            table_3.append(i)

    else:
        b = [
                {"Cutpath length": 4 * math.pi * diameter_heads+ 4*length_heads, "Thickness of the part": thickness_heads,  "Manipulated volume": volume_heads},
                {"Cutpath length": 2 * length_shell + 2 * math.pi * diameter_shell, "Thickness of the part": thickness_heads,  "Manipulated volume": volume_shell}
                ]
        for i in b:
            table_3.append(i)

    labor_cost=0
    material_cost=0
    utility_cost=0
    depreciation_cost=0

    for cutpaths in table_3:
        labor_cost += (labor_cost_plasma_cutting/60) * (
            (cutpaths["Cutpath length"]*cutpaths["Thickness of the part"]) 
            / (spca * tpcs * operation_factor_plasma_cutting)  
            + (starting_time_plasma_cutting*60)
            + (manipulation_time_plasma_cutting*60)*cutpaths["Manipulated volume"])

        print(f"\n Labor cost PC: {labor_cost}")
        material_cost += (material_cost_plasma_cutting/60) * (
            (cutpaths["Cutpath length"]*cutpaths["Thickness of the part"] 
            / (spca * tpcs * operation_factor_plasma_cutting) )
            )


        utility_cost += (utility_cost_plasma_cutting/60) * (
            (cutpaths["Cutpath length"]*cutpaths["Thickness of the part"] 
            / (spca * tpcs * operation_factor_plasma_cutting) )
            + (manipulation_time_plasma_cutting*60)*cutpaths["Manipulated volume"]
            )


        depreciation_cost += (depreciation_cost_plasma_cutting/60) * (
            (cutpaths["Cutpath length"]*cutpaths["Thickness of the part"] 
            / (spca * tpcs * operation_factor_plasma_cutting) )
            + (manipulation_time_plasma_cutting*60)*cutpaths["Manipulated volume"]
            )


    return labor_cost+material_cost+utility_cost+depreciation_cost


