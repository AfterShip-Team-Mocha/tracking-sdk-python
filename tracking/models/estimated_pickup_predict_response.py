# coding: utf-8
#
# This code was auto generated by AfterShip SDK Generator.
# Do not edit the class manually.

from __future__ import annotations
import pprint

from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional
from typing_extensions import Self

from tracking.models.order_processing_time_estimated_pickup_predict_response import (
    OrderProcessingTimeEstimatedPickupPredictResponse,
)


class EstimatedPickupPredictResponse(BaseModel):
    """
    EstimatedPickupPredictResponse
    """  # noqa: E501

    order_time: Optional[str] = None
    order_cutoff_time: Optional[str] = None
    business_days: Optional[List[int]] = None
    order_processing_time: Optional[OrderProcessingTimeEstimatedPickupPredictResponse] = None
    pickup_time: Optional[str] = None

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
