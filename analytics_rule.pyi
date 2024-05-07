from typing import Any, Dict

from .api_call import ApiCall

class AnalyticsRule(object):
    api_call: ApiCall
    rule_id: str

    def __init__(self, api_call: ApiCall, rule_id: str) -> None: ...
    def _endpoint_path(self) -> str: ...
    def retrieve(self) -> Dict[str, Any]: ...
    def delete(self) -> Dict[str, Any]: ...