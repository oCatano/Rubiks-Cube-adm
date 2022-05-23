from Shapes import *
from random import randrange


class Cube:
    front = [[], [], []]
    back = [[], [], []]
    up = [[], [], []]
    down = [[], [], []]
    right = [[], [], []]
    left = [[], [], []]

    def __init__(self):
        self.commands = None
        self.commands_list = None
        self.ideal_cube()
        self.solve_commands = []

    def solve_cube(self):
        self.solve_commands = []
        self.center_normalize()
        commands = [self.white_cross_yellow_center, self.white_cross,
                    self.first_lvl, self.second_lvl,
                    self.figures_on_the_top, self.corners,
                    self.final
                    ]
        i = 10
        # white cross yellow center
        if self.is_ideal():
            return
        elif self.is_corners():
            i = 6
        elif self.is_figures_on_the_top():
            i = 5
        elif self.is_second_lvl():
            i = 4
        elif self.is_first_lvl():
            i = 3
        elif self.is_white_cross():
            i = 2
        elif self.is_white_cross_yellow_center():
            i = 1
        else:
            i = 0
        if i != 10:
            if i == 0:
                commands[i]()
                i += 1
            while i != 7:
                commands[i](True)
                i += 1
        return self.solve_commands

    def center_normalize(self):
        if self.up[1][1] == 14 and self.down[1][1] == 32 and \
                self.front[1][1] == 41 and self.back == 50:
            return
        else:
            for i in range(4):
                if self.up[1][1] == 14:
                    break
                self.turn_y_2_pos()

            for i in range(4):
                if self.up[1][1] == 14:
                    break
                self.turn_x_2_pos()
            while self.front[1][1] != 41:
                self.turn_z_2_pos()

    # Makes white cross on up plane
    def white_cross_yellow_center(self):

        self.center_normalize()

        white = [29, 31, 33, 35]
        white_num = [29, 31, 33, 35]

        def turn_till_clear_on_up(i, j):
            while self.up[i][j] in white:
                self.turn_z_1_neg()

        indexes = [[0, 1, False], [1, 0, True], [2, 1, False], [1, 2, True]]
        for item in white_num:
            if item not in [self.up[0][1], self.up[1][0], self.up[2][1], self.up[1][2]]:
                for i, j, part in indexes:
                    if self.front[i][j] == item:
                        if part:
                            if j == 0:
                                turn_till_clear_on_up(1, 0)
                                self.turn_y_1_pos()
                                break
                            elif j == 2:
                                turn_till_clear_on_up(1, 2)
                                self.turn_y_3_pos()
                                break
                        else:
                            turn_till_clear_on_up(2, 1)
                            self.turn_x_1_pos()
                            if i == 0:
                                turn_till_clear_on_up(1, 0)
                                self.turn_y_1_pos()
                                break
                            elif i == 2:
                                turn_till_clear_on_up(1, 2)
                                self.turn_y_3_pos()
                                break
                    elif self.right[i][j] == item:
                        if part:
                            turn_till_clear_on_up(1, 2)
                            self.turn_y_3_pos()
                            if j == 0:
                                turn_till_clear_on_up(0, 1)
                                self.turn_x_3_pos()
                                break
                            elif j == 2:
                                turn_till_clear_on_up(2, 1)
                                self.turn_x_1_pos()
                                break
                        else:
                            if i == 0:
                                turn_till_clear_on_up(0, 1)
                                self.turn_x_3_pos()
                                break
                            elif i == 2:
                                turn_till_clear_on_up(2, 1)
                                self.turn_x_1_pos()
                                break
                    elif self.back[i][j] == item:
                        if part:
                            if j == 0:
                                turn_till_clear_on_up(1, 0)
                                self.turn_y_1_neg()
                                break
                            elif j == 2:
                                turn_till_clear_on_up(1, 2)
                                self.turn_y_3_neg()
                                break
                        else:
                            turn_till_clear_on_up(0, 1)
                            self.turn_x_3_pos()
                            if i == 0:
                                turn_till_clear_on_up(1, 2)
                                self.turn_y_3_neg()
                                break
                            elif i == 2:
                                turn_till_clear_on_up(1, 0)
                                self.turn_y_1_neg()
                                break
                    elif self.left[i][j] == item:
                        if part:
                            turn_till_clear_on_up(1, 0)
                            self.turn_y_1_pos()
                            if j == 0:
                                turn_till_clear_on_up(2, 1)
                                self.turn_x_1_neg()
                                break
                            elif j == 2:
                                turn_till_clear_on_up(0, 1)
                                self.turn_x_3_neg()
                                break
                        else:
                            if i == 0:
                                turn_till_clear_on_up(0, 1)
                                self.turn_x_3_neg()
                                break
                            elif i == 2:
                                turn_till_clear_on_up(2, 1)
                                self.turn_x_1_neg()
                                break
                    elif self.down[i][j] == item:
                        if part:
                            if j == 0:
                                turn_till_clear_on_up(1, 2)
                                self.turn_y_3_pos(2)
                                break
                            elif j == 2:
                                turn_till_clear_on_up(1, 0)
                                self.turn_y_1_pos(2)
                                break
                        else:
                            if i == 0:
                                turn_till_clear_on_up(0, 1)
                                self.turn_x_3_neg(2)
                                break
                            elif i == 2:
                                turn_till_clear_on_up(2, 1)
                                self.turn_x_1_neg(2)
                                break

    # Makes full white cross
    def white_cross(self, is_white_cross_yellow_center=False):
        """
        :param is_white_cross_yellow_center: False to make white cross yellow center
        :return:
        """
        if not is_white_cross_yellow_center:
            self.white_cross_yellow_center()

        white_num = [29, 31, 33, 35]
        white_num_pos = {29: [1, 0, self.turn_y_1_pos], 31: [0, 1, self.turn_x_3_pos],
                         33: [2, 1, self.turn_x_1_pos], 35: [1, 2, self.turn_y_3_pos]}
        for item in white_num:
            i = white_num_pos[item]
            while self.up[i[0]][i[1]] != item:
                self.turn_z_1_neg()
            i[2](2)

    def first_lvl(self, is_all_steps_done=False):
        if not is_all_steps_done:
            self.white_cross(is_white_cross_yellow_center=False)
        white = [28, 34, 30, 36]
        """
            indexes[0]: list of indexes on "up"
            indexes[1]: list of indexes on "down"
            indexes[2]: list of values un shape (white value always first)
            indexes[3]: orientation fo right turn (x, y, z)
        """
        indexes_commands = {28: [[0, 0], [0, 2], [28, 46, 7], [False, True, True]],
                            46: [[0, 0], [0, 2], [28, 46, 7], [False, True, True]],
                            7: [[0, 0], [0, 2], [28, 46, 7], [False, True, True]],
                            34: [[0, 2], [0, 0], [34, 19, 48], [False, False, True]],
                            19: [[0, 2], [0, 0], [34, 19, 48], [False, False, True]],
                            48: [[0, 2], [0, 0], [34, 19, 48], [False, False, True]],
                            36: [[2, 2], [2, 0], [36, 45, 21], [True, False, True]],
                            45: [[2, 2], [2, 0], [36, 45, 21], [True, False, True]],
                            21: [[2, 2], [2, 0], [36, 45, 21], [True, False, True]],
                            30: [[2, 0], [2, 2], [30, 9, 43], [True, True, True]],
                            9: [[2, 0], [2, 2], [30, 9, 43], [True, True, True]],
                            43: [[2, 0], [2, 2], [30, 9, 43], [True, True, True]]
                            }

        def put_all_up_to_right_position():
            count = 0
            ind = [[0, 0], [0, 2], [2, 0], [2, 2]]
            for counter in range(4):
                if count == 4:
                    break
                for i, j in ind:
                    elem = indexes_commands.get(self.up[i][j])
                    if elem:
                        indexes = elem[0]
                        down_ind = elem[1]
                        values = elem[2]
                        orientation = elem[3]
                        while self.up[indexes[0]][indexes[1]] not in values:
                            self.turn_z_1_neg()
                        while self.down[down_ind[0]][down_ind[1]] != values[0]:
                            self.right_turn(x=bool(orientation[0]), y=bool(orientation[1]), z=bool(orientation[2]))
                        count += 1
                        break

        put_all_up_to_right_position()
        indexes_on_down = [[0, 0], [0, 2], [2, 0], [2, 2]]
        for i, j in indexes_on_down:
            temp = indexes_commands.get(self.down[i][j])
            if temp:
                if temp[2][0] != self.down[i][j]:
                    self.right_turn(x=bool(temp[3][0]), y=bool(temp[3][1]), z=bool(temp[3][2]))

        put_all_up_to_right_position()

        # reset cube to solved one

    def second_lvl(self, is_all_steps_before_done=False):
        """
        index_position[0]: position to start
        index_position[1]: commands
        index_position[3]: orientation
        :param is_all_steps_before_done: If False will solve all previous steps
        :return:
        """
        index_position = {
            40: [[0, 1], [self.right_turn, self.left_turn], [True, True]],
            6: [[1, 2], [self.left_turn, self.right_turn], [True, True]],
            24: [[1, 0], [self.right_turn, self.left_turn], [True, False]],
            42: [[0, 1], [self.left_turn, self.right_turn], [True, False]],
            51: [[2, 1], [self.right_turn, self.left_turn], [False, False]],
            22: [[1, 0], [self.left_turn, self.right_turn], [False, False]],
            4: [[1, 2], [self.right_turn, self.left_turn], [False, True]],
            49: [[2, 1], [self.left_turn, self.right_turn], [False, True]]
        }

        def put_all_from_top_to_second():
            ind = [[0, 1], [1, 0], [2, 1], [1, 2]]
            for counter in range(4):
                for i, j in ind:
                    shape = self.up[i][j]
                    value = index_position.get(shape)
                    if value:
                        while self.up[value[0][0]][value[0][1]] != shape:
                            self.turn_z_1_neg()
                        orientation = value[2]
                        for item in value[1]:
                            item(x=bool(orientation[0]), y=bool(orientation[1]))
                        break


        def put_wrong_shapes_from_second_to_top():
            if self.front[1][0] != 40 and index_position.get(self.front[1][0]):
                self.right_turn(x=True, y=True)
                self.left_turn(x=True, y=True)
                put_all_from_top_to_second()
            if self.left[0][1] != 4 and index_position.get(self.left[0][1]):
                self.right_turn(x=False, y=True)
                self.left_turn(x=False, y=True)
                put_all_from_top_to_second()
            if self.back[1][2] != 51 and index_position.get(self.back[1][2]):
                self.right_turn(x=False, y=False)
                self.left_turn(x=False, y=False)
                put_all_from_top_to_second()
            if self.right[2][1] != 24 and index_position.get(self.right[2][1]):
                self.right_turn(x=True, y=False)
                self.left_turn(x=True, y=False)
                put_all_from_top_to_second()


        if not is_all_steps_before_done:
            self.first_lvl(is_all_steps_done=False)

        while not self.is_second_lvl():
            put_all_from_top_to_second()
            put_wrong_shapes_from_second_to_top()

    def figures_on_the_top(self, is_all_steps_before_done=False):
        yellow = [11, 13, 15, 17]
        indexes = [[0, 1], [1, 0], [2, 1], [1, 2]]

        if not is_all_steps_before_done:
            self.second_lvl(is_all_steps_before_done=False)

        def cross():
            for i, j in indexes:
                if self.up[i][j] not in yellow:
                    return False
            return True

        def stick():
            opposit_indexes = [[[0, 1], [2, 1]], [[1, 0], [1, 2]]]
            temp = opposit_indexes[0]
            if self.up[temp[0][0]][temp[0][1]] in yellow and \
                    self.up[temp[1][0]][temp[1][1]] in yellow:
                self.turn_y_1_neg()
                self.right_turn(x=True, y=True)
                self.turn_y_1_pos()
                return True
            temp = opposit_indexes[1]
            if self.up[temp[0][0]][temp[0][1]] in yellow and \
                    self.up[temp[1][0]][temp[1][1]] in yellow:
                self.turn_x_1_neg()
                self.right_turn(x=True, y=False)
                self.turn_x_1_pos()
                return True
            return False

        def corner():
            d = {
                0: [self.turn_y_1_neg, self.turn_y_1_pos, [True, True]],
                1: [self.turn_x_1_neg, self.turn_x_1_pos, [True, False]],
                2: [self.turn_y_3_pos, self.turn_y_3_neg, [False, False]],
                3: [self.turn_x_3_pos, self.turn_x_3_neg, [False, True]]
            }
            # indexes = [[0, 1], [1, 0], [2, 1], [1, 2]]
            for i in range(4):
                if self.up[indexes[i - 1][0]][indexes[i - 1][1]] in yellow and \
                        self.up[indexes[i][0]][indexes[i][1]] in yellow:
                    command = d.get(i)
                    command[0]()
                    self.right_turn(x=command[2][0], y=command[2][1], n=2)
                    command[1]()
                    return True
            return False

        def point():
            self.turn_x_1_neg()
            self.right_turn(x=True, y=False, n=2)
            self.turn_x_1_pos()
            check = stick()
            if not check:
                corner()

        if not cross():
            if not stick():
                if not corner():
                    point()

    def corners(self, is_all_steps_before_done=False):
        if not is_all_steps_before_done:
            self.figures_on_the_top(is_all_steps_before_done=False)

        index_position = {
            16: [[0, 0], [16, 1, 52]],
            52: [[0, 0], [16, 1, 52]],
            1: [[0, 0], [16, 1, 52]],
            10: [[0, 2], [10, 25, 54]],
            25: [[0, 2], [10, 25, 54]],
            54: [[0, 2], [10, 25, 54]],
            12: [[2, 2], [12, 27, 39]],
            27: [[2, 2], [12, 27, 39]],
            39: [[2, 2], [12, 27, 39]],
            18: [[2, 0], [18, 3, 37]],
            3: [[2, 0], [18, 3, 37]],
            37: [[2, 0], [18, 3, 37]],
        }

        index = [[0, 0], [0, 2], [2, 2], [2, 0]]
        orientation = [[True, False], [True, True], [False, True], [False, False]]

        def get_shape_to_pos(i, j):
            pos = index_position.get(self.up[i][j])[0]
            values = index_position.get(self.up[i][j])[1]
            while self.up[pos[0]][pos[1]] not in values:
                self.turn_z_1_neg()

        i = 0
        while True:
            temp = self.up[index[i][0]][index[i][1]]
            get_shape_to_pos(index[i][0], index[i][1])
            for k in range(4):
                if self.up[index[k][0]][index[k][1]] == temp:
                    i = k
                    break
            n1 = index_position.get(self.up[index[(i + 1) % 4][0]][index[(i + 1) % 4][1]])
            n2 = index_position.get(self.up[index[i - 1][0]][index[i - 1][1]])
            n3 = index_position.get(self.up[index[(i + 2) % 4][0]][index[(i + 2) % 4][1]])
            if self.up[n1[0][0]][n1[0][1]] in n1[1] and \
                    self.up[n2[0][0]][n2[0][1]] in n2[1]:
                break
            elif self.up[n1[0][0]][n1[0][1]] in n1[1]:
                x_y = orientation[(i + 1) % 4]
                self.right_turn(x=x_y[0], y=x_y[1], n=3)
                self.left_turn(x=x_y[0], y=x_y[1], n=3)
                break
            elif self.up[n2[0][0]][n2[0][1]] in n2[1]:
                x_y = orientation[i % 4]
                self.right_turn(x=x_y[0], y=x_y[1], n=3)
                self.left_turn(x=x_y[0], y=x_y[1], n=3)
                break
            elif self.up[n3[0][0]][n3[0][1]] in n3[1]:
                x_y = orientation[(i + 1) % 4]
                self.right_turn(x=x_y[0], y=x_y[1], n=3)
                self.left_turn(x=x_y[0], y=x_y[1], n=3)
            i = (i + 1) % 4
        for i in range(4):
            while self.up[2][0] not in [18, 12, 10, 16]:
                self.right_turn(x=True, y=True, z=False)
            self.turn_z_1_neg()

    def final(self, is_all_steps_before_done=False):
        if not is_all_steps_before_done:
            self.corners(is_all_steps_before_done=False)

        ind = [[0, 1], [1, 2], [2, 1], [1, 0]]
        yellow_pos = {
            13: [[0, 1], [False, True], [False, False]],
            11: [[1, 2], [False, False], [True, False]],
            15: [[2, 1], [True, False], [True, True]],
            17: [[1, 0], [True, True], [False, True]]
        }

        def make_r_l_turns():
            for i, j in ind:
                if [i, j] == yellow_pos[self.up[i][j]][0]:
                    orientation_1 = yellow_pos[self.up[i][j]][1]
                    orientation_2 = yellow_pos[self.up[i][j]][2]
                    self.right_turn(x=bool(orientation_1[0]), y=bool(orientation_1[1]))
                    self.left_turn(x=bool(orientation_2[0]), y=bool(orientation_2[1]))
                    self.right_turn(x=bool(orientation_1[0]), y=bool(orientation_1[1]), n=5)
                    self.left_turn(x=bool(orientation_2[0]), y=bool(orientation_2[1]), n=5)
                    break
            self.right_turn(x=True, y=False)
            self.left_turn(x=True, y=True)
            self.right_turn(x=True, y=False, n=5)
            self.left_turn(x=True, y=True, n=5)

        while self.up[0][0] != 16:
            self.turn_z_1_neg()

        checker = False
        while not checker:
            checker = True
            for i, j in ind:
                if [i, j] != yellow_pos[self.up[i][j]][0]:
                    checker = False
                    break
            if not checker:
                make_r_l_turns()

    def ideal_cube(self):
        # params = [[14, 'yellow'], [23, 'red'], [32, 'white'], [5, 'orange'],
        #           [41, 'blue'], [50, 'green']
        #           ]
        #
        # params = [[11, 26, 'yellow', 'red'],
        #           [15, 38, 'yellow', 'blue'],
        #           [17, 2, 'yellow', 'orange'],
        #           [13, 53, 'yellow', 'green'],
        #
        #           [40, 6, 'blue', 'orange'],
        #           [4, 49, 'orange', 'green'],
        #           [51, 22, 'green', 'red'],
        #           [24, 42, 'red', 'blue'],
        #
        #           [44, 33, 'blue', 'white'],
        #           [8, 29, 'orange', 'white'],
        #           [47, 31, 'green', 'white'],
        #           [20, 35, 'red', 'white'],
        #           ]


        # params = [[18, 3, 37, 'yellow', 'orange', 'blue'],
        #           [16, 52, 1, 'yellow', 'green', 'orange'],
        #           [10, 25, 54, 'yellow', 'red', 'green'],
        #           [12, 39, 27, 'yellow', 'blue', 'red'],
        #
        #           [43, 9, 30, 'blue', 'orange', 'white'],
        #           [7, 46, 28, 'orange', 'green', 'white'],
        #           [48, 19, 34, 'green', 'red', 'white'],
        #           [21, 45, 36, 'red', 'blue', 'white'],
        #           ]

        self.up = [[16, 13, 10],
                   [17, 14, 11],
                   [18, 15, 12]
                   ]

        self.down = [[34, 31, 28],
                     [35, 32, 29],
                     [36, 33, 30]
                     ]

        self.front = [[37, 38, 39],
                      [40, 41, 42],
                      [43, 44, 45]
                      ]

        self.back = [[46, 47, 48],
                     [49, 50, 51],
                     [52, 53, 54]
                     ]

        self.left = [[7, 4, 1],
                     [8, 5, 2],
                     [9, 6, 3]
                     ]

        self.right = [[25, 22, 19],
                      [26, 23, 20],
                      [27, 24, 21]
                      ]

    # returns new object of one plane (list of 3 lists)
    def __copy_part(self, a):
        temp = []
        for item in a:
            temp.append(item.copy())
        return temp

    # turn cube on z_1 clockwise n times
    def turn_z_1_neg(self, n=1, is_pos=True):
        for i in range(n):
            if is_pos:
                self.solve_commands.append(['U', 1])
            temp = self.__copy_part(self.up)

            # spin up plane
            self.up[0][0] = temp[2][0]
            self.up[2][0] = temp[2][2]
            self.up[2][2] = temp[0][2]
            self.up[0][2] = temp[0][0]

            self.up[0][1] = temp[1][0]
            self.up[1][0] = temp[2][1]
            self.up[2][1] = temp[1][2]
            self.up[1][2] = temp[0][1]

            front = self.__copy_part(self.front)
            back = self.__copy_part(self.back)
            left = self.__copy_part(self.left)
            right = self.__copy_part(self.right)

            # front -> left
            self.left[0][2] = front[0][0]
            self.left[1][2] = front[0][1]
            self.left[2][2] = front[0][2]

            # left -> back
            self.back[2][2] = left[0][2]
            self.back[2][1] = left[1][2]
            self.back[2][0] = left[2][2]

            # back -> right
            self.right[2][0] = back[2][2]
            self.right[1][0] = back[2][1]
            self.right[0][0] = back[2][0]

            # right -> front
            self.front[0][0] = right[2][0]
            self.front[0][1] = right[1][0]
            self.front[0][2] = right[0][0]

    # turn cube on z_1 clockwise n times
    def turn_z_1_pos(self, n=1):
        for i in range(n):
            self.solve_commands.append(['U', -1])
            self.turn_z_1_neg(3, is_pos=False)

    # turn cube on z_1 clockwise n times
    def turn_z_2_pos(self, n=1):
        for i in range(n):
            front = self.__copy_part(self.front)
            back = self.__copy_part(self.back)
            left = self.__copy_part(self.left)
            right = self.__copy_part(self.right)

            # left -> front
            self.front[1][0] = left[0][1]
            self.front[1][1] = left[1][1]
            self.front[1][2] = left[2][1]

            # front -> right
            self.right[2][1] = front[1][0]
            self.right[1][1] = front[1][1]
            self.right[0][1] = front[1][2]

            # right -> back
            self.back[1][2] = right[2][1]
            self.back[1][1] = right[1][1]
            self.back[1][0] = right[0][1]

            # back -> left
            self.left[0][1] = back[1][2]
            self.left[1][1] = back[1][1]
            self.left[2][1] = back[1][0]

    # turn cube on z_1 counterclockwise n times
    def turn_z_2_neg(self, n=1):
        for i in range(n):
            self.turn_z_2_pos(3)

    # turn cube on z_3 clockwise n times
    def turn_z_3_pos(self, n=1, is_pos=True):
        for i in range(n):
            if is_pos:
                self.solve_commands.append(['D', 1])
            front = self.__copy_part(self.front)
            back = self.__copy_part(self.back)
            left = self.__copy_part(self.left)
            right = self.__copy_part(self.right)
            down = self.__copy_part(self.down)

            # spin up plane
            self.down[0][1] = down[1][0]
            self.down[1][0] = down[2][1]
            self.down[2][1] = down[1][2]
            self.down[1][2] = down[0][1]

            self.down[0][2] = down[0][0]
            self.down[0][0] = down[2][0]
            self.down[2][0] = down[2][2]
            self.down[2][2] = down[0][2]

            # left -> front
            self.front[2][2] = left[2][0]
            self.front[2][1] = left[1][0]
            self.front[2][0] = left[0][0]

            # front -> right
            self.right[0][2] = front[2][2]
            self.right[1][2] = front[2][1]
            self.right[2][2] = front[2][0]

            # right -> back
            self.back[0][0] = right[0][2]
            self.back[0][1] = right[1][2]
            self.back[0][2] = right[2][2]

            # back -> left
            self.left[2][0] = back[0][0]
            self.left[1][0] = back[0][1]
            self.left[0][0] = back[0][2]

    # turn cube on z_3 counterclockwise n times
    def turn_z_3_neg(self, n=1):
        for i in range(n):
            self.solve_commands.append(['D', -1])
            self.turn_z_3_pos(3, is_pos=False)

    # turn x_1 counterclockwise n times
    def turn_x_1_pos(self, n=1, is_pos=True):
        for i in range(n):
            if is_pos:
                self.solve_commands.append(['F', -1])
            front = self.__copy_part(self.front)
            up = self.__copy_part(self.up)
            left = self.__copy_part(self.left)
            right = self.__copy_part(self.right)
            down = self.__copy_part(self.down)

            # changes on front side
            self.front[0][0] = front[0][2]
            self.front[2][0] = front[0][0]
            self.front[2][2] = front[2][0]
            self.front[0][2] = front[2][2]

            self.front[0][1] = front[1][2]
            self.front[1][0] = front[0][1]
            self.front[2][1] = front[1][0]
            self.front[1][2] = front[2][1]

            # right -> up
            self.up[2][0] = right[2][0]
            self.up[2][1] = right[2][1]
            self.up[2][2] = right[2][2]

            # up -> left
            self.left[2] = up[2]

            # left -> down
            self.down[2] = left[2]

            # down -> right
            self.right[2] = down[2]

    # turn x_1 clockwise n times
    def turn_x_1_neg(self, n=1):
        for i in range(n):
            self.solve_commands.append(['F', 1])
            self.turn_x_1_pos(3, is_pos=False)

    # turn x_2 counterclockwise n times
    def turn_x_2_pos(self, n=1):
        for i in range(n):
            up = self.__copy_part(self.up)
            left = self.__copy_part(self.left)
            right = self.__copy_part(self.right)
            down = self.__copy_part(self.down)

            # right -> up
            self.up[1] = right[1]

            # up -> left
            self.left[1] = up[1]

            # left -> down
            self.down[1] = left[1]

            # down -> right
            self.right[1] = down[1]

    # turn x_2 clockwise n times
    def turn_x_2_neg(self, n=1):
        for i in range(n):
            self.turn_x_2_pos(3)

    # turn x_3 counterclockwise n times
    def turn_x_3_pos(self, n=1, is_pos=True):
        for i in range(n):
            if is_pos:
                self.solve_commands.append(['B', 1])
            back = self.__copy_part(self.back)
            up = self.__copy_part(self.up)
            left = self.__copy_part(self.left)
            right = self.__copy_part(self.right)
            down = self.__copy_part(self.down)

            # changes on front side
            self.back[0][0] = back[2][0]
            self.back[2][0] = back[2][2]
            self.back[2][2] = back[0][2]
            self.back[0][2] = back[0][0]

            self.back[0][1] = back[1][0]
            self.back[1][0] = back[2][1]
            self.back[2][1] = back[1][2]
            self.back[1][2] = back[0][1]

            # right -> up
            self.up[0] = right[0]

            # up -> left
            self.left[0] = up[0]

            # left -> down
            self.down[0] = left[0]

            # down -> right
            self.right[0] = down[0]

    # turn x_3 clockwise n times
    def turn_x_3_neg(self, n=1):
        for i in range(n):
            self.solve_commands.append(['B', -1])
            self.turn_x_3_pos(3,is_pos=False)

    # turn y_1 counterclockwise n times
    def turn_y_1_pos(self, n=1, is_pos=True):
        for i in range(n):
            if is_pos:
                self.solve_commands.append(['L', -1])
            front = self.__copy_part(self.front)
            up = self.__copy_part(self.up)
            left = self.__copy_part(self.left)
            back = self.__copy_part(self.back)
            down = self.__copy_part(self.down)

            # changes on left
            self.left[0][0] = left[0][2]
            self.left[0][2] = left[2][2]
            self.left[2][2] = left[2][0]
            self.left[2][0] = left[0][0]

            self.left[0][1] = left[1][2]
            self.left[1][2] = left[2][1]
            self.left[2][1] = left[1][0]
            self.left[1][0] = left[0][1]

            # front -> up
            self.up[0][0] = front[0][0]
            self.up[1][0] = front[1][0]
            self.up[2][0] = front[2][0]

            # up -> back
            self.back[0][0] = up[0][0]
            self.back[1][0] = up[1][0]
            self.back[2][0] = up[2][0]

            # back -> down
            self.down[2][2] = back[0][0]
            self.down[1][2] = back[1][0]
            self.down[0][2] = back[2][0]

            # down -> front
            self.front[0][0] = down[2][2]
            self.front[1][0] = down[1][2]
            self.front[2][0] = down[0][2]

    # turn y_1 clockwise n times
    def turn_y_1_neg(self, n=1):
        for i in range(n):
            self.solve_commands.append(['L', 1])
            self.turn_y_1_pos(3, is_pos=False)

    # turn y_2 counterclockwise n times
    def turn_y_2_pos(self, n=1):
        for i in range(n):
            front = self.__copy_part(self.front)
            up = self.__copy_part(self.up)
            back = self.__copy_part(self.back)
            down = self.__copy_part(self.down)

            # front -> up
            self.up[0][1] = front[0][1]
            self.up[1][1] = front[1][1]
            self.up[2][1] = front[2][1]

            # up -> back
            self.back[0][1] = up[0][1]
            self.back[1][1] = up[1][1]
            self.back[2][1] = up[2][1]

            # back -> down
            self.down[2][1] = back[0][1]
            self.down[1][1] = back[1][1]
            self.down[0][1] = back[2][1]

            # down -> front
            self.front[0][1] = down[2][1]
            self.front[1][1] = down[1][1]
            self.front[2][1] = down[0][1]

    # turn y_2 clockwise n times
    def turn_y_2_neg(self, n=1):
        for i in range(n):
            self.turn_y_2_pos(3)

    # turn y_3 counterclockwise n times
    def turn_y_3_pos(self, n=1, is_pos=True):
        for i in range(n):
            if is_pos:
                self.solve_commands.append(['R', 1])
            front = self.__copy_part(self.front)
            up = self.__copy_part(self.up)
            right = self.__copy_part(self.right)
            back = self.__copy_part(self.back)
            down = self.__copy_part(self.down)

            # change right
            self.right[0][0] = right[2][0]
            self.right[2][0] = right[2][2]
            self.right[2][2] = right[0][2]
            self.right[0][2] = right[0][0]

            self.right[0][1] = right[1][0]
            self.right[1][0] = right[2][1]
            self.right[2][1] = right[1][2]
            self.right[1][2] = right[0][1]

            # front -> up
            self.up[0][2] = front[0][2]
            self.up[1][2] = front[1][2]
            self.up[2][2] = front[2][2]

            # up -> back
            self.back[0][2] = up[0][2]
            self.back[1][2] = up[1][2]
            self.back[2][2] = up[2][2]

            # back -> down
            self.down[2][0] = back[0][2]
            self.down[1][0] = back[1][2]
            self.down[0][0] = back[2][2]

            # down -> front
            self.front[0][2] = down[2][0]
            self.front[1][2] = down[1][0]
            self.front[2][2] = down[0][0]

    # turn y_3 clockwise n times
    def turn_y_3_neg(self, n=1):
        for i in range(n):
            self.solve_commands.append(['R', -1])
            self.turn_y_3_pos(3, is_pos=False)

    def right_turn(self, x=True, y=True, z=True, n=1):
        """
        Над каким ребром будет совершаться правый поворот
        :param x: первая ось (True - если вдоль оси ox False - против)
        :param y: Вторая ось (True - если вдоль оси oy False - против)
        :param z: ориентация кубика (True - если вдоль оси oz False - против)
        :param n: number of right turns
        """
        for i in range(n):
            if z:
                if (not x) & y:
                    self.turn_y_1_neg()
                    self.turn_z_1_neg()
                    self.turn_y_1_pos()
                    self.turn_z_1_pos()
                elif (not x) & (not y):
                    self.turn_x_3_pos()
                    self.turn_z_1_neg()
                    self.turn_x_3_neg()
                    self.turn_z_1_pos()
                elif x & (not y):
                    self.turn_y_3_pos()
                    self.turn_z_1_neg()
                    self.turn_y_3_neg()
                    self.turn_z_1_pos()
                elif x & y:
                    self.turn_x_1_neg()
                    self.turn_z_1_neg()
                    self.turn_x_1_pos()
                    self.turn_z_1_pos()
            else:
                if x & (not y):
                    self.turn_x_1_neg()
                    self.turn_z_3_pos()
                    self.turn_x_1_pos()
                    self.turn_z_3_neg()
                elif x & y:
                    self.turn_y_1_neg()
                    self.turn_z_3_pos()
                    self.turn_y_1_pos()
                    self.turn_z_3_neg()
                elif (not x) & y:
                    self.turn_x_3_pos()
                    self.turn_z_3_pos()
                    self.turn_x_3_neg()
                    self.turn_z_3_neg()
                elif (not x) & (not y):
                    self.turn_y_3_pos()
                    self.turn_z_3_pos()
                    self.turn_y_3_neg()
                    self.turn_z_3_neg()

    def left_turn(self, x=True, y=True, z=True, n=1):
        """
                Над каким ребром будет совершаться правый поворот
                :param x: first axis (True - along the axis ox False - against axis)
                :param y: second axis (True - along the axis oy False - against axis)
                :param z: cubes orientation (True - along the axis oz False - against axis)
                :param n: number of right turns
                """
        for i in range(n):
            if z:
                if x & (not y):
                    self.turn_x_1_pos()
                    self.turn_z_1_pos()
                    self.turn_x_1_neg()
                    self.turn_z_1_neg()
                elif x & y:
                    self.turn_y_1_pos()
                    self.turn_z_1_pos()
                    self.turn_y_1_neg()
                    self.turn_z_1_neg()
                elif (not x) & y:
                    self.turn_x_3_neg()
                    self.turn_z_1_pos()
                    self.turn_x_3_pos()
                    self.turn_z_1_neg()
                elif (not x) & (not y):
                    self.turn_y_3_neg()
                    self.turn_z_1_pos()
                    self.turn_y_3_pos()
                    self.turn_z_1_neg()
            else:
                if (not x) & y:
                    self.turn_y_1_pos()
                    self.turn_z_1_neg()
                    self.turn_y_1_neg()
                    self.turn_z_3_pos()
                elif (not x) & (not y):
                    self.turn_x_3_neg()
                    self.turn_z_3_neg()
                    self.turn_x_3_pos()
                    self.turn_z_3_pos()
                elif x & (not y):
                    self.turn_y_3_neg()
                    self.turn_z_3_neg()
                    self.turn_y_3_pos()
                    self.turn_z_3_pos()
                elif x & y:
                    self.turn_x_1_pos()
                    self.turn_z_3_neg()
                    self.turn_x_1_neg()
                    self.turn_z_3_pos()

    def is_white_cross_yellow_center(self):
        arr = [29, 31, 33, 35]
        up_elem_indexes = [[0, 1], [1, 0], [2, 1], [1, 2]]
        for i, j in up_elem_indexes:
            if self.up[i][j] in arr:
                arr.pop(arr.index(self.up[i][j]))
        return not arr

    def is_white_cross(self):
        """
        Check if cube has white cross
        :return:
        """
        return self.down[0][1] == 31 and self.down[1][2] == 29 and self.down[2][1] == 33 and self.down[1][0] == 35

    def is_first_lvl(self):
        down = [[34, 31, 28],
                [35, 32, 29],
                [36, 33, 30]
                ]
        return self.down == down

    def is_second_lvl(self):
        return self.is_first_lvl() and self.front[1] == [40, 41, 42] and \
               self.back[1] == [49, 50, 51]

    def is_ideal(self):
        compare = Cube()
        compare.ideal_cube()
        a = self.up == compare.up and self.down == compare.down and self.front == compare.front and \
            self.back == compare.back and \
            self.left == compare.left and self.right == compare.right
        return a

    def is_figures_on_the_top(self):
        yellow = [13, 11, 15, 17]
        ind = [[1, 0], [2, 1], [1, 2], [0, 1]]
        for i, j in ind:
            if self.up[i][j] in yellow:
                yellow.pop(yellow.index(self.up[i][j]))
        return len(yellow) == 0 and self.is_second_lvl()

    def is_corners(self):
        checker = True
        index = [[0, 0], [0, 2], [2, 2], [2, 0]]
        for i, j in index:
            if self.up[i][j] not in [16, 10, 18, 12]:
                checker = False
        return checker and self.is_figures_on_the_top()

    def shuffle(self):
        self.commands_list = []
        self.commands = [self.turn_z_1_neg, self.turn_z_1_pos, self.turn_z_2_pos,
                         self.turn_z_2_neg, self.turn_z_3_pos, self.turn_z_3_neg,
                         self.turn_x_1_neg, self.turn_x_1_pos, self.turn_x_2_pos,
                         self.turn_x_2_neg, self.turn_x_3_pos, self.turn_x_3_neg,
                         self.turn_y_1_neg, self.turn_y_1_pos, self.turn_y_2_pos,
                         self.turn_y_2_neg, self.turn_y_3_pos, self.turn_y_3_neg
                         ]

        for i in range(len(self.commands)):
            self.commands_list.append(randrange(len(self.commands)))
        for i in range(len(self.commands_list)):
            a = self.commands[i]
            a()
