##### Suggested clean drone startup sequence #####
import time, sys
import ps_drone  # Import PS-Drone-API
import socket
import sys

drone = ps_drone.Drone()  # Start using drone
drone.startup()  # Connects to drone and starts subprocesses

drone.reset()  # Sets drone's status to good (LEDs turn green when red)
while (drone.getBattery()[0] == -1):  time.sleep(0.1)  # Wait until the drone has done its reset
print
"Battery: " + str(drone.getBattery()[0]) + "%  " + str(drone.getBattery()[1])  # Gives a battery-status
drone.useDemoMode(False)  # Give me everything...fast
drone.getNDpackage(["demo", "pressure_raw", "altitude", "magneto", "wifi"])  # Packets, which shall be decoded
time.sleep(1.0)  # Give it some time to awake fully after reset

##### Mainprogram begin #####
NDC = drone.NavDataCount
end = False

###UDP Packet Sender###
#Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)



####### show video #######
drone.setConfigAllID()  # Go to multiconfiguration-mode
drone.sdVideo()  # Choose lower resolution (hdVideo() for...well, guess it)
drone.frontCam()  # Choose front view
CDC = drone.ConfigDataCount
while CDC == drone.ConfigDataCount:       time.sleep(0.0001)  # Wait until it is done (after resync is done)
drone.startVideo()  # Start video-function
drone.showVideo()  # Display the video

####### get nav data ########
NDC = drone.NavDataCount
end = False
while not end:
    while drone.NavDataCount == NDC:  time.sleep(0.001)  # Wait until next time-unit
    key = drone.getKey()
    NDC = drone.NavDataCount
    print "-----------"
    print "Aptitude [X,Y,Z] :            " + str(drone.NavData["demo"][2])
    #Assign data to be sent to the Telemetry data
    send_data = str(drone.NavData["demo"][2])
    sock.sendto(send_data.encode('utf-8'), (ip, port))
    print("Info sent")
    print "Altitude / sensor / pressure: " + str(drone.NavData["altitude"][3]) + " / " + str(drone.State[21]) + " / " + str(drone.NavData["pressure_raw"][0])
    print "Megnetometer [X,Y,Z]:         " + str(drone.NavData["magneto"][0])
    print "Wifi link quality:            " + str(drone.NavData["wifi"])
    if key == " ":
        if drone.NavData["demo"][0][2] and not drone.NavData["demo"][0][3]:
            drone.takeoff()
        else:
            drone.land()
    elif key == "p":
        end = True  # Stop if "p" key is pressed
    elif key == "0":
        drone.hover()
    elif key == "w":
        drone.moveForward()

    elif key == "s":
        drone.moveBackward()

    elif key == "a":
        drone.moveLeft()

    elif key == "d":
        drone.moveRight()

    elif key == "q":
        drone.turnLeft()

    elif key == "e":
        drone.turnRight()

    elif key == "7":
        drone.turnAngle(-10, 1)

    elif key == "9":
        drone.turnAngle(10, 1)

    elif key == "4":
        drone.turnAngle(-45, 1)

    elif key == "6":
        drone.turnAngle(45, 1)
        drone.stop()
    elif key == "1":
        drone.turnAngle(-90, 1)

    elif key == "3":
        drone.turnAngle(90, 1)

    elif key == "8":
        drone.moveUp()

    elif key == "2":
        drone.moveDown()

    elif key == "*":
        drone.doggyHop()

    elif key == "+":
        drone.doggyNod()

    elif key == "-":
        drone.doggyWag()


sock.close()

drone.stop()

