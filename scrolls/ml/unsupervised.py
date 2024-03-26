import numpy as np
from tqdm import tqdm
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt


def reduce_dimension(features, n_components=0.95):
    pca = PCA(n_components=n_components)
    return pca.fit_transform(features)


def elbow_method(features, k_range, n_init='auto', max_iter=300, verbose=False):
    distortions = []
    inertias = []

    tqdm_disable = not verbose
    for k in tqdm(k_range, disable=tqdm_disable):
        kmean_model = KMeans(n_clusters=k, n_init=n_init, max_iter=max_iter)
        kmean_model.fit(features)

        distortion = sum(np.min(cdist(features, kmean_model.cluster_centers_, 'euclidean'), axis=1)) / features.shape[0]

        distortions.append(distortion)
        inertias.append(kmean_model.inertia_)

    return distortions, inertias


def plot_results_of_elbow_method(k_range, distortions):
    plt.plot(k_range, distortions, 'bx-')
    plt.xlabel('Values of K')
    plt.ylabel('Distortion')
    plt.title('The Elbow Method using Distortion')
    plt.show()


def elbow_method_with_plot(features, k_range, n_init='auto', max_iter=300, verbose=False):
    distortions, inertias = elbow_method(features, k_range, n_init, max_iter, verbose)
    plot_results_of_elbow_method(k_range, distortions)
    return distortions, inertias
