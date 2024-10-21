#########################################
#                                       #
#          PROCESS OF LATHE             #
#                                       #
#########################################
import numpy as np
from RetrievingData import DesignDimensions_HE as DesHE
from RetrievingData import Dimensions_HE as DimHE
from RetrievingData import Volumes_HE as VolHE

#parameters of the operation:
kl=0.5
vcl=3.14*10*300
apl=10
fnl=1
########################


#DIMENSIONS FOR EVERY PART
#             Removed Volume        Volume
tubesheet=((((DesHE[4]+6*apl)/2)**2)*np.pi*(DesHE[7]+2*apl))-(((DesHE[4]/2)**2)*np.pi*DesHE[7]), VolHE[2]
flanges=((((DesHE[4]+6*apl)/2)**2)-(((DimHE[0]+6*apl)/2)**2))*np.pi*(DesHE[3]+2*apl)*((DesHE[4]/2)**2-((DimHE[0]/2)**2))*np.pi*DesHE[3], VolHE[7]
removable_cover=((((DesHE[23]+6*apl)/2)**2)*np.pi*(DesHE[24]+2*apl))-(((DesHE[23]/2)**2)*np.pi*DesHE[24]),VolHE[6]


Dim_lathe=[tubesheet,flanges,removable_cover]



LCph=30
MCph=30
UCph=30
DCph=30
STt=10
STh=1

                                                                                      
def CostLathe():
    Cost_of_Lathe=0
    i=0
    while i<len(Dim_lathe):

        Labor_cost_lathe=LCph*((Dim_lathe[i][0]/(kl*vcl*apl*fnl))+STt+STh*Dim_lathe[i][1])

        Material_cost_lathe=MCph*(Dim_lathe[i][0]/(kl*vcl*apl*fnl))

        Utility_cost_lathe=UCph*(Dim_lathe[i][0]/(kl*vcl*apl*fnl))

        Mach_Depreciation_cost_lathe=DCph*((Dim_lathe[i][0]/(kl*vcl*apl*fnl))+STt+STh*Dim_lathe[i][1])
   
        Cost_of_Lathe=Cost_of_Lathe+Labor_cost_lathe+Material_cost_lathe+Utility_cost_lathe+Mach_Depreciation_cost_lathe

        i+=1
    return Cost_of_Lathe
print(CostLathe())
