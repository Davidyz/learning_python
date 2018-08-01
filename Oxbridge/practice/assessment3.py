import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

table = pd.read_csv('skyserver.csv')
rows = table.shape[0]
columns_no = table.shape[1]
table_galaxy = table[table['class'] == 'GALAXY']

def object_type():
    objects = {'GALAXY':0,
               'QSO':0,
               'STAR':0}
    for i in table['class']:
        objects[i] += 1
    for i in objects:
        print('{}:{}'.format(i, objects[i]))

def valid_galaxy():
    temp = table_galaxy[table_galaxy['ra'] <= 180]
    temp = temp[temp['ra'] >= 150]
    temp = temp[temp['dec'] <= 40]
    temp = temp[temp['dec'] >= 10]
    return temp

object_type()
plot_galaxy = valid_galaxy()
plt.colorbar(plt.scatter(plot_galaxy['ra'], plot_galaxy['dec'], c = plot_galaxy['redshift'], s=1))
plt.show()
