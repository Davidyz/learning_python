import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpt
from scipy.optimize import curve_fit
import pylab

print("\n\nThe graphs will be saved in the working directory instead of simply showing!!!\n\n")
# Q1
table = pd.read_csv('skyserver.csv')
rows = table.shape[0]
columns_no = table.shape[1]

# Q2
def object_type():
    objects = {'GALAXY':0,
               'QSO':0,
               'STAR':0}
    for i in table['class']:
        objects[i] += 1
    for i in objects:
        print('{}:{}'.format(i, objects[i]))
    print('\n')

object_type()

# Q3
table_galaxy = table[table['class'] == 'GALAXY']

# Q4
def plot_galaxy():
    temp = table_galaxy[table_galaxy['ra'] <= 180]
    temp = temp[temp['ra'] >= 150]
    temp = temp[temp['dec'] >= 10]
    temp = temp[temp['dec'] <= 40]
    return temp

ploted_galaxy = plot_galaxy()

plt.scatter(ploted_galaxy['ra'],
            ploted_galaxy['dec'],
            c=ploted_galaxy['redshift'],
            s=1)

plt.colorbar()
plt.title('The Positions of Galaxies')
plt.xlabel('RA(degree)')
plt.ylabel('DEC(degree)')
plt.savefig('Q4.png')
plt.hold(False)

# Q5
table_galaxy['color'] = table_galaxy['u'] - table_galaxy['r']
plt.hist(table_galaxy['color'],
         bins = 1000,
         rwidth=1,
         range=(-0.5, 4))

plt.title('The Distribution of the Color of Galaxies, ie. u - r')
plt.xlabel('u - r(magnitude)')
plt.ylabel('Counts')
plt.savefig('Q5.png')
plt.hold(True)
plt.show()

# Q6
data = table_galaxy['color']
y, x = pylab.hist(data, 1000, alpha = .3, label = 'counts')[:2]
x = (x[1:] + x[:-1]) / 2

def gauss(x,mu,sigma,A):
    return A * pylab.exp(-(x-mu)**2/2/sigma**2)

def bimodal(x,mu1,sigma1,A1,mu2,sigma2,A2):
    return gauss(x,mu1,sigma1,A1)+gauss(x,mu2,sigma2,A2)

expected = (1, .2, 250, 2, .2, 125)
params, cov = curve_fit(bimodal, x, y, expected)
sigma = np.sqrt(pylab.diag(cov))

plt.plot(x,
         bimodal(x,*params),
         color='red',
         lw=1,
         label='model')
plt.legend()
plt.title('Attempt to approximate the curve')
plt.savefig('Q6.png')
plt.show()