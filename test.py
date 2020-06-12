from dronekit import connect
import time

#conn = connect('/dev/serial/by-id/usb-Hex_ProfiCNC_CubeOrange_39001B001551383439343731-if00', wait_ready=True)
conn = connect('tcp:127.0.0.1:5760', wait_ready=True)

class status:
    target_bearing = 0
    xtrack_error = 0
    heading = 0
    throttle = 0
    
def nav_callback(self, name, msg):
    status.target_bearing = msg.target_bearing
    status.xtrack_error = msg.xtrack_error

def vfr_callback(self, name, msg):
    status.heading = msg.heading
    status.throttle = msg.throttle

conn.add_message_listener('NAV_CONTROLLER_OUTPUT', nav_callback)
conn.add_message_listener('VFR_HUD', vfr_callback)

while True:
    print "BEA", status.target_bearing
    print "XTE", status.xtrack_error
    print "YAW", status.heading
    print "THR", status.throttle

    time.sleep(0.01)
