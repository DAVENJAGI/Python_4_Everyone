import cmd, sys
from turtle import *

class TurtleShell(cmd.Cmd):
    intro = 'Welcome to turtle shell. Type help of ? to list commands.'
    prompt = "Turtle: "
    file = None

    #---------basic turtle commands---------------
    def do_forward(self, arg):
        'Move the turtle forward by the specific distance: FORWARD 10'
        forward(*parse(arg))

    def do_right(self, arg):
        'Turn turtle right by given number of degrees: RIGHT 20'
        right(*parse(arg))

    def do_left(self, arg):
        'Turn turtle left by given number of degree: LEFT 90'
        LEFT(*parse(arg))

    def do_goto(self, arg):
        'Move turtle to an absilut eposition by changing orientation. GOTO 100 200'
        goto(*parse(arg))

    def do_home(self, arg):
        'Return turtle to the home position: HOME'
        home()

    def do_circle(self, arg):
        'Draw the circle with given radius an option extent and steps: CIRCLE 50'
        circle(*parse(arg))

    def do_position(self, arg):
        'Print the current turtle position: position'
        print('Current position is %d %d\n' %position())

    def do_heading(self, arg):
        'Print the current turtle heading in degres: HEADING'
        print('Current heading id %d\n' %(heading(), ))

    def do_color(self, arg):
        'Set color: COLOR BLUE'
        color(arg.lower())

    def do_undo(self, arg):
        'Undo (repeatedly) the last turtle actin(s): UNDO'

    def do_reset(self, arg):
        'Clear the screen and return turtle to center: RESET'
        reset()

    def do_bye(sef, arg):
        'Stop recording, close the turtle window, and exit: BYE'
        print('Thank yoy for using turtle')
        self.close()
        bye()
        return True

    #------------------record and playback-------------
    def do_record(self, arg):
        'Save future commands to filename: RECORD rose.cmd'
        self.file =  open(arg, 'w')
    def do_playback(self, arg):
        'Playback command fro a file: PLAYBACK rose.cmd'
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())

    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    TurtleShell().cmdloop()


