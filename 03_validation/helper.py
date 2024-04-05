import numpy as np
from scipy.optimize import curve_fit

def fit_bm(vol, en):
    a, b, c = np.polyfit(vol, en, 2)
    V0 = -b/(2*a)
    E0 = a*V0**2 + b*V0 + c
    B0 = 2*a*V0
    Bp = 4.0
    popt, pcov = curve_fit(birch_murnaghan_eval, vol, en, p0=[V0, E0, B0, Bp])
    return popt
    
def birch_murnaghan_eval(vol, V0, E0, B0, Bp):    
    eta = (vol/V0)**(1.0/3.0)
    E = E0 + 9.0*B0*V0/16.0 * (eta**2-1.0)**2 * (6.0 + Bp*(eta**2-1.0) - 4.0*eta**2)
    return E

def birch_murnaghan(df, compound, potential=None):
    if potential is None:
        dfs = df.loc[df['compound']==compound]
    else:
        dfs = df.loc[(df["potential"]==potential) & (df["compound"]==compound)]
    if len(dfs.volume.values) == 1:
        vol = dfs.volume.values[0]
        en = dfs.energy_per_atom.values[0]
    else:
        vol = dfs.volume.values
        en = dfs.energy_per_atom.values
    popt = fit_bm(vol, en)
    volfit = np.linspace(min(vol), max(vol), 10000)
    enfit = birch_murnaghan_eval(volfit, popt[0], popt[1], popt[2], popt[3])
    return volfit, enfit    