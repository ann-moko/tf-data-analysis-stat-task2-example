import pandas as pd 
import numpy as np 
from scipy.stats import t, expon
from scipy.stats import exponnorm

chat_id = 371784753 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    a = 2 * x / (71 ** 2)
    alpha = 1 - p
    loc = a.mean()
    scale = np.sqrt(np.var(a)) / np.sqrt(len(a))
    return loc - scale * norm.ppf(1 - alpha / 2), loc - scale * norm.ppf(alpha / 2)
