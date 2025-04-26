###################################################
#                                                 #
#          PROCESS OF ROOT PASS WELDING           #
#                                                 #
###################################################
import math

def calculate_cost_root_pass_welding(labor_cost_root_pass_welding,
                                material_cost_root_pass_welding, 
                                utility_cost_root_pass_welding,
                                depreciation_cost_root_pass_welding, 
                                starting_time_root_pass_welding, 
                                manipulation_time_root_pass_welding, 
                                density_root_pass_welding_material, 
                                average_deposition_rate , 
                                operation_factor_root_pass_welding, 
                                deposition_efficiency,
                                thickness_root_pass_welding,
                                thickness_shell, 
                                thickness_flange, 
                                thickness_baffles, 
                                thickness_pass_partitions, 
                                thickness_removable_covers, 
                                thickness_heads, 
                                thickness_tubesheets, 
                                number_plates_shell, 
                                number_trunks_shell,
                                diameter_flange, 
                                diameter_shell, 
                                width_pass_partitions, 
                                length_pass_partitions,
                                number_passes, 
                                number_tubes_pass, 
                                thickness_tubes, 
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
                                volume_shell_side_nozzles,
                                volume_tubes_side_nozzles,
                                shell_nozzles_inside_diameter,
                                     tubes_nozzles_inside_diameter,
                                tubes_outside_diameter,
                                volume_tubes,
                                number_tie_rods,
                                diameter_tie_rods,
                                volume_tie_rods,
                                length_shell,
                                length_tubes):
   #Look how to implement the amount of plates in this function, later we change it to be compatible with raw materials 
    #Consistency of data entered
    diameter_shell = float(diameter_shell.value)
    number_tubes_pass = float(number_tubes_pass.value)
    number_passes = float(number_passes.value)
    tubes_outside_diameter = float(tubes_outside_diameter.value) 
    number_baffles = float(number_baffles.value)
    length_shell = float(length_shell.value)
    volume_nozzles_flanges = 0 #change later
    labor_cost_root_pass_welding = float(labor_cost_root_pass_welding.value)
    material_cost_root_pass_welding = float(material_cost_root_pass_welding.value)
    utility_cost_root_pass_welding = float(utility_cost_root_pass_welding.value)
    depreciation_cost_root_pass_welding = float(depreciation_cost_root_pass_welding.value)
    starting_time_root_pass_welding = float(starting_time_root_pass_welding.value)
    manipulation_time_root_pass_welding = float(manipulation_time_root_pass_welding.value)

    density_root_pass_welding_material = float(density_root_pass_welding_material.value)/1000000000 #from kg/m3 to kg/mm3 
    average_deposition_rate = float(average_deposition_rate.value) 
    operation_factor_root_pass_welding = float(operation_factor_root_pass_welding.value)
    deposition_efficiency = float(deposition_efficiency.value) 
    thickness_root_pass_welding = float(thickness_root_pass_welding.value)



    #Table 6 for calculating Vrp 
    table_6 = [
            {"Volume of root welding": (2 * shell_nozzles_inside_diameter * math.pi * thickness_root_pass_welding**2), "Manipulated volume": (volume_shell_side_nozzles + volume_shell)},
            {"Volume of root welding": 2 * shell_nozzles_inside_diameter * math.pi * thickness_root_pass_welding**2, "Manipulated volume": volume_shell_side_nozzles + volume_nozzles_flanges/2}, #here, nozzles flanges are standard parts
            {"Volume of root welding": 2 * diameter_shell * math.pi * thickness_root_pass_welding**2, "Manipulated volume": volume_tubesheets + volume_shell},
            {"Volume of root welding": 2 * tubes_nozzles_inside_diameter * math.pi * thickness_root_pass_welding**2, "Manipulated volume": volume_tubes_side_nozzles + volume_nozzles_flanges/2}, #here is also the volume of the standard part
            {"Volume of root welding": 2 * tubes_nozzles_inside_diameter * math.pi * thickness_root_pass_welding**2 , "Manipulated volume": volume_tubes_side_nozzles + volume_heads},
            {"Volume of root welding": 4 * diameter_shell * math.pi * thickness_root_pass_welding**2, "Manipulated volume": volume_flange + volume_heads},
            {"Volume of root welding": number_tubes_pass * number_passes * 2 * tubes_outside_diameter * math.pi * thickness_root_pass_welding**2, "Manipulated volume": volume_tubes + volume_tubesheets},
            {"Volume of root welding": number_tie_rods * diameter_tie_rods * 2 * math.pi * thickness_root_pass_welding**2, "Manipulated volume": volume_tie_rods + volume_tubesheets},
            {"Volume of root welding": number_baffles * number_tie_rods * diameter_tie_rods * 2 * math.pi * thickness_root_pass_welding**2, "Manipulated volume": volume_tie_rods + volume_baffles},
            {"Volume of root welding": 2 * (number_passes -1) * length_pass_partitions * thickness_root_pass_welding**2, "Manipulated volume": volume_pass_partitions+ volume_heads}
            ]



    if diameter_shell>635: 
        a = [
            {"Volume of root welding": (number_plates_shell-1) * diameter_shell * math.pi * thickness_root_pass_welding**2, "Manipulated volume": volume_shell},
            {"Volume of root welding": (number_trunks_shell-1) * length_shell * thickness_root_pass_welding**2, "Manipulated volume": volume_shell},
            {"Volume of root welding": 2 * length_heads * thickness_root_pass_welding**2, "Manipulated volume": volume_heads}
             ]
        for i in a:
            table_6.append(i)
            


    if length_tubes>508:   #lenght of tubes is bigger the 20'
        b = [{"Volume of root welding": number_passes * number_tubes_pass * math.pi * (tubes_outside_diameter - 2 * thickness_tubes) * thickness_root_pass_welding**2, "Manipulated volume": volume_tubes}]
        for i in b:
            table_6.append(i)
    
    labor_cost = 0
    material_cost = 0
    utility_cost = 0
    depreciation_cost = 0


    for components in table_6:
        print(f"\n volume of rootwelding: {components["Volume of root welding"]}")
        Strp=density_root_pass_welding_material/(deposition_efficiency * operation_factor_root_pass_welding * average_deposition_rate)
        print(f"\n \nStrp is: {Strp}")
        print(f"\nand manipulated volume: {components["Manipulated volume"]}\n")
        labor_cost += (labor_cost_root_pass_welding/60) * (Strp * components["Volume of root welding"] + starting_time_root_pass_welding*60 + (manipulation_time_root_pass_welding*60 * components["Manipulated volume"]))
        print(f"\n \n Labor cost of root_pass_welding: ${labor_cost}")

        material_cost += ((material_cost_root_pass_welding/60) * components["Volume of root welding"] * Strp)
       
        print(f"\n material cost of root_pass_welding: ${material_cost}")

        utility_cost += (utility_cost_root_pass_welding/60) * (components["Volume of root welding"] * Strp + (manipulation_time_root_pass_welding*60*components["Manipulated volume"]))
        
        print(f"\n utility cost of root_pass_welding: ${utility_cost}")

        depreciation_cost += (depreciation_cost_root_pass_welding/60) * (components["Volume of root welding"] * Strp+ (manipulation_time_root_pass_welding*60*components["Manipulated volume"])
           )

        print(f"\n depreciation cost of root_pass_welding: ${depreciation_cost}")

    total_manufacturing_cost_root_pass_welding = labor_cost+material_cost+utility_cost+depreciation_cost


    return total_manufacturing_cost_root_pass_welding


#continue calculator the total cost of root welding the las for loop
