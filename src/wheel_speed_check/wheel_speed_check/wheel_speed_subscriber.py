import rclpy
from rclpy.node import Node
from robot_interfaces.msg import WheelSpeeds

class WheelSpeedsSubscriber(Node):
    def __init__(self):
        super().__init__("wheel_speed_subscriber")
        self.subscriber=self.create_subscription(WheelSpeeds,"wheels_speed",self.received,10)
    def received(self,msg):
        self.get_logger().info(f"\nLeft wheel speed is: {msg.left_wheel} \nRight wheel speed is: {msg.right_wheel}")
def main():
    rclpy.init()
    Sub=WheelSpeedsSubscriber()
    rclpy.spin(Sub)
    Sub.destroy_node()
    rclpy.shutdown()
if __name__=="__main__":
    main()