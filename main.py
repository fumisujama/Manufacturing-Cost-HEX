import flet as ft
import geometry_calculation
import volumes

#correr 150 ejemplos con la nueva version (test de consistencia) y a la nueva version se testea varias veces la novedad.
#al arreglar un bug. hay que identificar los ejemplos en los que el error ocurre. corriendo el nuevo 
#una vez superado el excel, tenerlo como repositorio de ejemplos.
#29/10/2024

#En el nuevo software, agregar unit testings para cada formula.
#En un excel, poner en cada columna el costos parciales, y su desglose

#Terminar el paper con un analisis de sensibilidad de cada parametro
#analizar la cantidad de parametros necesarios para obtener una desviacion del 5%

"""Tables used for calculating, should be moved later in next iterations
ask how to integrate them on the code, for now, we put it here 20/10/2024
"""
#Table D-5

table_d5 = [        # db        B        Rr        E 
{"db": 12.7,    "B": 31.75,     "Rr": 15.875,   "E":  15.875},#ok
{"db": 15.875,  "B": 38.1,      "Rr": 19.05,    "E":  19.05},   #ok
{"db": 19.05,   "B": 44.45,     "Rr": 20.6375,  "E":  20.6375}, #ok
{"db": 22.225,  "B": 52.3875,   "Rr": 23.8125,  "E":  23.8125}, #ok
{"db": 25.4,    "B": 57.15 ,    "Rr": 26.9875,  "E":  26.9875}, #ok,
{"db": 28.575,  "B": 63.5,      "Rr": 28.575,   "E":  28.575}, #o,k
{"db": 31.75,   "B": 71.4375,   "Rr": 31.75,    "E":  31.75},  #ok
{"db": 34.925,  "B": 77.7875,   "Rr": 34.925,   "E":  34.925}, #ok
{"db": 38.1,    "B": 82.55,     "Rr": 38.1,     "E":  38.1},  #}ok
{"db": 41.275,  "B": 88.9,      "Rr": 41.275,   "E":  41.275}, #ok
{"db": 44.45,   "B": 95.25,     "Rr": 44.45,    "E":  44.450}, #ok
{"db": 47.625,  "B": 101.6,     "Rr": 47.625,   "E":  47.625}, #ok
{"db": 50.8,    "B": 107.95,    "Rr": 50.8,     "E":  50.8}, #}ok
{"db": 57.15,   "B": 120.65,    "Rr": 57.15,    "E":  57.150}, #ok
{"db": 63.5,    "B": 133.35,    "Rr": 63.5,     "E":  60.325},#ok
{"db": 69.85,   "B": 146.05,    "Rr": 69.85,    "E":  66.675}, #ok
{"db": 76.2,    "B": 158.75,    "Rr": 76.2,     "E":  73.025}, #ok
{"db": 82.55,   "B": 168.275,   "Rr": 82.55,    "E":  76.2},  #}ok
{"db": 88.9,    "B": 180.975,   "Rr": 88.9,     "E":  82.55}, #ok
{"db": 95.25,   "B": 193.675,   "Rr": 95.25,    "E":  88.9}, #}ok
{"db": 101.6,   "B": 206.375,   "Rr": 101.6,    "E":  92.075}  #ok
 ]

#Table CB 4.41

table_cb441 = [
    {"Outside diameter shell": 356, "Distance between center baffles" : 305, "Baffle thickness": 1.6},
    {"Outside diameter shell": 356, "Distance between center baffles" : 610, "Baffle thickness": 3.2},
    {"Outside diameter shell": 356, "Distance between center baffles" : 914, "Baffle thickness": 4.8},
    {"Outside diameter shell": 356, "Distance between center baffles" : 1219, "Baffle thickness": 6.4},
    {"Outside diameter shell": 356, "Distance between center baffles" : 1524, "Baffle thickness": 9.5},
    {"Outside diameter shell": 356, "Distance between center baffles" : 100000, "Baffle thickness": 9.5},
    {"Outside diameter shell": 711, "Distance between center baffles" : 305, "Baffle thickness": 3.2},
    {"Outside diameter shell": 711, "Distance between center baffles" : 610, "Baffle thickness": 4.8},
    {"Outside diameter shell": 711, "Distance between center baffles" : 914, "Baffle thickness": 6.4},
    {"Outside diameter shell": 711, "Distance between center baffles" : 1219, "Baffle thickness": 9.5},
    {"Outside diameter shell": 711, "Distance between center baffles" : 1524, "Baffle thickness": 9.5},
    {"Outside diameter shell": 711, "Distance between center baffles" : 100000, "Baffle thickness": 12.7},
    {"Outside diameter shell": 965, "Distance between center baffles" : 305, "Baffle thickness": 4.8},
    {"Outside diameter shell": 965, "Distance between center baffles" : 610, "Baffle thickness": 6.4},
    {"Outside diameter shell": 965, "Distance between center baffles" : 914, "Baffle thickness": 7.9},
    {"Outside diameter shell": 965, "Distance between center baffles" : 1219, "Baffle thickness": 9.5},
    {"Outside diameter shell": 965, "Distance between center baffles" : 1524, "Baffle thickness": 12.7},
    {"Outside diameter shell": 965, "Distance between center baffles" : 100000, "Baffle thickness": 15.9},
    {"Outside diameter shell": 1524, "Distance between center baffles" : 305, "Baffle thickness": 6.4},
    {"Outside diameter shell": 1524, "Distance between center baffles" : 610, "Baffle thickness": 6.4},
    {"Outside diameter shell": 1524, "Distance between center baffles" : 914, "Baffle thickness": 9.5},
    {"Outside diameter shell": 1524, "Distance between center baffles" : 1219, "Baffle thickness": 12.7},
    {"Outside diameter shell": 1524, "Distance between center baffles" : 1524, "Baffle thickness": 15.9},
    {"Outside diameter shell": 1524, "Distance between center baffles" : 100000, "Baffle thickness": 15.9},
    {"Outside diameter shell": 2540, "Distance between center baffles" : 305, "Baffle thickness": 6.4},
    {"Outside diameter shell": 2540, "Distance between center baffles" : 610, "Baffle thickness": 9.5},
    {"Outside diameter shell": 2540, "Distance between center baffles" : 914, "Baffle thickness": 12.7},
    {"Outside diameter shell": 2540, "Distance between center baffles" : 1219, "Baffle thickness": 15.9},
    {"Outside diameter shell": 2540, "Distance between center baffles" : 1524, "Baffle thickness": 19.1},
    {"Outside diameter shell": 2540, "Distance between center baffles" : 100000, "Baffle thickness": 19.1}
    ]

#Table RCB 9.1.3.1

table_rcb9131 = [
        {"Diameter shell":610 , "Pass partition thickness":9.5},
        {"Diameter shell":1524, "Pass partition thickness":12.7},
        {"Diameter shell":2540, "Pass partition thickness":15.9}
        ]


#Table R 4.7.1

table_r471 = [
        {"Diameter shell": 381, "Tie rod diameter": 9.5, "Number of tie rods": 4},
        {"Diameter shell": 686, "Tie rod diameter": 9.5, "Number of tie rods": 6},
        {"Diameter shell": 838, "Tie rod diameter": 12.7, "Number of tie rods": 6},
        {"Diameter shell": 1219, "Tie rod diameter": 12.7, "Number of tie rods": 8},
        {"Diameter shell": 1524, "Tie rod diameter": 12.7, "Number of tie rods": 10},
        {"Diameter shell": 2540, "Tie rod diameter": 15.9, "Number of tie rods": 12}
        ]


#also stocks from should be moved to another place, for now, it'll stay here 20/10/2024
#A36 Steel Plates from https://www.metalsdepot.com/steel-products/steel-plate
    #Wp  Lp   tp           $
plates_table = [
{"Width": 1524,"Length": 3048,"Thickness":    4.7625,"Price":     482.50},
{"Width": 1524,"Length": 3048,"Thickness":    6.35,"Price":       643.0  },
{"Width": 1524,"Length": 3048,"Thickness":    9.525,"Price":      1034.0},
{"Width": 1524,"Length": 3048,"Thickness":    12.7,"Price":       1470.0},
{"Width": 1219.2,"Length": 2438.4,"Thickness":15.875,"Price":    1544.00},
{"Width": 1524,"Length": 3048,"Thickness":     19,"Price":      2894.50},
{"Width": 1219.2,"Length": 2438.4,"Thickness":22.225,"Price": 2676.16},
{"Width": 1524,"Length": 3048,"Thickness":25.4,"Price":       3675.50},
{"Width": 1219.2,"Length": 2438.4,"Thickness":28.575,"Price":  6616.64 },
{"Width": 1219.2,"Length": 2438.4,"Thickness":31.75,"Price":   3822.40},
{"Width": 1219.2,"Length": 2438.4,"Thickness":34.925,"Price": 6468.48},
{"Width": 1219.2,"Length": 2438.4,"Thickness":37.7,"Price": 4586.88},
{"Width": 1219.2,"Length": 2438.4,"Thickness":44.45,"Price":5351.36},
{"Width": 1219.2,"Length": 2438.4,"Thickness":50.8,"Price":6116.16},
{"Width": 1219.2,"Length": 1219.2,"Thickness":63.5,"Price":3822.56}
]

#Rods
    #OD    Lr   $
rods_table = [
{"Outside diameter": 3.175,"Length": 6000,"Price": 100},
{"Outside diameter": 6.35,"Length": 6000,"Price":  150},
{"Outside diameter": 9.525,"Length": 6000,"Price": 200},
{"Outside diameter": 12.7,"Length": 6000,"Price":  250},
{"Outside diameter": 15.875,"Length": 6000,"Price":300},
{"Outside diameter": 19.05,"Length": 6000,"Price": 350},
{"Outside diameter": 22.225,"Length": 6000,"Price":400},
{"Outside diameter": 25.4,"Length": 6000,"Price":  450},
{"Outside diameter": 28.575,"Length": 6000,"Price":500},
{"Outside diameter": 31.75,"Length": 6000,"Price":550},
{"Outside diameter": 34.925,"Length": 6000,"Price":600},
{"Outside diameter": 38.1,"Length": 6000,"Price":650},
{"Outside diameter": 41.275,"Length": 6000,"Price":700}
]

#Tubes from SCHEDULE 40s and 40 https://www.trupply.com/products/seamless-pipe-a106b?variant=41891233464482
   #dte     L   t       $
schedule40_table = [
{"Outside diameter": 21.3,"Length": 6096,"Wall thickness": 2.77,"Price": 61.34},
{"Outside diameter": 26.7,"Length": 6096,"Wall thickness": 2.87,"Price": 81.50},
{"Outside diameter": 33.4,"Length": 6096,"Wall thickness": 3.38,"Price": 120.96},
{"Outside diameter": 42.2,"Length": 6096,"Wall thickness": 3.56,"Price": 163.58},
{"Outside diameter": 48.3,"Length": 6096,"Wall thickness": 3.68,"Price": 195.84},
{"Outside diameter": 60.3,"Length": 6096,"Wall thickness": 3.91,"Price": 263.52},
{"Outside diameter": 88.9,"Length": 6096,"Wall thickness": 5.49,"Price": 382.18},
{"Outside diameter": 101.6,"Length": 6096,"Wall thickness": 5.74,"Price": 459.65},
{"Outside diameter": 114.3,"Length": 6096,"Wall thickness": 6.02,"Price": 544.32},
{"Outside diameter": 141.3,"Length": 6096,"Wall thickness": 6.55,"Price": 600},
{"Outside diameter": 168.3,"Length": 6096,"Wall thickness": 7.11,"Price": 711.6},
{"Outside diameter": 219.1,"Length": 6096,"Wall thickness": 8.18,"Price": 922.38},
{"Outside diameter": 273.0,"Length": 6096,"Wall thickness": 9.27,"Price": 1146},
{"Outside diameter": 323.8,"Length": 6096,"Wall thickness": 10.31,"Price": 1356.76},
{"Outside diameter": 355.6,"Length": 6096,"Wall thickness": 11.13,"Price": 1300},
{"Outside diameter": 406.4,"Length": 6096,"Wall thickness": 12.7,"Price": 1400},
{"Outside diameter": 457.0,"Length": 6096,"Wall thickness": 14.27,"Price": 1500},
{"Outside diameter": 508.0,"Length": 6096,"Wall thickness": 15.09,"Price": 1600},
{"Outside diameter": 610.0,"Length": 6096,"Wall thickness": 17.48,"Price": 9381.89}
]



def main(page: ft.Page):

    page.title = "Heat Exchanger manufacturing cost"
    page.vertical_alignment = ft.alignment.center
    page.horizontal_alignment = ft.alignment.center
    page.scroll = "adaptive"


    def button_clicked_test(e):
        data_entry.value = f"The value of data table is: '{ds.value}', '{ls.value}', '{dte.value}', '{lay.value}', '{ltp.value}', '{Nb.value}',  '{BC.value}', '{number_passes.value}', '{Ntp.value}'."
        page.update()

    def calculate_geometry():
        ts = calculate_geometry.calculate_shell_thickness(design_pressure, ds, S, Sb, welding_efficiency)

        Dcb = calculate_geometry.calculate_diameter_of_bolts_center(ds, ts, table_d5)

        diameter_bolts, diameter_flange, thickness_flange, number_bolts = geometry_calculation.calculate_flange_and_bolts(table_d5, ds, ts, design_pressure, gasket_material_factor, S, Sb, welding_efficiency)
        print(f"Nb is {Nb}")
        
        tubesheets_thickness = geometry_calculation.calculate_tubesheets_thickness(plates_table, Ds, design_pressure, corrosion_allowance, S, lay, ltp, dte)

        tubes_length = geometry_calculation.calculate_tubes_length(ls, tubesheets_thickness)
        
        baffles_diameter = geometry_calculation.calculate_baffles_diameter(ds)

        baffles_thickness = geometry_calculation.calculate_baffles_thickness(table_cb441, ds, ls, nb)
        
        nozzle_inside_diameter = geometry_calculation.calculate_nozzles_inside_diameter(shell_side_fluid_density, tube_side_fluid_density, shell_side_flow_velocity, tube_side_flow_velocity, shell_side_mass_flow, tube_side_mass_flow, schedule40_table)

        nozzles_length, nozzles_thickness = geometry_calculation.calculate_nozzles_length_thickness(diameter_flange, ds, schedule40_table)
        
        head_length, head_thickness, head_diameter = geometry_calculation.calculate_heads(ds, ts, nozzles_inside_diameter)

        pass_partition_diameter, pass_partition_length, pass_partitions_thickness = geometry_calculation.calculate_pass_partitions(head_diameter, head_length, table_rcb9131, ds)

        diameter_removable_cover, thickness_removable_cover = geometry_calculation.calculate_removable_cover(diameter_flange, thickness_flange)

        number_tie_rods, diameter_tie_rods, length_tie_rods = geometry_calculation.calculate_tie_rods(ds, table_r471)

    def calculate_volumes():
        volume_shell = volumes.volume_shell(diameter_shell, length_shell, thickness_shell, diameter_nozzles)

        volume_tubes = volumes.volume_tubes(tubes_length, number_tubes_pass, number_passes, dte, tt)

        volume_tubesheets = volumes.volume_tubes(thickness_tubesheets, diameter_flange, number_tubes_pass, number_passes, dte, number_baffles, diameter_baffles)
        
        volume_baffles = volumes.volume_baffles(diameter_baffles, number_tubes_pass, number_passes, BC, dte, number_baffles, thickness_baffles)

        volume_heads = volumes.volume_heads(heads_length, thickness_shell, diameter_shell, diameter_nozzles)

        volume_nozzles = volumes.volume_nozzles(length_nozzles, thickness_nozzles, diameter_nozzles)

        volume_removable_covers= volumes.volume_removable_cover(diameter_flange, thickness_flange, number_bolts, diameter_bolts)

        volume_flange = volumes.volume_flange(diameter_shell, diameter_flange, thickness_flange)

        volume_pass_partitions = volumes.volume_pass_partitions(number_passes, diameter_shell, thickness_pass_partitions, heads_length)

        volume_tie_rods = volumes.volume_tie_rods(number_tie_rods, diameter_tie_rods, length_tie_rods)



    #Data Entry

    ds = ft.TextField(label="Shell inside diameter", width=200) #agregar unidades de todo
    ls = ft.TextField(label="Shell length", width=200)
    dte = ft.TextField(label="Outside diameter of tubes", width=200)
    lay = ft.TextField(label="Pitch type", width=200)
    ltp = ft.TextField(label="Tube pitch ratio", width=200)
    Nb = ft.TextField(label="Number of baffles", width=200)
    BC = ft.TextField(label="Baffle cut", width=200)
    number_passes = ft.TextField(label="Number of passes", width=200)
    Ntp = ft.TextField(label="Number of tubes per pass", width=200)
    
    #Parameters
    S = ft.TextField(label="Maximum Allowable Stress")
    Sb = ft.TextField(label="Maximum Allowable Bolt Stress")
    m = ft.TextField(label="Gasket Material Factor")
    welding_efficiency = ft.TextField(label="Welding efficiency")
    corrosion_allowance = ft.TextField(label="Corrosion allowance")

    #Fluid Parameters
    shell_side_pressure = ft.TextField(label="Shell Side Pressure")
    tube_side_pressure = ft.TextField(label="Tube Side pressure")
    shell_side_fluid_velocity = ft.TextField(label="Shell Side Fluid Velocoity")
    tube_side_fluid_velocity = ft.TextField(label="Tube Side Fluid Velocity")
    shell_side_mass_flow = ft.TextField(label="Shell Side Mass Flow")
    tube_side_mass_flow = ft.TextField(label="Tube Side Mass Flow")
    shell_side_fluid_density = ft.TextField(label="Shell Side Fluid Density")
    tube_side_fluid_density = ft.TextField(label="Tube Side Fluid Density")

    design_pressure = max(shell_side_pressure.value, tube_side_pressure.value)

    #Assembly Settings
    labor_cost_assembly = ft.TextField(label="Labor cost per hour of assembly")
    manipulation_time_assembly = ft.TextField(label="Manipulation Time per 1000kg of material")
    
    labor_cost_bolted_joints = ft.TextField(label="Labor cost per hour of bolted joints")
    material_cost_bolted_joints = ft.TextField(label="Material cost per hour of bolted joints")
    utility_cost_bolted_joints = ft.TextField(label="Utility cost per hour of bolted joints")
    depreciation_cost_bolted_joints = ft.TextField(label="Depreciation cost per hour of bolted joints")

    #Economic Model Parameters
    cost_shipping = ft.TextField(label="Cost per kilometer of shipping")
    cost_foundation = ft.TextField(label="Cost per squared meter of foundation")
    km_shipping = ft.TextField(label="Kilometers of shipping")
    labor_cost_LAP = ft.TextField(label="Labor cost per hour of lift, alignment and positioning of heat exchanger")
    manipulation_time_assembly = ft.TextField(label="Manipulation Time per 1000kg of material")
    starting_time_LAP = ft.TextField(label="Starting time of lift, alignment and positioning of heat exchanger")
    
    #Operational Settings

    #Plasma Cutting operation parameters
    labor_cost_plasma_cutting = ft.TextField(label="Labor cost per hour of plasma cutting")
    material_cost_plasma_cutting = ft.TextField(label="Material cost per hour of plasma cutting")
    utility_cost_plasma_cutting = ft.TextField(label="Utility cost per hour of plasma cutting")
    depreciation_cost_plasma_cutting = ft.TextField(label="Depreciation cost per hour of plasma cutting")
    starting_time_plasma_cutting = ft.TextField(label="starting time of plasma cutting")    
    manipulation_time_plasma_cutting = ft.TextField(label="manipulation time per 1000kg of material")
    spca = ft.TextField(label="spca")
    tpcs = ft.TextField(label="tpcs")
    operation_factor_plasma_cutting = ft.TextField(label="Operation factor of plasma cutting")
    ec = ft.TextField(label="Width of plasma cutting")


    #Drilling operation parameters
    labor_cost_drilling = ft.TextField(label="Labor cost per hour of drilling")
    material_cost_drilling = ft.TextField(label="Material cost per hour of drilling")
    utility_cost_drilling = ft.TextField(label="Utility cost per hour of drilling")
    depreciation_cost_drilling = ft.TextField(label="Depreciation cost per hour of drilling")
    starting_time_drilling = ft.TextField(label="Starting time of drilling")    
    manipulation_time_drilling = ft.TextField(label="manipulation time per 1000kg of material")
    Stm = ft.TextField(label="Stm")
    rpm = ft.TextField(label="RPM of drilling tool")
    fnd = ft.TextField(label="Feed of tool")
    Stdo = ft.TextField(label="Stdo")
    Sdh = ft.TextField(label="Sdh")


    #Lathe operation parameters
    labor_cost_lathe = ft.TextField(label="Labor cost per hour of lathe")
    material_cost_lathe = ft.TextField(label="Material cost per hour of lathe")
    utility_cost_lathe = ft.TextField(label="Utility cost per hour of lathe")
    depreciation_cost_lathe = ft.TextField(label="Depreciation cost per hour of lathe")
    operation_factor_lathe = ft.TextField(label="Operation factor of lathe")
    vcl = ft.TextField(label="vcl")
    apl = ft.TextField(label="apl")
    fnl = ft.TextField(label="fnl")


    #Root pass welding operation parameters
    labor_cost_root_pass_welding = ft.TextField(label="Labor cost per hour of root pass welding")
    material_cost_root_pass_welding = ft.TextField(label="Material cost per hour of root pass welding")
    utility_cost_root_pass_welding = ft.TextField(label="Utility cost per hour of root pass welding")
    depreciation_cost_root_pass_welding = ft.TextField(label="Depreciation cost per hour of root pass welding")
    density_filler_material = ft.TextField(label="Density of filler material for root pass")
    nrp = ft.TextField(label="nrp")
    operation_factor_root_pass_welding = ft.TextField(label="Operation factor of root pass welding")
    rrp = ft.TextField(label="rrp")
    thickness_root_pass_welding = ft.TextField(label="Thickness of root pass welding")


    #Welding operation parameters
    labor_cost_welding = ft.TextField(label="Labor cost per hour of welding")
    material_cost_welding = ft.TextField(label="Material cost per hour of welding")
    utility_cost_welding = ft.TextField(label="Utility cost per hour of welding")
    depreciation_cost_welding = ft.TextField(label="Depreciation cost per hour of welding")
    density_filler_material = ft.TextField(label="Density of filler material for welding")
    nrp = ft.TextField(label="nrp")
    operation_factor_welding = ft.TextField(label="Operation factor of welding")
    rrp = ft.TextField(label="rrp")
    thickness_root_pass_welding = ft.TextField(label="Thickness of welding")
    

    #Blade Saw Cutting operation parameters
    labor_cost_blade_saw_cutting = ft.TextField(label="Labor cost per hour of blade saw cutting")
    material_cost_blade_saw_cutting = ft.TextField(label="Material cost per hour of blade saw cutting")
    utility_cost_blade_saw_cutting = ft.TextField(label="Utility cost per hour of blade saw cutting")
    depreciation_cost_blade_saw_cutting = ft.TextField(label="Depreciation cost per hour of blade saw cutting")
    Crbs = ft.TextField(label="Crbs")
    operation_factor_blade_saw_cutting = ft.TextField(label="Operation factor of blade saw cutting")



    data_entry = ft.Text("Data Entry")

    
    data_entry_Row = ft.Row(
        controls=[
            ft.Column(controls=[
                data_entry,
                ds,
                ls,
                dte,
                lay,
                ltp,
                Nb,
                BC,
                number_passes,
                Ntp,
                ft.ElevatedButton("test", on_click=button_clicked_test)
                ]
                      ),
            ft.Column(controls=[
                ft.Container(
                    ft.Text("Parameters"),
                    bgcolor=ft.colors.RED_400,
                    padding=5,
                    border_radius=10,
                    width=200,
                    height=100,
                    alignment=ft.alignment.center),
                                    
                    ft.Container(ft.Text("Fluid parameters"), bgcolor=ft.colors.RED, padding=5, border_radius=10, width=200, height=200, alignment=ft.alignment.center),
                    ft.Container(ft.Text("Assembly settings"), bgcolor=ft.colors.RED, padding=5, border_radius=10, width=200, height=200, alignment=ft.alignment.center),
                    ft.Container(ft.Text("Economic model parameters"), bgcolor=ft.colors.RED, padding=5, border_radius=10, width=200, height=200, alignment=ft.alignment.center),
                    ft.Container(ft.Text("Operational settings"), bgcolor=ft.colors.RED, padding=5, border_radius=10, width=200, height=200, alignment=ft.alignment.center)
                ]
                      ),
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Row(controls=[
                            ft.Text("Parameters"),
                            S,
                            Sb,
                            m,
                            welding_efficiency
                            ],
                               wrap=True
                           ),
                        border=ft.border.all(2, ft.colors.BLUE_200),
                                 ),

                    ft.Container(
                        ft.Row(controls=[
                            ft.Text("Assembly Settings"),
                            
                            labor_cost_assembly,
                            manipulation_time_assembly, 
    
                            labor_cost_bolted_joints,
                            material_cost_bolted_joints,
                            utility_cost_bolted_joints,
                            depreciation_cost_bolted_joints
                            ],
                               wrap=True
                               )
                        ),
                    
                    ft.Container(
                        ft.Row(
                            controls=[
                                ft.Text("Fluid Parameters"),
                                shell_side_pressure,
                                tube_side_pressure,
                                shell_side_fluid_velocity,
                                tube_side_fluid_velocity,
                                shell_side_mass_flow,
                                tube_side_mass_flow,
                                shell_side_fluid_density,
                                tube_side_fluid_density
                                ],
                                   wrap=True
                                   ),
                         border=ft.border.all(2, ft.colors.BLUE_200)
                        ),
                    
                    ft.Container(
                        ft.Row(
                            controls=[
                                ft.Text("Economic Model Parameters"),
                                cost_shipping,
                                cost_foundation,
                                km_shipping, 
                                labor_cost_LAP,
                                manipulation_time_assembly,
                                starting_time_LAP
                                ],
                               wrap=True
                            ),
                        border=ft.border.all(2, ft.colors.BLUE_200),
                        alignment=ft.alignment.center
                        ),

                    ft.Container(
                        ft.Row(controls=[
                            ft.Text("Operational Settings"),
                            ft.Text("Plasma Cutting"),
    #Plasma Cutting operation parameters
                            labor_cost_plasma_cutting, 
                            material_cost_plasma_cutting, 
                            utility_cost_plasma_cutting, 
                            depreciation_cost_plasma_cutting, 

    #Drilling operation parameters
                            labor_cost_drilling, 
                            material_cost_drilling, 
                            utility_cost_drilling, 
                            depreciation_cost_drilling, 
    
    #Lathe operation parameters
                            labor_cost_lathe, 
                            material_cost_lathe, 
                            utility_cost_lathe, 
                            depreciation_cost_lathe, 

    #Root pass welding operation parameters
                            labor_cost_root_pass_welding, 
                            material_cost_root_pass_welding, 
                            utility_cost_root_pass_welding, 
                            depreciation_cost_root_pass_welding, 

    #Welding operation parameters
                            labor_cost_welding, 
                            material_cost_welding, 
                            utility_cost_welding, 
                            depreciation_cost_welding, 
    
    #Blade Saw Cutting operation parameters
                            labor_cost_blade_saw_cutting, 
                            material_cost_blade_saw_cutting, 
                            utility_cost_blade_saw_cutting, 
                            depreciation_cost_blade_saw_cutting
                            ],
                                  wrap=True
                                  )
                        )
                    ]
                )
            ],
            wrap=True
        )
    
    #Calculated Geometry

    data_entry_list = [ds.value, ls.value, dte.value, lay.value, ltp.value, Nb.value, BC.value, number_passes.value, Ntp.value]
    

    page.add(data_entry_Row)
    
ft.app(main)

