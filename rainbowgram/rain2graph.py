import matplotlib
import matplotlib.pyplot as plt


cdict  = {
    'red':   ((0.0, 0.0, 0.0), (1.0, 0.0, 0.0)),
    'green': ((0.0, 0.0, 0.0), (1.0, 0.0, 0.0)),
    'blue':  ((0.0, 0.0, 0.0), (1.0, 0.0, 0.0)),
    'alpha': ((0.0, 1.0, 1.0), (1.0, 0.0, 0.0))
}
my_mask = matplotlib.colors.LinearSegmentedColormap('MyMask', cdict)
plt.register_cmap(cmap=my_mask)


def rain2graph(rainbowgram, ax=None):
    """
    Plot rainbowgram
    Args:
        rainbowgrams ([(mag, IF)]): list of rainbowgram datum (tuple of power and IF)
    """
    ax = ax if ax is not None else plt.subplots(1, 1)

    ax.matshow(rainbowgram[1][::-1, :], cmap=plt.cm.rainbow) # lower-side is 0 Hz
    ax.matshow(rainbowgram[0][::-1, :], cmap=my_mask)
