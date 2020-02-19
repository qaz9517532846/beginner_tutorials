#include "ros/ros.h"
#include "beginner_tutorials/vision_feedback.h"

int main(int argc, char **argv)
{
  ros::init(argc, argv, "msg_talker");
  ros::NodeHandle n;

  ros::Publisher feed_pose = n.advertise<beginner_tutorials::vision_feedback>("feedback", 1000);

  ros::Rate loop_rate(10);

  int count = 0;
  while (ros::ok())
  {
    beginner_tutorials::vision_feedback feedback;

    feedback.x = 0.1;
	feedback.y = 0.2;
	feedback.theta = 0.3;

    ROS_INFO("feedback x = %f", feedback.x);
	ROS_INFO("feedback y = %f", feedback.y);
	ROS_INFO("feedback theta = %f", feedback.theta);

    feed_pose.publish(feedback);

    ros::spinOnce();

    loop_rate.sleep();

    ++count;
  }
  return 0;
}