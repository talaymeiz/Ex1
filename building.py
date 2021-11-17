import json
from elevator import Elevator


class Building:

    # def init(self, _minFloor: int = None, _maxFloor: int = None, _elevators: list = [], **kwargs):
    #     self._minFloor = _minFloor
    #     self._maxFloor = _maxFloor
    #     for i in _elevators:
    #         elev = Elevator(_elevators[i])
    #         self._elevators.append(elev)

    def __init__(self, file_name: str) -> None:
        try:
            with open(file_name, "r") as f:
                dict_building = json.load(f)
                self._minFloor = dict_building['_minFloor']
                self._maxFloor = dict_building['_maxFloor']
                self._elevators = []
                for i in dict_building['_elevators']:
                    elev = Elevator(i)
                    self._elevators.append(elev)
        except json.decoder.JSONDecodeError:
            print("String could not be converted to JSON")


    def __str__(self):
        elevators = ""
        for i in self._elevators:
            elevators = " " + elevators + i.__str__()
        return f"Building: _minFloor:{self._minFloor}, _maxFloor:{self._maxFloor}, _elevators:{elevators}"