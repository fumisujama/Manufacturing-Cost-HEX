'''GEOMETRIC CALCULATION MODULE FOR ALL PARTS
'''

def calculate_shell_thickness(design_pressure, data_entry_table, max_allowable_stress, welding_efficiency):
    ts=math.ceil((design_pressure * data_entry_table) / (max_allowable_stress*welding_efficiency - 0.6*design_pressure))
    return ts



