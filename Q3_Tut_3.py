# -*- coding: utf-8 -*-
"""
Created on Mon May  7 06:39:54 2018

@author: Tankiso
"""

import numpy

class Nbody:

#Variable definition
	def __init__(self,masses = 0,xposition = 0, yposition = 0):
		self.masses = masses
		self.xposition = xposition
		self.yposition = yposition
  
#Dictionary entries
	value = {'no. of particles': 10, 'Gravitational constant': 6.67*10**-11}

	def SoftenedPotential(self,m,x,y):
             t = numpy.zeros(len(x))
             Ez = numpy.zeros(len(t))
             g = numpy.ones(len(t))
             E = numpy.zeros(len(t))
             r = ()

             for r in range(0,len(m)):
                 
			for j in range(0,len(x)):    
				t[j] = (((x[r]-x[j])**2 + (y[r]-y[j])**2 +  0.9)**1.5/numpy.sqrt(x[r]-x[j])**2 + (y[r]-y[j])**2)
    				#with softening factor
				if t[j] != 0:
					g[j] = t[j]

			for j in range(0,len(x)):
				Ez[j] = Nbody.value['Gravitational constant']*m[r]*m[j]

			for j in range(0,len(x)):
				if t[j] != 0:
					E[j] = Ez[j]/t[j]
			print (E.sum())

if __name__=="__main__":

        b = Nbody.value['no. of particles']
        p= size=b
        x = numpy.random.randint(0,11,p)
        y = numpy.random.randint(0,11,p)
        m = numpy.random.randint(1,5,p)
        Test = Nbody(m,x,y)


        print ('The masses  ' + repr(Test.masses))
        print ('The x position  ' + repr(Test.xposition))
        print ('The y position  ' + repr(Test.yposition),  "with softened potentials")

        Energy = Test.SoftenedPotential(Test.masses,Test.xposition,Test.yposition)