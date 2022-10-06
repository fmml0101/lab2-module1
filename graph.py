mrp= new_df['mrp']
qty= new_df['qty']
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
fig = plt.figure()
myaxes= fig.add_axes([0.1,0.1,1.6,1.6])
myaxes.plot(qty,mrp)

