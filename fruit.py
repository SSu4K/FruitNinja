G = 20

class Fruit:
    def __init__(self, size, color, pos, speed):
        self.pos=pos
        self.size = size
        self.color = color
        self.speed = speed

    def move(self, dt):
        self.pos[0]+=self.speed[0]
        self.pos[1]+=self.speed[1]
        self.speed[1]+=G*dt


    