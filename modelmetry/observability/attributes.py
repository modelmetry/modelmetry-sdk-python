from copy import deepcopy
from typing import Dict, Iterator

class Attributes:
  def __init__(self, attributes: Dict[str, any] = None) -> None:
    self.attributes = attributes or {}

  def set_attribute(self, key: str, value: any) -> "Attributes":
    self.attributes[key] = value
    return self

  def merge_attributes(self, attributes: Dict[str, any]) -> "Attributes":
    self.attributes.update(attributes)
    return self

  def put_attributes(self, attributes: Dict[str, any]) -> "Attributes":
    self.attributes = attributes
    return self
  
  def remove_attribute(self, key: str) -> "Attributes":
    self.attributes.pop(key)
    return self
  
  def get_attribute(self, key: str) -> any:
    return self.attributes.get(key)
  
  def has_attribute(self, key: str) -> bool:
    return key in self.attributes

  def to_dict(self) -> Dict[str, any]:
    return self.attributes

  def __str__(self) -> str:
    return str(self.attributes)

  def __repr__(self) -> str:
    return str(self.attributes)

  def __eq__(self, other: "Attributes") -> bool:
    return self.attributes == other.attributes

  def __ne__(self, other: "Attributes") -> bool:
    return self.attributes != other.attributes

  def __len__(self) -> int:
    return len(self.attributes)

  def __iter__(self) -> Iterator:
    return iter(self.attributes)
  
  def __getitem__(self, key: str) -> any:
    return self.attributes[key]

  def __setitem__(self, key: str, value: any) -> None:
    self.attributes[key] = value

  def __delitem__(self, key: str) -> None:
    del self.attributes[key]

  def __contains__(self, key: str) -> bool:
    return key in self.attributes

  def __copy__(self) -> "Attributes":
    return Attributes(self.attributes.copy())

  def __deepcopy__(self, memo: Dict) -> "Attributes":
    return Attributes(deepcopy(self.attributes, memo))

  def __add__(self, other: "Attributes") -> "Attributes":
    return Attributes(self.attributes | other.attributes)