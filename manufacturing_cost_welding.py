###################################################
#
#          PROCESS OF  WELDING
#
###################################################

import numpy as np
from RetrievingData import DesignDimensions_HE as DesHE
from RetrievingData import Dimensions_HE as DimHE
from RetrievingData import Volumes_HE as VolHE
import RawMaterialShell as RMs

#parameters of operations:
Ro=7,85*(10**(-6))
n=0.8
k=0.5
r=10
tw=1.6 #[mm]

#DIMENSIONS FOR EVERY PART
#           Volume of welding                           Vwroot                    Vh
shell_to_nozzles=2*DesHE[12]*np.pi*(tw**2),     VolHE[5]/2
flange_to_shell_nozzle=2*DesHE[12]*np.pi*(tw**2), VolHE[5]/2 #Dont use the vol of nozzles's flanges, ask agosta later
tubesheet_to_shell=2*DimHE[0]*np.pi*(tw**2),VolHE[2]+VolHE[0] 
nozzles_flange_to_head_nozzle=DesHE[12]*np.pi*(tw**2), VolHE[5]/2 #the same as above
head_to_nozzle=DesHE[12]*np.pi*(tw**2),VolHE[5]/2
flange_to_heads=4*DimHE[0]*np.pi*(tw**2), VolHE[7]
tube_to_tubesheets=DimHE[7]*DimHE[8]*2*DimHE[3]*np.pi*(tw**2),VolHE[1]
tierods_tubesheets=DesHE[21]*DesHE[20]*2*np.pi*(tw**2),VolHE[9]



Dim_Weld=[shell_to_nozzles,flange_to_shell_nozzle,tubesheet_to_shell,nozzles_flange_to_head_nozzle,head_to_nozzle,flange_to_heads,tube_to_tubesheets]

if DimHE[0]>609.6:
    shell_circumferencial=(RMs.RawMaterialShell()[1]-1)*DimHE[0]*np.pi*(tw**2), VolHE[0]
    shell_longitudinal=DimHE[1]*(tw**2), VolHE[0]
    head_length=2*DesHE[15]*(tw**2), VolHE[4]
    Dim_Weld.append(shell_circumferencial)
    Dim_Weld.append(shell_longitudinal)
    Dim_Weld.append(head_length)

LCph=1
MCph=1
UCph=1
DCph=1


STh=10

def CostWelding():
    Cost_of_Weld=0
    i=0
    while i<len(Dim_Weld):
        Labor_cost_Weld=LCph*(Ro/(n*k*r))*Dim_Weld[i][0]+STh*Dim_Weld[i][1]
        Material_cost_Weld=MCph*(Ro/(n*k*r))*Dim_Weld[i][0]
        Utility_cost_Weld=UCph*(Ro/(n*k*r))*Dim_Weld[i][0]
        Mach_Depreciation_cost_Weld=DCph*(Ro/(n*k*r))*Dim_Weld[i][0]+STh*Dim_Weld[i][1]
        Cost_of_Weld=Cost_of_Weld+Labor_cost_Weld+Material_cost_Weld+Utility_cost_Weld+Mach_Depreciation_cost_Weld
        i+=1
    return Cost_of_Weld
