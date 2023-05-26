G = 20
RED = (200, 50, 100)

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

    def is_in_bound(self, max_pos):
        if self.pos[0]+self.size < 0 or self.pos[1]+self.size < 0:
            return False
        if self.pos[0]-self.size > max_pos[0] or self.pos[1]-self.size > max_pos[1]:
            return False
        return True
    
    def hit(self):
        self.speed[0] = 0
        self.color=RED
        