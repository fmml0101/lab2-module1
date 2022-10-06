import pandas as pd
new_df= pd.read_csv("D:/sheetss.csv",encoding='unicode_escape')
new_df.columns
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D


sns.set(style = "darkgrid")

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x = new_df['loss'][:50]
y = new_df['profit'][:50]
z = new_df['net'][:50]

ax.set_xlabel("total_losss")
ax.set_ylabel("total_profit")
ax.set_zlabel("net_value")

ax.scatter(x, y, z)

plt.show()

