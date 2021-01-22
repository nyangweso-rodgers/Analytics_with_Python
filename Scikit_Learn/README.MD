# Introducing Scikit - Learn
There are several Python libraries that provide solid implementations of a range of machine learning algorithms. One of the best known is __Scikit-Learn__, a package that provides efficient versions of a large number of common algorithms. __Scikit-Learn__ is characterized by a _clean_, _uniform_, and _streamlined API_, as well as by very useful and complete online documentation. A benefit of this uniformity is that once you understand the basic use and syntax of Scikit-Learn for one type of model, switching to a new model or algorithm is very straightforward.

## Scikit-Learn’s Estimator API
The __Scikit-Learn__ API is designed with the following guiding principles in mind, as outlined in the _Scikit-Learn_ API paper:

## 1. Consistency
All objects share a common interface drawn from a limited set of methods, with consistent documentation.
## 2. Inspection
All specified parameter values are exposed as public attributes.
## 3. Limited object hierarchy
Only algorithms are represented by Python classes; datasets are represented in standard formats (NumPy arrays,Pandas DataFrames, SciPy sparse matrices) and parameter names use standard Python strings.
## 4. Composition
Many machine learning tasks can be expressed as sequences of more fundamental algorithms, and Scikit-Learn makes use of this wherever possible.
## 5. Sensible defaults
When models require user-specified parameters, the library defines an appropriate default value.

In practice, these principles make Scikit-Learn very easy to use, once the basic principles are understood. Every machine learning algorithm in Scikit-Learn is implemented via the Estimator API, which provides a consistent interface for a wide range of machine learning applications.

## Basics of the API
Most commonly, the steps in using the __Scikit-Learn estimator API__ are as follows:
1. Choose a class of model by importing the appropriate estimator class from __Scikit-Learn__.
2. Choose model __hyperparameters__ by instantiating this class with desired values.
3. Arrange data into a _features matrix_ and _target vector_.
4. __Fit__ the model to your data by calling the__ fit()__ method of the model instance.
5. Apply the model to new data:

• For __supervised learning__, often we _predict labels_ for unknown data using the ___predict()__ method.

• For __unsupervised learning__, we often transform or infer properties of the data using the __transform()__ or __predict()__ method.

## K-Means Clustering
__k-means__ clustering is a method of __vector quantization__ that aims to _partition n observations into k clusters_ in which each observation belongs to the cluster with the nearest mean (__cluster centers__ or __cluster centroid__), serving as a prototype of the cluster. This results in a partitioning of the data space into __Voronoi cells__. k-means clustering minimizes within-cluster variances (squared Euclidean distances), but not regular Euclidean distances.

In __clustering__x, we do not have a target to predict. We look at the data and then try to club similar observations and form different groups. Hence it is an unsupervised learning problem.

### Properties of Clusters
* All the data points in a cluster should be similar to each other
* The data points from different clusters should be as different as possible

### Applications of Clustering in Real-World Scenarios
* Customer Segmentation
* Document Clustering
* Image Segmentation
* Recommendation Engines

### Understanding the Different Evaluation Metrics for Clustering
1. __Inertia__: calculates the sum of distances of all the points within a cluster from the centroid of that cluster. _NOTE_: the lesser the inertia value, the better our clusters are.
2. __Dunn Index__: Along with the distance between the centroid and points, the _Dunn index_ also takes into account the distance between two clusters. This distance between the centroids of two different clusters is known as __inter-cluster__ distance. 

Dunn Index = min(Inter Cluster distance) / max(Intra Cluster distance)

_REMARK:_Dunn index is the ratio of the minimum of inter-cluster distances and maximum of intracluster distances. We want to maximize the Dunn index. The more the value of the Dunn index, the better will be the clusters.

### Introduction to K-Means Clustering
__K-means__ is a _centroid-based algorithm_, or a _distance-based algorithm_, where we calculate the distances to assign a point to a cluster. In K-Means, each cluster is associated with a centroid. The main objective of the __K-Means__ algorithm is to minimize the sum of distances between the points and their respective cluster centroid.

### Steps to Creating Clusters with K-means
1. __Step 1:__ Choose the number of clusters k
2. __Step 2:__ _Select k random points from the data as centroids_. Next, we randomly select the centroid for each cluster. Let’s say we want to have 2 clusters, so k is equal to 2 here. We then randomly select the centroid.
3. __Step 3:__ Assign all the points to the closest cluster centroid
4. __Step 4:__ _Recompute the centroids of newly formed clusters_. Now, once we have assigned all of the points to either cluster, the next step is to compute the centroids of newly formed clusters:
5. __Step 5:__ Repeat steps 3 and 4

## References
1. https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
2. https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/
