from multiprocessing import set_forkserver_preload
import vgamepad as vg
from test import XboxController

class VDS4(object):
    def __init__(self) -> None:
        self.gamepad = vg.VDS4Gamepad()
        self.joy = XboxController()

    def process(self):
        
        # gamepad.reset()
        # gamepad.update()
            
        if(self.joy.B > 0):
            self.gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
        else:
            self.gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
        if(self.joy.A > 0):
            self.gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
        else:
            self.gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
        if(self.joy.Y > 0):
            self.gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
        else:
            self.gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
        if(self.joy.X > 0):
            self.gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
        else:
            self.gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
        
        if(self.joy.Back > 0):
            self.gamepad.press_button(button=vg.DS4_SPECIAL_BUTTONS.DS4_SPECIAL_BUTTON_TOUCHPAD)
        else:
            self.gamepad.release_button(button=vg.DS4_SPECIAL_BUTTONS.DS4_SPECIAL_BUTTON_TOUCHPAD)
        if(self.joy.Start > 0):
            self.gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_OPTIONS)
        else:
            self.gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_OPTIONS)
        
        if(self.joy.LeftThumb > 0):
            self.gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_THUMB_LEFT)
        else:
            self.gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_THUMB_LEFT)
        if(self.joy.RightThumb > 0):
            self.gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_THUMB_RIGHT)
        else:
            self.gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_THUMB_RIGHT)
        if(self.joy.RightBumper > 0):
            self.gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT)
        else:
            self.gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT)
        if(self.joy.LeftBumper > 0):
            self.gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
        else:
            self.gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
        
        self.gamepad.left_trigger_float(self.joy.LeftTrigger)
        self.gamepad.right_trigger_float(self.joy.RightTrigger)
        
        self.gamepad.left_joystick_float(x_value_float=self.joy.LeftJoystickX,y_value_float=self.joy.LeftJoystickY)
        self.gamepad.right_joystick_float(x_value_float=self.joy.RightJoystickX,y_value_float=self.joy.RightJoystickY)
        
        if(self.joy.Hat0X == 0 and self.joy.Hat0Y == 0):
            self.gamepad.press_button(button=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NONE)
        elif(self.joy.Hat0X<0 and self.joy.Hat0Y==0):
            self.gamepad.press_button(button=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_WEST)
        elif(self.joy.Hat0X > 0 and self.joy.Hat0Y == 0):
            self.gamepad.press_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_EAST)
        elif(self.joy.Hat0X == 0 and self.joy.Hat0Y < 0 ):
            self.gamepad.press_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTH)
        elif(self.joy.Hat0X == 0 and self.joy.Hat0Y>0):
            self.gamepad.press_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_SOUTH)
        
        
        
        self.gamepad.update()

if __name__ == '__main__':
    v = VDS4()
    while (True):
        v.process()