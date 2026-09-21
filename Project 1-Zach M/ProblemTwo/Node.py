from typing import Self


class Node:
    _payload:int = -1
    _child_left:Self = None
    _child_right:Self = None

    def __init__(self, payload:int = -1, c_left:Self = None, c_Right:Self = None):
        self.setPayload(payload)
        self.setChildLeft(c_left)
        self.setChildRight(c_Right)


    # getters

    def getPayload(self) -> int:
        return self._payload

    def getChildLeft(self) -> Self:
        return self._child_left

    def getChildRight(self) -> Self:
        return self._child_right

    # setters

    def setPayload(self, payload: int):
        self._payload = payload

    def setChildLeft(self, child_left: Self):
        self._child_left = child_left

    def setChildRight(self, child_right: Self):
        self._child_right = child_right


