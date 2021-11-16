# class Elevator:
#
#     def _init_(self, _id: int = None, _speed: float = None, _minFloor: int = None, _maxFloor: int = None,
#                  _closeTime: float = None, _openTime: float = None, _startTime: float = None, _stopTime: float = None,
#                  **kwargs):
#         self._id = _id
#         self._speed = _speed
#         self._minFloor = _minFloor
#         self._maxFloor = _maxFloor
#         self._closeTime = _closeTime
#         self._openTime = _openTime
#         self._startTime = _startTime
#         self._stopTime = _stopTime
#
#     def _str_(self):
#         return f"Elevator: _id:{self._id}, _speed:{self._speed}, _minFloor:{self._minFloor}, _maxFloor:{self._maxFloor}," \
#                f"_closeTime:{self._closeTime}, _openTime:{self._openTime}, _startTime:{self._startTime}, _stopTime:{self._stopTime}"

from call import Call


class Elevator:

    def __init__(self, _dict: dict = None, **kwargs):
        self._id = int(_dict['_id'])
        self._speed = float(_dict['_speed'])
        self._minFloor = int(_dict['_minFloor'])
        self._maxFloor = int(_dict['_maxFloor'])
        self._closeTime = float(_dict['_closeTime'])
        self._openTime = float(_dict['_openTime'])
        self._startTime = float(_dict['_startTime'])
        self._stopTime = float(_dict['_stopTime'])
        self.wait = self._speed * 3
        self.lastcall = None
        self.curr_time = 0
        self.flag = False

    def __str__(self):
        return f"Elevator: _id:{self._id}, _speed:{self._speed}, _minFloor:{self._minFloor}, _maxFloor:{self._maxFloor}," \
               f" _closeTime:{self._closeTime}, _openTime:{self._openTime}, _startTime:{self._startTime}, _stopTime:{self._stopTime}"

    def stoptime(self):
        return self._stopTime + self._openTime + self._closeTime + self._startTime