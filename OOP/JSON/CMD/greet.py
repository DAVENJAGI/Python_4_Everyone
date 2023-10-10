import cmd
"""simple command interpretor"""

class HelloWorld(cmd.Cmd):
    """simple command processor example"""

    FRIENDS = [ 'Alice', 'Ashton', 'Adam', 'Barbara', 'Dave' ]

    def do_hello(self, person):
        """greet the person"""

        if person and person in self.FRIENDS:
            greeting = 'hi, %s!' % person
        elif person:
            greeting = "hello, " + person
        else:
            greeting = 'hello'
        print(greeting)

    def complete_greet(self, text, line, begidx, endidx):
        if not text:
            completion = self.FRIENDS[:]
        else:
            completions = [ f
                           for f in self.FRIENDS
                           if f.startswith(text) ]
            return completions

    def do_EOF(self, line):
        return True


if __name__ == "__main__":
    HelloWorld().cmdloop()
