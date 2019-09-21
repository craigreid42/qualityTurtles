#include <ros/ros.h>
#include <std_msgs/String.h>
#include <turtles/TurtleQuality.h>

void callback(const turtles::TurtleQuality& msg)
{
	ROS_INFO("%lu, %u", msg.index, msg.quality);
}

int main(int argc, char **argv)
{
	ros::init(argc, argv, "listener");

	ros::NodeHandle n;

	ros::Subscriber sub = n.subscribe("quality_turtles", 10, callback);

	ros::spin();

	return 0;
}
