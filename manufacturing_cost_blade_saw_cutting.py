#########################################
#                                       #
#     PROCESS OF BLADE SAW CUTING       #
#                                       #
#########################################

import numpy as np

from RetrievingData import DesignDimensions_HE as DesHE
from RetrievingData import Dimensions_HE as DimHE
from RetrievingData import Volumes_HE as VolHE
import RawMaterialNozzles as RMnz
import RawMaterialTubes as RMt
import Stocks

#DIMENSIONS FOR EVERY PART
shell_nozzles=2*np.pi*((DesHE[12]**2-RMnz.RawMaterialNozzles()[1]**2)/4), VolHE[5]/2, 1 #put Lpipe here
head_nozzles=2*np.pi*((DesHE[12]**2-RMnz.RawMaterialNozzles()[1]**2)/4), VolHE[5]/2,1
tubes=DimHE[7]*DimHE[8]*np.pi*((DimHE[3]**2-(DimHE[3]-2*DesHE[8])**2)/4), VolHE[1],1
Dim_BladeSaw=[shell_nozzles,head_nozzles,tubes]

LCph=30
MCph=30
UCph=30
DCph=30

STh=1
STco=0.8

Ro=7,85*(10**(-6))
IC=100

def CostBladeSawCutting():
    Cost_BladeSawCuting=0
    i=0
    while i<len(Dim_BladeSaw):
        Labor_cost_BladeSaw=LCph*((STco*Ro*Dim_BladeSaw[i][2]+IC)*Dim_BladeSaw[i][0])+STh*Dim_BladeSaw[i][1]
        Material_cost_BladeSaw=MCph*((STco*Ro*Dim_BladeSaw[i][2]+IC)*Dim_BladeSaw[i][0])
        Utility_cost_BladeSaw=UCph*((STco*Ro*Dim_BladeSaw[i][2]+IC)*Dim_BladeSaw[i][0])
        Mach_Depreciation_cost_BladeSaw=DCph*((STco*Ro*Dim_BladeSaw[i][2]+IC)*Dim_BladeSaw[i][0])+STh*Dim_BladeSaw[i][1]
        Cost_BladeSawCuting=Cost_BladeSawCuting+Labor_cost_BladeSaw+Material_cost_BladeSaw+Utility_cost_BladeSaw+Mach_Depreciation_cost_BladeSaw
        i+=1
        return Cost_BladeSawCuting
