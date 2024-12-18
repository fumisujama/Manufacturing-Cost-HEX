#########################################
#                                       #
#     PROCESS OF BLADE SAW CUTING       #
#                                       #
#########################################
import math

def calculate_cost_blade_saw_cutting(labor_cost_blade_saw_cutting, material_cost_blade_saw_cutting, utility_cost_blade_saw_cutting, depreciation_cost_blade_saw_cutting, starting_time_blade_saw_cutting, manipulation_time_blade_saw_cutting, operation_factor_blade_saw_cutting, diameter_nozzles, thickness_nozzles, outside_diameter_tubes, thickness_tubes, Crbs, number_tubes_per_pass, number_passes,volume_tubes):
    
    #Table 8 for cutarea_bs
    table_8 = [ 
               {"Cut area": math.pi/2 * (diameter_nozzles**2 - (diameter_nozzles - 2*thickness_nozzles)**2) ,"Manipulated volume": volume_nozzles/2},
            {"Cut area": math.pi/2 * (diameter_nozzles**2 - (diameter_nozzles - 2*thickness_nozzles)**2) ,"Manipulated volume": volume_nozzles/2},
            {"Cut area": number_tubes_per_pass * number_passes * (math.pi/4) * (outside_diameter_tubes**2 - (outside_diameter_tubes - 2*thickness_tubes)**2)  "Manipulated volume": volume_tubes}
            ]



    for cutareas in table_8:
        labor_cost = labor_cost_blade_saw_cutting * (
            (cutareas["Cut area"] / (operation_factor_blade_saw_cutting * Crbs) 
             ) 
            + starting_time_blade_saw_cutting
            + manipulation_time_blade_saw_cutting*cutareas["Manipulated volume"]
            )
        material_cost = material_cost_blade_saw_cutting * (
            (cutareas["Cut area"] / (operation_factor_blade_saw_cutting * Crbs)
             )
            )
        utility_cost = utility_cost_blade_saw_cutting * (
            (cutareas["Cut area"] / (operation_factor_blade_saw_cutting * Crbs)
             )
            + manipulation_time_blade_saw_cutting*cutareas["Manipulated volume"]
            )
        depreciation_cost = depreciation_cost_blade_saw_cutting * (
            (cutareas["Cut area"] / (operation_factor_blade_saw_cutting * Crbs) 
             )
            + manipulation_time_blade_saw_cutting*cutareas["Manipulated volume"]
            )

    return labor_cost+material_cost+utility_cost+depreciation_cost




