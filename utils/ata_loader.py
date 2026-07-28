import pandas as pd

def load_students():
    return pd.read_csv("data/students.csv")

def load_modules():
    return pd.read_csv("data/modules.csv")

def load_surveys():
    return pd.read_csv("data/surveys.csv")

def load_complaints():
    return pd.read_csv("data/complaints.csv")

def load_kpis():
    return pd.read_csv("data/strategic_kpis.csv")
