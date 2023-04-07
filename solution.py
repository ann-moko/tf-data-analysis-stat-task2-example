import pandas as pd 
import numpy as np 

chat_id = 371784753 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    min = (-x).min()
    z_2 = -np.log(1-p)/x.size    
    return 2*(-min-1/2)/(71*71), 2*(z_2-min-1/2)/(71*71)
