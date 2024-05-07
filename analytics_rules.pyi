from typing import Any, Dict, Optional

from .analytics_rule import AnalyticsRule
from .api_call import ApiCall

class AnalyticsRules(object):
    RESOURCE_PATH: str
    api_call: ApiCall
    rules: Dict[str, AnalyticsRule]

    def __init__(self, api_call: ApiCall) -> None: ...
    def __getitem__(self, rule_id: str) -> AnalyticsRule: ...
    def create(
        self, rule: Dict[str, Any], params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]: ...
    def upsert(self, id: str, rule: Dict[str, Any]) -> Dict[str, Any]: ...
    def retrieve(self) -> Dict[str, Any]: ...
