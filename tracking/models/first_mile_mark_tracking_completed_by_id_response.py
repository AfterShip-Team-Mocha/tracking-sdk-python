# coding: utf-8
#
# This code was auto generated by AfterShip SDK Generator.
# Do not edit the class manually.

from __future__ import annotations
import pprint

from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional
from typing_extensions import Self


class FirstMileMarkTrackingCompletedByIdResponse(BaseModel):
    """
    FirstMileMarkTrackingCompletedByIdResponse
    """  # noqa: E501

    tracking_number: Optional[str] = None
    slug: Optional[str] = None
    transit_time: Optional[int] = None
    courier_redirect_link: Optional[str] = None
    courier_tracking_link: Optional[str] = None

    def to_str(self, **kwargs) -> str:
        return pprint.pformat(self.model_dump(**kwargs))

    def to_json(self, **kwargs) -> str:
        return self.model_dump_json(**kwargs)

    def to_dict(self, **kwargs) -> Dict[str, Any]:
        return self.model_dump(**kwargs)

    @classmethod
    def from_json(cls, json_str: str, **kwargs) -> Optional[Self]:
        return cls.model_validate_json(json_str, **kwargs)

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]], **kwargs) -> Optional[Self]:
        return cls.model_validate(obj, **kwargs) if isinstance(obj, Dict) else None
