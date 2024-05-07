from typing import Any, Union

class TypesenseClientError(IOError):
    def __init__(self, *args: Union[str, bytes, int], **kwargs: Any) -> None: ...

class ConfigError(TypesenseClientError): ...
class Timeout(TypesenseClientError): ...
class RequestMalformed(TypesenseClientError): ...
class RequestUnauthorized(TypesenseClientError): ...
class RequestForbidden(TypesenseClientError): ...
class ObjectNotFound(TypesenseClientError): ...
class ObjectAlreadyExists(TypesenseClientError): ...
class ObjectUnprocessable(TypesenseClientError): ...
class ServerError(TypesenseClientError): ...
class ServiceUnavailable(TypesenseClientError): ...
class HTTPStatus0Error(TypesenseClientError): ...
class InvalidParameter(TypesenseClientError): ...
