# coding=utf8

import tracking
from tracking import exceptions
from tracking import auth

try:
    sdk = tracking.Client(
        tracking.Configuration(
            api_key="asat_870416d3ea2742dba0eb68e23ddfcbe9",
            authentication_type=auth.ApiKey,
        )
    )
    # result = sdk.tracking.get_tracking_by_id("b93c3984c3404910ad565385a5c40a1b")
    # print(result)
    # result = sdk.tracking.get_trackings()
    # print(result)

    # data = tracking.CreateTrackingRequest()
    # data.tracking_number = "<tracking_number>"
    # data.slug = "<slug>"
    # result = sdk.tracking.create_tracking(data)
    # print(result)

    # res = sdk.tracking.delete_tracking_by_id("b93c3984c3404910ad565385a5c40a1b")
    # print(res)
    #
    # result = sdk.tracking.get_trackings(keyword="test")
    # print(result)

    # result = sdk.tracking.get_tracking_by_id("b8ebdc47d885458690cf8347fe56731a")
    # print(result)

    # data = tracking.UpdateTrackingByIdRequest()
    # data.note = "test"
    # result = sdk.tracking.update_tracking_by_id("b8ebdc47d885458690cf8347fe56731a", data)
    # print(result)

    # result = sdk.tracking.retrack_tracking_by_id("b8ebdc47d885458690cf8347fe56731a")
    # print(result)

    # data = tracking.MarkTrackingCompletedByIdRequest()
    # data.reason = "DELIVERED"
    # result = sdk.tracking.mark_tracking_completed_by_id("b8ebdc47d885458690cf8347fe56731a", data)
    # print(result)

    # result = sdk.courier.get_user_couriers()
    # print(result)

    # result = sdk.courier.get_all_couriers()
    # print(result)

    # data = tracking.DetectCourierRequest()
    # data.tracking_number = "1ZFW80170320376216"
    # result = sdk.courier.detect_courier(data)
    # print(result)

    req = tracking.PredictBatchRequest()
    date = tracking.EstimatedDeliveryDateRequest()
    date.slug = "ups"
    date.origin_address = "USA"
    date.destination_address = "USA"

    req.estimated_delivery_dates = [date]
    result = sdk.estimated_delivery_date.predict_batch(req)

    print(result)
except exceptions.InvalidOptionError:
    pass
except exceptions.InvalidApiKeyError:
    pass
except exceptions.RateLimitExceedError:
    pass
