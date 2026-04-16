
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

def animate(i):

    data = pd.read_csv('data/data_experiment.csv')

    #dtypes
    data['click'] = data['click'].astype(int)
    data['visit'] = data['visit'].astype(int)

    x1 = np.arange(len(data.loc[data['group'] == 'control']))
    x2 = np.arange(len(data.loc[data['group'] == 'treatment']))
    y1 = data.loc[data['group'] == 'control', 'click'].cumsum() / data.loc[data['group'] == 'control', 'visit'].cumsum()
    y2 = data.loc[data['group'] == 'treatment', 'click'].cumsum() / data.loc[data['group'] == 'treatment', 'visit'].cumsum()

    plt.cla()
    plt.plot(x1, y1, label='Control Group')
    plt.plot(x2, y2, label='Treatment Group')
    plt.legend(loc='upper right')

ani = FuncAnimation( plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()