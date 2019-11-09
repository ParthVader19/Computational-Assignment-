import numpy as np


def machineAcc(e,floatType="unspecified"):
    
    if floatType=="single":
        e=np.single(e)
        while np.single(1.0)+e > np.single(1.0):
            e=e*np.single(0.5)
        return np.single(2.0)*e
    elif floatType=="double":
        e=np.double(e)
        while np.double(1.0)+e > np.double(1.0):
            e=e*np.double(0.5)
        return np.double(2.0)*e
    elif floatType=="extended":
        e=np.longdouble(e)
        while np.longdouble(1.0)+e > np.longdouble(1.0):
            e=e*np.longdouble(0.5)
        return np.longdouble(2.0)*e
    elif floatType=="unspecified":
        while 1.0+e > 1.0:
            e=e*0.5
        return 2.0*e
        
    

e=machineAcc(1.0)

print("The machine accuracy for:")
print("a) unspecified float type is",e)


e_single=machineAcc(1.0,floatType="single")
print("b) single precision floating point is:",e_single)
e_double=machineAcc(1.0,floatType="double")
print("b) double precision floating point is",e_double)
e_extended=machineAcc(1.0,floatType="extended")
print("b) extended precision floating point is",e_extended)



