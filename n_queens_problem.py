# n_queens_problem.py

#This file contains functions related to visualizing the N Queens problem solution.
#Bu dosya, N Vezir problemi çözümünü görselleştirmekle ilgili fonksiyonları içerir.

import cv2
import numpy as np

def visualize_board(solution):
    #Visualize the N Queens problem solution using OpenCV
    #OpenCV kullanarak N Vezir problemi çözümünü görselleştirir.
    board_size = len(solution)
    board = np.zeros((board_size, board_size, 3), dtype=np.uint8)

    for i in range(board_size):
        board[i, solution[i]] = [0, 255, 0] 
        #Mark queen positions in green.
        # Vezir pozisyonları yeşil renkte işaretlensin

    # Vezir pozisyonlarını yeşil renkte işaretle
    for i in range(board_size):
        board[i, solution[i]] = [0, 255, 0]  # Vezir pozisyonları yeşil renkte işaretlensin

        # Siyah kareleri beyaz çizgilerle ayır
    for i in range(0, board_size, 2):
        board[i, ::2] = [255, 255, 255]  # Beyaz çizgiler
    for i in range(1, board_size, 2):
        board[i, 1::2] = [255, 255, 255]  # Beyaz çizgiler


    # Specify a custom window size
    cv2.namedWindow("N Queens Problem Solution", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("N Queens Problem Solution", 400, 400)  # You can adjust these dimensions

    cv2.imshow("N Queens Problem Solution", board)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
