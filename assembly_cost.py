'''
Assembly cost calculation
'''

def cost_assembly(LCpha, STt, Sth, VHEX, labor_cost_bolted_joints, material_cost_bolted_joints, utility_cost_bolted_joints, depreciation_cost_bolted_joints, number_bolts, STba):
    STba = float(STba.value)

    STt = float(STt.value)
    Sth = float(Sth.value)
    LCpha = float(LCpha.value)

    labor_cost_bolted_joints = float(labor_cost_bolted_joints.value)
    material_cost_bolted_joints = float(material_cost_bolted_joints.value)
    utility_cost_bolted_joints = float(utility_cost_bolted_joints.value)
    depreciation_cost_bolted_joints = float(depreciation_cost_bolted_joints.value)


    labor_cost_assembly = (LCpha/60) * (STt*60 + Sth*60*VHEX)
    
    labor_cost = (labor_cost_bolted_joints/60)* number_bolts * STba*60
    material_cost = (material_cost_bolted_joints/60) * number_bolts * STba*60
    utility_cost = (utility_cost_bolted_joints/60) * number_bolts * STba*60
    depreciation_cost = (depreciation_cost_bolted_joints/60) * number_bolts * STba*60

    cost_assembly = labor_cost_assembly + labor_cost + material_cost + utility_cost + depreciation_cost
    return cost_assembly


