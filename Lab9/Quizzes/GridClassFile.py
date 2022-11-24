# Contains class for representing the grid environment
# Uses random to get a random grid initialization
import random
import math
import time # for sleep

class GridEnvironment():
    def __init__(self, size=9, num_snakes=5):
        random.seed() # I guess we seed here?
        self.size = size # 21*21 grid by default
        self.center = self.size//2 # the centre position
        self.centre_coord = [self.center, self.center] # in list form
        self.grid = [] # the actual grid
        self.num_snakes = num_snakes # number of snakes
        self.snakes = [] # list of snakes
        self.snake_positions = []
        self.iguana_pos = self.centre_coord # by initialization (will change)
        for i in range(self.size):
            self.grid.append(['-']*self.size) # '-' means nothing there
        self.grid[self.center][self.center] = "I"

        self.initialize_snakes()
        
        #self.goal = [None, None] # To make the goal
        self.initialize_goal() # To make the goal

        self.iguana_ded = False
        self.iguana_escaped = False

        

    def initialize_snakes(self):
        '''Places the snakes on the grid at initialization'''
        for i in range(self.num_snakes):
            valid_location_found = False
            while not valid_location_found:
                one_coord = random.randint(0, self.size-1)
                options = [[0, one_coord],[self.size-1, one_coord],[one_coord, 0],[one_coord, self.size-1]]
                location = random.choice(options) # Either on left, right, top, or bot
                #print(location)
                if (self.grid[location[1]][location[0]] != "S"): # row, column to x, y (swap)
                    self.grid[location[1]][location[0]] = "S"
                    temp_snake = Snake(location)
                    self.snakes.append(temp_snake)
                    self.snake_positions.append(temp_snake.pos)
                    valid_location_found = True

    def initialize_goal(self):
        goal_generated = False
        while not goal_generated:
            one_coord = random.randint(0, self.size-1)
            options = [[0, one_coord],[self.size-1, one_coord],[one_coord, 0],[one_coord, self.size-1]]
            location = random.choice(options)
            if (self.grid[location[1]][location[0]] != "S"):
                self.goal = location
                self.grid[location[1]][location[0]] = "G"
                goal_generated = True

    def check_loss(self):
        '''True if loss, false else'''
        for snake in self.snakes:
            if snake.pos == self.iguana_pos:
                self.iguana_ded = True
                self.grid[self.iguana_pos[1]][self.iguana_pos[0]] = "X" # for eaten iguana
                self.print_grid("end")
                return True
        return False

    def check_win(self):
        '''True if win, false else'''
        if self.goal == self.iguana_pos:
            self.iguana_escaped = True
            self.grid[self.iguana_pos[1]][self.iguana_pos[0]] = "W" # w for win!
            self.print_grid("end")
            return True
        else:
            return False

    def run_round(self, iguana_move, speed=1):
        '''Runs a round'''
        ip = self.iguana_pos
        self.grid[self.iguana_pos[1]][self.iguana_pos[0]] = "." # Clear old iguana pos
        if (iguana_move == "up"):
            # do 1 move at a time and test for goal
            ip_1 = [ip[0], max(0, ip[1] - 1)]
            ip_2 = [ip[0], max(0, ip_1[1] - 1)]
        elif (iguana_move == "down"):
            ip_1 = [ip[0], min(self.size, ip[1]+1)]
            ip_2 = [ip[0], min(self.size, ip_1[1]+1)]
        elif (iguana_move == "left"):
            ip_1 = [max(0, ip[0]-1), ip[1]]
            ip_2 = [max(0, ip_1[0]-1), ip[1]]
        elif (iguana_move == "right"):
            ip_1 = [min(self.size, ip[0]+1), ip[1]]
            ip_2 = [min(self.size, ip_1[0]+1), ip[1]]

        self.iguana_pos = ip_1
        if self.check_win():
            self.grid[self.iguana_pos[1]][self.iguana_pos[0]] = "W" # w for win!
            return
        elif self.check_loss():
            self.grid[self.iguana_pos[1]][self.iguana_pos[0]] = "X" # for eaten iguana
            return
        else:
            self.grid[self.iguana_pos[1]][self.iguana_pos[0]] = "I"

        # optionally draw the grid
        self.print_grid()

        if (speed == 2):
            self.grid[self.iguana_pos[1]][self.iguana_pos[0]] = "."
            self.iguana_pos = ip_2
            if self.check_win():
                self.grid[self.iguana_pos[1]][self.iguana_pos[0]] = "W" # w for win!
                return
            elif self.check_loss():
                self.grid[self.iguana_pos[1]][self.iguana_pos[0]] = "X" # for eaten iguana
                return
            else:
                self.grid[self.iguana_pos[1]][self.iguana_pos[0]] = "I"

            # optionally draw the grid
            self.print_grid()

        # Now clean the grid of footsteps
        '''for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if (self.grid[i][j] == "."):
                    self.grid[i][j] = "-"'''

        self.snake_positions = []
        for snake in self.snakes:
            self.grid[snake.pos[1]][snake.pos[0]] = "~" # Slithers
            #print(snake.pos)
            iguana_ded = snake.generate_next_pos(self)
            #print(snake.pos)
            if iguana_ded and snake.pos == self.iguana_pos:
                self.grid[snake.pos[1]][snake.pos[0]] = "X" # for eaten iguana
                self.iguana_ded = True
            else:
                self.grid[snake.pos[1]][snake.pos[0]] = "S"
                self.snake_positions.append(snake.pos)

        self.print_grid("s") # Finally print the updated grid

        # Now clean the grid of slithers
        '''for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if (self.grid[i][j] == "~"):
                    self.grid[i][j] = "-"'''
                

    def print_grid(self, turn="i"):
        '''Prints out the grid for the user'''
        # Always update goal to show (unless 'W')
        if self.grid[self.goal[1]][self.goal[0]] != 'G' and self.grid[self.goal[1]][self.goal[0]] != 'W':
            self.grid[self.goal[1]][self.goal[0]] = 'G'
            
        time.sleep(0.25) # Comment this out if it's annoying to you

        print("-"*(self.size*2 + 6))
        if (turn == "i"):
            print(" "*(self.size//2)+"Iguana's Turn!")
        elif (turn == "s"):
            print(" "*(self.size//2)+"Snakes' Turn!")
        elif (turn == "start"):
            print(" "*(self.size//2)+"Start State")
        else:
            print(" "*(self.size//2)+"End State")
            
        print("-"*(self.size*2 + 6))
        for row in self.grid:
            print(" "*3, end='')
            print(*row)
        print("-"*(self.size*2 + 6))

class Snake():
    def __init__(self, pos):
        self.pos = pos # list with 2 items [x, y]

    def generate_next_pos(self, grid):
        '''Updates the pos of the snake so that it moves closer to the iguana. Returns true if eats iguana, false else'''
        iguana_pos = grid.iguana_pos
        pos_diff = [iguana_pos[0] - self.pos[0], iguana_pos[1] - self.pos[1]]
        if (abs(pos_diff[0]) >= abs(pos_diff[1])): # if closer via x will always move 1 closer there
            self.pos = [self.pos[0] + pos_diff[0]//abs(pos_diff[0]), self.pos[1]] # moves 1 closer in x (column)
        else:
            self.pos = [self.pos[0], self.pos[1] + pos_diff[1]//abs(pos_diff[1])] # moves 1 closer in y (row)
        if (self.pos == iguana_pos):
            return True
        else:
            return False

if __name__ == "__main__":
    # Just for me to test some stuff
    my_grid = GridEnvironment() # 21*21, 5 snakes
    #print(my_grid.size)
    #print(my_grid.center)
    my_grid.run_round("right")
    my_grid.run_round("up")

    #for snake in my_grid.snakes:
        #print(snake.generate_next_pos(my_grid))
        
