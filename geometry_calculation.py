'''GEOMETRIC CALCULATION MODULE FOR ALL PARTS
'''
import math


def calculate_shell_thickness(design_pressure, data_entry_table, max_allowable_stress, welding_efficiency):
    shell_thickness=math.ceil((design_pressure * data_entry_table) / (max_allowable_stress*welding_efficiency - 0.6*design_pressure))
    return shell_thickness


def calculate_flange_and_bolts(table_d5, Ds, ts, design_pressure, gasket_material_factor, max_allowable_stress, max_allowable_bolt_stress, welding_efficiency):
    #First calculate diameter of centers of bolts for the selected diameter
    for bolts in table_d5:
        Dcb = Ds + 2.4*ts + 2*bolts["Rr"]

        diameter_flange = Dcb + bolts["E"]  #2nd the diameter of the flange

        force_applied_to_bolts = 0.785*((Ds + 4*ts)**2)*design_pressure + 2*math.pi*ts*(Ds + 4*ts)*gasket_material_factor*design_pressure #3rd calculate force applied to the bolts
        
        d = Ds + 2*ts
        hg = 1.4*ts + 2*bolts["Rr"]
        c = 0.3
        Em = 210000 #MPa units
        K = diameter_flange / (Ds + 2*ts)
        Kl = 0.2
        flange_thickness = max(
                d * math.sqrt(
            (c*design_pressure / (max_allowable_stress*welding_efficiency)) + (1.9 * force_applied_to_bolts * hg / (max_allowable_stress * welding_efficiency * d**3))
            ),
                109.4 * total_moment_acting_on_flange / (Kl * Em * math.log(K))
                               ) #4th calculate flange thickness

        max_number_of_bolts = math.floor(math.pi*Dcb / bolts["B"]) #5th calculate max number of bolts
        
        Bmax = 2*bolts["db"] + (6*flange_thickness / (gasket_material_factor + 0.5))
        min_number_of_bolts = max(
                math.ceil(math.pi*Dcb / Bmax),
                4
                ) #6th calculate the min number of bolts
        
        Ab = (math.pi*bolts["db"]**2) / 4
        Nbforce = math.ceil(force_applied_to_bolts / (max_allowable_bolt_stress * Ab)
                            ) #7th Calculate number of bolts needed to resist the force
        
        #Check condition if the bolts is the correct, it'll end the iteration
        if max_number_of_bolts>max(min_number_of_bolts,Nbforce):
            continue
        else:
            number_bolts = max(min_number_of_bolts, Nbforce)
            return bolts["db"], diameter_flange, thickness_flange, number_bolts


def calculate_tubesheets_thickness(
        plates_table, shell_outside_diameter, design_pressure, corrosion_allowance, max_allowable_stress, lay, ltp, dte):
    if lay=="Square":
        nu= 1 - 0.785 / ((ltp / dte)**2)
    else:
        nu = 1- 0.907 / ((ltp / dte)**2)
    F = 1
    condition = (F * shell_outside_diameter) / 3 * math.sqrt(design_pressure / (nu * max_allowable_stress)) + corrosion_allowance
    for i, plates in enumerate(plates_table):
        if i<condition:
            continue
        else:
            tubesheets_thickness = i
            return tubesheets_thickness


def calculate_tubes_length(shell_length, tubesheets_thickness):
    tubes_length = shell_length + 2*tubesheets_thickness
    return tubes_length


def calculate_baffles_diameter(shell_outside_diameter):
    if shell_outside_diameter <= 635:
        cleareance = 1.5875
    else:
        clearence = 3.175
    baffles_diameter = shell_outside_diameter - 2*clearence
    return baffles_diameter


def calculate_baffles_thickness(table_cb441, Ds, length_shell, number_baffles): 
    df = length_shell/number_baffles
    for i,items in enumerate(table_cb441):
        if Ds<=items["Outside diameter shell"]:
            if df<=items["Distance between center baffles"]:
                return table_cb441[i-1]["Baffle Thickness"]
            else:
                continue
        else:
            continue




def calculate_nozzles_inside_diameter(shell_side_fluid_density, tube_side_fluid_density, shell_side_flow_velocity, tube_side_flow_velocity, shell_side_mass_flow_rate, tube_side_mass_flow_rate, schedule40_table):
    nozzles_inside_diameter = max(2*math.sqrt(shell_side_mass_flow_rate / 
                                              (math.pi * shell_side_flow_velocity * shell_side_fluid_density)
                                              ),
                                  2*math.sqrt(tube_side_mass_flow_rate / 
                                              (math.pi * tube_side_flow_velocity * tubeside_fluid_density)
                                              )
                                  )

    #Aproximate to the nearest inside diameter of schedule40
    for i,tubes in enumerate(schedule40_table):
        if nozzles_inside_diameter<=(tubes["Outside diameter"]-2*tubes["Wall thickness"]):
            nozzles_inside_diameter = schedule40_table[i]["Outside diameter"] - 2*schedule40_table[i]["Wall thickness"]
        
        else:
            continue

    return nozzles_inside_diameter


def calculate_nozzles_length_thickness(diameter_flange, outside_diameter_shell, schedule40_table):
    for tubes in schedule40_table:
        if nozzles_inside_diameter==tubes["Outside diameter"]-2*tubes["Wall thickness"]:
            thickness_nozzles = tubes["Wall thickness"]
        else:
            continue

    length_nozzles = (diameter_flange - outside_diameter_shell)/2 + 2*thickness_nozzles
    return length_nozzles, thickness_nozzles

def calculate_heads(outside_diameter_shell, thickness_shell, nozzles_inside_diameter):
    head_length = 5*nozzles_inside_diameter
    head_thickness = thickness_shell
    head_diameter = outside_diameter_shell
    return head_length,head_thickness,head_diameter

def calculate_pass_partitions(head_diameter, head_length, table_rcb9131, diameter_shell):
    pass_partitions_diameter = head_diameter
    pass_partitions_length = head_length
    for plates in table_rcb9131:
        if diameter_shell<=plates["Diameter shell"]:
            pass_partitions_thickness = plates["Pass partition thickness"]
        else:
            continue
    return pass_partitions_diameter, pass_partitions_length, pass_partitions_thickness

def calculate_removable_covers(diameter_flange, thickness_flange):
    diameter_removable_cover = diameter_flange
    thickness_removable_cover = thickness_flange
    return diameter_removable_cover, thickness_removable_cover

def calculate_tie_rods(diameter_shell, table_r471, length_shell):
    for items in table_r471:
        if diameter_shell<=items["Diameter shell"]:
            number_tie_rods = items["Number of tie rods"]
            diameter_tie_rods = items["Tie rod diameter"]
            length_tie_rods = length_shell
            return number_tie_rods, diameter_tie_rods, length_tie_rods
        
        else:
            continue
