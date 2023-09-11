class Circuit:
    def __init__(self, voltage, current):
        self.voltage = voltage
        self.current = current


    def resistance(self):
        return self.voltage/self.current
    
    def capacitance(self):
        return self.voltage/(self.current * 2 * 3.1426)

   
b = float(input("Voltage: "))
a = float(input("Current: "))

x=Circuit(b, a)

res=x.resistance()
cap=x.capacitance()
print("Resistance: ", res)
print("Capacitance: ", cap)
