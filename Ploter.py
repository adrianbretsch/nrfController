import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import StringHelper as sth

def plot_udp_unicast_payload_test():
    """
        time/bytes chart. Showing the packages lost and time needed to receive the udp from a Unicast
    """
    results = pd.read_csv("results/udp_payload_test/udp_payload_test_h-3_02-09-20_02-54-51.csv",
                          usecols=[sth.PingValues.BYTES.value, sth.PingValues.TIME.value])
    chart = sns.boxplot(x='bytes', y='time', data=results,)
    plt.ylabel('Response time in ms')
    plt.xlabel('Payload in bytes')
    plt.ylim(0, None)
    plt.xlim(0, None)
    plt.title("Unicast Package Test; Hops = 1")
    plt.show()

def plot_udp_unicast_package_lost():
    results = pd.read_csv("results/udp_payload_test/udp_payload_test_h-3_02-09-20_02-54-51.csv",
                          usecols=[sth.PingValues.BYTES.value, sth.PingValues.TIME.value])

    results_bytes = results.groupby(sth.UdpValues.BYTES.value)

    size=results_bytes.size()
    plt.plot(size, "gx")
    plt.ylabel('Packages received')
    plt.xlabel('Payload in bytes')
    plt.ylim(0, None)
    plt.xlim(0, None)
    plt.title("Unicast UDP Packages received; Hops=1; Packages sent=500")
    plt.show()

def plot_multicast_package_test():
    """time/bytes chart. Showing the packages lost and time needed to receive the ping from a Multicast
    - 0 - 0 anfangen
    - Zeit braucht einheit
    - CDFs
    - mehr messungen
    """

    results = pd.read_csv("results/multicast-package-test/multicast-package-test_01-09-20_17-28-09.csv",
                          usecols=[sth.PingValues.BYTES.value, sth.PingValues.TIME.value])
    chart = sns.jointplot(x='bytes', y='time', ratio=10, data=results, marker='x')
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

def plot_unicast_interval_test():
    """
    """
    results_path = "results/unicast_interval_test/unicast_interval_test_01-16-20_11-05-42.csv"
    results = pd.read_csv(results_path,
                          usecols=[sth.PingValues.INTERVAL.value, sth.PingValues.TIME.value])
    chart = sns.boxplot(x='interval', y='time', data=results, color="#009EE0")
    plt.ylabel('Time in ms')
    plt.xlabel('Interval in ms')
    plt.ylim(0, None)
    plt.xlim(0, None)
    sparsify_axis_labels(chart, 5)
    plt.title("Unicast Interval Test")
    plt.show()

"""@author mbatchkarov https://github.com/mwaskom/seaborn/issues/636"""
def sparsify_axis_labels(ax, n=2):
    for idx, label in enumerate(ax.xaxis.get_ticklabels()):
        if (idx + 1) % n != 0:
            label.set_visible(False)


plot_udp_unicast_package_lost()
