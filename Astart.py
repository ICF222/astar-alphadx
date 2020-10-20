from Map import Map
from Point import Point, Node

class Astart():

    def __init__(self, start_pos_, goal_pos_, map_, height_, width_):
        
        self.start_pos = start_pos_
        self.goal_pos = goal_pos_
        self.cost = 0
        self.map = map_
        self.height = height_
        self.width = width_
        #Definir una estructura para guardar la open y close list
        self.lista_nodos = Lista_nodos()
        self.solution_path = []

        #self.open_list = 
        #self.close_list = 

    def FindPath(self):
        #Por defecto siempre abrirá el primer nodo
        self.lista_nodos.abrir_nodo(self.start_pos.x, self.start_pos.y, self.goal_pos)
        #Mientras queden nodos abiertos y no se haya llegado a la meta, se irán cerrándo otros nodos los cuales abrirán sus vecinos.
        #En la práctica, nunca se quedará sin nodos abiertos... porque son todos los casos factibles.
        while(not(self.check_goal()) and len(self.lista_nodos.nodos_abiertos)!= 0):
            self.lista_nodos.cerrar_nodo(self.map, self.height, self.width, self.goal_pos)

        #El último nodo
        if(len(self.lista_nodos.nodos_abiertos)!= 0):
            self.solution_path.append(self.lista_nodos.nodos_abiertos[(self.goal_pos.x, self.goal_pos.y)])
            while(self.solution_path[-1].padre != None):
                self.solution_path.append(self.solution_path[-1].padre)

            self.solution_path.reverse()

        self.cost = len(self.solution_path)
        return self.solution_path


    def PrintPath(self, out_file_):
        #Debe imprimir la solución encontrada
        for i in self.solution_path:
            print(i.x, i.y)
        #Ejemplo salida
        """
        1
        10 10
        10 11
        10 12
        10 13
        11 13
        """

        pass

    def check_goal(self):
        if((self.goal_pos.x, self.goal_pos.y) in self.lista_nodos.nodos_abiertos.keys()):
            return True
        else:
            return False

class Lista_nodos():
    def __init__(self):
        self.nodos_abiertos = dict()
        self.nodos_cerrados = dict()

    def abrir_nodo(self, x_=0, y_=0, destino_=Point(0, 0), padre_=None):
        if ((x_, y_) not in self.nodos_abiertos.keys() and (x_, y_) not in self.nodos_cerrados.keys()):
        #if ((x_, y_) not in self.nodos_abiertos.keys()):
            nodo = Node(x_, y_, padre_, destino_)
            self.nodos_abiertos[(x_, y_)] = nodo

    def cerrar_nodo(self, mapa_, height_, width_, destino_):
        indice = None
        min = None
        for i in self.nodos_abiertos:
            if (min is None or self.nodos_abiertos[i].f < min):
                indice = i
                min = self.nodos_abiertos[i].f
        # si min es none, quiere decir que no quedaban nodos abiertos, por lo tanto no hay camino posible
        if (min is not None):
            self.nodos_cerrados[indice] = self.nodos_abiertos.pop(indice, None)
            # nodo = self.nodos_abiertos[indice]
            # lista de puntos
            vecinos = self.obtener_vecinos(Point(self.nodos_cerrados[indice].x, self.nodos_cerrados[indice].y), mapa_, height_, width_)
            for punto in vecinos:
                self.abrir_nodo(punto.x, punto.y, destino_, self.nodos_cerrados[indice])

    def obtener_vecinos(self, punto_, mapa_, height_, width_):
        # para 4 conectados
        salida = list()
        if(1 <= punto_.x - 1  <= width_):
            if (mapa_[punto_.y - 1][punto_.x - 1 - 1] == 1):
                salida.append(Point(punto_.x - 1, punto_.y))
        if (1 <= punto_.x + 1 <= width_):
            if (mapa_[punto_.y - 1][punto_.x + 1 - 1] == 1):
                salida.append(Point(punto_.x + 1, punto_.y))
        if (1 <= punto_.y - 1 <= height_):
            if (mapa_[punto_.y -1 - 1][punto_.x - 1] == 1):
                salida.append(Point(punto_.x, punto_.y -1))
        if (1 <= punto_.y + 1 <= height_):
            if (mapa_[punto_.y +1 - 1][punto_.x - 1] == 1):
                salida.append(Point(punto_.x, punto_.y +1))

        return salida


