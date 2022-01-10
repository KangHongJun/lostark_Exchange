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
    conn = sqlite3.connect("Battle_Item.db")
    Potion = pd.read_sql("SELECT * FROM Potion",conn,index_col=None)
    Potion_List = Potion.values.tolist()
    return Potion_List

def Buff_Data():
    conn = sqlite3.connect("Battle_Item.db")
    Buff = pd.read_sql("SELECT * FROM Buff",conn,index_col=None)
    Buff_List = Buff.values.tolist()
    return Buff_List

def Attack_Data():
    conn = sqlite3.connect("Battle_Item.db")
    Attack = pd.read_sql("SELECT * FROM Attack",conn,index_col=None)
    Attack_List = Attack.values.tolist()
    return Attack_List

def Assistance_Data():
    conn = sqlite3.connect("Battle_Item.db")
    Assistance = pd.read_sql("SELECT * FROM Assistance",conn,index_col=None)
    Assistance_List = Assistance.values.tolist()
    return Assistance_List

def Plant_Data():
    conn = sqlite3.connect("Life.db")
    Plant = pd.read_sql("SELECT * FROM Plant",conn,index_col=None)
    Plant_List = Plant.values.tolist()
    return Plant_List

def Logging_Data():
    conn = sqlite3.connect("Life.db")
    Logging = pd.read_sql("SELECT * FROM Logging",conn,index_col=None)
    Logging_List = Logging.values.tolist()
    return Logging_List

def Mining_Data():
    conn = sqlite3.connect("Life.db")
    Mining = pd.read_sql("SELECT * FROM Mining",conn,index_col=None)
    Mining_List = Mining.values.tolist()
    return Mining_List

def Hunting_Data():
    conn = sqlite3.connect("Life.db")
    Hunting = pd.read_sql("SELECT * FROM Hunting",conn,index_col=None)
    Hunting_List = Hunting.values.tolist()
    return Hunting_List

def Fishing_Data():
    conn = sqlite3.connect("Life.db")
    Fishing = pd.read_sql("SELECT * FROM Fishing",conn,index_col=None)
    Fishing_List = Fishing.values.tolist()
    return Fishing_List

def Archaeology_Data():
    conn = sqlite3.connect("Life.db")
    Archaeology = pd.read_sql("SELECT * FROM Archaeology",conn,index_col=None)
    Archaeology_List = Archaeology.values.tolist()
    return Archaeology_List
