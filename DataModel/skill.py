class Skill:

    lvls = [3, 8, 16, 29, 50, 84, 139, 228, 372]
    txt = ["wiejski głupek", "niezguła", "samouk", "adept", "pomocnik", "wymyslec", "bohater", "mistrz", "guru"]

    value = 0
    current_lvl = 0

    def __init__(self):
        self.current_lvl = self.return_lvl()
        return

    def __init__(self, value):
        self.value = value
        self.current_lvl = self.return_lvl()

    def train(self, value):
        self.value += value
        self.update_lvl()

    def update_lvl(self):
        i = self.current_lvl
        while self.value > self.lvls[i]:
            i += 1
        self.current_lvl = i

    def return_lvl(self):
        i = 0
        for x in self.lvls:
            if self.value > x:
                i += 1
                continue
            else:
                break
        return i
