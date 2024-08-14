import unittest
from typing import Dict
from modelmetry.observability.attributes import Attributes

class TestAttributes(unittest.TestCase):
  def setUp(self) -> None:
    self.attributes = Attributes()

  def test_set_attribute(self) -> None:
    self.attributes.set_attribute("key1", "value1")
    self.assertEqual(self.attributes.get_attribute("key1"), "value1")

  def test_merge_attributes(self) -> None:
    attributes_to_merge = {"key2": "value2", "key3": "value3"}
    self.attributes.merge_attributes(attributes_to_merge)
    self.assertEqual(self.attributes.get_attribute("key2"), "value2")
    self.assertEqual(self.attributes.get_attribute("key3"), "value3")

  def test_put_attributes(self) -> None:
    attributes_to_put = {"key4": "value4", "key5": "value5"}
    self.attributes.put_attributes(attributes_to_put)
    self.assertEqual(self.attributes.get_attribute("key4"), "value4")
    self.assertEqual(self.attributes.get_attribute("key5"), "value5")

  def test_remove_attribute(self) -> None:
    self.attributes.set_attribute("key6", "value6")
    self.attributes.remove_attribute("key6")
    self.assertIsNone(self.attributes.get_attribute("key6"))

  def test_get_attribute(self) -> None:
    self.attributes.set_attribute("key7", "value7")
    self.assertEqual(self.attributes.get_attribute("key7"), "value7")

  def test_has_attribute(self) -> None:
    self.attributes.set_attribute("key8", "value8")
    self.assertTrue(self.attributes.has_attribute("key8"))
    self.assertFalse(self.attributes.has_attribute("nonexistent_key"))

if __name__ == '__main__':
  unittest.main()