from typing import Any, Dict, Optional

from .api_call import ApiCall

class Document(object):
    api_call: ApiCall
    collection_name: str
    document_id: str

    def __init__(
        self, api_call: ApiCall, collection_name: str, document_id: str
    ) -> None: ...
    def _endpoint_path(self) -> str: ...
    def retrieve(self) -> Dict[str, Any]: ...
    def update(
        self, document: Dict[str, Any], params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]: ...
    def delete(self) -> Dict[str, Any]: ...
