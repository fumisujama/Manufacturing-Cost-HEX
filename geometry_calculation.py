'''GEOMETRIC CALCULATION MODULE FOR ALL PARTS
'''
import math


def calculate_shell_thickness(shell_side_pressure, tube_side_pressure, diameter_shell, max_allowable_stress, welding_efficiency): #poner unidades de cada varialbe
    diameter_shell=float(diameter_shell)
    shell_side_pressure= float(shell_side_pressure.value)
    tube_side_pressure=float(tube_side_pressure.value)
    design_pressure=max(shell_side_pressure, tube_side_pressure)
    max_allowable_stress = float(max_allowable_stress)
    welding_efficiency = float(welding_efficiency)
    #maybe in the future add explicit format and error catching of values,example :diameter shell should be only an integer
    #only to get strict values from the user, probably add max and min value to every parameter?
    shell_thickness=math.ceil((design_pressure * diameter_shell) / (max_allowable_stress*welding_efficiency - 0.6*design_pressure))
    print(f"\n #### first calculation of geometry ####\nthickness of shell: {shell_thickness}")
    return shell_thickness #agregar unidad de la variable que devuelve


def calculate_flange_and_bolts(table_d5, 
                               Ds, 
                               ts,
                               shell_side_pressure, 
                               tube_side_pressure, 
                               gasket_material_factor, 
                               max_allowable_stress, 
                               max_allowable_bolt_stress, 
                               welding_efficiency):

    shell_side_pressure= float(shell_side_pressure.value)
    tube_side_pressure=float(tube_side_pressure.value)
    design_pressure=max(shell_side_pressure, tube_side_pressure)
    Ds=float(Ds.value)
    ts=float(ts)
    gasket_material_factor = float(gasket_material_factor.value)
    max_allowable_stress = float(max_allowable_stress.value)
    max_allowable_bolt_stress = float(max_allowable_bolt_stress.value)
    welding_efficiency = float(welding_efficiency.value)
    #First calculate diameter of centers of bolts for the selected diameter
    design_pressure=max(shell_side_pressure, tube_side_pressure)
    for bolts in table_d5:
        Dcb = Ds + 2.4*ts + 2*bolts["Rr"]
        print("Dcb is "+str(Dcb))
        
        diameter_flange = Dcb + bolts["E"]  #2nd the diameter of the flange

        force_applied_to_bolts = 0.785*((Ds + 4*ts)**2)*design_pressure+ 2*math.pi*ts*(Ds + 4*ts)*gasket_material_factor*design_pressure
        #3rd calculate force applied to the bolts
        print("force applied to bolts is "+str(force_applied_to_bolts))
        d = Ds + 2*ts
        hg = 1.4*ts + 2*bolts["Rr"]
        c = 0.3
        Em = 210000 #MPa units
        print("Diameter of flange is "+ str(diameter_flange))
        K = diameter_flange / (Ds + 2*ts)
        print("K is "+ str(K))
        print("Ds + 2 ts is "+ str(Ds+2*ts))
        Kl = 0.2
        total_moment_acting_on_flange = 0.5 * force_applied_to_bolts * (Dcb - (Ds + 4*ts))
        flange_thickness = max(
                d * math.sqrt(
            (c*design_pressure/ (max_allowable_stress*welding_efficiency)) + (1.9 * force_applied_to_bolts * hg / (max_allowable_stress * welding_efficiency * d**3))
            ),
                ((109.4 * total_moment_acting_on_flange) / (Kl * Em * math.log(K)))**(1/3)
                               ) #4th calculate flange thickness
        debug_first_tfl =d * math.sqrt((c*design_pressure/ (max_allowable_stress*welding_efficiency)) + (1.9 * force_applied_to_bolts * hg / (max_allowable_stress * welding_efficiency * d**3)))
        debug_sec_tfl = (109.4 * total_moment_acting_on_flange) / (Kl * Em * math.log(K))**(1/3)
        
        max_number_of_bolts = math.floor(math.pi*Dcb / bolts["B"]) #5th calculate max number of bolts
        
        Bmax = 2*bolts["db"] + (6*flange_thickness / (gasket_material_factor + 0.5))
        min_number_of_bolts = max(
                math.ceil(math.pi*Dcb / Bmax),
                4
                ) #6th calculate the min number of bolts
        
        Ab = (math.pi*bolts["db"]**2) / 4
        Nbforce = math.ceil(force_applied_to_bolts / (max_allowable_bolt_stress * Ab)) #7th Calculate number of bolts needed to resist the force

        #Check condition if the bolts is the correct, it'll end the iteration
        if max_number_of_bolts<=max(min_number_of_bolts,Nbforce):


            continue
        else:
            break
    number_bolts = max(min_number_of_bolts, Nbforce)
    print(f"Diameter of bolts: {bolts["db"]}")   
    print(f"Diameter flange: {diameter_flange}")
    print(f"Flange thickness: {flange_thickness}")
    print(f"Number of bolts: {number_bolts}\n")

    return bolts["db"], diameter_flange, flange_thickness, number_bolts

def calculate_tubesheets_thickness(plates_table, 
                                   shell_outside_diameter, 
                                   shell_side_pressure, tube_side_pressure, 
                                   corrosion_allowance, 
                                   max_allowable_stress, 
                                   lay, 
                                   ltp, 
                                   dte,
                                   dfl):
    shell_side_pressure= float(shell_side_pressure.value)
    tube_side_pressure=float(tube_side_pressure.value)
    shell_outside_diameter= float(shell_outside_diameter.value)
    corrosion_allowance = float(corrosion_allowance.value)
    design_pressure=max(shell_side_pressure, tube_side_pressure)
    lay = lay.value
    ltp = float(ltp.value)
    dte = float(dte.value)
    tubesheets_diameter = dfl
    max_allowable_stress = float(max_allowable_stress.value)

    if lay=="Square":
        nu= (1 - 0.785) / ((ltp / dte)**2)
    else:
        nu = (1- 0.907) / ((ltp / dte)**2)
    F = 1
     
    condition = (F * shell_outside_diameter) / 3 * math.sqrt(design_pressure/ (nu * max_allowable_stress)) + corrosion_allowance
    for plates in plates_table:
        if plates["Thickness"]<condition:
            continue
        else:
            tubesheets_thickness = plates["Thickness"]
            print(f"thicknes of tubesheet: {tubesheets_thickness}")
            print(f"diameter of tubesheet: {tubesheets_diameter}")
            return tubesheets_thickness, tubesheets_diameter


def calculate_tubes_length(shell_length, tubesheets_thickness):
    shell_length = float(shell_length.value)
    tubes_length = shell_length + 2*tubesheets_thickness
    print(f"length of tubes: {tubes_length}")

    return tubes_length

def calculate_tubes_thickness(schedule40_table, dte):
    dte=float(dte.value)
    for tubes in schedule40_table:
        if tubes["Outside diameter"]<dte:
            continue
        else:
            tubes_thickness=tubes["Wall thickness"]
            print(f"tubes thickness is: {tubes_thickness}")

            return tubes_thickness

def calculate_baffles_diameter(shell_outside_diameter):
    
    shell_outside_diameter= float(shell_outside_diameter.value)
    if shell_outside_diameter <= 635:
        clearance = 1.5875
    else:
        clearance = 3.175
    baffles_diameter = shell_outside_diameter - 2*clearance
    print(f"Baffles diameter: {baffles_diameter}")
    return baffles_diameter


def calculate_baffles_thickness(table_cb441, Ds, shell_length, number_baffles): 
    Ds= float(Ds.value)
    shell_length = float(shell_length.value)
    number_baffles = float(number_baffles.value)
    df =shell_length/number_baffles
    for i,items in enumerate(table_cb441):
        if Ds>items["Outside diameter shell"]:
            continue
        else:
            if df>items["Distance between center baffles"]:
                continue
            else:
                baffle_thickness = table_cb441[i]["Baffle thickness"]
                print(f"Baffle thickness is {baffle_thickness}")
                return baffle_thickness




def calculate_nozzles_inside_diameters(shell_side_fluid_density, 
                                       tube_side_fluid_density, 
                                       shell_side_flow_velocity, 
                                       tube_side_flow_velocity, 
                                       shell_side_mass_flow_rate, 
                                       tube_side_mass_flow_rate, 
                                       schedule40_table):
    shell_side_fluid_density = float(shell_side_fluid_density.value)
    tube_side_fluid_density = float(tube_side_fluid_density.value)
    shell_side_flow_velocity = float(shell_side_flow_velocity.value) 
    tube_side_flow_velocity = float(tube_side_flow_velocity.value) 
    shell_side_mass_flow_rate = float(shell_side_mass_flow_rate.value) 
    tube_side_mass_flow_rate = float(tube_side_mass_flow_rate.value)


    shell_nozzles_inside_diameter = 2*math.sqrt(shell_side_mass_flow_rate / 
                                              (math.pi * shell_side_flow_velocity * shell_side_fluid_density)
                                              )
    tubes_nozzles_inside_diameter = 2*math.sqrt(tube_side_mass_flow_rate / 
                                                (math.pi * tube_side_flow_velocity * tube_side_fluid_density)
                                              )
                                  

    #Aproximate to the nearest inside diameter of schedule40
    for i,tubes in enumerate(schedule40_table):
        if shell_nozzles_inside_diameter<=(tubes["Outside diameter"]-2*tubes["Wall thickness"]):
            shell_nozzles_inside_diameter = schedule40_table[i]["Outside diameter"] - 2*schedule40_table[i]["Wall thickness"]
        else:
            continue

    for i,tubes in enumerate(schedule40_table):
        if tubes_nozzles_inside_diameter<=(tubes["Outside diameter"]-2*tubes["Wall thickness"]):
            tubes_nozzles_inside_diameter = schedule40_table[i]["Outside diameter"] - 2*schedule40_table[i]["Wall thickness"]
        
        else:
            continue
    print(f"shell nozzles inside diameter: {shell_nozzles_inside_diameter}")
    print(f"tubes nozzles inside diameter: {tubes_nozzles_inside_diameter}")
    return shell_nozzles_inside_diameter, tubes_nozzles_inside_diameter


def calculate_nozzles_length_thickness(diameter_flange, 
                                       outside_diameter_shell,
                                       shell_nozzles_inside_diameter,
                                       tubes_nozzles_inside_diameter,
                                       schedule40_table):
    diameter_flange = float(diameter_flange)
    outside_diameter_shell =float(outside_diameter_shell.value)


    for tubes in schedule40_table:
        if shell_nozzles_inside_diameter==tubes["Outside diameter"]-2*tubes["Wall thickness"]:
            shell_side_nozzles_thickness = tubes["Wall thickness"]
            shell_side_nozzles_length = ((diameter_flange - outside_diameter_shell)/2) + 2* shell_side_nozzles_thickness

        else:
            continue
    for tubes in schedule40_table:
        if tubes_nozzles_inside_diameter==tubes["Outside diameter"]-2*tubes["Wall thickness"]:
            tubes_side_nozzles_thickness = tubes["Wall thickness"]
            tubes_side_nozzles_length = ((diameter_flange - outside_diameter_shell)/2) + 2* tubes_side_nozzles_thickness

        else:
            continue
    print(f"shell_side_nozzles_length is {shell_side_nozzles_length}")
    print(f"shell_side_nozzles_thickness is {shell_side_nozzles_thickness}")
    print(f"tubes_side_nozzles_length is {tubes_side_nozzles_length}")
    print(f"tubes_side_nozzles_thickness is {tubes_side_nozzles_thickness}")
    return shell_side_nozzles_length, shell_side_nozzles_thickness, tubes_side_nozzles_length, tubes_side_nozzles_thickness 

def calculate_heads(outside_diameter_shell, 
                    thickness_shell, 
                    tubes_nozzles_inside_diameter):
    outside_diameter_shell = float(outside_diameter_shell.value) 
    thickness_shell =float(thickness_shell)
    tubes_nozzles_inside_diameter = float(tubes_nozzles_inside_diameter)


    head_length = 5*tubes_nozzles_inside_diameter
    head_thickness = thickness_shell
    head_diameter = outside_diameter_shell
    return head_length,head_thickness,head_diameter

def calculate_pass_partitions(head_diameter, 
                              head_length, 
                              table_rcb9131, 
                              diameter_shell):

    diameter_shell = float(diameter_shell.value)

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

def calculate_tie_rods(diameter_shell, table_r471, shell_length):
    diameter_shell = float(diameter_shell.value)
    shell_length= float(shell_length.value)
    for items in table_r471:
        if diameter_shell<=items["Diameter shell"]:
            number_tie_rods = items["Number of tie rods"]
            diameter_tie_rods = items["Tie rod diameter"]
            length_tie_rods = shell_length
            return number_tie_rods, diameter_tie_rods, length_tie_rods
        
        else:
            continue
