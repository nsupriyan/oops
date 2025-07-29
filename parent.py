class ParentActor:
    def __init__(self, name, Pworth):
        self.Pname = name
        self.Pworth = Pworth
        print(f"{self.Pname} is the parent")

    def Passets(self):
        print(f"{self.Pname} assets are {self.Pworth} cr")

class ChildActor(ParentActor):
    def __init__(self, Pname, Cname, Pworth):
        super().__init__(Pname, Pworth)
        self.Cname = Cname
        print(f"{self.Cname} is came by the reference of {self.Pname}")

    def Cassets(self, worth):
        self.Cworth = worth
        print(f"{self.Cname} is having worth of {self.Cworth} cr")

    def TotalAssets(self):
        print(f"Total assets of {self.Cname} is {self.Pworth + self.Cworth} cr")

# Object creation and method calls
ramcharan = ChildActor("chiranjeevi", "ramcharan", 100)
ramcharan.Cassets(75)
ramcharan.TotalAssets()
ramcharan.Passets()