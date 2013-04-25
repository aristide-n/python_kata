__author__ = 'Aristide'

# Coordinates
X_COORD = 0
Y_COORD = 1

# Directions
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

DIRECTIONS_LIST = [NORTH, SOUTH, EAST, WEST]

class Planet:
    """
    Abstraction of a planet.

    Doctests:
        >>> p = Planet((5,5), obstacles_list=[(1,1)])
        >>> p.get_size()
        (5, 5)

        >>> p.position_is_accessible((1,1))
        False

        >>> p.position_is_accessible((3,1))
        True

        >>> p.set_obstacles([(3, 1), (7, 8)])
        >>> p.position_is_accessible((3,1))
        False
        >>> p.position_is_accessible((7, 8))
        False
    """

    def __init__(self, size, obstacles_list = None):
        self._size = size
        self._geometry = dict( ((i,j),True) for i in range(size[0]) for j in range(size[1]) )

        if obstacles_list is not None: self.set_obstacles(obstacles_list)


    def get_size(self):
        return self._size


    def position_is_accessible(self, position):
        wrapped_position = (position[X_COORD] % self._size[0], position[Y_COORD] % self._size[1])
        return self._geometry[wrapped_position]


    def set_obstacles(self, obstacles_list):
        for obstacle in obstacles_list:
            obstacle_position = (obstacle[X_COORD] % self._size[0], obstacle[Y_COORD] % self._size[1])
            self._geometry[obstacle_position] = False





class Rover:
    """
    Abstraction of a mobile, directed rover.

    Doctests:

        >>> planet = Planet((5,5), obstacles_list=[(2,2),(1,1)])
        >>> rover = Rover (planet, (0,0), NORTH)

        >>> rover.get_position()
        (0, 0)

        >>> rover.set_position((8,8))
        (3, 3)

        >>> rover.get_direction() is NORTH
        True

        >>> rover.go_forth().get_position()
        (3, 4)

        >>> rover.go_back().get_position()
        (3, 3)

        >>> rover.set_direction(SOUTH) is SOUTH
        True

        >>> rover.go_forth().get_position()
        (3, 2)

        >>> rover.go_back().get_position()
        (3, 3)

        >>> rover.turn_left().get_direction() is EAST
        True

        >>> rover.go_forth().get_position()
        (4, 3)

        >>> rover.go_back().get_position()
        (3, 3)

        >>> rover.turn_right().turn_right().get_direction() is WEST
        True

        >>> rover.go_forth().get_position()
        (2, 3)

        >>> rover.go_back().get_position()
        (3, 3)

        >>> rover.go_forth().turn_left().go_forth().get_position()
        Obstacle averted!
        (4, 4)

        >>> rover.get_direction()
        'south'
        >>> rover.set_direction('test')
        'north'
    """

    def __init__(self, planet, position, direction):

        self._planet = planet
        self._position = None
        self.set_position(position)
        self.set_direction(direction)



    def set_position(self,position):

        max_position = self._planet.get_size()
        new_position = (position[X_COORD] % max_position[0], position[Y_COORD] % max_position[1])

        if self._planet.position_is_accessible(new_position):
            self._position = new_position
        else:
            self._position = (max_position[0] - 1, max_position[1] - 1)
            print ("Obstacle averted!")

        return self._position


    def get_position(self):
        return self._position


    def set_direction(self, direction):
        # Set the direction. If the value is invalid, assume NORTH.
        self._direction = direction if direction in DIRECTIONS_LIST else NORTH

        return self._direction


    def get_direction(self):
        return self._direction


    def decrease_x_coordinate(self):
        return self.set_position((self._position[X_COORD] - 1, self._position[Y_COORD]))


    def increase_x_coordinate(self):
        return self.set_position((self._position[X_COORD] + 1, self._position[Y_COORD]))


    def decrease_y_coordinate(self):
        return self.set_position((self._position[X_COORD], self._position[Y_COORD] - 1))


    def increase_y_coordinate(self):
        return self.set_position((self._position[X_COORD], self._position[Y_COORD] + 1))


    def go_forth(self):
        """
        change the position depending on the direction
        """
        forward_actions = {
            NORTH : self.increase_y_coordinate,
            SOUTH : self.decrease_y_coordinate,
            EAST : self.increase_x_coordinate,
            WEST : self.decrease_x_coordinate
        }

        forward_actions.get(self._direction)()
        return self


    def go_back(self):
        """
        change the position depending on the direction
        """
        backward_actions = {
            NORTH : self.decrease_y_coordinate,
            SOUTH : self.increase_y_coordinate,
            EAST : self.decrease_x_coordinate,
            WEST : self.increase_x_coordinate
        }

        backward_actions.get(self._direction)()
        return self


    def turn_right(self):
        """
        change the direction depending on the current direction
        """
        right_actions = {
            NORTH : EAST,
            SOUTH : WEST,
            EAST : SOUTH,
            WEST : NORTH
        }

        self._direction = right_actions.get(self._direction)
        return self


    def turn_left(self):
        """
        change the direction depending on the current direction
        """
        left_actions = {
            NORTH : WEST,
            SOUTH : EAST,
            EAST : NORTH,
            WEST : SOUTH
        }

        self._direction = left_actions.get(self._direction)
        return self




def explore_mars(start_point, direction, commands_list):
    """
    Test an api that moves a rover around on a grid:

    You are given the initial starting point (x,y) of a rover and the direction (N,S,E,W) it is facing.
    The rover receives a character array of commands.
    Implement commands that move the rover forward/backward (f,b).
    Implement commands that turn the rover left/right (l,r).
    Implement wrapping from one edge of the grid to another. (planets are spheres after all)
    Implement obstacle detection before each move to a new square. If a given sequence of commands encounters an
    obstacle, the rover moves up to the last possible point and reports the obstacle.
    Example: The rover is on a 100x100 grid at location (0, 0) and facing NORTH. The rover is given the commands
     "ffrff" and should end up at (2, 2)

    Doctests:
        >>> explore_mars((0,0), NORTH, 'ffrff')
        (2, 2)
        >>> explore_mars((0,0), SOUTH, 'lfffrrbblb')
        (5, 1)
        >>> explore_mars((0,0), SOUTH, 'lfffrrbblbb')
        Obstacle averted!
        (99, 99)
    """

    mars = Planet((100, 100),  obstacles_list= [(5,2)])
    curiosity = Rover(mars, start_point, direction)

    command_actions = {
        'f': curiosity.go_forth,
        'b': curiosity.go_back,
        'r': curiosity.turn_right,
        'l': curiosity.turn_left
    }

    for command in commands_list:
        command_actions.get(command)()

    return curiosity.get_position()


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)