import pytest
from functions.calculate_numbers import calculate_numbers_function


@pytest.mark.parametrize("input_field, rows, cols, expected_field", [


    # teste matriz 6x6 - 8 bombas
    ([
        [-1, 0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1, -1,  0,],
        [0, -1,  0,  0,  0,  0,],
        [0,  0,  0, -1,  0,  0,],
        [-1, 0,  0, -1,  0, -1],
    ], 6, 6, [
        [-1, 1,  0,  0,  0,  0,],
        [1,  1,  1,  2,  2,  1,],
        [1,  1,  2, -1, -1,  1,],
        [1, -1,  3,  3,  3,  1,],
        [2,  2,  3, -1,  3,  1,],
        [-1, 1,  2, -1,  3, -1],
    ]),

    # teste matriz 7x7 - 9
    ([
        [-1, 0,  0,  0,  0,  0, -1],
        [0,  0,  0,  0,  0,  0, 0],
        [0,  0,  0, -1, -1,  0, 0],
        [0, -1,  0,  0,  0,  0, 0],
        [0,  0,  0, -1,  0,  0, 0],
        [-1, 0,  0, -1,  0, -1, 0],
        [0, 0,  0, 0,  0, 0, 0],
    ], 7, 7, [
        [-1,  1,  0,  0,  0,  1, -1],
        [1,  1,  1,  2,  2,  2, 1],
        [1,  1,  2, -1, -1,  1, 0],
        [1, -1,  3,  3,  3,  1, 0],
        [2,  2,  3, -1,  3,  1, 1],
        [-1, 1,  2, -1,  3, -1, 1],
        [1,  1,  1,  1,  2, 1, 1],
    ]),

    # para o tabuleiro de nível fácil - 10 testes no total

    # teste 1
    ([
        [0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1, -1,  0,  0,  0],
        [0,  0,  0,  0,  0,  0, -1,  0],
        [0,  0,  0, -1,  0,  0,  0, - 1],
        [-1,  0,  0, -1,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0, -1, -1,  0],
        [0,  0,  0,  0,  0,  0, -1,  0],
    ], 8, 8, [
        [0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  1,  2,  2,  1,  0,  0],
        [0,  0,  1, -1, -1,  2,  1,  1],
        [0,  0,  2,  3,  3,  2, -1,  2],
        [1,  1,  2, -1,  2,  1,  2, -1],
        [-1,  1,  2, -1,  3, 2,  3, 2],
        [1,  1,  1,  1,  2, -1, -1, 2],
        [0,  0,  0,  0,  1,  3, -1, 2]
    ]),

    # teste 2
    ([
        [0,  0, -1,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0, -1,  0,  0,],
        [0,  0,  0,  0,  0,  0, -1,  0,],
        [0,  0, -1,  0,  0,  0,  0,  0,],
        [-1,  0,  0,  0,  0, -1,  0,  0,],
        [0, -1,  0,  0, -1,  0,  0, -1,],
        [0,  0,  0,  0,  0,  0, -1,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,],
    ], 8, 8, [
        [0,  1, -1, 1,  1,  1,  1,  0,],
        [0,  1,  1, 1,  1, -1,  2,  1,],
        [0,  1,  1, 1,  1,  2, -1,  1,],
        [1,  2, -1, 1,  1,  2,  2,  1,],
        [-1, 3,  2,  2, 2, -1,  2,  1,],
        [2, -1,  1, 1, -1,  3,  3, -1,],
        [1,  1,  1, 1,  1,  2, -1,  2,],
        [0,  0,  0, 0,  0,  1,  1,  1,],
    ]),

    # teste 3
    ([
        [-1,  0, 0,  0,  0,  0,  0,  0,],
        [-1, 0,  0,  0,  0,  0,  0,  0,],
        [0,  0, 0,  0,  0,  0,  0, - 1,],
        [0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, 0, -1, -1,  0,  0,  0, -1,],
        [0,  0,  0, -1,  0,  0,  0,  0,],
        [-1,  0, 0, 0,  0, - 1,  0,  0,],
    ], 8, 8, [
        [-1, 2,  0,  0,  0,  0,  0,  0,],
        [-1, 2,  0,  0,  0,  0,  1,  1,],
        [1,  1,  0,  0,  0,  0,  1, -1,],
        [0,  0,  0,  0,  0,  0,  1,  1,],
        [1,  2,  2,  2,  1,  0,  1,  1,],
        [-1, 2, -1, -1,  2,  0,  1, -1,],
        [2,  3,  3, -1,  3,  1,  2,  1,],
        [-1, 1,  1,  1,  2, -1,  1,  0,],
    ]),

    # Teste 4
    ([
        [0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0, -1, -1,  0,  0,  0],
        [0,  0,  0,  0,  0,  0, -1,  0],
        [0,  0,  0, -1,  0,  0,  0, - 1],
        [-1,  0,  0, -1,  0,  0,  0,  0],
        [0,  0,  0,  0,  0, -1, -1,  0],
        [0,  0,  0,  0,  0,  0, -1,  0],
    ], 8, 8, [
        [0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  1,  2,  2,  1,  0,  0],
        [0,  0,  1, -1, -1,  2,  1,  1],
        [0,  0,  2,  3,  3,  2, -1,  2],
        [1,  1,  2, -1,  2,  1,  2, -1],
        [-1,  1,  2, -1,  3, 2,  3, 2],
        [1,  1,  1,  1,  2, -1, -1, 2],
        [0,  0,  0,  0,  1,  3, -1, 2]
    ]),

    # Teste 5
    ([
        [0,  0, -1,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0, -1,  0,  0],
        [0,  0,  0,  0,  0,  0, -1,  0],
        [0,  0, -1,  0,  0,  0,  0,  0],
        [-1,  0,  0,  0,  0, -1,  0,  0],
        [0, -1,  0,  0, -1,  0,  0, -1],
        [0,  0,  0,  0,  0,  0, -1,  0],
        [0,  0,  0,  0,  0,  0,  0,  0],
    ], 8, 8, [
        [0,  1, -1, 1,  1,  1,  1,  0],
        [0,  1,  1, 1,  1, -1,  2,  1],
        [0,  1,  1, 1,  1,  2, -1,  1],
        [1,  2, -1, 1,  1,  2,  2,  1],
        [-1, 3,  2,  2, 2, -1,  2,  1],
        [2, -1,  1, 1, -1,  3,  3, -1],
        [1,  1,  1, 1,  1,  2, -1,  2],
        [0,  0,  0, 0,  0,  1,  1,  1],
    ]),

    # Teste 6
    ([
        [-1,  0, 0,  0,  0,  0,  0,  0],
        [-1, 0,  0,  0,  0,  0,  0,  0],
        [0,  0, 0,  0,  0,  0,  0, - 1],
        [0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0],
        [-1, 0, -1, -1,  0,  0,  0, -1],
        [0,  0,  0, -1,  0,  0,  0,  0],
        [-1,  0, 0, 0,  0, - 1,  0,  0],
    ], 8, 8, [
        [-1, 2,  0,  0,  0,  0,  0,  0],
        [-1, 2,  0,  0,  0,  0,  1,  1],
        [1,  1,  0,  0,  0,  0,  1, -1],
        [0,  0,  0,  0,  0,  0,  1,  1],
        [1,  2,  2,  2,  1,  0,  1,  1],
        [-1, 2, -1, -1,  2,  0,  1, -1],
        [2,  3,  3, -1,  3,  1,  2,  1],
        [-1, 1,  1,  1,  2, -1,  1,  0],
    ]),

    # Teste 7
    ([
        [0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0, -1, -1,  0,  0,  0],
        [0,  0,  0,  0,  0,  0, -1,  0],
        [0,  0,  0, -1,  0,  0,  0, - 1],
        [-1,  0,  0, -1,  0,  0,  0,  0],
        [0,  0,  0,  0,  0, -1, -1,  0],
        [0,  0,  0,  0,  0,  0, -1,  0],
    ], 8, 8, [
        [0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  1,  2,  2,  1,  0,  0],
        [0,  0,  1, -1, -1,  2,  1,  1],
        [0,  0,  2,  3,  3,  2, -1,  2],
        [1,  1,  2, -1,  2,  1,  2, -1],
        [-1,  1,  2, -1,  3, 2,  3, 2],
        [1,  1,  1,  1,  2, -1, -1, 2],
        [0,  0,  0,  0,  1,  3, -1, 2]
    ]),

    # Teste 8
    ([
        [0,  0, - 1,  0,  0,  0,  0,  0,],
        [0, - 1,  0,  0,  0,  0,  0, - 1,],
        [0,  0,  0,  0,  0,  0, - 1, - 1,],
        [0,  0,  0,  0, - 1,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0, - 1,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, - 1,  0,  0,  0,],
        [-1,  0,  0,  0,  0, - 1,  0,  0,],
    ],  8, 8, [
        [1,  2, -1,  1,  0,  0,  1,  1],
        [1, -1,  2,  1,  0,  1,  3, -1],
        [1,  1,  1,  1,  1,  2, -1, -1],
        [0,  0,  0,  1, -1,  3,  3,  3],
        [0,  0,  0,  1,  1,  2, -1,  1],
        [0,  0,  0,  1,  1,  2,  1,  1],
        [1,  1,  0,  1, -1,  2,  1,  0],
        [-1, 1,  0,  1,  2, -1,  1,  0],
    ]),

    # Teste 9
    ([
        [-1,  0, 0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0, - 1],
        [0,  0,  0,  0,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0],
        [-1, 0, -1, -1,  0,  0,  0, -1],
        [0,  0,  0, -1,  0,  0,  0,  0],
        [-1,  0, 0, 0,  0, - 1,  0,  0],
    ], 8, 8, [
        [-1, 1,  0,  0,  0,  0,  0,  0],
        [1,  1,  0,  0,  0,  0,  1,  1],
        [0,  0,  0,  0,  0,  0,  1, -1],
        [0,  0,  0,  0,  0,  0,  1,  1],
        [1,  2,  2,  2,  1,  0,  1,  1],
        [-1, 2, -1, -1,  2,  0,  1, -1],
        [2,  3,  3, -1,  3,  1,  2,  1],
        [-1, 1,  1,  1,  2, -1,  1,  0],
    ]),
    # Teste 10
    ([
        [0,  0,  0,  0,  0,  0,  0, -1,],
        [0, -1,  0,  0,  0,  0, -1,  0],
        [0,  0,  0, -1,  0,  0,  0,  0],
        [0,  0, -1,  0,  0, -1,  0,  0],
        [0,  0,  0, -1,  0,  0,  0,  0],
        [0,  0,  0,  0,  0,  0,  0,  0],
        [-1, 0,  0,  0,  0, -1,  0,  0],
        [0,  0,  0,  0,  0, -1,  0,  0],
    ], 8, 8, [
        [1,  1,  1,  0,  0,  1,  2, -1],
        [1, -1,  2,  1,  1,  1, -1,  2],
        [1,  2,  3, -1,  2,  2,  2,  1],
        [0,  1, -1,  3,  3, -1,  1,  0],
        [0,  1,  2, -1,  2,  1,  1,  0],
        [1,  1,  1,  1,  2,  1,  1,  0],
        [-1, 1,  0,  0,  2, -1,  2,  0],
        [1,  1,  0,  0,  2, -1,  2,  0],
    ]),

    # teste matriz 9x9

    ([
        [0, - 1, - 1,  0, - 1,  0, - 1,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0, - 1,  0,],
        [0,  0,  0, - 1,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0, - 1, - 1,  0,  0,],
        [0,  0,  0, - 1,  0,  0,  0,  0,  0,],
        [0,  0,  0, - 1,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, - 1,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ], 9, 9, [
        [1, -1, -1,  2, -1,  2, -1,  2,  1,],
        [1,  2,  3,  3,  2,  2,  2, -1,  1,],
        [0,  0,  1, -1,  2,  2,  3,  2,  1,],
        [0,  0,  2,  2,  3, -1, -1,  1,  0,],
        [0,  0,  2, -1,  3,  2,  2,  1,  0,],
        [0,  0,  2, -1,  2,  0,  0,  0,  0,],
        [0,  0,  2,  2,  2,  0,  0,  0,  0,],
        [0,  0,  1, -1,  1,  0,  0,  0,  0,],
        [0,  0,  1,  1,  1,  0,  0,  0,  0,],
    ]),
    # teste matriz 10x10

    ([
        [0, - 1,  0, - 1,  0,  0, - 1, - 1,  0,  0,],
        [0,  0, - 1,  0, - 1,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0, - 1,  0,  0,  0,  0,],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0, - 1,  0,  0,  0, - 1,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ], 10, 10, [
        [1, -1,  3, -1,  2,  2, -1, -1,  1,  0,],
        [1,  2, -1,  3, -1,  3,  3,  2,  1,  0,],
        [1,  2,  1,  2,  2, -1,  1,  0,  0,  0,],
        [-1, 1,  0,  0,  1,  1,  1,  0,  0,  0,],
        [2,  2,  1,  1,  1,  0,  1,  1,  1,  0,],
        [-1, 1,  1, -1,  1,  0,  1, -1,  1,  0,],
        [2,  2,  1,  1,  1,  0,  1,  1,  1,  0,],
        [-1, 1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [1,  1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ]),


    # teste matriz 10x14
    ([
        [0, - 1, - 1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0, - 1,  0,  0, - 1,  0, - 1,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, - 1, - 1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0, - 1, - 1,  0, - 1, - 1,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, - 1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, - 1,  0, - 1,  0,  0, - 1, - 1,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0,  0, - 1,  0, - 1, - 1,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0, - 1, - 1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ], 10, 14, [
        [2, -1, -1,  2,  1,  1,  2,  1,  1,  0,  0,  0,  0,  0,],
        [-1, 4, -1,  4,  3, -1,  2, -1,  1,  0,  0,  0,  0,  0,],
        [2,  4,  4, -1, -1,  4,  4,  2,  1,  0,  0,  0,  0,  0,],
        [-1, 2, -1, -1,  5, -1, -1,  1,  0,  0,  0,  0,  0,  0,],
        [2,  3,  5, -1,  4,  3,  4,  3,  1,  0,  0,  0,  0,  0,],
        [2, -1,  3, -1,  3,  3, -1, -1,  2,  0,  0,  0,  0,  0,],
        [-1, 3,  3,  4, -1,  4, -1, -1,  2,  0,  0,  0,  0,  0,],
        [-1, 2,  1, -1, -1,  3,  2,  2,  1,  0,  0,  0,  0,  0,],
        [1,  1,  1,  2,  2,  1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ]),


    # teste matriz 10x15

    ([
        [0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, -1, -1, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1, -1,  0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, -1,  0,  0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0, -1,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ], 10, 15, [
        [1, -1, -1,  2,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [2,  5, -1,  4,  2, -1,  2,  1,  0,  0,  0,  0,  0,  0,  0,],
        [3, -1, -1, -1,  4,  4, -1,  3,  1,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1, -1,  3, -1, -1, -1,  1,  0,  0,  0,  0,  0,  0,],
        [-1, 8, -1,  4,  2,  2,  3,  2,  1,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  3,  2,  3,  2,  1,  0,  0,  0,  0,  0,  0,  0,],
        [4, -1,  4,  3, -1, -1, -1,  2,  1,  0,  0,  0,  0,  0,  0,],
        [-1, 3, -1,  2,  2,  3,  3, -1,  1,  0,  0,  0,  0,  0,  0,],
        [1,  2,  1,  1,  0,  0,  1,  1,  1,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ]),



    # para o tabuleiro de nível intermediário - 10 testes no total
    # teste 01
    ([
        [0, -1, -1, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, -1,  0, -1, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0, -1, -1,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  0,  0, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  0, -1,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0, -1, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ], 10, 16, [
        [1, -1, -1, -1, 2, 1, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 4, -1, -1, 4, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0],
        [2, -1, 6, -1, -1, 1, 2, -1, 2, 0, 0, 0, 0, 0, 0, 0],
        [-1, 3, -1, -1, 3, 2, 4, -1, 3, 0, 0, 0, 0, 0, 0, 0],
        [3, 5, 4, 3, 2, 2, -1, -1, 3, 0, 0, 0, 0, 0, 0, 0],
        [-1, -1, -1, 2, 3, -1, 6, -1, 2, 0, 0, 0, 0, 0, 0, 0],
        [-1, -1, 5, -1, 5, -1, -1, 3, 1, 0, 0, 0, 0, 0, 0, 0],
        [-1, 3, 3, -1, -1, 4, -1, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]),


    # teste 02
    ([
        [0, -1,  0, -1,  0,  0, -1, - 1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, -1,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1, - 1,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0, -1,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, - 1, - 1,  0,  0,  0, -1, - 1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0, -1, - 1,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, -1,  0,  0, -1,  0, -1, - 1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0, -1, - 1,  0, -1, - 1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ], 10, 16, [
        [2, -1,  3, - 1,  1,  2, -1, -1,  1,  0,  0,  0,  0,  0,  0,  0,],
        [2, -1,  5,  3,  2,  2, -1,  4,  2,  0,  0,  0,  0,  0,  0,  0,],
        [2,  4, - 1, -1,  1,  2,  3, - 1,  1,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  6, - 1,  4,  1,  2, -1,  4,  2,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  4,  1,  2, -1, -1,  2,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  6, - 1, -1,  2,  3,  5, - 1,  3,  0,  0,  0,  0,  0,  0,  0,],
        [3, - 1,  5,  5, - 1,  4, - 1, -1,  2,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  3, - 1, -1,  3, - 1, -1,  3,  1,  0,  0,  0,  0,  0,  0,  0,],
        [1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    ]),

    # teste 03
    ([
        [-1,  0,  0, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1, -1,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0,  0, -1, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  0,  0, -1, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ], 10, 16, [
        [-1,  2, 2,  -1, 3, 4, -1,  2,  0,  0,  0,  0,  0,  0,  0,  0,],
        [3, 5, -1, 4, -1, -1, -1, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        [-1, -1, -1, 3, 3, -1, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        [-1, 4, 3, 3, 3, 4, -1, 3, 1, 0, 0, 0, 0, 0, 0, 0],
        [2, 2, 1, -1, -1, 5, -1, -1, 2, 0, 0, 0, 0, 0, 0, 0],
        [-1, 3, 2, 4, -1, -1, 7, -1, 3, 0, 0, 0, 0, 0, 0, 0],
        [-1, -1, 2, 4, -1, -1, -1, -1, 3, 0, 0, 0, 0, 0, 0, 0],
        [2, 2, 2, -1, -1, 4, 4, -1, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    ]),

    # # teste 04
    ([
        [0, -1,  0, -1, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0, -1,  0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, -1, -1,  0, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, -1, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  0, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0,  0, -1,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ], 10, 16, [
        [2, -1,  3, -1, -1,  3,  4, -1,  2,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  2,  4, -1,  6, -1, -1, -1,  3,  0,  0,  0,  0,  0,  0,  0,],
        [1,  1,  3, -1, -1,  4,  4, -1,  2,  0,  0,  0,  0,  0,  0,  0,],
        [1,  2,  4, -1, -1,  4,  2,  2,  1,  0,  0,  0,  0,  0,  0,  0,],
        [1, -1, -1,  5, -1,  6, -1,  3,  1,  0,  0,  0,  0,  0,  0,  0,],
        [3,  4,  4,  4, -1, -1, -1, -1,  1,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  2, -1,  4,  6, -1,  5,  2,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  3,  2,  2, -1,  3, -1, -1,  1,  0,  0,  0,  0,  0,  0,  0,],
        [1, 1, 0, 1, 1, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    ]),

    # teste 05
    ([
        [-1, -1,  0, -1, -1, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0, -1,  0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, -1,  0, -1,  0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, -1,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1, -1,  0, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ], 10, 16, [
        [-1, -1,  3, -1, -1, -1, -1, -1,  2,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  4,  5, -1,  7, -1, -1, -1,  3,  0,  0,  0,  0,  0,  0,  0,],
        [3, -1,  3, -1,  5, -1, -1, -1,  2,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  3,  3,  1,  3, -1,  5,  3,  2,  0,  0,  0,  0,  0,  0,  0,],
        [2, -1,  2,  2,  2,  2,  2, -1,  1,  0,  0,  0,  0,  0,  0,  0,],
        [1,  3, -1,  5, -1,  2,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,],
        [0,  3, -1, -1, -1,  3,  2,  1,  1,  0,  0,  0,  0,  0,  0,  0,],
        [0,  2, -1, -1,  4, -1,  2, -1,  1,  0,  0,  0,  0,  0,  0,  0,],
        [0, 1, 2, 2, 2, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    ]),

    # # teste 06
    ([
        [0, -1, -1,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  0, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0, -1, -1, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  0, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0,  0, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ], 10, 16, [
        [3, -1, -1,  2,  1,  2, -1, -1,  1,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  5,  4, -1,  3,  3,  3,  2,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  3, -1,  3,  3, -1,  2,  0,  0,  0,  0,  0,  0,  0,],
        [3,  5,  4,  5,  4, -1,  4, -1,  3,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  3, -1, -1, -1,  3,  4, -1,  2,  0,  0,  0,  0,  0,  0,  0,],
        [3,  6, - 1, -1,  4,  4, -1,  3,  1,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  5, -1,  5, -1,  3,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  4,  2,  3, -1,  4, -1,  2,  0,  0,  0,  0,  0,  0,  0,  0,],
        [1, 1, 0, 1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    ]),

    # # teste 07
    ([
        [0, -1,  0, -1,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, -1,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  0, -1,  0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0, -1, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0, -1,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, -1,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ], 10, 16, [
        [2, -1,  3, -1,  2,  2, -1, -1,  1,  0,  0,  0,  0,  0,  0,  0,],
        [2, -1,  5,  4,  5, -1,  4,  2,  1,  0,  0,  0,  0,  0,  0,  0,],
        [3,  4, -1, -1, -1, -1,  5,  2,  1,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  5, -1,  6, -1, -1, -1,  1,  0,  0,  0,  0,  0,  0,  0,],
        [3,  5, -1,  4,  4, -1, -1,  4,  1,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  4, -1, -1,  3,  4, -1,  4,  1,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  4,  4, -1,  3,  4, -1, -1,  1,  0,  0,  0,  0,  0,  0,  0,],
        [2, -1,  2,  1,  2, -1, -1,  3,  1,  0,  0,  0,  0,  0,  0,  0,],
        [1, 1, 1, 0, 1, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    ]),

    # # teste 08
    ([
        [-1, -1,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, -1, -1, -1,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  0, -1, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, -1,  0, -1,  0, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0, -1, -1, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ], 10, 16, [
        [-1, -1,  3,  2,  2, -1, -1,  2,  0,  0,  0,  0,  0,  0,  0,  0,],
        [3,  5, -1, -1,  3,  3, -1,  3,  1,  0,  0,  0,  0,  0,  0,  0,],
        [3, -1, -1, -1,  5,  4,  4, -1,  1,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  7, -1, -1, -1, -1,  3,  2,  0,  0,  0,  0,  0,  0,  0,],
        [4, -1,  6, -1,  7, -1,  5, -1,  1,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  3, -1, -1, -1,  4, -1,  2,  1,  0,  0,  0,  0,  0,  0,  0,],
        [1,  2,  3,  6, -1,  4,  2,  2,  1,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  1, -1, -1,  2,  1, -1,  1,  0,  0,  0,  0,  0,  0,  0,],
        [0, 0, 1, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    ]),

    # # teste 09
    ([
        [-1, -1, -1, -1, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0,  0,  0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  0,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, -1, -1,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  0, -1,  0,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0, -1, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ], 10, 16, [
        [-1, -1, -1, -1, -1,  3, -1,  1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  6, -1,  4,  4, -1,  5,  3,  1,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  3,  2,  2,  3, -1, -1, -1,  1,  0,  0,  0,  0,  0,  0,  0,],
        [3,  3,  2, -1,  3,  4,  5,  3,  1,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  4,  2,  2, -1, -1,  2,  1,  0,  0,  0,  0,  0,  0,  0,],
        [5, -1, -1,  2,  2,  3,  5, -1,  2,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  4, -1,  3,  4, -1, -1,  3,  0,  0,  0,  0,  0,  0,  0,],
        [2,  2,  2,  2, -1, -1, -1, -1,  2,  0,  0,  0,  0,  0,  0,  0,],
        [0, 0, 0, 1, 2, 3, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    ]),

    #  teste 10
    ([
        [0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  0, -1,  0, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1, -1, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0, -1,  0, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0, -1,  0, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ], 10, 16, [
        [3, -1, -1,  3,  1,  2,  2,  2,  1,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  6, -1,  4, -1, -1,  1,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1, -1, -1,  5, -1,  4,  2,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  7,  6, -1,  4, -1,  3, -1,  1,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1, -1,  3,  4,  2,  4,  2,  2,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  5,  3, -1,  2, -1,  3, -1,  2,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  2,  2,  3,  4,  2,  4, -1,  3,  0,  0,  0,  0,  0,  0,  0,],
        [1,  1,  1, -1, -1,  1,  2, -1,  2,  0,  0,  0,  0,  0,  0,  0,],
        [0, 0, 1, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    ]),


    # teste matriz 17x17 - 32 bombas
    ([
        [-1, -1,  0, -1, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0,  0,  0, -1, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  0,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0, -1,  0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0, -1, -1,  0, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  0, -1,  0, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  0, -1,  0, -1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
    ], 17, 17, [
        [-1, -1,  2, -1, -1,  4,  4, -1,  2,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  4,  3,  5, -1, -1, -1, -1,  2,  0,  0,  0,  0,  0,  0,  0,  0,],
        [3,  4, -1,  4, -1,  5,  3,  2,  1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  3,  4, -1,  4,  3,  2,  1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [3,  4,  4, -1,  4, -1, -1, -1,  1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [3, -1, -1,  4, -1,  5, -1,  3,  1,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1, -1,  5, -1,  5, -1,  4,  2,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [-1,  4, -1,  3, -1, -1, -1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,],
        [1, 2, 1, 2, 2, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
    ]),

    # teste matriz 18x18 - 36 bombas
    # teste matriz 22x22 - 70 bombas
    # teste matriz 23x23 - 80 bombas


    # para o tabuleiro de nível intermediário - 5 testes no total



    # teste matriz 25x25 - 110 bombas
    # teste matriz 26x26 - 120 bombas

])
def test_calculate_numbers(input_field, rows, cols, expected_field):
    calculate_numbers_function(input_field, rows, cols)
    assert input_field == expected_field
