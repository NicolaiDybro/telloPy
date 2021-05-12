
from serial.tools import list_ports
from pydobot import Dobot
from djitellopy import Tello
#Tello:


#Dobot:
port = list_ports.comports()[0].device
print(port)
device = Dobot(port=port)

#Dobot Position:
print(device.pose())
pose = device.pose()

while True:
    valg = input("Vælg 1 eller 2    ")
    print("")
    if valg == '1':
        device.move_to(device.x, device.y, 120, device.r, wait=False)
        device.move_to(200, device.y, 120, device.r, wait=True)
        device.move_to(180, 200, 120, device.r, wait=True)
        device.move_to(0, 230, 90, device.r, wait=True)
        device.move_to(15, 307, 90, device.r, wait=True)

        device.move_to(15, 307, 35, device.r, wait=True)
        device.suck(True)
        device.move_to(15, 307, 90, device.r, wait=True)
        device.move_to(0, 230, 90, device.r, wait=True)
        device.move_to(180, 200, 120, device.r, wait=True)
        device.move_to(200, device.y, 120, device.r, wait=True)
        device.move_to(device.x, device.y, 120, device.r, wait=True)
        device.suck(False)
        device.move_to(device.x, device.y, device.z, device.r, wait=True)

    if valg == '2':
        device.move_to(device.x, device.y, 60, device.r, wait=False)
        device.move_to(device.x, device.y, device.z, device.r, wait=True)
    if valg == '3':
        tello = Tello()
        tello.connect()
        tello.enable_mission_pads()
        tello.set_mission_pad_detection_direction(0)
        pad = tello.get_mission_pad_id()
        tello.takeoff()
        pad = tello.get_mission_pad_id()
        while pad != 8:
            tello.move_forward(20)
            pad = tello.get_mission_pad_id()
        tello.go_xyz_speed_mid(11, 0, 40, 15, 8)
        tello.land()
    if valg == '4':
        tello.takeoff()
        tello.go_xyz_speed_mid(11, 0, 40, 15, 8)
        tello.land()