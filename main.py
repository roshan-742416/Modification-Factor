# Modification factor for tension steel
# Units in N/mm2
import pandas as pd
from scipy.interpolate import interp2d


def modification_factor():
    df = pd.read_csv('modification_factor.csv')
    df.index = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0]
    x = df.columns
    y = df.index
    z = df.values
    f = interp2d(x, y, z, kind='linear')
    fs = float(input("Enter value of fs:"))
    percent_steel = float(input("Enter value of percentage steel:"))
    return f(fs, percent_steel)


print(modification_factor())
