import time
import pandas as pd
import numpy as np

with open('subset_elemets.txt') as f:
        subset_elements = f.read().split('\n')
    
with open('all_elements.txt') as f:
    all_elements = f.read().split('\n')

def Number_elements(file1,file2):
    """Defined a function named Number_elements.This also contains intersect1d function from numpy module.
       ##parameters
       file1,file2
       
       ##Returns:
       returns the total number of elements present in both the files.    
     """
    start = time.time()

    verified_element = np.intersect1d(np.array(file1), np.array(file2)) 

    print(len(verified_element))
    print(f'Duration: {time.time() - start} seconds')

Number_elements(subset_elements, all_elements)

Method_one(subset_elements, all_elements)

# This is using datastructures

def Method_two(file1,file2):
  """Defined a function named Method_two.This also uses the built in function intersection to find out the elements that are present as common in both the files.
       ##parameters
       file1,file2
       
       ##Returns:
       returns the total number of elements present in both the files.    
     """
    start = time.time()

    verified_element=set(file1).intersection(file2)

    print(len(verified_element))
    print('Duration: {} seconds'.format(time.time() - start))

Method_two(subset_elements, all_elements)
