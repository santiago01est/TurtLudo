class Casilla:
    def __init__(self, id, num, pos_x, pos_y):
        self.id = id
        self.num = num
        self.pos_x = pos_x
        self.pos_y = pos_y

    def get_id(self):
        return self.id