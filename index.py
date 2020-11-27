import info
import serial
import time
import comm_handle
start_time = time.time()


# print(f'name of project: {info.project} version: {info.app_version}')
#
# ser = serial.Serial()
# ser.baudrate = 115200
# ser.port = 'COM3'
# ser.timeout = 1
# ser.setRTS(False)
# ser.open()
#
# ser.write(b'x#')
#
# data = []
# # while (data[len(data)] != 'END'):
# a = ser.read_until('o')
# print(a)
# ser.close()

print("--- %s seconds ---" % (time.time() - start_time))