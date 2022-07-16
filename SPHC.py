
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