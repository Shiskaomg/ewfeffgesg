import pstats


class Hero():
    def __init__(self,pos,land):
        self.land = land
        self.hero = self.loader.loadModel('model/metal_sonic_remake.obj')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
        self.mode = True

    
    
    def accept_events(self):
        base.accept('c', self.changeView)
        base.accept('n', self.turn_left)
        base.accept('n'+'-repeat', self.turn_left)
        base.accept('s', self.back)
        base.accept('s' + '-repeat', self.back)
        base.accept('e', self.up)
        base.accept('e' + '-repeat', self.up)
        base.accept('z', self.changeMode)
    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)
    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind

    def changeMode(self):
        if self.mode == True:
            self.mode = False
        else:
            self.mode = True

    

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1.5)
        pos = self.hero.getPos()
        base.mouseInterfaceNide.setPos(-pos[0], -pos[2, - 3])
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = True
        
    def look_at(self, angle):
        from_x = round(self.hero.getX())
        from_y = round(self.hero.getY())
        from_z = round(self.hero.getZ())

        dx, dy = self.hero.sheck_dir(self, angle)

        return from_x + dx, from_y + dy, from_z
    
    def move_to(self,angle):
        if self.mode:
            self.try_move(angle)
        else:
            self.try_move(angle)

    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)
        
    def foward(self):
        pass
    def back(self):
        angle =(self.hero.getH()+180) % 360
        self.move_to(angle)
    def left(self):
        pass
    def right(self):
        pass
    def up(self):
        self.hero.setZ(self.hero.getZ() + 1)

    def try_move(self, angle):
        pos = self.look_at(angle)

    def isEmpty(self, pos):
        blocks = self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True
        self.block.setTag('at', str(pos))
    def findBlocks(self, pos):
        return self.land.findAllMatches("=at=" + str(pos))
    
    def findHighestEmpty(self,pos):
        x, y, z = pos
        z = 1
        while not self.isEmpty((x, y, z)):
            z += 1
        return (x, y, z)