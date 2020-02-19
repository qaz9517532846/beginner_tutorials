import rospy
from beginner_tutorials.msg import vision_feedback

def callback(data):
    rospy.loginfo('feedback x = %f', data.x)
    rospy.loginfo('feedback y = %f', data.y)
    rospy.loginfo('feedback theta = %f', data.theta)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('msg_listener', anonymous=True)

    rospy.Subscriber('feedback', vision_feedback, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()