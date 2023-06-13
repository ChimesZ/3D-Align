import math
import pandas as pd

def eucliDist(a,b):
    return math.sqrt(math.sqrt(sum([(a - b)**2 for (a,b) in zip(a,b)])))

def get_coordinate(path):
    data = np.load(path,allow_pickle=True)
    centers = []
    for cell in data:
        center = cell['center']
        centers.append(center)
    centers = np.asarray(centers)
    type(centers)
    x,y,z = centers[:,0], centers[:,1],centers[:,2]
    return x,y,z

def organizer_init(path:str, title:str): 
    x,y,z = get_coordinate(path)
    organizer = pd.DataFrame(zip(x,y,z))
    organizer.columns = list('xyz')
    organizer[title] = 1
    return organizer 

def organizer_append(organizer: pd.DataFrame, path:str, title:str, thresh=3): 
    x,y,z = get_coordinate(path)
    row, col = organizer.shape
    organizer[title] = 0
    for i in range(len(x)):
        coordinate_new = [x[i],y[i],z[i]]
        mark = 1
        for j in range(row):
            coordinate = list(organizer.iloc[j])
            coordinate = coordinate[0:3]
            if eucliDist(coordinate,coordinate_new) < thresh:
                organizer[title][j] = 1
                mark = 0
                break
        if mark:
            organizer.loc[len(organizer.index)] = [x[i],y[i],z[i]] + [0 for i in range(col-3)] + [1]
    return organizer