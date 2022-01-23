from api.models import DataPoint


def get_data_points(from_timestamp: str = None, to_timestamp: str = None) -> [DataPoint]:
    if not from_timestamp and not to_timestamp:
        return DataPoint.objects.all()
    filter_kwargs = {}
    if from_timestamp:
        filter_kwargs['t__gte'] = int(from_timestamp)
    if to_timestamp:
        filter_kwargs['t__lte'] = int(to_timestamp)
    return DataPoint.objects.filter(**filter_kwargs)


def get_data_points_for_name(datapoint_name: str = None, from_timestamp: str = None,
                             to_timestamp: str = None) -> [DataPoint]:
    filter_kwargs = {'name': datapoint_name}
    if from_timestamp:
        filter_kwargs['t__gte'] = int(from_timestamp)
    if to_timestamp:
        filter_kwargs['t__lte'] = int(to_timestamp)
    return DataPoint.objects.filter(**filter_kwargs)


def is_datapoint_name_in_db(datapoint_name: str) -> bool:
    return DataPoint.objects.filter(name=datapoint_name).exists()


def is_request_data_valid(from_timestamp: str, to_timestamp: str) -> bool:
    if from_timestamp and not from_timestamp.isdigit():
        return False
    if to_timestamp and not to_timestamp.isdigit():
        return False
    return True
