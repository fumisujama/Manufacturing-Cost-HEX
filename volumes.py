import math

def volume_shell(Ds,Ls,ts,Dnzs):
    Ds=float(Ds.value)
    Ls=float(Ls.value)
    Vs=(math.pi*Ls*ts*Ds-2*(math.pi*(Dnzs**2)/4)*ts)/1000000000
    print(f"\n ############# \n Volume of shell: {Vs} \n ############")
    return Vs

def volume_tubes(Lt,Ntp,Np,dte,tt):
    Ntp=float(Ntp.value)
    Np=float(Np.value)
    dte=float(dte.value)
    Vt=(math.pi*Lt*Ntp*Np*tt*dte)/1000000000
    print(f"\n ############# \n Volume of tubes: {Vt} \n ############")
    return Vt

def volume_tubesheets(tubesheets_thickness,diameter_tubesheets,Ntp,Np,dte,Nb,db):
    Ntp=float(Ntp.value)
    Np=float(Np.value)
    dte=float(dte.value)
    Vts=(math.pi/2)*tubesheets_thickness*((diameter_tubesheets**2)-(Ntp*Np*(dte**2))-(Nb*(db**2)))/1000000000
    print(f"\n ############# \n Volume of tubesheets: {Vts} \n ############")
    return Vts

def volume_baffles(Db,Ntp,Np,Bc,dte,Nb,tb, Dtr, Ntr):
    Ntp=float(Ntp.value)
    Np=float(Np.value)
    Nb=float(Nb.value)
    dte=float(dte.value)
    Bc=float(Bc.value)
    Vb = (Nb * tb * (
            (math.pi/4) * Db**2
            - (
                (Db**2)/4 * math.acos(1 - Bc/50)
                -(Db/2 - Db*Bc/100) * math.sqrt(
                    (Db**2)*Bc*(1/100 - Bc/5000)
                    )
                )
            -Ntp * Np * ((math.pi/4)*dte**2) * (1-Bc/100)
            -Ntr * ((math.pi/4)*Dtr**2)
            ))/1000000000
    print(f"\n ############# \n Volume of baffles: {Vb} \n ############")
    return Vb

def volume_heads(Lh,ts,Ds,Dnzt):
    Ds=float(Ds.value)

    Vh=(2*(math.pi*Lh*ts*Ds-(math.pi*(Dnzt**2)/4)*ts))/1000000000
    print(f"\n ############# \n Volume of heads: {Vh} \n ############")
    return Vh

def volume_shell_side_nozzles(Lnzs,tnzs,Dnzs):
    Vnzs=4*math.pi*Lnzs*tnzs*Dnzs/1000000000
    print(f"\n ############# \n Volume of shell side nozzles: {Vnzs} \n ############")
    return Vnzs

def volume_tubes_side_nozzles(Lnzt,tnzt,Dnzt):
    Vnzt=4*math.pi*Lnzt*tnzt*Dnzt/1000000000
    print(f"\n ############# \n Volume of tube side nozzles: {Vnzt} \n ############")
    return Vnzt

def volume_removable_cover(diameter_removable_covers,thickness_removable_covers,Nbolts,dbolts):
    Vrc=2*thickness_removable_covers*((math.pi/4)*(diameter_removable_covers**2)-Nbolts*(math.pi/4)*(dbolts**2))/1000000000
    print(f"\n ############# \n Volume of removable covers: {Vrc} \n ############")
    return Vrc

def volume_flange(Ds, ts, Dfl,tfl):
    Ds=float(Ds.value)

    Vfl=4*math.pi*(((Dfl**2)/4)-(((Ds+2*ts)**2)/4))*tfl/1000000000
    print(f"\n ############# \n Volume of flange: {Vfl} \n ############")
    return Vfl

def volume_pass_partitions(number_passes,Ds,tpp,Lh):
    Ds=float(Ds.value)
    number_passes = float(number_passes.value)
    Vpp=(number_passes-1)*Ds*Lh*tpp/1000000000
    print(f"\n ############# \n Volume of pass partitions: {Vpp} \n ############")
    return Vpp

def volume_tie_rods(Ntr,Dtr,length_tie_rods):
    Vtr=Ntr*((math.pi*(Dtr**2))/4)*length_tie_rods/1000000000
    print(f"\n ############# \n Volume of tie rods: {Vtr} \n ############")
    return Vtr

#def MassOfExchanger(rs):
    #global Mex
    #Mex=rs*(Vs+Vt+Vts+Vh+Vnzh+Vnzs+Vb+Vfl+Vrc+Vpp+Vpp+Vtr)
