from typing import List

from typing import List

import event
import storage

class DBException(Exception):
    pass

class NoteDB:
    def __init__(self):
        self._storage = storage.LocalStorage()

    def create(self, note: event.Calendar) -> str:
        try:
            return self._storage.create(note)
        except Exception as ex:
            raise DBException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[event.Calendar]:
        try:
            return self._storage.list()
        except Exception as ex:
            raise DBException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> event.Calendar:
        try:
            return self._storage.read(_id)
        except Exception as ex:
            raise DBException(f"failed READ operation with: {ex}")

    def update(self, _id: str, note: event.Calendar):
        try:
            return self._storage.update(_id, note)
        except Exception as ex:
            raise DBException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._storage.delete(_id)
        except Exception as ex:
            raise DBException(f"failed DELETE operation with: {ex}")
