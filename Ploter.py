import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

import StringHelper as sth


def plot_multicast_package_test():
    "bytes/time"
    "responses/bytes"
    results = pd.read_csv("results/multicast-package-test/multicast-package-test_12-20-19_10-18-51.csv",
                          usecols=[sth.PingValues.BYTES.value, sth.PingValues.ICMP_SEQ.value,
                                   sth.PingValues.TIME.value])

    received = results.groupby('icmp_seq').count()
    count_seq = max(results.groupby('icmp_seq').groups)
    first_seq = min(results.groupby('icmp_seq').groups)
    sns.boxplot(x='bytes', y='time', data=results)
    """plt.xlabel("bytes")
    plt.ylabel("time in ms")
    seq_data = results.groupby("bytes")
    seq_time = seq_data.time
    sns.boxplot([n for v in seq_time.groups.values() for n in v])
    plt.show()
    """"""label="{} bytes".format(seq_bytes.iloc[0])"""


plot_multicast_package_test()
