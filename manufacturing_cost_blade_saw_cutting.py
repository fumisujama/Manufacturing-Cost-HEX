#########################################
#                                       #
#     PROCESS OF BLADE SAW CUTING       #
#                                       #
#########################################
import math

def calculate_cost_blade_saw_cutting(labor_cost_blade_saw_cutting, 
                                     material_cost_blade_saw_cutting, 
                                     utility_cost_blade_saw_cutting, 
                                     depreciation_cost_blade_saw_cutting, 
                                     starting_time_blade_saw_cutting, 
                                     manipulation_time_blade_saw_cutting, 
                                     operation_factor_blade_saw_cutting, 
                                     shell_nozzles_inside_diameter,
                                     tubes_nozzles_inside_diameter,
                                     shell_side_nozzles_thickness,
                                     tubes_side_nozzles_thickness,
                                     outside_diameter_tubes, 
                                     thickness_tubes, 
                                     Crbs, 
                                     number_tubes_per_pass, 
                                     number_passes,
                                     volume_tubes,
                                     volume_shell_side_nozzles,
                                     volume_tubes_side_nozzles):
       #Consistency of data entered
    labor_cost_blade_saw_cutting = float(labor_cost_blade_saw_cutting.value)
    material_cost_blade_saw_cutting = float(material_cost_blade_saw_cutting.value)
    utility_cost_blade_saw_cutting = float(utility_cost_blade_saw_cutting.value)
    depreciation_cost_blade_saw_cutting = float(depreciation_cost_blade_saw_cutting.value)
    operation_factor_blade_saw_cutting = float(operation_factor_blade_saw_cutting.value)
    starting_time_blade_saw_cutting = float(starting_time_blade_saw_cutting.value)
    manipulation_time_blade_saw_cutting = float(manipulation_time_blade_saw_cutting.value) 
    Crbs = float(Crbs.value)
    number_tubes_per_pass = float(number_tubes_per_pass.value)
    number_passes = float(number_passes.value)
    outside_diameter_tubes = float(outside_diameter_tubes.value)

    #Table 8 for cutarea_bs
    table_8 = [ 
               {"Cut area": math.pi/2 * ((shell_nozzles_inside_diameter+2*shell_side_nozzles_thickness)**2 -shell_nozzles_inside_diameter**2) ,"Manipulated volume": volume_shell_side_nozzles},
            {"Cut area": math.pi/2 * ((tubes_nozzles_inside_diameter+2*tubes_side_nozzles_thickness)**2 -tubes_nozzles_inside_diameter**2) ,"Manipulated volume": volume_tubes_side_nozzles},
            {"Cut area": number_tubes_per_pass * number_passes * (math.pi/4) * (outside_diameter_tubes**2 - (outside_diameter_tubes - 2*thickness_tubes)**2), "Manipulated volume": volume_tubes}
            ]

    labor_cost = 0
    material_cost = 0
    utility_cost = 0
    depreciation_cost = 0

    for cutareas in table_8:
        STbsc = 1 / (operation_factor_blade_saw_cutting * Crbs)
        labor_cost += (labor_cost_blade_saw_cutting/60) * (cutareas["Cut area"] * STbsc   + starting_time_blade_saw_cutting*60 + manipulation_time_blade_saw_cutting*60*cutareas["Manipulated volume"])
        print(f"\n\nlabor cost of bsc: ${labor_cost}")
        print(f"\n manipulated volume: {cutareas["Manipulated volume"]}")


        material_cost += (material_cost_blade_saw_cutting/60) * (cutareas["Cut area"] * STbsc)



        print(f"\n material cost of bsc: ${material_cost}")
        utility_cost += (utility_cost_blade_saw_cutting/60) * (cutareas["Cut area"] * STbsc + manipulation_time_blade_saw_cutting*60*cutareas["Manipulated volume"])

        print(f"\n utility cost of bsc: ${utility_cost}")

        depreciation_cost += (depreciation_cost_blade_saw_cutting/60) * (cutareas["Cut area"] * STbsc + manipulation_time_blade_saw_cutting*60*cutareas["Manipulated volume"])

        print(f"\n depreciation cost of bsc: ${depreciation_cost}")


    return labor_cost+material_cost+utility_cost+depreciation_cost




