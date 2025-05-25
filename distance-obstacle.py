#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan

def scan_callback(msg):
    range_ahead = msg.ranges[len(msg.ranges) // 2]
    rospy.loginfo("Range ahead: %0.1f meters", range_ahead)

def main():
    rospy.init_node('range_ahead')
    rospy.Subscriber('scan', LaserScan, scan_callback)
    rospy.spin()

if __name__ == '__main__':
    main()
