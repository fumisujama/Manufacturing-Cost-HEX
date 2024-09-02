'''GEOMETRIC CALCULATION MODULE FOR ALL PARTS
'''
import math


def calculate_shell_thickness(design_pressure, data_entry_table, max_allowable_stress, welding_efficiency):
    shell_thickness=math.ceil((design_pressure * data_entry_table) / (max_allowable_stress*welding_efficiency - 0.6*design_pressure))
    return shell_thickness


def calculate_diameter_of_bolts_center(shell_diameter, shell_thickness,
                                       distance_between_bolts):
    diameter_center_bolts = shell_diameter + 2.4*shell_thickness + 2*distance_between_bolts
    return diameter_center_bolts


def calculate_flange_outside_diameter(diameter_center_bolts, edge_distance):
    flange_outside_diameter = diameter_center_bolts + edge_distance
    return flange_outside_diameter



def calculate_force_applied_to_bolts(design_pressure, gasket_load_reaction_diameter, gasket_factor, shell_thickness):
    force_applied_to_bolts = 0.785 * (gasket_load_reaction_diameter**2) * design_pressure
    + 2 * math.pi * shell_thickness * gasket_load_reaction_diameter * gasket_factor * design_pressure
    return force_applied_to_bolts


def calculate_flange_thickness(
        plates_table, design_pressure, force_applied_to_bolts, shell_diameter,
        diameter_center_bolts, elasticity_modulus, shell_thickness,
        flange_outside_diameter, distance_between_bolts, max_allowable_stress,
        welding_efficiency):
    for i, plates_table in enumerate(plates_table): #change later to reflex front end changes using dictionaries
        d = shell_diameter + 2*shell_thickness
        hg = 1.4*shell_thickness + distance_between_bolts
        C = 0.3
        gasket_load_reaction_diameter = shell_diameter + 4*shell_thickness
        total_moment_acting_on_flange = (force_applied_to_bolts * (diameter_center_bolts - gasket_load_reaction_diameter)) / 2
        K = flange_outside_diameter / (shell_diameter + 2*shell_thickness)
        Kl = 0.2

        flange_thickness = max(d * math.sqrt((c*design_pressure / (max_allowable_stress*welding_efficiency)) + (1.9 * force_applied_to_bolts * hg / (max_allowable_stress * welding_efficiency * d**3))), 109.4 * total_moment_acting_on_flange / (Kl * welding_efficiency * math.log(K)))
        return flange_thickness


def calculate_max_number_of_bolts(diameter_center_bolts, min_distance_between_bolts):
    max_number_of_bolts = math.floor(math.pi * diameter_center_bolts / min_distance_between_bolts)
    return max_number_of_bolts


def calculate_max_distance_between_bolts(diameter_bolts, flange_thickness, gasket_material_factor):
    max_distance_between_bolts = 2*diameter_bolts + 6*flange_thickness / (gasket_factor +0.5)
    return max_distance_between_bolts


def calculate_min_number_of_bolts(diameter_center_bolts, max_distance_between_bolt):
    min_number_of_bolts = math.max(
            math.ceil(math.pi*diameter_center_bolts / 4),
            4)
    return min_number_of_bolts


def calculate_number_bolts_to_resist_force(force_applied_to_bolts, bolts_max_allowable_stress):
    area_of_bolt = math.pi * diameter_bolts**2 /4

    number_bolts_to_resist_force = math.ceil(force_applied_to_bolts / bolts_max_allowable_stress*area_of_bolts)
    return number_bolts_to_resist_force


def calculate_number_of_bolts(max_number_of_bolts, min_number_of_bolts, number_bolts_to_resist_force):
    if max_number_of_bolts > max(min_number_of_bolts, number_bolts_to_resist_force):
        #iterate again for the next bolt
        pass
    else:
        number_of_bolts = max(min_number_of_bolts, number_bolts_to_resist_force)
        return number_of_bolts


def calculate_tubesheets_thickness(
        plates_table, shell_diameter, design_pressure, corrosion_allowance, max_allowable_stress):
    if lay=="Square":
        nu= 1 - 0.785 / ((ltp / dte)**2)
    else:
        nu = 1- 0.907 / ((ltp / dte)**2)
    F = 1
    condition = (F * shell_diameter) / 3 * math.sqrt(design_pressure / (nu * max_allowable_stress)) + corrosion_allowance
    for i, plates in enumerate(plates_table):
        if i<condition:
            continue
        else:
            tubesheets_thickness = i
            return tubesheets_thickness

