import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class WorldPublisher(Node):

    def __init__(self):
        super().__init__('world_publisher')
        self.publisher_ = self.create_publisher(String, '/world', 10)  # (msg type, topic name, queue size)
        timer_period = 0.5 
        self.timer = self.create_timer(timer_period, self.timer_callback)
    

    def timer_callback(self):
        msg = String()
        msg.data = 'world'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        


def main(args=None):
    rclpy.init(args=args)

    world_publisher = WorldPublisher()

    rclpy.spin(world_publisher)

    world_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
