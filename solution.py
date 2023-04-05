import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import t

chat_id = 371784753 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    alpha = 1 - p
    df = n - 1
    t_value = t(df).ppf(1 - alpha / 2)
    x_mean = np.mean(x)
    x_std = np.std(x, ddof=1)
    interval_half_width = t_value * x_std / np.sqrt(n)
    return x_mean - interval_half_width, x_mean + interval_half_width
