# import sys
import csv
import random
import sys

from call import Call
from elevator import Elevator
from building import Building


#
#
# # בהנחה שהקריאות באותו כיוון כמובן
# def shave_up(elev, call, flag):
#     if call.src < elev._minFloor or call.dst < elev._minFloor or call.src > elev._maxFloor or call.dst > elev._maxFloor:
#         return -1
#     if elev.lastcall is None:
#         return 1
#     if flag is True:  # changed direction
#         elev.curr_time += (abs(elev.lastcall.dst - elev.lastcall.src) / elev._speed) + elev.stoptime()
#         if call.src < elev.lastcall.dst:
#             return -1
#         distance = (call.src - elev.lastcall.dst / elev._speed) + elev.stoptime()
#         if elev.curr_time + distance - call.time <= elev.wait:
#             return 1
#     else:
#         if call.src < elev.lastcall.src:
#             return -1
#         distance = (call.src - elev.lastcall.src / elev._speed) + elev.stoptime()
#         if elev.curr_time + distance - call.time <= elev.wait:
#             return 1
#     return -1
#
#
# def shave_down(elev, call, flag):
#     if call.src < elev._minFloor or call.dst < elev._minFloor or call.src > elev._maxFloor or call.dst > elev._maxFloor:
#         return -1
#     if elev.lastcall is None:
#         return 1
#     if flag is True:  # changed direction
#         elev.curr_time += (abs(elev.lastcall.dst - elev.lastcall.src) / elev._speed) + elev.stoptime()
#         if call.src > elev.lastcall.dst:
#             return -1
#         distance = (elev.lastcall.dst - call.src / elev._speed) + elev.stoptime()
#         if elev.curr_time + distance - call.time <= elev.wait:
#             return 1
#     else:
#         if call.src > elev.lastcall.src:
#             return -1
#         distance = (elev.lastcall.src - call.src / elev._speed) + elev.stoptime()
#         if elev.curr_time + distance - call.time <= elev.wait:
#             return 1
#     return -1
#
#
def read_calls(file_path: str = None):
    calls = []
    with open(file_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            call = Call(row)
            calls.append(call)
    return calls


def output(calls: list = [], file_n: str = ''):
    with open(file_n, 'w', newline="") as f:
        writer = csv.writer(f)
        for call in calls:
            row = call.into_list()
            writer.writerow(row)


# # def algo_random(building: Building = None, calls: list = [], file_name: str = ''):
# #     for call in calls:
# #         call.elev = random.randrange(1, len(building._elevators) + 1)
# #     output(calls, file_name)


def elev_flag(flag: int = 0, num_elev: int = 0, building: Building = None):
    if flag == num_elev:
        return 0
    return flag


def worth(call: Call = None, last_call: Call = None, elev: Elevator = None):
    if last_call is None:
        return True
    if call.direction != last_call.direction:
        return False
    if call.time - last_call.time <= 3:
        if call.direction == 1:
            if 5 > call.src - last_call.src >= 0:
                return True
        if call.direction == -1:
            if 5 > last_call.src - call.src >= 0:
                return True
        else:
            return False
    # if call.time - last_call.time < time_dist(elev, call, last_call) < call.time - last_call.time + 5:
    #     return True
    return False


def time_dist(elev: Elevator, call_a: Call, call_b: Call):
    time = 0
    time += elev._closeTime + elev._startTime + abs(call_a.src - call_b.src)/elev._speed + elev._stopTime + elev._openTime
    return time

def algotipesh(building: Building = None, calls: list = [], file_name: str = ''):
    num_elev = len(building._elevators)
    flag = elev_flag(0, num_elev)
    elev_in_flag = building._elevators[flag]
    last_call = None

    for call in calls:
        if worth(call, last_call, elev_in_flag):
            call.elev = building._elevators[flag]._id
        else:
            flag = elev_flag(flag + 1, num_elev)
            call.elev = building._elevators[flag]._id
        last_call = call
    output(calls, file_name)

    # def algosh(building: Building = None, calls: list = [],file_name: str = ''):
    #     calls_up = []
    #     calls_down = []
    #     for i in calls:
    #         if i.direction > 0:
    #             calls_up.append(i)
    #         else:
    #             calls_down.append(i)
    #
    #     num_up = len(calls_up)
    #     num_down = len(calls_down)
    #     num_elevators = len(building._elevators)
    #     up_elev = round((num_up * num_elevators) / (num_up + num_down), 0)
    #     down_elev = round((num_down * num_elevators) / (num_up + num_down), 0)
    #     a=0
    #     while a<5:
    #         a +=1
    #         up = 0
    #         down = 0
    #         direction = True
    #
    #         for elev in building._elevators:
    #             if direction:
    #                 for call in calls_up:
    #                     if elev.lastcall is None:
    #                         last = call
    #                     else:
    #                         last = elev.lastcall
    #                     if shave_up(elev, call, elev.flag) > 0:
    #                         call.elev = elev._id
    #                         elev.curr_time = max(last.time, elev.curr_time) + (
    #                                     abs(last.src - call.src) / elev._speed) + elev.stoptime()
    #                         elev.lastcall = call
    #                         calls_up.remove(call)
    #                         elev.flag = False
    #                 elev.flag = True
    #                 for call in calls_down:
    #                     if elev.lastcall is None:
    #                         last = call
    #                     else:
    #                         last = elev.lastcall
    #                     if shave_down(elev, call, elev.flag) > 0:
    #                         call.elev = elev._id
    #                         elev.curr_time = max(last.time, elev.curr_time) + (
    #                                 abs(last.src - call.src) / elev._speed) + elev.stoptime()
    #                         elev.lastcall = call
    #                         calls_down.remove(call)
    #                         elev.flag = False
    #                 elev.flag = True
    #                 up += 1
    #                 if down_elev != down:
    #                     direction = False
    #
    #
    #             else:
    #                 for call in calls_down:
    #                     if elev.lastcall is None:
    #                         last = call
    #                     else:
    #                         last = elev.lastcall
    #                     if shave_down(elev, call, elev.flag) > 0:
    #                         call.elev = elev._id
    #                         elev.curr_time = max(last.time, elev.curr_time) + (
    #                                 abs(last.src - call.src) / elev._speed) + elev.stoptime()
    #                         elev.lastcall = call
    #                         calls_down.remove(call)
    #                         elev.flag = False
    #                 elev.flag = True
    #                 for call in calls_up:
    #                     if elev.lastcall is None:
    #                         last = call
    #                     else:
    #                         last = elev.lastcall
    #                     if shave_up(elev, call, elev.flag) > 0:
    #                         call.elev = elev._id
    #                         elev.curr_time = max(last.time, elev.curr_time) + (
    #                                 abs(last.src - call.src) / elev._speed) + elev.stoptime()
    #                         elev.lastcall = call
    #                         calls_up.remove(call)
    #                         elev.flag = False
    #                 elev.flag = True
    #                 down += 1
    #                 if up_elev != up:
    #                     direction = True
    #     output(calls,file_name)
    #
    #


if __name__ == '__main__':
    calls = read_calls(r'Calls_b.csv')
    building = Building(r'B3.json')
    output_file = 'output.csv'
    algotipesh(building, calls, output_file)
