import numpy as np 
def find_period(L0, L1):
    #this function calculate and print pendulum period T for lengths from L0 to L1
    #for 1 meter increments
    g = 9.81 # in m/s^2
    for L in range(L0, L1+1, 1):
        T = 2 * np.pi * np.sqrt(L / g)
        print(f"When L = {L:.1f} m, T = {T:.1f} s")
        
    T0 = 2 * np.pi * np.sqrt(L0 / g) #in s
    T1 = 2 * np.pi * np.sqrt(L1 / g) #in s
    return T0,T1
myresult = find_period(2, 10)


