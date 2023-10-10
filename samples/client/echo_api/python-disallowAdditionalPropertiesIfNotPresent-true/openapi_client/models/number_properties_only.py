# coding: utf-8

"""
    Echo Server API

    Echo Server API

    The version of the OpenAPI document: 0.1.0
    Contact: team@openapitools.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt
from pydantic import Field
from typing_extensions import Annotated
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class NumberPropertiesOnly(BaseModel):
    """
    NumberPropertiesOnly
    """
    number: Optional[Union[StrictFloat, StrictInt]] = None
    var_float: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="float")
    double: Optional[Union[Annotated[float, Field(le=50.2, strict=True, ge=0.8)], Annotated[int, Field(le=50, strict=True, ge=1)]]] = None
    __properties: ClassVar[List[str]] = ["number", "float", "double"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NumberPropertiesOnly from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.model_dump(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of NumberPropertiesOnly from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in NumberPropertiesOnly) in the input: " + _key)

        _obj = cls.model_validate({
            "number": obj.get("number"),
            "float": obj.get("float"),
            "double": obj.get("double")
        })
        return _obj

