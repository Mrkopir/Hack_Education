import optparse

class Parcer:
    def __init__(self):
        self.parcer = optparse.OptionParser()
        self.options = None
        self.args = None

    def parce(self):
        self.parcer.add_option("-i", "--interface", dest = "interface", help = "If you need help, you should go to documentation. OLEG PIDARAS")
        
        (self.options, self.args) = self.parcer.parse_args()

        if not self.options.interface:
            self.parcer.error("You need specify 2 arguments INTERFACE(-i) & MAC(-m)")
        
        return self.options