
class Point():
    x = 0
    y = 0

    def __init__(self, x_ = 0, y_ = 0):
        self.x = x_
        self.y = y_

class Node(Point):
    padre = None
    h = None
    g = None
    f = None

    def __init__(self, x_ = 0, y_ = 0, padre_ = None, destino_ = Point(0,0)):
        self.x = x_
        self.y = y_
        if(padre_ is None):
            #nodo inicial
            self.padre = None
            self.g = 0
        else:
            self.padre = padre_
            self.g = padre_.g + 1
        self.h = self.__calcular_heuristica(destino_)
        self.f = self.h + self.g

    def __calcular_heuristica(self, destino_):
        #Distancia Manhattan
        return abs(self.x - destino_.x) + abs(self.y - destino_.y)








