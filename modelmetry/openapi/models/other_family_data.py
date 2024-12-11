from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="OtherFamilyData")


@_attrs_define
class OtherFamilyData:
    """ """

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        other_family_data = cls()

        return other_family_data
