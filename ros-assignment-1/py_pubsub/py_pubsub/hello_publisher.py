import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloPublisher(Node):

    def __init__(self):
        super().__init__('hello_publisher')
        self.publisher_ = self.create_publisher(String, '/hello', 10)  # (msg type, topic name, queue size)
        timer_period = 0.5 
        self.timer = self.create_timer(timer_period, self.timer_callback)
    

    def timer_callback(self):
        msg = String()
        msg.data = 'hello'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        


def main(args=None):
    rclpy.init(args=args)

    hello_publisher = HelloPublisher()

    rclpy.spin(hello_publisher)

    hello_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
