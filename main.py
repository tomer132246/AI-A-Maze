from Robot import *
from MazeProblem import *
from Animation import Animation
from Heuristics import *
from Utilities import *
from Experiments import *


if __name__ == "__main__":
    #test_robot(BreadthFirstSearchRobot, [0, 1, 2, 3, 4, 5])
    #(UniformCostSearchRobot, [0, 1, 2, 3, 4, 5])


    test_robot(UniformCostSearchRobot, [99])
    test_robot(WAStartRobot, [99], heuristic=center_manhattan_heuristic)
    test_robot(WAStartRobot, [99], heuristic=tail_manhattan_heuristic)




