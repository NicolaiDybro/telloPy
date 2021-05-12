from serial.tools import list_ports
from pydobot import Dobot
from djitellopy import Tello

tello = Tello()
tello.connect()

port = list_ports.comports()[0].device
print(port)
device = Dobot(port=port)
# configure drone
tello.enable_mission_pads()
tello.set_mission_pad_detection_direction(0)  # forward detection only

pose = device.pose()
print(pose)
print(tello.get_battery())
tello.takeoff()
pad = tello.get_mission_pad_id()
tello.move_up(50)

tello.get_mission_pad_id()
while pad != 8:
    tello.move_forward(25)
    pad = tello.get_mission_pad_id()

tello.go_xyz_speed_mid(0,0,40,15,8)
tello.go_xyz_speed_mid(0,0,30,15,8)
tello.go_xyz_speed_mid(0,0,20,15,8)
tello.go_xyz_speed_mid(0,0,15,15,8)
tello.disable_mission_pads()
tello.land()
tello.end()
#(275.7630310058594, 15.815352439880371, -65.15946960449219, 3.282388210296631, 3.282388210296631, 68.19369506835938, 51.665924072265625, 0.0)

#device.move_to(device.x, device.y, 120, device.r, wait=False)

device.close()