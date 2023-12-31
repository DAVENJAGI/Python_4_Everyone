import cmd

class HelloWorld(cmd.Cmd):
    """Simple command provessor example"""

    prompt = 'prompt: '
    intro = "Simple command processor example."

    doc_header = 'doc_header'
    misc_header = 'misc_header'
    undoc_header = 'undoc_header'

    ruler = '-'

    def do_prompt(self, line):
        """change interactive prompt"""
        self.prompt = line + ': '

    def do_hello(self, person):
        if person:
            print("hello, ", person)
        else:
            print("hello")

    def do_EOF(self, line):
        return True

if __name__ == "__main__":
    HelloWorld().cmdloop()
