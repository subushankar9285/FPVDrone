#!/bin/env python

import math
import sys
import time
import openvr
import socket

#clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#clientsocket.connect(('', 8089))
#Enter IP Address to create a socket. You must also have a client.py file
openvr.init(openvr.VRApplication_Scene)

# Create data structure to hold locations of tracked devices such as headsets, controllers, and lighthouses
poses_t = openvr.TrackedDevicePose_t * openvr.k_unMaxTrackedDeviceCount
poses = poses_t()

# Print out headset transform five times a second for 20 seconds
for i in range(1000):
    textfile = open("output.txt","w")

    openvr.VRCompositor().waitGetPoses(poses, len(poses), None, 0)
    #hmd_pose = poses[openvr.eETrackingResult]
    hmd_pose = poses[openvr.k_unTrackedDeviceIndex_Hmd]

    #print "X: " + str(hmd_pose.mDeviceToAbsoluteTracking[0][3])
    #print "Y: " + str(hmd_pose.mDeviceToAbsoluteTracking[1][3])
    #print "Z: " + str(hmd_pose.mDeviceToAbsoluteTracking[2][3])

    #xrot = -1 * math.asin(hmd_pose.mDeviceToAbsoluteTracking[2][0]) + 1.57095
    xrot = math.atan2(hmd_pose.mDeviceToAbsoluteTracking[2][1],hmd_pose.mDeviceToAbsoluteTracking[2][2])
    yrot = math.atan2(-hmd_pose.mDeviceToAbsoluteTracking[2][0],math.sqrt((hmd_pose.mDeviceToAbsoluteTracking[2][1])**2+hmd_pose.mDeviceToAbsoluteTracking[2][2]**2))
    zrot = math.atan2(hmd_pose.mDeviceToAbsoluteTracking[1][0],hmd_pose.mDeviceToAbsoluteTracking[0][1])
    #yrot = -1 * math.asin(hmd_pose.mDeviceToAbsoluteTracking[2][1]) + 1.57095
    #zrot = -1 * math.asin(hmd_pose.mDeviceToAbsoluteTracking[2][2]) + 1.57095

    xdeg = math.degrees(xrot)
    ydeg = math.degrees(yrot)
    zdeg = math.degrees(zrot)

    print "\nPitch: " + str(xdeg)
    print "Yaw: " + str(ydeg)
    print "Roll: " + str(zdeg)
    #clientsocket.send(str(xdeg))
    #clientsocket.send(str(ydeg))
    #clientsocket.send(str(zdeg))

    #theta = math.degrees(theta)
    #print theta
    #print(hmd_pose.mDeviceToAbsoluteTracking[0][:])
    #print(hmd_pose.mDeviceToAbsoluteTracking[1][:])
    #print(hmd_pose.mDeviceToAbsoluteTracking[2][:])
    print " "
    textfile.write(str(hmd_pose.mDeviceToAbsoluteTracking))

    sys.stdout.flush()
    time.sleep(0.2)

openvr.shutdown()
