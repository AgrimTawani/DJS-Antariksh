
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Subscriber(Node):

    def __init__(self):
        super().__init__('Hello_World_subscriber')
        self.hello_subscription = self.create_subscription(String,'hello', self.hello_callback, 10)  # (msg type, topic name, callback, queue size)
        self.world_subscription = self.create_subscription(String,'world', self.world_callback, 10)
        self.publisher_ = self.create_publisher(String, '/hello_world', 10)
        self.hello = ""
        self.world = ""

    def hello_callback(self, msg):  # everytime a new msg is recieved on the /hello topic, this func is triggered
        self.hello = msg.data

    def world_callback(self, msg):
        self.world = msg.data

        if self.hello:
            hello_world = String()
            hello_world.data = self.hello + " " + self.world
            self.publisher_.publish(hello_world)
            self.get_logger().info(f'I heard from /hello and /world : "{hello_world.data}"')




def main(args=None):
    rclpy.init(args=args)

    subscriber = Subscriber()

    rclpy.spin(subscriber)

    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
