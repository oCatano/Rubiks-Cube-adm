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
            a.append(Cube.randrange(len(commands)))
            commands[a[i]]()
        return a

    cube.turn_y_1_pos()
    cube.turn_y_3_neg()
    cube.turn_x_3_neg()
    # shuffle(cube)
    # bug_combination = [5, 1, 6, 15, 0, 5, 14, 2, 4, 3,
    #                    3, 14, 4, 9, 17, 1, 1, 2]
    # commands = [cube.turn_z_1_neg, cube.turn_z_1_pos, cube.turn_z_2_pos,
    #             cube.turn_z_2_neg, cube.turn_z_3_pos, cube.turn_z_3_neg,
    #             cube.turn_x_1_neg, cube.turn_x_1_pos, cube.turn_x_2_pos,
    #             cube.turn_x_2_neg, cube.turn_x_3_pos, cube.turn_x_3_neg,
    #             cube.turn_y_1_neg, cube.turn_y_1_pos, cube.turn_y_2_pos,
    #             cube.turn_y_2_neg, cube.turn_y_3_pos, cube.turn_y_3_neg
    #             ]
    # for i in bug_combination:
    #     commands[i]()
    # cube.white_cross_yellow_center()
    # print(cube.up)
    # print(is_white_cross(cube))
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
    for i in range(10000):
        shuffle(cube)
        cube.shuffle()
        cube.white_cross_yellow_center()
        if not is_white_cross(cube):
            print(False)
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
        commands[Cube.randrange(len(commands))]()


def test_white_cross(cube: Cube):
    # cube.shuffle()
    # cube.white_cross_yellow_center()
    # cube.white_cross()
    # print(cube.front)
    # print(cube.is_white_cross(is_white_cross_yellow_center=True))
    for i in range(10000):
        cube.shuffle()
        cube.white_cross()
        # print(cube.down)
        if not cube.is_white_cross():
            print(False)


def test_first_lvl(cube: Cube):
    down = [[34, 31, 28],
            [35, 32, 29],
            [36, 33, 30]
            ]
    for i in range(10000):
        cube.shuffle()
        cube.first_lvl()
        if cube.down != down:
            print(False)


def test_second_lvl(cube: Cube):
    for i in range(10000):
        cube.shuffle()
        # print(cube.up)
        cube.second_lvl()
        # print(cube.front)
        # print(cube.left)
        # print(cube.right)
        if not cube.is_second_lvl():
            print(cube.is_second_lvl())


def test_figures_on_top(cube: Cube):
    for i in range(10000):
        cube.shuffle()
        cube.figures_on_the_top()
        if not cube.is_figures_on_the_top():
            print(cube.up)


def test_corners(cube: Cube):
    for i in range(10000):
        cube.shuffle()
        cube.corners()
        # print(cube.up)
        if not cube.is_corners():
            print('No')


def test_final(cube: Cube):
    for i in range(10000):
        cube.shuffle()
        cube.final()
        if not cube.is_ideal():
            print('No')


def test_solve_cube(cube: Cube):
    for i in range(10000):
        cube.shuffle()
        cube.solve_cube()
        if not cube.is_ideal():
            print('No')


def test_for_fun(cube: Cube):
    cube.turn_z_1_neg()
    cube.solve_cube()
    print(cube.is_ideal())
    cube.turn_z_2_pos()
    cube.turn_x_2_neg()
    cube.turn_z_2_neg()
    cube.turn_x_2_pos()
    cube.solve_cube()
    print(cube.is_ideal())

    cube.right_turn()
    cube.left_turn()
    cube.solve_cube()
    print(cube.is_ideal())

    cube.right_turn(False,False,False)
    cube.solve_cube()
    print(cube.is_ideal())


def test():
    cube = Cube.Cube()
    cube.ideal_cube()

    # test_turn_z1(cube)

    # test_turn_z2(cube)

    # test_turn_z3(cube)

    # test_turn_x1(cube)

    # test_turn_x2(cube)

    # test_turn_x3(cube)

    # test_right_turn(cube)

    # test_white_cross_yellow_center_1(cube)

    # test_white_cross_yellow_center_2(cube)

    # test_white_cross(cube)

    # test_first_lvl(cube)

    # test_second_lvl(cube)

    test_figures_on_top(cube)

    test_corners(cube)

    test_final(cube)

    test_solve_cube(cube)

    test_for_fun(cube)

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
