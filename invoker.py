from commands import Command

"""Class dedicated to Invoker"""
class Invoker:
      
    """command method"""
    def command(self, cmd: Command):
        self.cmd = cmd
  
    """execute method"""
    def execute(self):
        return self.cmd.process()
