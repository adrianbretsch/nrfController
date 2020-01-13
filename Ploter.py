import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import StringHelper as sth


def plot_multicast_package_test():
    """time/bytes chart. Showing the packages lost and time needed to receive the ping from a Multicast
    - 0 - 0 anfangen
    - Zeit braucht einheit
    - CDFs
    - mehr messungen
    """

    results = pd.read_csv("results/multicast-package-test/multicast-package-test_01-09-20_17-28-09.csv",
                          usecols=[sth.PingValues.BYTES.value, sth.PingValues.TIME.value])
    chart = sns.jointplot(x='bytes', y='time',ratio=10, data=results, marker='x')
    plt.show()

def plot_unicast_package_test():
    """time/bytes chart. Showing the packages lost and time needed to receive the ping from a Unicast
    """
    results = pd.read_csv("results/unicast_package_test/unicast_package_test_01-13-20_12-38-28.csv",
                          usecols=[sth.PingValues.BYTES.value, sth.PingValues.TIME.value])
    chart = sns.boxplot(x='bytes', y='time', data=results)
    plt.ylabel('time in ms')
    plt.xlabel('bytes')
    plt.ylim(0, None)
    plt.xlim(0, None)
    sparsify_axis_labels(chart, 5)
    plt.title("Unicast Package Test")
    plt.show()


def sparsify_axis_labels(ax, n=2):
    for idx, label in enumerate(ax.xaxis.get_ticklabels()):
        if (idx+1) % n != 0:
            label.set_visible(False)


plot_unicast_package_test()
