import pyautogui
import time
import pandas as pd
import openpyxl

pyautogui.press("win")
time.sleep(0.7)
pyautogui.write("C")
pyautogui.write("h")
pyautogui.write("r")
pyautogui.write("o")
pyautogui.write("m")
pyautogui.write("e")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(4)
pyautogui.click(x=800, y=373)
pyautogui.write("email.teste@gmail.com")
time.sleep(0.5)
pyautogui.press("tab")
pyautogui.write("4070senha2024!")
pyautogui.press("enter")
time.sleep(1.5)



tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    #para o codigo do produto
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.click(x=686, y=256)
    pyautogui.write(codigo)
    time.sleep(0.7)
    pyautogui.press("tab")
    #marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    time.sleep(0.7)
    pyautogui.press("tab")
    #tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    time.sleep(0.7)
    pyautogui.press("tab")
    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    time.sleep(0.7)
    pyautogui.press("tab")
    #preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    time.sleep(0.7)
    pyautogui.press("tab")
    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    time.sleep(0.7)
    pyautogui.press("tab")
    #obs
    pyautogui.write(str(tabela.loc[linha, "obs"]))
    time.sleep(0.7)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(10000)
    time.sleep(1.5)