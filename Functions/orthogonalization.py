# Math
import math as mt
import numpy as np

class dataset:
    def __init__(self, array):
        self.array = np.delete(array, np.s_[0], axis=1)  
        self.x = self.array[:,0]
        self.y = self.array[:,1]
        self.z = self.array[:,2]
        self.w = self.array[:,3] 

## CP1
# Centerline
def CP1(data):

    # Convert the array into list
    lista = data.tolist()
    # New list with onyl coordinates x,y,z
    center_line = [(lista[i][0],lista[i][1],lista[i][2]+8000) for i in range(len(lista))]
    return center_line


## CP2
# Boundaries of channel
def CP2(x,y,z,w,data):
    "These parameters define the channel. This function apply the orthogonalization,"
    "in order to honor the width at each deviation"
    # Defining the boundary list
    upper_boundary = []
    # Loop for creating the list of points
    for i in range(1, len(x)-1):
        # X-coordinates
        x2 = x[i+1]
        x1 = x[i]
        x0 = x[i-1]
        # Y-coordinates
        y2 = y[i+1]
        y1 = y[i]
        y0 = y[i-1]
        # Width
        w0 = w[i]
        # Ortoghonalization
        distance = [x2-x0, y2-y0]
        norm = mt.sqrt(distance[0]**2 + distance[1]**2)
        direction = [distance[0]/norm, distance[1]/norm]
        # Up and down boundary for one point
        ub = [x1-direction[1]*w0/2, y1+direction[0]*w0/2]
        # Add the whole values in the list
        upper_boundary += [ub]
    # Ortoghonalization for first and last point
    distance = [x[1]-x[0], y[1]-y[0]-5]
    norm = mt.sqrt(distance[0]**2 + distance[1]**2)
    direction = [distance[0]/norm, distance[1]/norm]
    distanca = [x[-1]-x[-2], y[-1]-y[-2]+5]
    norma = mt.sqrt(distanca[0]**2 + distanca[1]**2)
    directione = [distanca[0]/norma, distanca[1]/norma]
    # Up and down boundary for one point
    ub_first = [x[0]-direction[1]*w0/2, y[0]+direction[0]*w0/2]
    ub_last  = [x[-1]-directione[1]*w0/2, y[-1]+directione[0]*w0/2]
    # Build the boundary of the channel
    right_channel = [ub_first] + upper_boundary + [ub_last]
    # Splitting the boundary only to plot easly
    # Upper boundary list for x,y
    ubx = [right_channel[i][0] for i in range(len(right_channel))]
    uby = [right_channel[i][1] for i in range(len(right_channel))]
    # Convert the array into list
    lista = data.tolist()
    # New list with onyl coordinates x,y,z
    center_line = [(lista[i][0],lista[i][1],lista[i][2]+8000) for i in range(len(lista))]
    # Left and Right
    right_bbox  = [(ubx[i],uby[i],center_line[i][2]+20) for i in range(len(center_line))]
    return right_bbox


## CP4
# Middle right point
def CP4(x,y,z,w,data):
    "These parameters define the channel. This function apply the orthogonalization,"
    "in order to honor the width at each deviation"
    # Defining the boundary list
    upper_boundary = []
    # Loop for creating the list of points
    for i in range(1, len(x)-1):
        # X-coordinates
        x2 = x[i+1]
        x1 = x[i]
        x0 = x[i-1]
        # Y-coordinates
        y2 = y[i+1]
        y1 = y[i]
        y0 = y[i-1]
        # Width
        w0 = w[i]
        # Ortoghonalization
        distance = [x2-x0, y2-y0]
        norm = mt.sqrt(distance[0]**2 + distance[1]**2)
        direction = [distance[0]/norm, distance[1]/norm]
        # Up and down boundary for one point
        ub = [x1-direction[1]*w0/4, y1+direction[0]*w0/4]
        # Add the whole values in the list
        upper_boundary += [ub]      
    # Ortoghonalization for first and last point
    distance = [x[1]-x[0], y[1]-y[0]-5]
    norm = mt.sqrt(distance[0]**2 + distance[1]**2)
    direction = [distance[0]/norm, distance[1]/norm]
    distanca = [x[-1]-x[-2], y[-1]-y[-2]+5]
    norma = mt.sqrt(distanca[0]**2 + distanca[1]**2)
    directione = [distanca[0]/norma, distanca[1]/norma]
    # Up and down boundary for one point
    ub_first = [x[0]-direction[1]*w0/4, y[0]+direction[0]*w0/4]
    ub_last  = [x[-1]-directione[1]*w0/4, y[-1]+directione[0]*w0/4]  
    # Build the boundary of the channel
    right_channel = [ub_first] + upper_boundary + [ub_last]
    # Splitting the boundary only to plot easly
    # Upper boundary list for x,y
    ubx = [right_channel[i][0] for i in range(len(right_channel))]
    uby = [right_channel[i][1] for i in range(len(right_channel))]    
    # Convert the array into list
    lista = data.tolist()
    # New list with onyl coordinates x,y,z
    center_line = [(lista[i][0],lista[i][1],lista[i][2]+8000) for i in range(len(lista))]
    # Left and Right
    middle_right  = [(ubx[i],uby[i],center_line[i][2]+5) for i in range(len(center_line))]    
    return middle_right


## CP5
# Middle left point
def CP5(x,y,z,w,data):
    "These parameters define the channel. This function apply the orthogonalization,"
    "in order to honor the width at each deviation"  
    # Defining the boundary list
    lower_boundary = []
    # Loop for creating the list of points
    for i in range(1, len(x)-1):
        # X-coordinates
        x2 = x[i+1]
        x1 = x[i]
        x0 = x[i-1]
        # Y-coordinates
        y2 = y[i+1]
        y1 = y[i]
        y0 = y[i-1]
        # Width
        w0 = w[i]
        # Ortoghonalization
        distance = [x2-x0, y2-y0]
        norm = mt.sqrt(distance[0]**2 + distance[1]**2)
        direction = [distance[0]/norm, distance[1]/norm]
        # Up and down boundary for one point
        lb = [x1+direction[1]*w0/4, y1-direction[0]*w0/4]
        # Add the whole values in the list
        lower_boundary += [lb]        
    # Ortoghonalization for first and last point
    distance = [x[1]-x[0], y[1]-y[0]-5]
    norm = mt.sqrt(distance[0]**2 + distance[1]**2)
    direction = [distance[0]/norm, distance[1]/norm]
    distanca = [x[-1]-x[-2], y[-1]-y[-2]+5]
    norma = mt.sqrt(distanca[0]**2 + distanca[1]**2)
    directione = [distanca[0]/norma, distanca[1]/norma]
    # Up and down boundary for one point
    lb_first = [x[0]+direction[1]*w0/4, y[0]-direction[0]*w0/4]
    lb_last = [x[-1]+directione[1]*w0/4, y[-1]-directione[0]*w0/4]
    # Build the boundary of the channel
    left_channel = [lb_first] + lower_boundary + [lb_last]
    # Splitting the boundary only to plot easly
    # Lower boundary list for x,y
    lbx = [left_channel[i][0] for i in range(len(left_channel))]
    lby = [left_channel[i][1] for i in range(len(left_channel))]    
    # Convert the array into list
    lista = data.tolist()
    # New list with onyl coordinates x,y,z
    center_line = [(lista[i][0],lista[i][1],lista[i][2]+8000) for i in range(len(lista))]
    # Left and Right
    middle_left  = [(lbx[i],lby[i],center_line[i][2]+5) for i in range(len(center_line))]    
    return middle_left

## CP3
# Boundary of channel
def CP3(x,y,z,w,data):
    "These parameters define the channel. This function apply the orthogonalization,"
    "in order to honor the width at each deviation"   
    # Defining the boundary list
    lower_boundary = []
    # Loop for creating the list of points
    for i in range(1, len(x)-1):
        # X-coordinates
        x2 = x[i+1]
        x1 = x[i]
        x0 = x[i-1]
        # Y-coordinates
        y2 = y[i+1]
        y1 = y[i]
        y0 = y[i-1]
        # Width
        w0 = w[i]
        # Ortoghonalization
        distance = [x2-x0, y2-y0]
        norm = mt.sqrt(distance[0]**2 + distance[1]**2)
        direction = [distance[0]/norm, distance[1]/norm]
        # Up and down boundary for one point
        lb = [x1+direction[1]*w0/2, y1-direction[0]*w0/2]
        # Add the whole values in the list
        lower_boundary += [lb]      
    # Ortoghonalization for first and last point
    distance = [x[1]-x[0], y[1]-y[0]-5]
    norm = mt.sqrt(distance[0]**2 + distance[1]**2)
    direction = [distance[0]/norm, distance[1]/norm]
    distanca = [x[-1]-x[-2], y[-1]-y[-2]+5]
    norma = mt.sqrt(distanca[0]**2 + distanca[1]**2)
    directione = [distanca[0]/norma, distanca[1]/norma]
    # Up and down boundary for one point
    lb_first = [x[0]+direction[1]*w0/2, y[0]-direction[0]*w0/2]
    lb_last = [x[-1]+directione[1]*w0/2, y[-1]-directione[0]*w0/2]
    # Build the boundary of the channel
    left_channel = [lb_first] + lower_boundary + [lb_last]
    # Lower boundary list for x,y
    lbx = [left_channel[i][0] for i in range(len(left_channel))]
    lby = [left_channel[i][1] for i in range(len(left_channel))]
    # Convert the array into list
    lista = data.tolist()
    # New list with onyl coordinates x,y,z
    center_line = [(lista[i][0],lista[i][1],lista[i][2]+8000) for i in range(len(lista))]
    # Left and Right
    left_bbox = [(lbx[i],lby[i],center_line[i][2]+20) for i in range(len(center_line))]
    return left_bbox

def controlpoints(x,y,z,w,array):
    # Control points
    centerline = CP1(array)
    points_CP2 = CP2(x,y,z,w,array)
    points_CP3 = CP3(x,y,z,w,array)
    points_CP4 = CP4(x,y,z,w,array)
    points_CP5 = CP5(x,y,z,w,array)
    # Data point of channels
    global_channel = points_CP2 + points_CP4 + centerline + points_CP5 + points_CP3
    return global_channel