from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero
from panda3d.core import Point3
from direct.showbase.ShowBase import ShowBase
import pandas as pd

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()

        # Завантажуємо модель .obj
        self.hero = self.loader.loadModel('srb2-metal-sonic.obj')  # Вказуємо шлях до моделі .obj
        self.hero.setColor(1, 0.5, 0)  # Встановлюємо колір моделі
        self.hero.setScale(0.3)  # Масштабування моделі
        self.hero.setPos(0, 10, 0)  # Позиція моделі
        self.hero.reparentTo(self.render)  # Додаємо модель до сцени

        # Позиціюємо камеру
        self.camera.setPos(0, -20, 3)
        self.camera.lookAt(self.hero)  # Камера дивиться на модель

app = MyApp()
app.run()

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager(self)  # Передаємо об'єкт ShowBase до Mapmanager
        self.camLens.setFov(90)  # Встановлюємо поле огляду камери
        self.land.addBlock((0, 0, 0))
        self.land.loadLand("land.txt")
        self.hero = Hero((0, 10, 0),self.land)

game = Game()
game.run()