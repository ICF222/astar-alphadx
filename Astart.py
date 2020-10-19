from Map import Map
from Point import Point

class Astart():

    def __init__(self, start_pos_, goal_pos_, map_):
        
        self.start_pos = start_pos_
        self.goal_pos_ = goal_pos_
        self.cost = 0
        self.map = map_
        self.solution_path = []
        #Definir una estructura para guardar la open y close list
        
        #self.open_list = 
        #self.close_list = 

    def FindPath(self):
        # Debe buscar el camino utilizando A* en entregar un camino

        #ejemplo
        path = [0,1,2]
        return path

    def PrintPath(self, out_file_):
        #Debe imprimir la solución encontrada

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
