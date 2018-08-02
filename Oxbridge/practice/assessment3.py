import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpt
from scipy.optimize import curve_fit
import pylab

print("\n\nThe graphs will be saved in the working directory as well as showing!!!\n\n")
############################# Q1 ###########################
table = pd.read_csv('skyserver.csv')
rows = table.shape[0]
columns_no = table.shape[1]

############################# Q2 ###########################
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

############################# Q3 ############################
table_galaxy = table[table['class'] == 'GALAXY']
print('The number of GALAXY is: {}\n'.format(table_galaxy.shape[0]))

############################# Q4 ############################
plt.scatter(table_galaxy['ra'],
            table_galaxy['dec'],
            c=table_galaxy['redshift'],
            s=1)

plt.xlim(150, 180)
plt.ylim(10, 40)
plt.colorbar()
plt.title('The Positions of Galaxies')
plt.xlabel('RA(degree)')
plt.ylabel('DEC(degree)')
plt.savefig('Q4.png')
plt.show()

############################# Q5 ##############################
table_galaxy['color'] = table_galaxy['u'] - table_galaxy['r']

plt.hist(table_galaxy['color'],
         bins = 1000)
plt.xlim(0, 4)

def names():
    plt.title('The Distribution of the Color of Galaxies, ie. u - r')
    plt.xlabel('u - r(magnitude)')
    plt.ylabel('Counts')

names()
plt.savefig('Q5.png')
plt.show()

############################# Q6 ###############################
y, x, _ = plt.hist(table_galaxy['u'] - table_galaxy['r'], bins = 1000, alpha = 1, label = 'counts')
x = (x[1:] + x[:-1]) / 2
mean1, mean2 = 0, 0

def gauss(x, mu, sigma, A):
    return A * pylab.exp(-(x - mu) ** 2 / 2 / sigma ** 2)

def bimodal(x, mu1, sigma1, A1, mu2, sigma2, A2):
    global mean1, mean2
    mean1, mean2 = mu1, mu2
    return gauss(x, mu1, sigma1, A1) + gauss(x, mu2, sigma2, A2)

expected = (1, .2, 250, 2, .2, 125)
params, cov = curve_fit(bimodal, x, y, expected)
sigma = np.sqrt(pylab.diag(cov))
plt.xlim(0, 4)

plt.plot(x,
         bimodal(x,*params),
         color='red',
         lw=1,
         label='model')

names()
plt.savefig('Q6.png')
plt.show()

############################## Q7 ################################
print('\nThe values of colors are {} and {}.'.format(mean1, mean2))
