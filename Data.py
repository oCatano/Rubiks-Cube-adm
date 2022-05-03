import Cube

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


def test_white_cross_yellow_center(cube : Cube):
    cube.turn_z_3_pos()
    cube.white_cross_yellow_center()
    print(cube.up)



def test():
    cube = Cube.Cube()
    cube.ideal_cube()
    cube.check_structure()

    # test_turn_z1(cube)

    # test_turn_z2(cube)

    # test_turn_z3(cube)

    # test_turn_x1(cube)

    # test_turn_x2(cube)

    #test_turn_x3(cube)

    #test_right_turn(cube)

    test_white_cross_yellow_center(cube)

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

    # self.down = [[34, 31, 28],
    #              [35, 32, 29],
    #              [36, 33, 30]
    #              ]
