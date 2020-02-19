import rospy
from beginner_tutorials.msg import vision_feedback

def talker():
    pub = rospy.Publisher('feedback', vision_feedback, queue_size=10)
    rospy.init_node('msg_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        feedback_pose = vision_feedback()
        feedback_pose.x = 0.1
        feedback_pose.y = 0.2
        feedback_pose.theta = 0.3
        x_str = "feedback x = %f" % feedback_pose.x
        y_str = "feedback y = %f" % feedback_pose.y
        theta_str = "feedback theta = %f" % feedback_pose.theta
        rospy.loginfo(x_str)
        rospy.loginfo(y_str)
        rospy.loginfo(theta_str)
        pub.publish(feedback_pose)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass