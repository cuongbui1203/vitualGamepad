from asyncio import events
import inputs
import math
import threading

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):
        self.gamepad = inputs.devices.gamepads[0]
        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0
        self.Hat0X = 0
        self.Hat0Y = 0
        
        self.vibrationLeft = 0
        self.vibrationRight = 0
        self.streng = 0
        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    def vibration(self,left,right,streng):
        self.vibrationLeft = left
        self.vibrationRight = right
        self.streng = streng

    def read(self): # return the buttons/triggers that you care about in this methode
        x1 = self.LeftJoystickX
        y1 = self.LeftJoystickY
        if(y1>-3.12e-5 and y1<0):
            y1 = 0.0
        
        x2 = self.RightJoystickX
        y2 = self.RightJoystickY
        if(y2>-3.12e-5 and y2<0):
            y2 = 0.0
        a = self.A
        b = self.B # b=1, x=2
        x = self.X
        y = self.Y
        rb = self.Hat0X
        lb = self.Hat0Y
        rt = self.RightDPad
        lt = self.DownDPad
        return [x1, y1,x2,y2, a, b,x,y, rb,rt,lb,lt]

    def vibration(self,left:float,right:float):
        if(left == 0 and right == 0):
            self.gamepad._stop_vibration_win()
        

    def _monitor_controller(self):
        self.gamepad = inputs.devices.gamepads[0]
        # self.gamepad._start_vibration_win(1,1)
        while True:
            events = self.gamepad.read()
            
            for event in events:
                print(event.code)
                print(event.state)
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                    if(self.LeftJoystickY>-3.12e-5 and self.LeftJoystickY<0):
                        self.LeftJoystickY = 0.0
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                    if(self.RightJoystickY>-3.12e-5 and self.RightJoystickY<0):
                        self.RightJoystickY = 0.0
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.X = event.state
                elif event.code == 'BTN_WEST':
                    self.Y = event.state
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Start = event.state
                elif event.code == 'BTN_START':
                    self.Back = event.state
                elif event.code == 'ABS_HAT0X':
                    self.Hat0X = event.state
                elif event.code == 'ABS_HAT0Y':
                    self.Hat0Y = event.state
                
                # gamepad.set_vibration(1,1,0.5)

if __name__ == '__main__':
    joy = XboxController()
    
    while True:
        pass
        # print(joy.read())
        