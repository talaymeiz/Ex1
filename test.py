import unittest
from call import Call
from main import worth


class MyTestCase(unittest.TestCase):

    def test_something(self):
        x = ['Elevator', 'call,38.28582116,-4,68,0,-1']
        y = ['Elevator', 'call,39.19202924,-4,6,0,-1']
        z = ['Elevator', 'call,39.19202924,20,6,0,-1']
        call_x = Call(x)
        call_y = Call(y)
        call_z = Call(z)
        self.assertEqual(worth(call_x, call_y), True)
        self.assertEqual(worth(call_z, call_y), False)


if __name__ == '__main__':
    unittest.main()
