import Cube
from random import randrange

ideal_cube = Cube.Cube()


def test_turn_z1(cube):
    print(cube.front)
    cube.turn_z_1_neg()
    print(cube.front)
    cube.turn_z_1_neg(3)
    print(cube.front)

    print()
    # test up
    print(cube.up)
    cube.turn_z_1_neg()
    print(cube.up)
    cube.turn_z_1_neg(3)
    print(cube.up)


def test_turn_z2(cube):
    print(cube.front)
    cube.turn_z_2_neg()
    print(cube.front)
    cube.turn_z_2_neg(3)
    print(cube.front)

    print()
    # test up
    print(cube.back)
    # cube.turn_z_2_pos()
    print(cube.back)
    cube.turn_z_2_pos(3)
    print(cube.back)


def test_turn_z3(cube):
    cube.turn_z_3_pos()
    print(cube.front)
    cube.turn_z_3_neg()
    print(cube.front)


def test_turn_x1(cube):
    cube.turn_x_1_pos()
    print(cube.up)
    cube.turn_x_1_pos(2)
    print(cube.up)
    cube.turn_x_1_neg(3)
    print(cube.up)


def test_turn_x2(cube):
    cube.turn_x_2_pos()
    print(cube.up)
    cube.turn_x_2_pos(2)
    print(cube.up)
    cube.turn_x_2_neg(3)
    print(cube.up)


def test_turn_x3(cube):
    cube.turn_x_3_pos()
    print(cube.up)
    cube.turn_x_3_pos(2)
    print(cube.up)
    cube.turn_x_3_neg(3)
    print(cube.up)


def test_right_turn(cube):
    cube.right_turn()
    print(cube.up)
    cube.right_turn(n=5)
    print(cube.up)
    cube.right_turn(x=False)
    print(cube.up)
    cube.right_turn(n=5)
    print(cube.up)


def test_white_cross_yellow_center_1(cube: Cube):
    cube.turn_z_3_pos()
    cube.white_cross_yellow_center()
    print(cube.up)


def test_white_cross_yellow_center_2(cube: Cube):
    def is_white_cross(cube: Cube):
        arr = [29, 31, 33, 35]
        up_elem_indexes = [[0, 1], [1, 0], [2, 1], [1, 2]]
        for i, j in up_elem_indexes:
            if cube.up[i][j] in arr:
                arr.pop(arr.index(cube.up[i][j]))
        return not arr

    def sh(cube):
        a = []
        commands = [cube.turn_z_1_neg, cube.turn_z_1_pos, cube.turn_z_2_pos,
                    cube.turn_z_2_neg, cube.turn_z_3_pos, cube.turn_z_3_neg,
                    cube.turn_x_1_neg, cube.turn_x_1_pos, cube.turn_x_2_pos,
                    cube.turn_x_2_neg, cube.turn_x_3_pos, cube.turn_x_3_neg,
                    cube.turn_y_1_neg, cube.turn_y_1_pos, cube.turn_y_2_pos,
                    cube.turn_y_2_neg, cube.turn_y_3_pos, cube.turn_y_3_neg
                    ]
        for i in range(len(commands)):
            a.append(randrange(len(commands)))
            commands[a[i]]()
        return a
    cube.turn_y_1_pos()
    cube.turn_y_3_neg()
    cube.turn_x_3_neg()
    #shuffle(cube)
    # bug_combination = [14, 11, 4, 17, 15, 14, 5, 9, 11, 12, 7,
    #                    7, 16, 12, 17, 4, 11, 17]
    # commands = [cube.turn_z_1_neg, cube.turn_z_1_pos, cube.turn_z_2_pos,
    #             cube.turn_z_2_neg, cube.turn_z_3_pos, cube.turn_z_3_neg,
    #             cube.turn_x_1_neg, cube.turn_x_1_pos, cube.turn_x_2_pos,
    #             cube.turn_x_2_neg, cube.turn_x_3_pos, cube.turn_x_3_neg,
    #             cube.turn_y_1_neg, cube.turn_y_1_pos, cube.turn_y_2_pos,
    #             cube.turn_y_2_neg, cube.turn_y_3_pos, cube.turn_y_3_neg
    #             ]
    # for i in bug_combination:
    #     commands[i]()
    # print()
    # print(cube.up)
    # print(cube.down)
    # print(cube.front)
    # print(cube.left)
    # print(cube.back)
    # print(cube.right)
    # print()
    # cube.white_cross_yellow_center()
    # print(cube.up)
    # print(cube.is_white_cross())

    count = 0
    for i in range(100000):
        #shuffle(cube)
        # print(sh(cube))
        # print()
        # print(cube.up)
        # print(cube.down)
        # print(cube.front)
        # print(cube.left)
        # print(cube.back)
        # print(cube.right)
        # print()
        cube.white_cross_yellow_center()
        if not is_white_cross(cube):
            print(cube.up)
            count += 1
    print(count)


def shuffle(cube: Cube):
    commands = [cube.turn_z_1_neg, cube.turn_z_1_pos, cube.turn_z_2_pos,
                cube.turn_z_2_neg, cube.turn_z_3_pos, cube.turn_z_3_neg,
                cube.turn_x_1_neg, cube.turn_x_1_pos, cube.turn_x_2_pos,
                cube.turn_x_2_neg, cube.turn_x_3_pos, cube.turn_x_3_neg,
                cube.turn_y_1_neg, cube.turn_y_1_pos, cube.turn_y_2_pos,
                cube.turn_y_2_neg, cube.turn_y_3_pos, cube.turn_y_3_neg
                ]
    for i in range(len(commands)):
        commands[randrange(len(commands))]()



def test():
    cube = Cube.Cube()
    cube.ideal_cube()
    cube.check_structure()

    # test_turn_z1(cube)

    # test_turn_z2(cube)

    # test_turn_z3(cube)

    # test_turn_x1(cube)

    # test_turn_x2(cube)

    # test_turn_x3(cube)

    # test_right_turn(cube)

    #test_white_cross_yellow_center_1(cube)

    test_white_cross_yellow_center_2(cube)

    # self.front = [[37, 38, 39],
    #               [40, 41, 42],
    #               [43, 44, 45]
    #               ]
    #
    # self.back = [[46, 47, 48],
    #              [49, 50, 51],
    #              [52, 53, 54]
    #              ]
    #
    # self.left = [[7, 4, 1],
    #              [8, 5, 2],
    #              [9, 6, 3]
    #              ]
    #
    # self.right = [[25, 22, 19],
    #               [26, 23, 20],
    #               [27, 24, 21]
    #               ]
    # self.up = [[16, 13, 10],
    #            [17, 14, 11],
    #            [18, 15, 12]
    #            ]

    """[[0, 1, False],   [2, 1, False], [1, 0, True],[1, 2, True], ]"""

    # self.down = [[34, 31, 28],
    #              [35, 32, 29],
    #              [36, 33, 30]
    #              ]
