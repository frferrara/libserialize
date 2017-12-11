"""
This file contains the serializer library for the fleet communication project.
"""

# Import modules
from proto.Any_pb2            import Any
from proto.ByteMultiArray_pb2 import ByteMultiArray


def serialize(name, ros_msg):
        """
        This function is used to serialize the data using a two step
        serialization.
        Inputs:
        - name:    name of the serialization (needed for Any.proto)
        - ros_msg: ROS message to be serialized
        Outputs:
        - data: serialized data (byte string, resulting from Any.proto)
        """
        data = None
        return data

def deserialize(data):
    """
    This function is used to deserialize the data using a two step
    serialization.
    Inputs:
    - data: serialized data (byte string, resulting from Any.proto)
    Outputs:
    - name:    name of the serialization (needed for Any.proto)
    - ros_msg: ROS message to be serialized
    """
    name = None
    ros_msg = None
    return name, ros_msg


# Basic testing
if __name__ == "__main__":
    serialize("bla", "bla")
    deserialize("bla")