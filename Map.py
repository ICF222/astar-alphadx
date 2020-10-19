
class Map():

    height = 0
    width = 0

    mapOriginal = [[]]
    mapVision = [[]]
    
    def __init__(self, vision_):
        self.vision = vision_

    def Read(self, filename_):

        aux_info_map = []
        with open(filename_, 'r') as file:
            for num, line in enumerate(file, start= 1):
                if num == 2:
                    self.height = int(line.split(' ')[1])
                if num == 3:
                    self.width = int(line.split(' ')[1])
                
                if num > 4:
                    aux_arr = []
                    for element in line:
                        if element == '@' or element == 'T':
                            aux_arr.append(0)    
                        elif element == '.':
                            aux_arr.append(1)
                    aux_info_map.append(aux_arr)
        
        self.mapVision = [[1 for i in range(self.width)] for i in range(self.height)]

        self.mapOriginal = aux_info_map


    def IsValidSolution(self, posible_path_):
                    
        for path in posible_path_:
            #Actualizar el mapa y preguntar si el camino es posible o no
            self.UpdateMap(path)
            pass        
        
        is_valid = False

        return is_valid


    def UpdateMap(self, path_):
        #Actualizar el mapa con el rango de visión
        pass