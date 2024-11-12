#Johnson Lab Rsource code - author: Mary Smith

#import packages
import numpy as np
import matplotlib.pyplot as plt

#importing latex fonts
plt.rc('text',usetex=True)
plt.rc('font', **{'family':'serif','serif':['Times New Roman']})

#%% - define constants

kB=1.380649e-23 #Boltzmann constant
T=296.65 #room temperature
vn=4e-9 #voltage noise density from specs
inn=12e-15 #current noise density from specs

#%% - define function to be maximized

def f(Rsource):
    f=(4*kB*T*Rsource)/(vn**(2)+inn**(2)*Rsource**2)
    return f

#%% - find solutions

#list of values to pass through function
x=np.linspace(0,600000,num=80000000)

#pass the function through the list and saving values
solns=[]
for val in x:
    solns.append(f(val))

#visualizing the function
plt.plot(x,solns)
plt.xlabel(r'$R_{source}$')
plt.ylabel(r'Ratio Value')
plt.title(r'Finding $R_{source}$ at Maximum of Ratio')
plt.show()

#%% - finding the value of Rsource for the maximum value of the ratio

#maximum value of the ratio
fmax=max(solns)

#find index of maximum value
pos=solns.index(fmax)

#find Rsource value at ratio maximum
Rval=x[pos]
print(Rval)