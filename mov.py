import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

def poseCallback(pose_message):
    global x
    global y,z, ang
    x = pose_message.x
    y = pose_message.y
    ang = pose_message.theta


def mov():
        velocity_message = Twist()
        global x, y
        x0 = x
        y0 = y

        dist = loginfo("Digite a distância:")
        andar = 0.0
        rate = rospy.Rate(10)
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)

        #Loop para o movimento em linha reta
        while True:
                velocity_publisher.publish(velocity_message)

                rate.sleep()

                andar = andar + abs(0.5 * math.sqrt(((x-x0) ** 2) + ((y - y0) ** 2)))
                print(dist)

                if not (andar < dist):
                    break

        velocity_message.linear.x = 0
        velocity_publisher.publish(velocity_message)


def rotate(speed):

    angulo = loginfo("Digite o angulo:")

    angular_speed = speed*2*PI/360
    relative_angle = angulo*2*PI/360

    vel_msg = Twist()
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    t0 = rospy.Time.now().to_sec()
    current_angle = 0
    rate = rospy.Rate(10)

    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        rate.sleep()
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)

        if (current_angle > relative_angle):
            break

    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

def move_and_rotate():

    move()
    rotate(30)
    move()
    rotate(30)
    move()
    rotate(90)
    move()
    pass


if __name__ == '__main__':
    try:

        rospy.init_node('turtlesim_motion_pose', anonymous = True)

        cmd_vel_topic = '/turtle1/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size = 10)
        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)
        time.sleep(2)
        move_and_rotate()

    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")