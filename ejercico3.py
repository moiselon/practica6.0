class ClaseA:
  def __init__(self):
      self.claseA = "Esa es la clase A"
      print(self.claseA)

class ClaseB(ClaseA):
  def __init__(self):
    super().__init__()
    self.claseB  = "Esa es la clase B"
    print(self.claseB)

class ClaseC(ClaseB):
  def init(self):
    super().__init__()
    self.claseC = "Esa es la clase C"
    print(self.claseC)

txt = ClaseC()

print(txt)