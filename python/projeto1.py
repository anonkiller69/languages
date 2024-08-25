from direct.showbase.ShowBase import ShowBase
from panda3d.core import LVector3

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Carrega um modelo de panda
        self.panda = self.loader.loadModel("panda")
        self.panda.reparentTo(self.render)

        # Define a posição e escala do panda
        self.panda.setPos(LVector3(0, 10, 0))
        self.panda.setScale(0.5, 0.5, 0.5)

        # Adiciona rotação contínua ao panda
        self.panda.hprInterval(3, LVector3(360, 0, 0)).loop()

app = MyApp()
app.run()
