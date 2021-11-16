class Call:

    def __init__(self, row: list = None):
        x = row[1].split(',')
        self.time = float(x[1])
        self.src = int(x[2])
        self.dst = int(x[3])
        self.elev = int(x[5])
        if self.dst - self.src > 0:
            self.direction = 1
        else:
            self.direction = -1

    def __str__(self):
        return f'time: {self.time}, src: {self.src}, dst: {self.dst}, elev:{self.elev}, direction:{self.direction}.'

    def __repr__(self):
        return f'time: {self.time}, src: {self.src}, dst: {self.dst}, elev:{self.elev}, direction:{self.direction}.'

    def into_list(self):
        return ['Elevator call', f'{self.time}', f'{self.src}', f'{self.dst}', '0', f'{self.elev}']