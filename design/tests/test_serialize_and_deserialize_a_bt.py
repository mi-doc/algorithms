import unittest
from ..binary_tree_tools import create_tree, level_order_traversal
from ..serialize_and_deserialize_a_bt import Codec

class SerializeAndDeserializeABtTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.ser = Codec()
        self.deser = Codec()
        return super().setUp()

    def test1(self):
        root = create_tree([1,2,3,None,None,4,5])
        ser_data = self.ser.serialize(root)
        assert ser_data == "1,2,N,N,3,4,N,N,5,N,N"

        deser_data = self.deser.deserialize(ser_data)

        vals_root = level_order_traversal(root)
        vals_res = level_order_traversal(deser_data)
        assert vals_res == vals_root
