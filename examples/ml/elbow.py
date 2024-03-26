from sklearn.datasets import make_blobs
from scrolls.ml.unsupervised import elbow_method_with_plot

X, y = make_blobs(n_samples=1000, n_features=256, centers=8, random_state=42)
elbow_method_with_plot(X, range(1, 16), verbose=True)
