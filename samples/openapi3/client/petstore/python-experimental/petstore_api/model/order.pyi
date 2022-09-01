# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class Order(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        class properties:
            id = schemas.Int64Schema
            petId = schemas.Int64Schema
            quantity = schemas.Int32Schema
            shipDate = schemas.DateTimeSchema
            
            
            class status(
                schemas.SchemaEnumMakerClsFactory(
                    enum_value_to_name={
                        "placed": "PLACED",
                        "approved": "APPROVED",
                        "delivered": "DELIVERED",
                    }
                ),
                schemas.StrSchema
            ):
                
                @classmethod
                @property
                def PLACED(cls):
                    return cls("placed")
                
                @classmethod
                @property
                def APPROVED(cls):
                    return cls("approved")
                
                @classmethod
                @property
                def DELIVERED(cls):
                    return cls("delivered")
            complete = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "petId": petId,
                "quantity": quantity,
                "shipDate": shipDate,
                "status": status,
                "complete": complete,
            }
        additional_properties = schemas.AnyTypeSchema
    
    id: typing.Union[MetaOapg.properties.id, schemas.Unset]
    petId: typing.Union[MetaOapg.properties.petId, schemas.Unset]
    quantity: typing.Union[MetaOapg.properties.quantity, schemas.Unset]
    shipDate: typing.Union[MetaOapg.properties.shipDate, schemas.Unset]
    status: typing.Union[MetaOapg.properties.status, schemas.Unset]
    complete: typing.Union[MetaOapg.properties.complete, schemas.Unset]
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["petId"]) -> typing.Union[MetaOapg.properties.petId, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["quantity"]) -> typing.Union[MetaOapg.properties.quantity, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["shipDate"]) -> typing.Union[MetaOapg.properties.shipDate, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["complete"]) -> typing.Union[MetaOapg.properties.complete, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def __getitem__(self, name: typing.Union[str, typing.Literal["id"], typing.Literal["petId"], typing.Literal["quantity"], typing.Literal["shipDate"], typing.Literal["status"], typing.Literal["complete"], ]):
        # dict_instance[name] accessor
        if not hasattr(self.MetaOapg, 'properties') or name not in self.MetaOapg.properties.__annotations__:
            return super().__getitem__(name)
        try:
            return super().__getitem__(name)
        except KeyError:
            return schemas.unset

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, int, schemas.Unset] = schemas.unset,
        petId: typing.Union[MetaOapg.properties.petId, int, schemas.Unset] = schemas.unset,
        quantity: typing.Union[MetaOapg.properties.quantity, int, schemas.Unset] = schemas.unset,
        shipDate: typing.Union[MetaOapg.properties.shipDate, datetime, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        complete: typing.Union[MetaOapg.properties.complete, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'Order':
        return super().__new__(
            cls,
            *args,
            id=id,
            petId=petId,
            quantity=quantity,
            shipDate=shipDate,
            status=status,
            complete=complete,
            _configuration=_configuration,
            **kwargs,
        )