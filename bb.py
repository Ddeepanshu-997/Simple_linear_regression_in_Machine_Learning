class temperature:
    def __init__(self,value):
        self._celsius=value
    @property
    def temp(self):
        return self._celsius
    @temp.setter
    def temp(self,value):
        if value < -273:
            raise ValueError("Temperature cannot be set below absolute zero (-273.15°C)")

        self._celsius=value
    def feh(self):
        print((self._celsius* 9/5)+32 ," is the temperature in the faherenheit")
deepak=temperature(-300)
deepak.feh()