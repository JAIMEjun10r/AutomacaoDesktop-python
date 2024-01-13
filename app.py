import openpyxl
import pyperclip
import pyautogui

tabela = openpyxl.load_workbook('dadosEmpresa.xlsx') 
sheet = tabela['Sheet1']
for linha in sheet.iter_rows(min_row=2):
    nome_empresa = linha[0].value
    pyperclip.copy(nome_empresa)
    pyautogui.click(809,308, duration=0.5)
    pyautogui.hotkey('ctrl', 'v')
    
    #produto
    nome_produto = linha[1].value
    pyperclip.copy(nome_produto)
    pyautogui.click(806,346, duration=0.5)
    pyautogui.hotkey('ctrl', 'v')

    # serial
    serial = linha[2].value
    pyperclip.copy(serial)
    pyautogui.click(805,387, duration=0.5)
    pyautogui.hotkey('ctrl', 'v')

    # quantidade
    quantidade = linha[3].value
    pyperclip.copy(quantidade)
    pyautogui.click(805,424, duration=0.5)
    pyautogui.hotkey('ctrl', 'v')

    # valor
    valor = linha[4].value
    pyperclip.copy(valor)
    pyautogui.click(805,463, duration=0.5)
    pyautogui.hotkey('ctrl', 'v')

    # botão cadastrar
    pyautogui.click(879,571, duration=0.3)

    #botão OK
    pyautogui.click(1049,611, duration=0.5)

