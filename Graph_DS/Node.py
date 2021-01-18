from typing import Any, Dict, Tuple, Union
import json
from random import *


class Node:
    def __init__(self,
                 key: int,
                 pos: Union[Tuple[float, float, float], str, None] = None) -> None:
        if pos is None:
            pos = (random(), random(), random())
        self.__key = key
        if isinstance(pos, str):
            self.__pos = tuple([float(point) for point in pos.split(',')])
        else:
            self.__pos = pos

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Node) and o.__key == self.__key:
            return True
        return False

    def __hash__(self) -> int:
        return hash(self.__key)

    def dict(self) -> Dict[str, Any]:
        return {
            "id": self.__key,
            "pos": "{},{},{}".format(*self.__pos)
        }

    def __str__(self) -> str:
        return json.dumps(self.dict())

    def __repr__(self) -> str:
        return self.__str__()

    @ property
    def id(self):
        return self.__key

    def getPos(self) -> Tuple[float, float, float]:
        return self.__pos

    def setPos(self, pos: Union[Tuple[float, float, float], str, None] = None) -> None:
        if pos is None:
            pos = (random(), random(), random())
        if isinstance(pos, str):
            self.__pos = tuple([float(point) for point in pos.split(',')])
        else:
            self.__pos = pos

    pos = property(getPos, setPos)
