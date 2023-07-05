# Superpixel Hierarchical Clustering Algorithm (SPHC) For Professional Image Segmentation\
\
This is a comprehensive project that uses Superpixels for initial image segmenting. The algorithm finds it genesis in the paucity of online resources that discuss image segmentation algorithms utilizing superpixels. An interesting observation that neighboring superpixels often share color similarities and these can be exploited to define boundaries led to the formulation of this algorithm.\
\
The algorithm uses two main inputs: an RGB pixel grid that represents an image and a grid of segments from the sklearn SLIC superpixel-creating algorithm.\
\
After segment assignment, the superpixel hierarchical clus