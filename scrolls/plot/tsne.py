import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from sklearn.manifold import TSNE
from scrolls.cv.image_processing import everything_to_pil_image


def show_tsne(x, y, selected_filenames, zoom=1):
    fig, axis = plt.subplots()
    fig.set_size_inches(22, 22, forward=True)
    plot_images_in_2d(x, y, selected_filenames, zoom=zoom, axis=axis)
    plt.show()


def plot_images_in_2d(x, y, images, axis=None, zoom=1):
    x, y = np.atleast_1d(x, y)
    for x0, y0, image in zip(x, y, images):
        image.thumbnail((100, 100))
        img = OffsetImage(image, zoom=zoom)
        anno_box = AnnotationBbox(img, (x0, y0),
                                  xycoords='data',
                                  frameon=False)
        axis.add_artist(anno_box)
    axis.update_datalim(np.column_stack([x, y]))
    axis.autoscale()


def tsne_to_grid_plotter_manual(x, y, selected_filenames, zoom=1):
    S = 2000
    s = 100
    x = (x - min(x)) / (max(x) - min(x))
    y = (y - min(y)) / (max(y) - min(y))
    x_values = []
    y_values = []
    filename_plot = []
    x_y_dict = {}
    for i, image_path in enumerate(selected_filenames):
        a = np.ceil(x[i] * (S - s))
        b = np.ceil(y[i] * (S - s))
        a = int(a - np.mod(a, s))
        b = int(b - np.mod(b, s))
        if str(a) + "|" + str(b) in x_y_dict:
            continue
        x_y_dict[str(a) + "|" + str(b)] = 1
        x_values.append(a)
        y_values.append(b)
        filename_plot.append(image_path)
    fig, axis = plt.subplots()
    fig.set_size_inches(22, 22, forward=True)
    plot_images_in_2d(x_values, y_values, filename_plot, zoom=zoom, axis=axis)
    plt.show()


class TSNEVisualizer:

    def __init__(self, features, images_input, zoom=1) -> None:
        self._tsne_results = TSNE(
            n_components=2,
            verbose=1,
            metric='euclidean'
        ).fit_transform(features)
        self._images = list(map(everything_to_pil_image, images_input))
        self.zoom = zoom

    def plot(self):
        plt.scatter(self._tsne_results[:, 0], self._tsne_results[:, 1])
        plt.show()

    def plot_icons(self):
        show_tsne(self._tsne_results[:, 0], self._tsne_results[:, 1], self._images, zoom=self.zoom)

    def plot_icons_grid(self):
        tsne_to_grid_plotter_manual(self._tsne_results[:, 0], self._tsne_results[:, 1], self._images, zoom=self.zoom)
