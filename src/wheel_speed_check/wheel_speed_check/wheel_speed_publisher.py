import rclpy
from rclpy.node import Node
from robot_interfaces.msg import WheelSpeeds
from rcl_interfaces.msg import SetParametersResult

class WheelSpeedsPublisher(Node):
    def __init__(self):
        super().__init__("wheel_speed_publisher")
        self.publisher=self.create_publisher(WheelSpeeds,"wheels_speed",10)
        self.create_timer(5.0,self.message)
        self.declare_parameter("Left_wheel",0.0)
        self.declare_parameter("Right_wheel",0.0)
    def message(self):
        right=self.get_parameter("Right_wheel").value
        left=self.get_parameter("Left_wheel").value
        Speed=WheelSpeeds()
        Speed.left_wheel=left
        Speed.right_wheel=right
        self.publisher.publish(Speed)
def main():
    rclpy.init()
    Publisher=WheelSpeedsPublisher()
    rclpy.spin(Publisher)
    Publisher.destroy_node()
    rclpy.shutdown()
if __name__=="__main__":
    main()
