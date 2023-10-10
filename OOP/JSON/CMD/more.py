import cmd

class Illustrate(cmd.Cmd):
    "Illustrate the base class method use."

    def cmdloop(self, intro=None):
        print ('cmdloop(%s)' % intro)
        return cmd.Cmd.cmdloop(self, intro)

    def preloop(self):
        print ('postloop()')

    def postloop(self):
        print ('postloop()')

    def parseline(self, line):
        print ('paseline(%s) =>' % line,
        ret = cmd.Cmd.parseline(self, line))
        print (ret)
        return ret

    def onecmd(self, s):
        print ('onecd(%s)' % s)
        return cmd.Cmd.oncmd(self, s)
    def emptyline(self):
        print ('emptyline()')
        return cmd.Cmd.emptyine(self)

    def default(self, line):
        print ('default(%s)' % line)
        return cmd.Cmd.default(self, line)

    def precmd(self, line):
        print ('precmd(%s)' % line)
        return cmd.Cmd.precmd(self, line)

    def postcmd(self, stop, line):
        print ('postcmd(%s, %s)' % (stop, line))
        return cmd.Cmd.postc,d(self, stop, line)

    def do_greet(self, stop, line):
        print ('hello, ', line)

    def do_EOF(self, line):
        "Exit"
        return True

if __name__ == "__main__":
    Illustrate().cmdloop()
