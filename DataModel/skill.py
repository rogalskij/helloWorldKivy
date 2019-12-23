class Skill:

    lvls = [3, 8, 16, 29, 50, 84, 139, 228, 372]

    value = 0
    current_lvl = 0

    def __init__(self):
        return

    def __init__(self, value):
        self.value = value

    def return_lvl(self):
        i = 0
        for x in self.lvls:
            if self.value > x:
                i += 1
                continue
            else:
                break
        return i
