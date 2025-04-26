##############################
#                            #
#   PROCESS OF DRILLING      #
#                            #
##############################
import math

def calculate_cost_drilling(labor_cost_drilling, 
                            material_cost_drilling, 
                            utility_cost_drilling, 
                            depreciation_cost_drilling, 
                            starting_time_drilling, 
                            manipulation_time_drilling, 
                            Stm, 
                            RPM, 
                            Fnd, 
                            STdo,
                            SDh,
                            thickness_flange, 
                            thickness_baffles,
                            thickness_removable_covers, 
                            thickness_tubesheets, 
                            number_tubes_per_pass, 
                            number_passes, 
                            number_baffles, 
                            number_tie_rods, 
                            volume_tubesheets, 
                            volume_flange, 
                            volume_baffles, 
                            volume_pass_partitions, 
                            volume_removable_covers, 
                            volume_shell, 
                            volume_heads,
                            tube_outside_diameter,
                            number_bolts,
                            diameter_bolts,
                            diameter_tie_rods):

       #Consistency of data entered
    labor_cost_drilling = float(labor_cost_drilling.value)
    material_cost_drilling = float(material_cost_drilling.value)
    utility_cost_drilling = float(utility_cost_drilling.value)
    depreciation_cost_drilling = float(depreciation_cost_drilling.value)
    starting_time_drilling = float(starting_time_drilling.value)
    manipulation_time_drilling = float(manipulation_time_drilling.value) 
    Stm = float(Stm.value)
    RPM = float(RPM.value)
    Fnd = float(Fnd.value)
    STdo = float(STdo.value)
    SDh = float(SDh.value)
    number_tubes_per_pass = float(number_tubes_per_pass.value)
    number_passes = float(number_passes.value)
    tube_outside_diameter = float(tube_outside_diameter.value)
    number_baffles = float(number_baffles.value)

    #Table 4 for calculating STd
    table_4 = [ 
            {"Drilling time": 2 * number_tubes_per_pass * number_passes * (Stm + (thickness_tubesheets / (RPM*Fnd)) + STdo),"Number of drilling passes": math.ceil(tube_outside_diameter/SDh) , "Manipulated volume": volume_tubesheets},
            {"Drilling time": 2 * number_bolts * (Stm + (thickness_tubesheets / (RPM*Fnd)) + STdo), "Number of drilling passes": math.ceil(diameter_bolts/SDh), "Manipulated volume": volume_tubesheets},
            {"Drilling time": number_tubes_per_pass * number_passes * (Stm + ((thickness_baffles * number_baffles) / (RPM*Fnd)) + STdo) , "Number of drilling passes": math.ceil(tube_outside_diameter/SDh), "Manipulated volume": volume_baffles},
            {"Drilling time": number_tie_rods * (Stm + ((thickness_baffles * number_baffles)/ (RPM*Fnd)) + STdo), "Number of drilling passes": math.ceil(diameter_tie_rods/SDh), "Manipulated volume": volume_baffles},
            {"Drilling time": 4 * number_bolts * (Stm + (thickness_flange/ (RPM*Fnd)) + STdo), "Number of drilling passes": math.ceil(diameter_bolts/SDh), "Manipulated volume": volume_pass_partitions},
            {"Drilling time": 2 * number_bolts * (Stm + (thickness_removable_covers / (RPM*Fnd)) + STdo), "Number of drilling passes": math.ceil(diameter_bolts/SDh), "Manipulated volume": volume_removable_covers}
            ]


    labor_cost=0
    material_cost=0
    utility_cost=0
    depreciation_cost=0 

    for components in table_4:
        labor_cost += (labor_cost_drilling/60) * (
            (components["Drilling time"]*components["Number of drilling passes"] 
             ) 
            + (starting_time_drilling*60)
            + (manipulation_time_drilling*60)*components["Manipulated volume"]
            )
        print(f"Labor cost of Drilling: {labor_cost}")
        material_cost += (material_cost_drilling/60) * (
            (components["Drilling time"]*components["Number of drilling passes"] 
             )
            )
        print(f"\n Material cost of Drilling: {material_cost}")
        utility_cost += (utility_cost_drilling/60) * (
            (components["Drilling time"]*components["Number of drilling passes"] 
             )
            + (manipulation_time_drilling*60)*components["Manipulated volume"]
            )
        print(f"\n Utily cost of Drilling: {utility_cost}")
        depreciation_cost += (depreciation_cost_drilling/60) * (
            (components["Drilling time"]*components["Number of drilling passes"] 
             )
            + (manipulation_time_drilling*60)*components["Manipulated volume"]
            )
        print(f"\n Depreciation cost of Drilling: {depreciation_cost} \n \n ")

    return labor_cost+material_cost+utility_cost+depreciation_cost



