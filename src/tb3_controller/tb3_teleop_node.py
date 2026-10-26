#!/usr/init/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TB3Teleop(Node):
    def __init__(self):
        super().__init__('tb3_teleop_node')
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.get_logger().info('TurtleBot3 Teleop Node Initialized')

def main(args=None):
    rclpy.init(args=args)
    node = TB3Teleop()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
