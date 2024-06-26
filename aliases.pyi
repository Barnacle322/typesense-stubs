from typing import Any, Dict

from .alias import Alias
from .api_call import ApiCall

class Aliases(object):
    RESOURCE_PATH: str
    api_call: ApiCall
    aliases: Dict[str, Alias]

    def __init__(self, api_call: ApiCall) -> None: ...
    def __getitem__(self, name: str) -> Alias: ...
    def _endpoint_path(self, alias_name: str) -> str: ...
    def upsert(self, name: str, mapping: Dict[str, Any]) -> Dict[str, Any]: ...
    def retrieve(self) -> Dict[str, Any]: ...
