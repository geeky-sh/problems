from dataclasses import dataclass
from typing import Optional, Any
import pytest
import time
import functools


def get_timestamp_bucket(timestamp):
    return int(timestamp/500)


cache = {}
def get_cache_key(api_endpoint: str, method: str, service_id: int, tbucket: int):
    return "{api_endpoint}.{method}.{service_id}.{tbucket}".format(
        api_endpoint=api_endpoint, method=method, service_id=service_id, tbucket=tbucket
    )

def put_timestamp(api_endpoint: str, method: str, service_id: int, timestamp: int):
    key = get_cache_key(api_endpoint, method, service_id, get_timestamp_bucket(timestamp))
    if key in cache:
        cache[key] += 1
    else:
        cache[key] = 1

def get_recent_timestamp_count(api_endpoint: str, method: str, service_id: int, timestamp: int):
    key = get_cache_key(api_endpoint, method, service_id, get_timestamp_bucket(timestamp))
    return cache.get(key)

@dataclass
class APIObj:
    service_id: int
    limit: int
    api_endpoint: str
    method: str

@dataclass
class Request:
    url: str
    method: str

def get_api_obj(api_endpoint: str, method: str, service_id: int) -> APIObj:
    return APIObj(service_id=service_id, method=method, api_endpoint=api_endpoint, limit=3)

def api_rate_limiter(api_endpoint: str, method: str, service_id: int):
    timestamp: int = int(time.time())
    api_obj: APIObj = get_api_obj(api_endpoint, method, service_id)
    count = get_recent_timestamp_count(api_endpoint, method, service_id, timestamp)
    if count and count + 1 > api_obj.limit:
        return False
    put_timestamp(api_endpoint, method, service_id, timestamp)
    return True

def api_rate_limiter_decorator(view: Any, service_id: int):
    @functools.wraps(view)
    def wrapper(request: Request, *args, **kwargs):
        api_endpoint = request.url
        method = request.method
        if api_rate_limiter(api_endpoint, method, service_id):
            return view(request, *args, **kwargs)
        raise Exception('API LIMIT REACHED')
    return wrapper  

def test_api_function_limit():
    api_endpoint = "/"
    method = 'GET'
    service_id = 1

    t = int(time.time())
    with pytest.raises(Exception) as e:
        api_rate_limiter(api_endpoint, method, service_id)
        api_rate_limiter(api_endpoint, method, service_id)
        api_rate_limiter(api_endpoint, method, service_id)
        api_rate_limiter(api_endpoint, method, service_id)
    assert get_recent_timestamp_count(api_endpoint, method, service_id, t) == 3





