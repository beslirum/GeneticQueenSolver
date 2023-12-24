# visualization.py

#This file contains functions related to visualizing the N Queens problem solution with color.
#Bu dosya, renki bir şekilde N Vexir problemi çözümünü görselleştirmekle ilgili fonksiyonları içerir.

import cv2
import numpy as np

def create_colored_board(solution):
    #Create a colored board visualization using OpenCV.
    #OpenCV kullanarak renkli bir tahta görselleşştirmesi oluşturur.

    board_size = len(solution)
    board = np.zeros((board_size, board_size, 3), dtype=np.uint8)

    for i in range(board_size):
        board[i, solution[i]] = [0, 255, 0] 
        # Vezir pozisyonları yeşil renkte işaretlensin
        # Mark queen positions in green.
    
    # Specify a custom window size
    cv2.namedWindow("Colored N Queens Board", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Colored N Queens Board", 400, 400)  # You can adjust these dimensions

    cv2.imshow("Colored N Queens Board", board)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
