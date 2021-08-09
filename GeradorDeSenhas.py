import random
import PySimpleGUI as sg
import os

class PassGen:
  def __init__(self):
    # Declarando o Layout
    sg.theme('Black')
    layout = [
      [sg.Text('Site/Software', sizer=(10, 1)),
       sg.Input(key='site', size=(20, 1))],
      [sg.Text('E-mail/Usuário', sizer=(10, 1)),
       sg.Input(key='usuario', sizer=(20, 1))],
      [sg.Text('Quantidade de caracteres'), sg.combo(values=list(
        range(30)), key='total_chars', default_value=1, size=(3, 1))],
      [sg.Output(size=(32, 5))],
      [sg.Button('Gerar Senha')]
    ]

  def Iniciar(self):
    pass

  def salvar_senha(self):
    pass

gen = PassGen()
gen.Iniciar()