#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64
from tf.transformations import euler_from_quaternion

pub = rospy.Publisher('heading',Float64, queue_size=10)

def calculateHeading(imuMsg):
    roll=0
    pitch=0
    yaw=0

    quaternion = (
      imuMsg.orientation.x,
      imuMsg.orientation.y,
      imuMsg.orientation.z,
      imuMsg.orientation.w)
    (roll,pitch,yaw) = euler_from_quaternion(quaternion)
    pub.publish(yaw)


if __name__ == '__main__':
    try:
	rospy.init_node('header', anonymous=True)
	sub = rospy.Subscriber('imu', Imu, calculateHeading)
	rospy.spin()
    except rospy.ROSInterruptException:
        pass
