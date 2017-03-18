from point.py import point
from path.py import path
from code.py import code
from motor.py import motor, sensor, commander, cursor
from tools.py import tools_point, tools_2d


class draw():
    def __init__(self, data_cursor):
        self.Cursor = cursor(data_cursor)
        self.CodeToExecute = code()
        self.GCodeToExecute = []
        self.Tool = tools_point()

    def _decode_code(self):
        self.CodeToExecute._decode_data(code)

    def _decode_gcode(self):
        pass

    def _generate_road(self):
        self.CodeToExecute._ben_ben()

    def _execute(self):
        for point in CodeToExecute.PointByPointRoad:
            ####
            self.Cursor._move_axe_one_step(self.Tool._get_axe_sens(self.Cursor.Position, point))
