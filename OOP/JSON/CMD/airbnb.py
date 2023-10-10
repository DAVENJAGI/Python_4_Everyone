#!/usr/bin/python3
import cmd

class MyConsole(cmd.Cmd):
    prompt = "HBNB : "
    
    def do_close(self, exit):
        print("Do you want to exit")

if __name__ == "__main__":
    MyConsole().cmdloop()
