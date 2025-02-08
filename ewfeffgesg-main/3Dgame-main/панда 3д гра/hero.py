class Hero():
    def try_move(self, angle):
        pos = self.look_at(angle)
        if self.land.isEmpty()