import time
import warnings
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def fake_streaming(channels, callback, time_start, duration=5, ni_fs=1000):
    from math import sin
    import numpy as np
    period = 1.0 / ni_fs
    i = 0
    raw_sigs = []
    timestamps = []
    #plt.plot()
    #plt.show()
    plt.ion()
    #count = 0
    while time.time()-time_start < duration:
        #print(i)
        now = time.time()
        raw_sig = sin(2 * np.pi * 3 * i) + sin(2 * np.pi * 0.5 * i)
        raw_sigs.append(raw_sig)
        #timestamp = time.time()-time_start
        timestamps.append(time.time()-time_start)
        #if count % 20 == 0:
        #    plt.plot(timestamp, raw_sig)
        #time.sleep(0.0001)
        callback([raw_sig, raw_sig])
        i += period
        #count += 1
    #print('len timestamps', len(timestamps))
    #print('len raw_sigs', len(raw_sigs))
    #plt.plot(np.array(timestamps), np.array(raw_sigs))
    #plt.show()
    #plot_real_time(timestamps, raw_sigs)



        # elapsed = time.time() - now
        # try:
        #     time.sleep(period - elapsed)
        # except:
        #     warnings.warn(
        #         'System cannot handle such high frame rate, lower the desired frequency or simplify your callback fucntion')
        #     continue

def plot_real_time(duration=15, ni_fs=1000):
    from math import sin
    import numpy as np
    period = 1.0 / ni_fs
    i = 0
    timeCount = 0.0
    timestamps_to_plot = []
    raw_sigs_to_plot = []
    arrayCount = 0
    timestamps = []
    raw_sigs = []
    time_start = time.time()
    count = 0
    while time.time()-time_start < duration:
        #print(i)
        now = time.time()
        raw_sig = sin(2 * np.pi * 3 * i) + sin(2 * np.pi * 0.5 * i)
        timestamps.append(now - time_start)
        raw_sigs.append(raw_sig)
        i += period
        count += 1
        if count % 10 == 0:
            plt.plot(timestamps, raw_sigs)
            plt.show()

        #time.sleep(0.01)

        #timestamp = time.time()-time_start

    """
    while arrayCount*10 < len(timestamps) and timeCount < 5:
        timestamps_to_plot.append(timestamps[arrayCount*10])
        raw_sigs_to_plot.append(raw_sigs[arrayCount*10])
        plt.plot(timestamps_to_plot, raw_sigs_to_plot)
        plt.show()
        time.sleep(0.01)
        timeCount += 0.01
        arrayCount += 1
        #timeCount += 0.01
    """

def jupyter_test(duration=15, ni_fs=1000):
    from math import sin
    import numpy as np
    period = 1.0 / ni_fs
    i = 0
    timeCount = 0.0
    timestamps_to_plot = []
    raw_sigs_to_plot = []
    arrayCount = 0
    timestamps = []
    raw_sigs = []
    time_start = time.time()
    count = 0
    while time.time() - time_start < duration:
        # print(i)
        now = time.time()
        raw_sig = sin(2 * np.pi * 3 * i) + sin(2 * np.pi * 0.5 * i)
        timestamps.append(now - time_start)
        raw_sigs.append(raw_sig)
        i += period
    return timestamps, raw_sigs

if __name__ == '__main__':
    plot_real_time()
