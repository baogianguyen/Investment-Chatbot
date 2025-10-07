import IBM_Stock_API
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import numpy as np
import torch.optim as optim
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = IBM_Stock_API.get_stock_data()

train_df, test_df = train_test_split(df,test_size=0.2, random_state=42)

print(train_df.head())