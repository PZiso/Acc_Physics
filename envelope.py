import numpy as np
import matplotlib.pylab as plt
import pandas as pd

from scipy.signal import savgol_filter

def orbit(beta,phi,phi0=0,emit=1e-5):

    sz = np.sqrt(emit*beta)
    z = sz * np.cos(phi+phi0)
    
    return z

optics = pd.read_csv('ANKA_optics_simple.csv')

rang = np.linspace(0,2*np.pi,45) # initial conditions
plt.figure(figsize = (12,8))

beam = np.empty((len(rang),len(optics.index)))

for k,phi0 in enumerate(rang):
    z = orbit(beta = optics['betx'], phi = optics['phix'],phi0 = phi0)
    beam[k,:] = 100*savgol_filter(z, 51, 3)

plt.plot(beam.T, color = 'royalblue')
plt.plot(beam.T[:,0], color = 'royalblue',label = 'Orbit')
ids = np.argmax(beam,0)
plt.plot(np.max(beam,0),'navy',linewidth = 4)
plt.plot(np.min(beam,0),'navy', linewidth = 4, label = 'Envelope')


plt.xlabel('s [m]')
plt.ylabel('x [mm]')
plt.xlim(10,192)
plt.legend()
plt.show()