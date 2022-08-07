
### Superpixel Hierarchical Clustering algorithm (SPHC)
## Method and Code for merging Superpixels created by Paul Thompson (Please credit if you use this code)
# The algorithm takes image superpixels created by the skimage SLIC function and merges neighors in order of
# color similarity (using euclidean distance).

#References:
#1. http://www.kev-smith.com/papers/SLIC_Superpixels.pdf
#2. http://www.pyimagesearch.com/2014/07/28/a-slic-superpixel-tutorial-using-python/

#####INSTRUCTIONS###################################################################################
### To use:
### 1. Change the parameters below
### 2. Change image path. This was only tested with jpg's.
### 3. Run program

imagePath = 'conan2.jpg'

#SLIC Parameters:
numSegments = 500  # How many superpixels to start with - input for SLIC function
Sigma = 4 # This parameter controls superpixel shape. Higher values make superpixels more square.

#SPHC Parameters:
segmentsToMerge = 50 # How many superpixels to merge based on color similarity
distance_limit = .6  # Limits which segments get merged based on their difference in average color
####################################################################################################

import matplotlib.pyplot as plt, argparse, numpy as np, math, sys, copy
from skimage.segmentation import slic, mark_boundaries
from skimage.util import img_as_float
from skimage import io
from collections import defaultdict

def initiateSegmentAttributes(segm_grid, image):
    '''
    Each segment formed by sklearn's SLIC function is assigned a dictionary of attributes for efficiency.
    :param segm_grid: Each pixel has been identified with a segment identifier by the skimage SLIC function
    :param image: Each pixel has R, B, and G value associated with it
    :return: Dictionary of dictionaries of attributes for each segment
    '''
    def initialSegmAttr():
        return {'neighbors': set(), 'R': [], 'G': [], 'B': [], 'coord': set(),
                         'R_avg': 0.0, 'G_avg': 0.0, 'B_avg': 0.0}
    segm_dict = defaultdict(initialSegmAttr)

    for i in range(len(segm_grid)):
        for j in range(len(segm_grid[i])):
            if j <> len(segm_grid[i]) - 1 and segm_grid[i][j] <> segm_grid[i][j+1]:
                segm_dict[segm_grid[i][j]]['neighbors'].add(segm_grid[i][j+1])
                segm_dict[segm_grid[i][j+1]]['neighbors'].add(segm_grid[i][j])
            if i <> len(segm_grid) - 1 and segm_grid[i][j] <> segm_grid[i+1][j]:
                segm_dict[segm_grid[i][j]]['neighbors'].add(segm_grid[i+1][j])
                segm_dict[segm_grid[i+1][j]]['neighbors'].add(segm_grid[i][j])
            segm_dict[segm_grid[i][j]]['R'].append(image[i][j][0])
            segm_dict[segm_grid[i][j]]['B'].append(image[i][j][1])
            segm_dict[segm_grid[i][j]]['G'].append(image[i][j][2])
            segm_dict[segm_grid[i][j]]['coord'].add((i,j))
    return segm_dict

def getNearestNeighbors(segm_dict):
    '''
    Calculates the average R, B, and G values for each segment. Then finds the two neighboring segments with
    the smallest euclidean distance (for the three dimensions of R, B, and G).
    :param segm_dict: dictionary of dictionaries of segment attributes
    :return: segment pair with smallest color euclidean distance; distance value
    '''
    for k, v in segm_dict.items():
        v['R_avg'] = sum(v['R'])/len(v['R'])
        v['B_avg'] = sum(v['B'])/len(v['B'])
        v['G_avg'] = sum(v['R'])/len(v['G'])
    neighbor_pairs = set()