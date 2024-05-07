from typing import Any, Dict

from .api_call import ApiCall
from .key import Key

class Keys(object):
    RESOURCE_PATH: str
    api_call: ApiCall
    keys: Dict[str, Key]

    def __init__(self, api_call: ApiCall) -> None: ...
    def __getitem__(self, key_id: str) -> Key: ...
    def create(self, schema: Dict[str, Any]) -> Dict[str, Any]: ...
    def generate_scoped_search_key(
        self, search_key: str, parameters: Dict[str, Any]
    ) -> str: ...
    def retrieve(self) -> Dict[str, Any]: ...
