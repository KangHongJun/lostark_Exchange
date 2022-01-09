import sqlite3
import pandas as pd

#db데이터 읽어오기
def Reforging_Data():
    conn = sqlite3.connect("Reinforce.db")
    Reforging = pd.read_sql("SELECT * FROM Reforging",conn,index_col=None)
    Reforging_List = Reforging.values.tolist()
    return Reforging_List

def Reforging_Add_Data():
    conn = sqlite3.connect("Reinforce.db")
    Reforging_Add = pd.read_sql("SELECT * FROM Reforging_Add",conn,index_col=None)
    Reforging_Add_List = Reforging_Add.values.tolist()
    return Reforging_Add_List

def Potion_Data():
    conn = sqlite3.connect("Reinforce.db")
    Reforging_Add = pd.read_sql("SELECT * FROM Reforging_Add",conn,index_col=None)
    Reforging_Add_List = Reforging_Add.values.tolist()
    return Reforging_Add_List

def Buff_Data():
    conn = sqlite3.connect("Reinforce.db")
    Reforging_Add = pd.read_sql("SELECT * FROM Reforging_Add",conn,index_col=None)
    Reforging_Add_List = Reforging_Add.values.tolist()
    return Reforging_Add_List

def Attack_Data():
    conn = sqlite3.connect("Reinforce.db")
    Reforging_Add = pd.read_sql("SELECT * FROM Reforging_Add",conn,index_col=None)
    Reforging_Add_List = Reforging_Add.values.tolist()
    return Reforging_Add_List

def Assistance_Data():
    conn = sqlite3.connect("Reinforce.db")
    Reforging_Add = pd.read_sql("SELECT * FROM Reforging_Add",conn,index_col=None)
    Reforging_Add_List = Reforging_Add.values.tolist()
    return Reforging_Add_List
