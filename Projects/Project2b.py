from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer
from pyclustering.utils.metric import distance_metric, type_metric
import matplotlib.pyplot as plot
import numpy as np

data_set_raw = [(2, 10), (4, 7), (3, 12), (5, 11), (2, 5), (6, 13), (4, 7), (7, 14), (8, 12), (3, 10),
                (9, 6), (5, 7), (4, 13), (6, 16), (8, 15)]

centers = kmeans_plusplus_initializer(data_set_raw, 3).initialize()
eudi = distance_metric(type_metric.EUCLIDEAN)
km = kmedoids(data_set_raw, [0, 1, 2], metric=eudi)
km.process()
f_cluster = km.get_clusters()
f_mediod = km.get_medoids()
print(f_cluster, f_mediod)
# Saved as Figure_2
ax = plot.subplot(111)
array = np.array(data_set_raw)
f_center = np.array(f_mediod)
plot.title('K-medoids')
plot.scatter(array[f_cluster[0][:]][:, 0],
             array[f_cluster[0][:]][:, 1],
             s=50,
             c='lightgreen',
             marker='s',
             label='Category 1')
plot.scatter(array[f_cluster[1][:]][:, 0],
             array[f_cluster[1][:]][:, 1],
             s=50,
             c='orange',
             marker='o',
             label='Category 2')
plot.scatter(array[f_cluster[2][:]][:, 0],
             array[f_cluster[2][:]][:, 1],
             s=50,
             c='yellow',
             marker='v',
             label='Category 3')
plot.scatter(array[f_mediod][:][:, 0],
             array[f_mediod][:][:, 1],
             s=60,
             c='red',
             marker='*',
             label='Mediods')

plot.legend(loc='center left',
            scatterpoints=1, bbox_to_anchor=(1, 0.5))

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
plot.show()
plot.show()
