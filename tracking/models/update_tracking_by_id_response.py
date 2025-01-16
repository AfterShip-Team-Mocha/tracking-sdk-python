# coding: utf-8
#
# This code was auto generated by AfterShip SDK Generator.
# Do not edit the class manually.

from __future__ import annotations
import pprint

from pydantic import BaseModel
from typing import Any, Dict, List, Optional
from typing_extensions import Self

from tracking.models.courier_estimated_delivery_date_update_tracking_by_id_response import (
    CourierEstimatedDeliveryDateUpdateTrackingByIdResponse,
)
from tracking.models.shipment_weight_update_tracking_by_id_response import (
    ShipmentWeightUpdateTrackingByIdResponse,
)
from tracking.models.tag_v1 import TagV1
from tracking.models.checkpoint import Checkpoint
from tracking.models.aftership_estimated_delivery_date_update_tracking_by_id_response import (
    AftershipEstimatedDeliveryDateUpdateTrackingByIdResponse,
)
from tracking.models.custom_estimated_delivery_date_update_tracking_by_id_response import (
    CustomEstimatedDeliveryDateUpdateTrackingByIdResponse,
)
from tracking.models.first_estimated_delivery_update_tracking_by_id_response import (
    FirstEstimatedDeliveryUpdateTrackingByIdResponse,
)
from tracking.models.latest_estimated_delivery_update_tracking_by_id_response import (
    LatestEstimatedDeliveryUpdateTrackingByIdResponse,
)
from tracking.models.carbon_emissions_update_tracking_by_id_response import (
    CarbonEmissionsUpdateTrackingByIdResponse,
)
from tracking.models.first_mile_update_tracking_by_id_response import (
    FirstMileUpdateTrackingByIdResponse,
)
from tracking.models.last_mile_update_tracking_by_id_response import (
    LastMileUpdateTrackingByIdResponse,
)
from tracking.models.customers_update_tracking_by_id_response import (
    CustomersUpdateTrackingByIdResponse,
)


class UpdateTrackingByIdResponse(BaseModel):
    """
    Object describes the tracking information.<div style="display:none; height: 0"></div>
    """  # noqa: E501

    id: Optional[str] = None
    legacy_id: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    tracking_number: Optional[str] = None
    slug: Optional[str] = None
    active: Optional[bool] = None
    custom_fields: Optional[Any] = None
    transit_time: Optional[int] = None
    origin_country_region: Optional[str] = None
    origin_state: Optional[str] = None
    origin_city: Optional[str] = None
    origin_postal_code: Optional[str] = None
    origin_raw_location: Optional[str] = None
    destination_country_region: Optional[str] = None
    destination_state: Optional[str] = None
    destination_city: Optional[str] = None
    destination_postal_code: Optional[str] = None
    destination_raw_location: Optional[str] = None
    courier_destination_country_region: Optional[str] = None
    courier_estimated_delivery_date: Optional[
        CourierEstimatedDeliveryDateUpdateTrackingByIdResponse
    ] = None
    note: Optional[str] = None
    order_id: Optional[str] = None
    order_id_path: Optional[str] = None
    order_date: Optional[str] = None
    shipment_package_count: Optional[float] = None
    shipment_pickup_date: Optional[str] = None
    shipment_delivery_date: Optional[str] = None
    shipment_type: Optional[str] = None
    shipment_weight: Optional[ShipmentWeightUpdateTrackingByIdResponse] = None
    signed_by: Optional[str] = None
    source: Optional[str] = None
    tag: Optional[TagV1] = None
    subtag: Optional[str] = None
    subtag_message: Optional[str] = None
    title: Optional[str] = None
    tracked_count: Optional[float] = None
    last_mile_tracking_supported: Optional[bool] = None
    language: Optional[str] = None
    unique_token: Optional[str] = None
    checkpoints: Optional[List[Checkpoint]] = None
    subscribed_smses: Optional[List[str]] = None
    subscribed_emails: Optional[List[str]] = None
    return_to_sender: Optional[bool] = None
    order_promised_delivery_date: Optional[str] = None
    delivery_type: Optional[str] = None
    pickup_location: Optional[str] = None
    pickup_note: Optional[str] = None
    courier_tracking_link: Optional[str] = None
    first_attempted_at: Optional[str] = None
    courier_redirect_link: Optional[str] = None
    tracking_account_number: Optional[str] = None
    tracking_key: Optional[str] = None
    tracking_ship_date: Optional[str] = None
    on_time_status: Optional[str] = None
    on_time_difference: Optional[float] = None
    order_tags: Optional[List[str]] = None
    aftership_estimated_delivery_date: Optional[
        AftershipEstimatedDeliveryDateUpdateTrackingByIdResponse
    ] = None
    custom_estimated_delivery_date: Optional[
        CustomEstimatedDeliveryDateUpdateTrackingByIdResponse
    ] = None
    order_number: Optional[str] = None
    first_estimated_delivery: Optional[FirstEstimatedDeliveryUpdateTrackingByIdResponse] = None
    latest_estimated_delivery: Optional[LatestEstimatedDeliveryUpdateTrackingByIdResponse] = None
    shipment_tags: Optional[List[str]] = None
    courier_connection_id: Optional[str] = None
    tracking_origin_country_region: Optional[str] = None
    tracking_destination_country_region: Optional[str] = None
    tracking_postal_code: Optional[str] = None
    tracking_state: Optional[str] = None
    carbon_emissions: Optional[CarbonEmissionsUpdateTrackingByIdResponse] = None
    location_id: Optional[str] = None
    shipping_method: Optional[str] = None
    failed_delivery_attempts: Optional[int] = None
    signature_requirement: Optional[str] = None
    delivery_location_type: Optional[str] = None
    aftership_tracking_url: Optional[str] = None
    aftership_tracking_order_url: Optional[str] = None
    first_mile: Optional[FirstMileUpdateTrackingByIdResponse] = None
    last_mile: Optional[LastMileUpdateTrackingByIdResponse] = None
    customers: Optional[List[CustomersUpdateTrackingByIdResponse]] = None

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
