from Shapes import *

"""
Возможные проблемы:
1) Центр будет перевернут (отзеркаленный верх)
"""


class Cube:
    one_shape = []  # 6
    two_shapes = []  # 12
    three_shapes = []  # 8
    front = [[], [], []]
    back = [[], [], []]
    up = [[], [], []]
    down = [[], [], []]
    right = [[], [], []]
    left = [[], [], []]

    def __init__(self):
        self.ideal_cube()

    def is_ideal(self):
        compare = Cube()
        compare.ideal_cube()
        if self.up == compare.up and self.down == compare.down and self.front == compare.front and \
                self.back == compare.back and \
                self.left == compare.left and self.right == compare.right:
            return

    def solve_cube(self):
        white_on_up = 0
        white_num = [29, 31, 33, 35]
        compare = Cube()

        # white cross yellow center
        if self.up == compare.up and self.down == compare.down and self.front == compare.front and \
                self.back == compare.back and \
                self.left == compare.left and self.right == compare.right:
            return
        elif self.down == compare.down:
            # solve if down already solved
            pass
        else:
            self.white_cross_yellow_center()

    def is_white_cross(self):
        arr = [29, 31, 33, 35]
        up_elem_indexes = [[0, 1], [1, 0], [2, 1], [1, 2]]
        for i, j in up_elem_indexes:
            if self.up[i][j] in arr:
                arr.pop(arr.index(self.up[i][j]))
        return not arr

    # Makes white cross on up plane
    def white_cross_yellow_center(self):
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

    # reset cube to solved one
    def ideal_cube(self):
        self.one_shape.clear()
        self.two_shapes.clear()
        self.three_shapes.clear()
        params = [[14, 'yellow'], [23, 'red'], [32, 'white'], [5, 'orange'],
                  [41, 'blue'], [50, 'green']
                  ]
        for items in params:
            self.one_shape.append(OneShape(items[0], items[1]))

        params = [[11, 26, 'yellow', 'red'],
                  [15, 38, 'yellow', 'blue'],
                  [17, 2, 'yellow', 'orange'],
                  [13, 53, 'yellow', 'green'],

                  [40, 6, 'blue', 'orange'],
                  [4, 49, 'orange', 'green'],
                  [51, 22, 'green', 'red'],
                  [24, 42, 'red', 'blue'],

                  [44, 33, 'blue', 'white'],
                  [8, 29, 'orange', 'white'],
                  [47, 31, 'green', 'white'],
                  [20, 35, 'red', 'white'],
                  ]

        for items in params:
            self.two_shapes.append(TwoShapes(items[0], items[1], items[2], items[3]))

        params = [[18, 3, 37, 'yellow', 'orange', 'blue'],
                  [16, 52, 1, 'yellow', 'green', 'orange'],
                  [10, 25, 54, 'yellow', 'red', 'green'],
                  [12, 39, 27, 'yellow', 'blue', 'red'],

                  [43, 9, 30, 'blue', 'orange', 'white'],
                  [7, 46, 28, 'orange', 'green', 'white'],
                  [48, 19, 34, 'green', 'red', 'white'],
                  [21, 45, 36, 'red', 'blue', 'white'],
                  ]

        for items in params:
            self.three_shapes.append(ThreeShapes(items[0], items[1], items[2], items[3], items[4], items[5]))

        # self.up = [[self.__three(16),self.__two(13),self.__three(10)],
        #            [self.__two(17), self.__one(14), self.__two(11)],
        #            [self.__three(18),self.__two(15),self.__three(12)]
        #            ]
        #
        # self.front = [[self.__three(37), self.__two(38), self.__three(39)],
        #               [self.__two(40), self.__one(41), self.__two(42)],
        #               [self.__three(43), self.__two(44), self.__three(45)]
        #               ]
        #
        # self.down = [[self.__three(34), self.__two(31), self.__three(28)],
        #            [self.__two(25), self.__one(32), self.__two(29)],
        #            [self.__three(36), self.__two(33), self.__three(30)]
        #            ]
        #
        # self.back = [[self.__three(46),self.__two(47),self.__three(48)],
        #            [self.__two(49), self.__one(50), self.__two(51)],
        #            [self.__three(52),self.__two(53),self.__three(54)]
        #         ]
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

    def __one(self, number):
        for item in self.one_shape:
            if item.number_1 == number:
                return item
        return False

    def __two(self, number):
        for item in self.two_shapes:
            if item.number_1 == number or item.number_2 == number:
                return item
        return False

    def __three(self, number):
        for item in self.three_shapes:
            if item.number_1 == number or item.number_2 == number or item.number_3 == number:
                return item
        return False

    # returns new object of one plane (list of 3 lists)
    def __copy_part(self, a):
        temp = []
        for item in a:
            temp.append(item.copy())
        return temp

    # check is it all 54 unique number
    def check_structure(self):
        array = []
        for items in self.one_shape:
            array.append(items.number_1)

        for items in self.two_shapes:
            array.append(items.number_1)
            array.append(items.number_2)

        for items in self.three_shapes:
            array.append(items.number_1)
            array.append(items.number_2)
            array.append(items.number_3)

        array.sort()
        for i in range(1, 55):
            if i != array[i - 1]:
                return False

        array.clear()
        for i in range(3):
            for j in range(3):
                array.append(self.up[i][j])
                array.append(self.down[i][j])
                array.append(self.front[i][j])
                array.append(self.back[i][j])
                array.append(self.left[i][j])
                array.append(self.right[i][j])

        array.sort()
        for i in range(1, 55):
            if i != array[i - 1]:
                return False

    def __get_shape(self, number):
        for item in self.one_shape:
            if item.number_1 == number:
                return item

        for item in self.two_shapes:
            if item.number_1 == number or item.number_2 == number:
                return item

        for item in self.three_shapes:
            if item.number_1 == number or item.number_2 == number or item.number_3 == number:
                return item
        return False

    # turn cube on z_1 clockwise n times
    def turn_z_1_neg(self, n=1):
        for i in range(n):
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
            self.turn_z_1_neg(3)

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
    def turn_z_3_pos(self, n=1):
        for i in range(n):
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
            self.turn_z_3_pos(3)

    # turn x_1 counterclockwise n times
    def turn_x_1_pos(self, n=1):
        for i in range(n):
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
            self.turn_x_1_pos(3)

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
    def turn_x_3_pos(self, n=1):
        for i in range(n):
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
            self.turn_x_3_pos(3)

    # turn y_1 counterclockwise n times
    def turn_y_1_pos(self, n=1):
        for i in range(n):
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
            self.turn_y_1_pos(3)

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
    def turn_y_3_pos(self, n=1):
        for i in range(n):
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
            self.turn_y_3_pos()

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
                    self.turn_x_3_neg()
                    self.turn_z_1_neg()
                    self.turn_x_3_pos()
                    self.turn_z_1_pos()
                elif x & (not y):
                    self.turn_y_3_neg()
                    self.turn_z_1_neg()
                    self.turn_y_3_pos()
                    self.turn_z_1_pos()
                elif x & y:
                    self.turn_x_1_neg()
                    self.turn_z_1_neg()
                    self.turn_x_1_pos()
                    self.turn_z_1_pos()
            else:
                if x & (not y):
                    self.turn_x_1_neg()
                    self.turn_z_3_neg()
                    self.turn_x_1_pos()
                    self.turn_z_3_pos()
                elif x & y:
                    self.turn_y_1_neg()
                    self.turn_z_3_neg()
                    self.turn_y_1_pos()
                    self.turn_z_3_pos()
                elif (not x) & y:
                    self.turn_x_3_neg()
                    self.turn_z_3_neg()
                    self.turn_x_3_pos()
                    self.turn_z_3_pos()
                elif (not x) & (not y):
                    self.turn_y_3_neg()
                    self.turn_z_3_neg()
                    self.turn_y_3_pos()
                    self.turn_z_3_pos()

    def left_turn(self, x=True, y=True, z=True, n=1):
        """
                Над каким ребром будет совершаться правый поворот
                :param x: первая ось (True - если вдоль оси ox False - против)
                :param y: Вторая ось (True - если вдоль оси oy False - против)
                :param z: ориентация кубика (True - если вдоль оси oz False - против)
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
                    self.turn_x_3_pos()
                    self.turn_z_1_pos()
                    self.turn_x_3_neg()
                    self.turn_z_1_neg()
                elif (not x) & (not y):
                    self.turn_y_3_pos()
                    self.turn_z_1_pos()
                    self.turn_y_3_neg()
                    self.turn_z_1_neg()
            else:
                if (not x) & y:
                    self.turn_y_1_pos()
                    self.turn_z_3_pos()
                    self.turn_y_1_neg()
                    self.turn_z_1_neg()
                elif (not x) & (not y):
                    self.turn_x_3_pos()
                    self.turn_z_3_pos()
                    self.turn_x_3_neg()
                    self.turn_z_3_neg()
                elif x & (not y):
                    self.turn_y_3_pos()
                    self.turn_z_3_pos()
                    self.turn_y_3_neg()
                    self.turn_z_3_neg()
                elif x & y:
                    self.turn_x_1_pos()
                    self.turn_z_3_pos()
                    self.turn_x_1_neg()
                    self.turn_z_3_neg()
