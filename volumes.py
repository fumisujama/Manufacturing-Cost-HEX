import math

def volume_shell(Ds,Ls,ts,Dnzh):
    Vs=math.pi*Ls*ts*Ds-2*(math.pi*(Dnzh**2)/4)*ts
    return Vs

def volume_tubes(Lt,Ntp,Np,dte,tt):
    Vt=math.pi*Lt*Ntp*Np*tt*dte
    return Vt

def volume_tubesheets(tss,Dfl,Ntp,Np,dte,Nb,db):
    Vts=2*((math.pi/4)*tss*(Dfl**2-Ntp*Np*(dte**2)-Nb*(db**2)))
    return Vts

def volume_baffles(Db,Ntp,Np,Bc,dte,Nb,tb, Dtr, Ntr):
    Vb = Nb * tb * (
            (math.pi/4) * Db**2
            - (
                (Db**2)/4 * math.acos(1 - Bc/50)
                -(Db/2 - Db*Bc/100) * math.sqrt(
                    (Db**2)*Bc*(1/100 - Bc/5000)
                    )
                )
            -Ntp * Np * ((math.pi/4)*dte**2) * (1-Bc/100)
            -Ntr * ((math.pi/4)*Dtr**2)
            )
    return Vb

def volume_heads(Lh,ts,Ds,Dnzh):
    Vh=2*(math.pi*Lh*ts*Ds-(math.pi*(Dnzh**2)/4)*ts)
    return Vh

def volume_nozzles(Lnzh,tnzh,Dnzh):
    Vnzh=4*math.pi*Lnzh*tnzh*Dnzh
    return Vnzh

def volume_removable_cover(Dfl,tfl,Nbolts,dbolts):
    Vrc=2*(math.pi*((Dfl**2)/4)*tfl)-Nbolts*tfl*math.pi*((dbolts**2)/4)
    return Vrc

def volume_flange(Ds,Dfl,tfl):
    Vfl=4*math.pi*(((Dfl**2)/4)-((Ds**2)/4))*tfl
    return Vfl

def volume_pass_partitions(number_passes,Ds,tpp,Lh):
    Vpp=(Number_passes-1)*Ds*Lh*tpp
    return Vpp

def volume_tie_rods(Ntr,Dtr,length_tie_rods):
    Vtr=Ntr*((math.pi*(Dtr**2))/4)*length_tie_rods
    return Vtr

#def MassOfExchanger(rs):
    #global Mex
    #Mex=rs*(Vs+Vt+Vts+Vh+Vnzh+Vnzs+Vb+Vfl+Vrc+Vpp+Vpp+Vtr)
