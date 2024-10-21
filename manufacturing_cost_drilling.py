##############################
#                            #
#   PROCESS OF DRILLING      #
#                            #
##############################

from RetrievingData import DesignDimensions_HE as DesHE
from RetrievingData import Dimensions_HE as DimHE
from RetrievingData import Volumes_HE as VolHE

#parameters of the machine:
STm=1
RPMd=500
STdo=1
fnd=1
SDh=25.4
######################

#DIMENSIONS FOR EVERY PART
                            #drilling time Td                Ndp              V
Tubesheet_holes_for_tubes=DimHE[7]*DimHE[8]*(STm+DesHE[7]*(RPMd/fnd)+STdo) ,    1+(DimHE[3]/SDh),    VolHE[2]
Tubesheet_holes_for_flange_bolts=DesHE[0]*(STm+DesHE[7]*(RPMd/fnd)+STdo), 1+(DesHE[1]/SDh), VolHE[2]
Baffles=DimHE[7]*DimHE[8]*(STm+DesHE[11]*DesHE[0]*(RPMd/fnd)+STdo),         1+(DimHE[3]/SDh)  , VolHE[3]
Flange_holes_for_flange_bolts=DesHE[0]*(STm+DesHE[3]*(RPMd/fnd)+STdo),   1+(DesHE[1]/SDh),   VolHE[7]
Removable_cover= DesHE[0]*(STm+DesHE[24]*(RPMd/fnd)+STdo),                1+(DesHE[1]/SDh),   VolHE[6]




Dim_drilling=[Tubesheet_holes_for_tubes,Tubesheet_holes_for_flange_bolts,Baffles,Flange_holes_for_flange_bolts,Removable_cover]

LCph=30
MCph=30
UCph=30
DCph=30
STh=1
STt=10

def CostDrilling():
    Cost_of_Drilling=0
    i=0
    print(len(Dim_drilling))
    while i<len(Dim_drilling):
        Labor_cost_drill=LCph*(Dim_drilling[i][0]*Dim_drilling[i][1])+STt+STh*Dim_drilling[i][2]
        Material_cost_drill=MCph*(Dim_drilling[i][0]*Dim_drilling[i][1])
        Utility_cost_drill=UCph*Dim_drilling[i][0]*Dim_drilling[i][1]
        Mach_Depreciation_cost_drill=DCph*(Dim_drilling[i][0]*Dim_drilling[i][1]+STt+STh*Dim_drilling[i][2])
        #Cost_of_Drilling=Cost_of_Drilling+Labor_cost_drill()+Material_cost_drill()+Utility_cost_drill()+Mach_Depreciation_cost_drill()
        i+=1

    return Cost_of_Drilling
print(CostDrilling())
