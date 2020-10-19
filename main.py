import argparse
from Map import Map
from Point import Point
from Astart import Astart

# python main.py --vision 11 --map maps/ca_cave.map --start_pos 122.208 --goal_pos 125.209 --out camino.out
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--vision', '-v',help='Nivel de vision del agente')
    parser.add_argument('--map', '-m',help='Nombre del mapa')
    parser.add_argument('--start_pos', '-sp',help='Posición del agente')
    parser.add_argument('--goal_pos', '-gp',help='Posición del objetivo')
    parser.add_argument('--out', '-o',help='Archivo de salida')
    args = parser.parse_args()

    start_pos_x = args.start_pos.split('.')[0]
    start_pos_y = args.start_pos.split('.')[1]

    goal_pos_x = args.goal_pos.split('.')[0]
    goal_pos_y = args.goal_pos.split('.')[1]

    print(f'El agente tiene un nivel de visión de {args.vision}')
    print(f'Mapa a ejecutar {args.map}')

    print(f'El agente se encuentra en {start_pos_x} {start_pos_y}')

    print(f'El objetivo esta en {goal_pos_x} {goal_pos_y}')

    my_map = Map(int(args.vision))
    my_map.Read(args.map)

    
    start_pos = Point(start_pos_x, start_pos_y)
    goal_pos = Point(goal_pos_x, goal_pos_y)

    is_valid_soluction = False

    while not(is_valid_soluction):

        solver = Astart(start_pos, goal_pos, my_map.mapVision)

        posible_path = solver.FindPath()

        is_valid_soluction = my_map.IsValidSolution(posible_path)
        break #Debe borrar este break, esta para el codigo de ejemplo

    print(f'El costo de la solución es {solver.cost}')


    print(f'El camino encontrado debe ir en el archivo {args.out}')
    solver.PrintPath(args.out)
    
    #Ejemplo salida
    """
    10 10
    10 11
    10 12
    10 13
    11 13
    """