import rospy
import sys
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def move():
	ospy.init_node('move', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    v_linear = loginfo("Digite a velocidae linear:")
    v_ang = ("Digite a velocidae angular:")
    rospy.Subscriber('/turtle1/pose',Pose, rospy.loginfo("X = %f : Y=%f : Z=%f\n",pose.x,pose.y,pose.theta))
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        velocidade = Twist()
        vel.linear.x = v_linear
        vel.angular.z = v_ang
        rospy.loginfo(velocidade)
        pub.publish(velocidade)

        rate.sleep()

try:
    mov()
except rospy.ROSInterruptException:
    pass