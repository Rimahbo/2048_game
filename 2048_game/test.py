import pygame
import pytest
from main import draw_over, take_turn, new_pieces, draw_board, draw_pieces, draw_current_state
pygame.init()


def test_draw_over():
    width = 400
    height = 500
    screen = pygame.Surface((width, height))
    draw_over()
    rect_color = screen.get_at((50, 50))
    assert rect_color == (0, 0, 0, 255), "La couleur du rectangle est incorrecte."
    text1_color = screen.get_at((130, 65))
    assert text1_color == (255, 255, 255, 255), "La couleur du texte 'Game Over!' est incorrecte."
    text2_color = screen.get_at((70, 105))
    assert text2_color == (255, 255, 255, 255), "La couleur du texte 'Press Enter to Restart' est incorrecte."


def test_take_turn():

    board = [
        [2, 0, 2, 0],
        [0, 4, 0, 4],
        [2, 0, 2, 0],
        [0, 4, 0, 4]
    ]
    # Test pour la direction UP
    expected_board_up = [
        [4, 8, 4, 8],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert take_turn('UP', board) == expected_board_up, "Le tableau de jeu après la direction UP n'est pas correct."

    # Test pour la direction DOWN
    expected_board_down = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [4, 8, 4, 8]
    ]
    assert take_turn('DOWN', board) == expected_board_down, \
        "Le tableau de jeu après la direction DOWN n'est pas correct."

    # Test pour la direction LEFT
    expected_board_left = [
        [4, 0, 0, 0],
        [8, 0, 0, 0],
        [4, 0, 0, 0],
        [8, 0, 0, 0]
    ]
    assert take_turn('LEFT', board) == expected_board_left, \
        "Le tableau de jeu après la direction LEFT n'est pas correct."

    # Test pour la direction RIGHT
    expected_board_right = [
        [0, 0, 0, 4],
        [0, 0, 0, 8],
        [0, 0, 0, 4],
        [0, 0, 0, 8]
    ]
    assert take_turn('RIGHT', board) == expected_board_right, \
        "Le tableau de jeu après la direction RIGHT n'est pas correct."


def test_new_pieces():

    board_with_space = [
        [2, 4, 8, 0],
        [4, 8, 2, 4],
        [8, 2, 4, 8],
        [2, 4, 8, 2]
    ]
    new_board, full = new_pieces(board_with_space)
    assert any(0 in row for row in new_board), "Aucun nouvel élément n'a été ajouté au tableau de jeu."
    assert not full, "Le tableau de jeu est plein, ce qui ne devrait pas être le cas."
    for row in new_board:
        for cell in row:
            assert cell == 2 or cell == 4, "Les nouveaux éléments ajoutés ne sont pas 2 ou 4."


def test_draw_board():
    screen = pygame.Surface((400, 500))
    draw_board()
    assert screen.get_at((0, 0)) == (187, 173, 160, 255)
    assert screen.get_at((10, 410)) == (0, 0, 0, 255)
    assert screen.get_at((10, 450)) == (0, 0, 0, 255)


def test_draw_pieces():
    screen = pygame.Surface((400, 500))
    board = [[2, 0, 4, 0],
             [0, 8, 16, 0],
             [32, 64, 128, 256],
             [512, 1024, 2048, 4096]]
    draw_pieces(board)

    assert screen.get_at((20, 20)) == (238, 228, 218, 255), "Couleur de la case incorrecte"
    assert screen.get_at((157, 157)) == (249, 246, 242, 255), "Couleur du texte incorrecte"


def test_draw_current_state():
    pygame.init()
    screen = pygame.Surface((400, 500))
    show_image = True
    draw_current_state()

    if show_image:
        assert screen.get_at((0, 0)) == (255, 255, 255, 255)
    else:

        assert screen.get_at((0, 0)) == (187, 173, 160, 255)
        assert screen.get_at((10, 410)) == (0, 0, 0, 255)
        assert screen.get_at((10, 450)) == (0, 0, 0, 255)


if __name__ == "__main__":
    pytest.main()
