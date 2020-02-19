#!/usr/bin/env python

from beginner_tutorials.srv import *
import rospy

def handle_add_two_ints(req):
    result_server = testResponse()
    result_server.sum = req.a + req.b
    result_server.check = "true"
    print "Returning [%s + %s = %s]"%(req.a, req.b, result_server.sum)
    print "Is this server calculation? [%s]"%(result_server.check)
    return [result_server.check, result_server.sum]

def add_two_ints_server():
    rospy.init_node('test_server')
    s = rospy.Service('test', test, handle_add_two_ints)
    print "Ready to add two ints."
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()