from implib import tools
from implib import gpiotools
from point import point

class motor():
    #Motor Class : input pins
    #Methods :
    # _move : input steps
    # _move_steps : input steps
    # _set_pins : input steps

    """   this section still need some work
    changing gpio controll to class in gpiotools """

    def __init__(self, pins):
        self.Pins = pins

    def _move(self, steps):
        #still needs to be defined
        pass

    def _move_steps(self, a):
        self._move(a)

    def _set_pins(self, pins):
        self.Pins = pins

class sensor():
    #Sensor Class : input pin
    #Methods :
    # _status : output Boolean
    # _set_pins : input pins

    def __init__(self, pin):
        self.Pin = pin

    def _status(self):
        pass

    def _set_pin(self, pin):
        self.Pin = pin

class commander():
    #Commander Class : input name ,pins ,step ,sensorpin
    #Atributes : Name , Motor , Sensor_Pin , Home, Pos, Adjusted_Step
    #Methods
    #_set_motor_pins : intput pins
    #_set_sensor_pin : input pin
    #_define_step_unity : input step
    #_pin_status
    #_move_one_step : intput sens
    #_is_home
    #_home

    def __init__(self, name, pins, step, sensorpin):
        self.Motor = motor(pins)
        self.Name = name
        self.Sensor_Pin = sensor(sensorpin)
        self.Home = False
        self.Pos = 0
        self.Adjusted_Step = step

    def _set_motor_pins(self, pins):
        self.Motor.Pins = pins

    def _set_sensor_pin(self, pin):
        self.Sensor_Pin._set_pin(pin)

    def _define_step_unity(self, step):
        self.Motor._movesteps(step)
        self.Adjusted_Step = step

    def _pin_status(self):
        return self.Sensor_Pin._status()

    def _move_one_step(self, sens):
        self.Motor._movesteps(self.Ajusted_Step*sens)

    def _is_home(self):
        return self.Home

    def _home(self):
        #some work her eplz#
        # needs to relate sensor pin and motor to find home position
        pass

class cursor():
    #Cursor Class : *args format "name.1-1-1-1.8.5"
    #Methods :
    #_actual_position
    #_home
    #_home_all
    #_move_axe_one_step : input axe sens

    def __init__(self, *args):
        self.CommandersList = []
        self.ToolDecrypt = tools_decrypt()
        for i, j in enumerate(args):
            self.CommanderList.append(commander(ToolDecrypt._infocom(j)))
        self.Type = len(self.CommandersList)
        self.Position = point()

    def _actual_position(self):
        return self.Position.xyz()

    def _home(self, axe):
        self.CommanderList[axe]._home()

    def _home_all(self):
        for i in self.CommanderList:
            i._home()

    def _move_axe_one_step(self, axe, sens):
        self.CommanderList[axe]._move_one_step(sens)
