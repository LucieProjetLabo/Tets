#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import module for NURBS (geomdl)
from geomdl import BSpline
from geomdl import utilities

# Numpy
import numpy as np

def Bspline(points):
    "We use NURBS-Python to generate the channel surface St"
    "St is in parametric form and generates a set of evaluation points"
    
    # Create a BSpline surface instance (Bezier surface)
    surf = BSpline.Surface()

    # Set up the Bezier surface
    # Define the degree of u,v
    surf.degree_u = 3
    surf.degree_v = 3
    control_points = points

    # 2D control points dimension for u,v
    u = 5                  # the five points are displaced along quadratic form
    v = int(len(points)/u) # this value can change all the time due to the number of centerline points. 
                           # for that reason is resonable to explicit that number like that

    # Define the size and knotvector of u,v vector
    surf.set_ctrlpts(control_points, u, v)
    surf.knotvector_u = utilities.generate_knot_vector(surf.degree_u, surf.ctrlpts_size_u)
    surf.knotvector_v = utilities.generate_knot_vector(surf.degree_v, surf.ctrlpts_size_v)

    # Set sample size
    surf.delta_v = 0.0005 # Prof.Caumon chose this value
    surf.delta_u = 0.005  # Prof.Caumon chose this value

    # Evaluate surface
    surf.evaluate()

    # Visualize data and evaluated points together
    evalpts = np.array(surf.evalpts)
        
    return evalpts

def Bsplinectp(points):
    "We use NURBS-Python to generate the channel surface St"
    "St is in parametric form and generates a set of evaluation points"
    
    # Create a BSpline surface instance (Bezier surface)
    surf = BSpline.Surface()

    # Set up the Bezier surface
    # Define the degree of u,v
    surf.degree_u = 3
    surf.degree_v = 3
    control_points = points
    
    return control_points

