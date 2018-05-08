# -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:37:32 2018

@author: Tankiso
"""

import numpy

class Complex:
    def __init__(self,r=0,i=0):
        self.r=r
        self.i=i
        
        #Absolute value
    def Absolute(self):
        return numpy.sqrt(self.r**2+self.i**2)
        
        #Addition
    def Addition(self,y):
        rb = self.r + y.r
        ib = self.i +  y.i
        return Complex(rb,ib)
        
        #Subtraction
    def Subtraction(self,x):
        ra = self.r - x.r
        ia = self.i - x.i
        return Complex(ra,ia)
                
        #Multiplication 
    def Multiplication(self,z):
        rc = (self.r*z.r)-(self.i*z.i)
        ic = (self.r*z.i)+(z.r*self.i)
        return Complex(rc,ic)
        
        #Division
    def Division(self,d):
        rg = ((self.r*1.0*d.r)+(self.i*d.i))/(d.r**2+d.i**2)
        ig = ((self.i*1.0*d.r)-(self.r*d.i))/(d.r**2+d.i**2)
        return Complex(rg,ig)

a = Complex(5,2)
b = Complex(3,4)

c = a.Addition(b)
d = a.Subtraction(b)
e = a.Multiplication(b)
f = a.Division(b)

print('c = ',c.r,c.i)
print('d = ',d.r,d.i)
print('e = ',e.r,e.i)
print('f = ',f.r,f.i)