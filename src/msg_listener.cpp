#include "ros/ros.h"
#include "beginner_tutorials/vision_feedback.h"

void chatterCallback(const beginner_tutorials::vision_feedback::ConstPtr& msg)
{
  ROS_INFO("I heard feedback x = %f", msg->x);
  ROS_INFO("I heard feedback y = %f", msg->y);
  ROS_INFO("I heard feedback theta = %f", msg->theta);
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "msg_listener");

  ros::NodeHandle n;

  ros::Subscriber sub = n.subscribe("feedback", 1000, chatterCallback);

  ros::spin();

  return 0;
}