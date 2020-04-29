import numpy as np
from fakeStreaming import *
import matplotlib.pyplot as plt
import warnings

CALIBRATION = [53, 51.9]  ##Modl [77(RIGHT),76(LEFT)]
LEFT_SENSOR = "Dev1/ai1"
RIGHT_SENSOR = "Dev1/ai0"


class signal_processor(object):
    def __init__(self, channels=[RIGHT_SENSOR, LEFT_SENSOR], ni_fs=1000, ref_inx=0):
        """
        channels: list of string that indicates which port to read
        ni_fs: sampling rate
        ref_inx: index number for the channel list of which arm is the reference arm
        """
        savetag_cali = 'testStreaming0427'
        savedir = '/Users/thereseschachner/Desktop/Arm_Torque_Game/StreamingData/'
        self.savepath_cali = savedir + savetag_cali + '.csv'

        self.channels = channels
        self.ni_fs = ni_fs
        self.ref_inx = ref_inx

        render_fps = 27
        self.render_lag = int(ni_fs / render_fps)

        # self.pre_exp = calibrator(self.ref_inx, self.savepath_cali)

        self.to_record_arr = []
        self.counter = 0
        self.record_flag = False
        self.now = time.time()
        #while time.time() - self.duration < 2:
        try:
            fake_streaming(channels, self.callback_cali, self.now, 5, ni_fs)
        except:
            pass
        print(time.time() - self.now)
        self.record_to_file(self.to_record_arr, self.savepath_cali)

    def callback_cali(self, sample):
        if type(sample) != list:
            sample = [sample]

        # print(sample)
        if self.counter > self.render_lag:
            self.record_flag = True
            self.counter = 0

        if self.record_flag:
            timestamp = time.time() - self.now
            self.to_record_arr.append([sample, timestamp])
            # print('to_record_arr: ', self.to_record_arr)

        self.counter += 1
        ##Test sampling rate#####
        # self.counter+=1
        # timestamp=time.time()
        # elapsed=timestamp-self.now
        # if elapsed>2.0:
        #     fs=self.counter/2.0
        #     print(fs)
        #     self.counter=0
        #     self.now=time.time()

    def record_to_file(self, array, savepath):
        """
        array=[data,tag,timestamp]
        type(data)==list
        [sensor_data,sensor_data,...]
        tag=str i.e 'reference'
        """

        row = ''
        for a in array:
            for d in a[0]:  # data
                row += str(d)
                row += ','
            row += str(a[1])
            row += '\n'
        with open(savepath, 'a') as f:
            f.write(row)
            print('wrote to file')

        # Save and plot the sin function data
        array_np = np.array(array)
        array_data = array_np[:,0]
        timestamps = array_np[:,1]
        all_data = np.array([np.array(xi) for xi in array_data])
        data = all_data[:,0] + all_data[:,1]

        plt.figure(figsize=(4, 3))
        plt.plot(timestamps, data)
        plt.title('Torque: Sin Function')
        plt.xlabel('Time (s)')
        plt.ylabel('Torque (Nm)')
        plt.savefig('sin_graph_torque.png')
        plt.show()

        # Save and plot the ramp function data
        ramp_data = ramp_function(timestamps, 0.5, 0) + ramp_function(timestamps, -0.75, 2.5)
        #max_ramp_torque = max(ramp_data)
        #max_ramp_time = np.where(ramp_data == max_ramp_torque)[0][0]
        #print('Max torque in ramp function: ', max_ramp_torque)
        with open('testStreamingRamp.csv', 'w') as f:
            for i in range(0,timestamps.shape[0]):
                line = str(timestamps[i]) + ', ' + str(ramp_data[i])
                print(line, file=f)
        plt.figure(figsize = (6,4))
        plt.plot(timestamps, ramp_data)
        plt.title('Torque: Ramp Function')
        plt.xlabel('Time (s)')
        plt.ylabel('Torque (Nm)')
        plt.savefig('ramp_graph_torque')
        plt.show()





def ramp_function(time, slope, offset):
    length = len(time)
    torque = np.zeros(length)
    for i in range(0,length):
        if time[i] >= offset:
            torque[i] = slope * (time[i] + offset)
    return torque


def main():
    signal_processor(ni_fs=800)


if __name__ == '__main__':
    main()
