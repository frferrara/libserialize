"""
This file contains the serializer library for the fleet communication project.
"""

# Import modules
from proto.Any_pb2            import Any
from proto.ByteMultiArray_pb2 import ByteMultiArray
from proto.ByteMultiArray_pb2 import MultiArrayLayout


def serialize_bma(ros_msg):
    """
    This function is used to serialize the ByteMultiArray data.
    Inputs:
    - ros_msg: ROS message to be serialized
    Outputs:
    - bma_data: serialized data (see ByteMultiArray.proto)
    """
    # Create the Serialization objects
    multi_array_layout = MultiArrayLayout()
    byte_multi_array = ByteMultiArray()

    # Loop through the dimensions in the layout
    for dim in ros_msg.layout.dim:
        ma_dim = multi_array_layout.dim.add()
        ma_dim.label = dim.label
        ma_dim.size = dim.size
        ma_dim.stride = dim.stride
    
    # Set the data offset
    multi_array_layout.data_offset = ros_msg.layout.data_offset

    # Set the ByteMultiArray
    byte_multi_array.layout = multi_array_layout
    byte_multi_array.data = ros_msg.data

    bma_data = byte_multi_array.SerializeToString()
    return bma_data

def serialize_any(name, bma_data):
    """
    This function is used to serialize the Any data.
    Inputs:
    - name:     name of the serialization (needed for Any.proto)
    - bma_data: serialized data (see ByteMultiArray.proto)
    Outputs:
    - any_data: serialized data (see Any.proto)
    """
    # Create the Serialization object
    any_proto = Any()

    # Set the data
    any_proto.type_url = name
    any_proto.value = bma_data

    # Serialize
    any_data = any_proto.SerializeToString()

    return any_data


def serialize(name, ros_msg):
    """
    This function is used to serialize the data using a two step
    serialization.
    Inputs:
    - name:    name of the serialization (needed for Any.proto)
    - ros_msg: ROS message to be serialized
    Outputs:
    - any_data: serialized data (byte string, resulting from Any.proto)
    """
    # Perform the serialization
    bma_data = serialize_bma(ros_msg)
    any_data = serialize_any(name, bma_data)

    return any_data

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