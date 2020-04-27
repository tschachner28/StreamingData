import time
import warnings


def fake_streaming(channels, callback, time_start, duration=5, ni_fs=1000):
    from math import sin
    import numpy as np
    period = 1.0 / ni_fs
    i = 0
    while time.time()-time_start < duration:
        now = time.time()
        raw_sig = sin(2 * np.pi * 3 * i) + sin(2 * np.pi * 0.5 * i)
        callback([raw_sig, raw_sig])
        i += period

        # elapsed = time.time() - now
        # try:
        #     time.sleep(period - elapsed)
        # except:
        #     warnings.warn(
        #         'System cannot handle such high frame rate, lower the desired frequency or simplify your callback fucntion')
        #     continue

