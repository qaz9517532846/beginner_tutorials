import rospy
from beginner_tutorials.srv import test

if __name__ == "__main__":
    print "Requesting %s+%s"%(5, 4)
    
    rospy.wait_for_service('test')
    try:
        add_two_ints = rospy.ServiceProxy('test', test)
        resp1 = add_two_ints(5, 4)
        print resp1.check
        print resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
    