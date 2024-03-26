from sklearn.decomposition import PCA


def reduce_dimension(features, n_components=0.95):
    pca = PCA(n_components=n_components)
    return pca.fit_transform(features)
