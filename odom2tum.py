#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry

def odom_callback(data):
    # Extract the necessary information from the Odometry message
    timestamp = data.header.stamp
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    z = data.pose.pose.position.z
    qx = data.pose.pose.orientation.x
    qy = data.pose.pose.orientation.y
    qz = data.pose.pose.orientation.z
    qw = data.pose.pose.orientation.w

    # Convert the quaternion to Euler angles
    roll, pitch, yaw = quaternion_to_euler(qx, qy, qz, qw)

    # Write the data to a file in TUM format
    with open('/home/crz/al-huace/Spin-LIO/src/Spin-LIO/Log/odom.txt', 'a') as f:
        f.write('{:.9f} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f}\n'.format(
            timestamp.to_sec(), x, y, z, roll, pitch, yaw, 0.0))

def quaternion_to_euler(x, y, z, w):
    import math
    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll = math.atan2(t0, t1)

    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch = math.asin(t2)

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw = math.atan2(t3, t4)

    return roll, pitch, yaw

if __name__ == '__main__':
    rospy.init_node('odom_to_tum')
    rospy.Subscriber('/Odometry', Odometry, odom_callback)
    rospy.spin()
