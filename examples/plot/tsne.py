import numpy as np
from sklearn.datasets import load_digits
from scrolls.plot.tsne import TSNEVisualizer
from scrolls.cv.image_processing import triple_channel, to_image_255

digits = load_digits()
X = digits['data']
y = digits['target']

# In this example we use images pixels as a features
# In real world applications you probably want use some feature extractor
features = X.copy()

np_images = X.reshape(-1, 8, 8)

# sklearn digits dataset is grayscale so we need to convert it to triple channel
np_images = np.array(list(map(triple_channel, np_images)))

# sklearn digits dataset is in range 0-16 so we need to convert it to range 0-255
np_images = np.array(list(map(to_image_255, np_images)))

# You can use numpy images, list of image paths, or list of PIL images in TSNEVisualizer images_input
tsne_visualizer = TSNEVisualizer(features=features, images_input=np_images, zoom=2)
tsne_visualizer.plot_icons()  # .plot(), .plot_icons(), .plot_icons_grid() are available
