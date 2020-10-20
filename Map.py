from Point import Point

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

        is_valid = True
        for index, path in enumerate(posible_path_):
            if(self.mapOriginal[path.y -1][path.x -1] == 0):
                is_valid = False
                self.UpdateMap(posible_path_[index - 1])
                break
        return is_valid


    def UpdateMap(self, punto_de_vista):
        x0 = max(1, punto_de_vista.x - self.vision)
        x1 = min(self.width, punto_de_vista.x + self.vision +1)
        y0 = max(1, punto_de_vista.y - self.vision)
        y1 = min(self.height, punto_de_vista.y + self.vision +1)
        for y in range(y0, y1):
            for x in range(x0, x1):
                self.mapVision[y-1][x-1] = self.mapOriginal[y-1][x-1]
                #print(self.mapOriginal[y-1][x-1], end = "")
            #print()
