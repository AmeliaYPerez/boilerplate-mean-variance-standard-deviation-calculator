import numpy as np

def calculate(list):

    #memory reserve for the dictionary
  calculations = {
        
            'mean': [],
            'variance': [],
            'standard deviation': [],
            'max': [],
            'min': [],
            'sum': []

            }

  if not len(list) == 9:
    raise ValueError("List must contain nine numbers.")
    
  matrix = np.array(list).reshape((3,3)) #this is because list is a python lits

  calculations['mean'] = [np.mean(matrix,axis=0).tolist(),np.mean(matrix,axis=1).tolist(),np.mean(matrix)]

  calculations['variance'] =  [np.var(matrix,axis=0).tolist(),np.var(matrix,axis=1).tolist(),np.var(matrix)]

  calculations['standard deviation'] = [np.std(matrix,axis=0).tolist(),np.std(matrix,axis=1).tolist(),np.std(matrix)] 

  calculations['max'] =  [np.max(matrix,axis=0).tolist(),np.max(matrix,axis=1).tolist(),np.max(matrix)]

  calculations['min'] =   [np.min(matrix,axis=0).tolist(),np.min(matrix,axis=1).tolist(),np.min(matrix)]     

  calculations['sum'] =  [np.sum(matrix,axis=0).tolist(),np.sum(matrix,axis=1).tolist(),np.sum(matrix)]

  return calculations
