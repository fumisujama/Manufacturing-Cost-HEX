'''
##################################
#                                #
#       PROCESS OF  WELDING      #
#                                #
##################################
'''
import math

def calculate_cost_welding(labor_cost_welding,
                                material_cost_welding, 
                                utility_cost_welding,
                                depreciation_cost_welding, 
                                starting_time_welding, 
                                manipulation_time_welding, 
                                density_welding_material, 
                                average_deposition_rate , 
                                operation_factor_welding, 
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
                                length_tubes,shell_side_nozzles_thickness,tubes_side_nozzles_thickness):
   #Look how to implement the amount of plates in this function, later we change it to be compatible with raw materials 
    #Consistency of data entered
    diameter_shell = float(diameter_shell.value)
    number_tubes_pass = float(number_tubes_pass.value)
    number_passes = float(number_passes.value)
    tubes_outside_diameter = float(tubes_outside_diameter.value) 
    number_baffles = float(number_baffles.value)
    length_shell = float(length_shell.value)
    volume_nozzles_flanges = 0 #change later
    labor_cost_welding = float(labor_cost_welding.value)
    material_cost_welding = float(material_cost_welding.value)
    utility_cost_welding = float(utility_cost_welding.value)
    depreciation_cost_welding = float(depreciation_cost_welding.value)
    starting_time_welding = float(starting_time_welding.value)
    manipulation_time_welding = float(manipulation_time_welding.value)

    density_welding_material = float(density_welding_material.value)/1000000000 #from kg/m3 to kg/mm3 
    average_deposition_rate = float(average_deposition_rate.value) 
    operation_factor_welding = float(operation_factor_welding.value)
    deposition_efficiency = float(deposition_efficiency.value) 
    thickness_root_pass_welding = float(thickness_root_pass_welding.value)



    #Table 7 for calculating Vrp 
    table_7 = [
            {"Volume of welding": (2 * shell_nozzles_inside_diameter * math.pi * (shell_side_nozzles_thickness-thickness_root_pass_welding)**2), "Manipulated volume": (volume_shell_side_nozzles + volume_shell)},
            {"Volume of welding": 2 * shell_nozzles_inside_diameter * math.pi * (shell_side_nozzles_thickness-thickness_root_pass_welding)**2, "Manipulated volume": volume_shell_side_nozzles + volume_nozzles_flanges/2}, #here, nozzles flanges are standard parts
            {"Volume of welding": 2 * diameter_shell * math.pi * (thickness_shell-thickness_root_pass_welding)**2, "Manipulated volume": volume_tubesheets + volume_shell},
            {"Volume of welding": 2 * tubes_nozzles_inside_diameter * math.pi *(tubes_side_nozzles_thickness-thickness_root_pass_welding)**2, "Manipulated volume": volume_tubes_side_nozzles + volume_nozzles_flanges/2}, #here is also the volume of the standard part
            {"Volume of welding": 2 * tubes_nozzles_inside_diameter * math.pi * (tubes_side_nozzles_thickness-thickness_root_pass_welding)**2 , "Manipulated volume": volume_tubes_side_nozzles + volume_heads},
            {"Volume of welding": 4 * diameter_shell * math.pi * (thickness_flange-thickness_root_pass_welding)**2, "Manipulated volume": volume_flange + volume_heads},
            {"Volume of welding": number_tubes_pass * number_passes * 2 * tubes_outside_diameter * math.pi * (thickness_tubes-thickness_root_pass_welding)**2, "Manipulated volume": volume_tubes + volume_tubesheets},
            {"Volume of welding": number_tie_rods * diameter_tie_rods * 2 * math.pi * (thickness_tubesheets-thickness_root_pass_welding)**2, "Manipulated volume": volume_tie_rods + volume_tubesheets},
            {"Volume of welding": number_baffles * number_tie_rods * diameter_tie_rods * 2 * math.pi * (thickness_baffles-thickness_root_pass_welding)**2, "Manipulated volume": volume_tie_rods + volume_baffles},
            {"Volume of welding": 2 * (number_passes -1) * length_pass_partitions * (thickness_pass_partitions-thickness_root_pass_welding)**2, "Manipulated volume": volume_pass_partitions+ volume_heads}
            ]



    if diameter_shell>635: 
        a = [
            {"Volume of welding": (number_plates_shell-1) * diameter_shell * math.pi * (thickness_shell-thickness_root_pass_welding)**2, "Manipulated volume": volume_shell},
            {"Volume of welding": (number_trunks_shell-1) * length_shell * (thickness_shell-thickness_root_pass_welding)**2, "Manipulated volume": volume_shell},
            {"Volume of welding": 2 * length_heads * (thickness_heads-thickness_root_pass_welding)**2, "Manipulated volume": volume_heads}
             ]
        for i in a:
            table_7.append(i)
            


    if length_tubes>508:   #lenght of tubes is bigger the 20'
        b = [{"Volume of welding": number_passes * number_tubes_pass * math.pi * (tubes_outside_diameter - 2 * thickness_tubes) * (thickness_tubes-thickness_root_pass_welding)**2, "Manipulated volume": volume_tubes}]
        for i in b:
            table_7.append(i)
    
    labor_cost = 0
    material_cost = 0
    utility_cost = 0
    depreciation_cost = 0


    for components in table_7:
        print(f"\n volume of welding: {components["Volume of welding"]}")
        Strp=density_welding_material/(deposition_efficiency * operation_factor_welding * average_deposition_rate)
        print(f"\n \nStrp is: {Strp}")
        print(f"\nand manipulated volume: {components["Manipulated volume"]}\n")
        labor_cost += (labor_cost_welding/60) * (Strp * components["Volume of welding"] + starting_time_welding*60 + (manipulation_time_welding*60 * components["Manipulated volume"]))
        print(f"\n \n Labor cost of welding: ${labor_cost}")

        material_cost += ((material_cost_welding/60) * components["Volume of welding"] * Strp)
       
        print(f"\n material cost of welding: ${material_cost}")

        utility_cost += (utility_cost_welding/60) * (components["Volume of welding"] * Strp + (manipulation_time_welding*60*components["Manipulated volume"]))
        
        print(f"\n utility cost of welding: ${utility_cost}")

        depreciation_cost += (depreciation_cost_welding/60) * (components["Volume of welding"] * Strp+ (manipulation_time_welding*60*components["Manipulated volume"])
           )

        print(f"\n depreciation cost of welding: ${depreciation_cost}")

    total_manufacturing_cost_welding = labor_cost+material_cost+utility_cost+depreciation_cost


    return total_manufacturing_cost_welding


"""
import math

def calculate_cost_welding(labor_cost_welding, 
                           material_cost_welding, 
                           utility_cost_welding, 
                           depreciation_cost_welding, 
                           starting_time_welding, 
                           manipulation_time_welding, 
                           density_welding_material, 
                           average_deposition_rate , 
                           operation_factor_welding, 
                           deposition_efficiency,
                           thickness_root_pass_welding,
                           thickness_shell, 
                           thickness_flange, 
                           thickness_baffles, 
                           thickness_pass_partitions, 
                           thickness_removable_covers, 
                           thickness_heads, 
                           thickness_tubesheets,
                           thickness_nozzles,
                           thickness_tubes,
                           number_plates_shell,
                           number_trunks_shell,
                           diameter_flange, 
                           diameter_shell, 
                           width_pass_partitions, 
                           length_pass_partitions,
                           number_passes, 
                           number_tubes_per_pass, 
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
                           volume_nozzles,
                           diameter_nozzles,
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
    number_tubes_per_pass = float(number_tubes_per_pass.value)
    number_passes = float(number_passes.value)
    tubes_outside_diameter = float(tubes_outside_diameter.value) 
    number_baffles = float(number_baffles.value)
    length_shell = float(length_shell.value)
    volume_nozzles_flanges = 0 #change later

    labor_cost_welding = float(labor_cost_welding.value)
    material_cost_welding = float(material_cost_welding.value)
    utility_cost_welding = float(utility_cost_welding.value)
    depreciation_cost_welding = float(depreciation_cost_welding.value)
    starting_time_welding = float(starting_time_welding.value)
    manipulation_time_welding = float(manipulation_time_welding.value)

    density_welding_material = float(density_welding_material.value)
    average_deposition_rate = float(average_deposition_rate.value) 
    operation_factor_welding = float(operation_factor_welding.value)
    deposition_efficiency = float(deposition_efficiency.value) 
    thickness_root_pass_welding = float(thickness_root_pass_welding.value)



    #Table 7 for calculating Vrp 
    table_7 = [ 
               {"Volume of welding": 2 * diameter_nozzles * math.pi * (thickness_nozzles - thickness_root_pass_welding)**2, "Manipulated volume": volume_nozzles/2 + volume_shell},
               {"Volume of welding": 2 * diameter_nozzles * math.pi * (thickness_nozzles - thickness_root_pass_welding)**2, "Manipulated volume": volume_nozzles/2 + volume_nozzles_flanges/2}, #here, nozzles flanges are standard parts
               {"Volume of welding": 2 * diameter_shell * math.pi * (thickness_shell - thickness_root_pass_welding)**2, "Manipulated volume": volume_tubesheets + volume_shell},
               {"Volume of welding": 2 * diameter_nozzles * math.pi * (thickness_nozzles - thickness_root_pass_welding)**2, "Manipulated volume": volume_nozzles/2 + volume_nozzles_flanges/2}, #here is also the volume of the standard part
            {"Volume of welding": 2 * diameter_nozzles * math.pi * (thickness_nozzles - thickness_root_pass_welding)**2 , "Manipulated volume": volume_nozzles/2 + volume_heads},
            {"Volume of welding": 4 * diameter_shell * math.pi * (thickness_flange - thickness_root_pass_welding)**2, "Manipulated volume": volume_flange + volume_heads},
            {"Volume of welding": number_tubes_per_pass * number_passes * 2 * tubes_outside_diameter * math.pi * (thickness_tubes - thickness_root_pass_welding)**2, "Manipulated volume": volume_tubes + volume_tubesheets},
               {"Volume of welding": number_tie_rods * diameter_tie_rods * 2 * math.pi * (thickness_tubesheets - thickness_root_pass_welding)**2, "Manipulated volume": volume_tie_rods + volume_tubesheets},
               {"Volume of welding": number_baffles * number_tie_rods * diameter_tie_rods * 2 * math.pi * (thickness_baffles - thickness_root_pass_welding)**2, "Manipulated volume": volume_tie_rods + volume_baffles},
               {"Volume of welding": 4 * (number_passes -1) * length_pass_partitions * 2 * (thickness_pass_partitions - thickness_root_pass_welding)**2, "Manipulated volume": volume_pass_partitions}
            ]


    if diameter_shell>635: 
        a = [
            {"Volume of welding":  (number_plates_shell-1) * diameter_shell * math.pi * (thickness_shell - thickness_root_pass_welding)**2, "Manipulated volume": volume_shell},
            {"Volume of welding": (number_trunks_shell-1) * length_shell * (thickness_shell - thickness_root_pass_welding)**2, "Manipulated volume": volume_shell},
            {"Volume of welding": 2 * length_heads * (thickness_heads - thickness_root_pass_welding)**2, "Manipulated volume": volume_heads}
             ]
        for i in a:
            table_7.append(i)

    if length_tubes>508:   #lenght of tubes is bigger the 20'
        b = [
                {"Volume of welding": number_passes * number_tubes_per_pass * math.pi * (tubes_outside_diameter - 2 * thickness_tubes) * (thickness_tubes - thickness_root_pass_welding)**2, "Manipulated volume": volume_tubes}
                ]
        for i in b:
            table_7.append(i)

    labor_cost = 0
    material_cost = 0
    utility_cost = 0
    depreciation_cost = 0

    for components in table_7:
        labor_cost += labor_cost_welding * ((components["Volume of welding"] * density_welding_material / (deposition_efficiency * operation_factor_welding * average_deposition_rate)) + starting_time_welding + manipulation_time_welding*components["Manipulated volume"])

        material_cost += material_cost_welding * ((components["Volume of welding"]* density_welding_material) / (deposition_efficiency * operation_factor_welding * average_deposition_rate))


        utility_cost += utility_cost_welding * ((components["Volume of welding"]* density_welding_material / (deposition_efficiency * operation_factor_welding * average_deposition_rate)) + manipulation_time_welding*components["Manipulated volume"])


        depreciation_cost += depreciation_cost_welding * ((components["Volume of welding"]* density_welding_material / (deposition_efficiency * operation_factor_welding * average_deposition_rate)) + manipulation_time_welding*components["Manipulated volume"])


    total_manufacturing_cost_welding = labor_cost+material_cost+utility_cost+depreciation_cost


    return total_manufacturing_cost_welding


"""
