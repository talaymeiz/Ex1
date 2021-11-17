import csv
import sys

from call import Call
from elevator import Elevator
from building import Building


def read_calls(file_path: str = None):
    calls = []
    try:
        with open(file_path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                call = Call(row)
                calls.append(call)
        return calls
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise


def output(calls: list = [], file_n: str = ''):
    try:
        with open(file_n, 'w', newline="") as f:
            writer = csv.writer(f)
            for call in calls:
                row = call.into_list()
                writer.writerow(row)
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise


def elev_flag(flag: int = 0, num_elev: int = 0):
    if flag == num_elev:
        return 0
    return flag


def worth(call: Call = None, last_call: Call = None):

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
    time += elev._closeTime + elev._startTime + abs(
        call_a.src - call_b.src) / elev._speed + elev._stopTime + elev._openTime
    return time


def algo(building: Building = None, calls: list = [], file_name: str = ''):
    num_elev = len(building._elevators)
    flag = elev_flag(0, num_elev)
    elev_in_flag = building._elevators[flag]
    last_call = None

    for call in calls:
        if worth(call, last_call, elev_in_flag):
            call.elev = building._elevators[flag]._id
            building._elevators[flag].last_call = call
        else:
            flag = elev_flag(flag + 1, num_elev)
            call.elev = building._elevators[flag]._id
            building._elevators[flag].last_call = call
        last_call = call
    output(calls, file_name)

def worth_long(call: Call = None, listelev: list = [], elev_in_flag: Elevator = None):
    # for 70
    newlist = sorted(listelev)
    for elev in newlist:
        if elev.last_call is not None and call.direction == elev.last_call:
            elev.lastcall = call
            return elev._id
    elev_in_flag.lastcall = call
    return elev_in_flag._id


if __name__ == '__main__':
    # calls = read_calls(r'Calls_c.csv')
    # building = Building(r'B3.json')
    # output_file = 'output.csv'

    building_name = sys.argv[1]
    calls_name = sys.argv[2]
    output_name = sys.argv[3]

    calls = read_calls(calls_name)
    building = Building(building_name)

    algo(building, calls, output_name)
    # algo(building, calls, output_file)

