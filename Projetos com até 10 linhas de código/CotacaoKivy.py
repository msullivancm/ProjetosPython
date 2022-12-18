# -*- coding: utf-8 -*-

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
import requests

class MeuApp(App):
    vlr = 'BTC'
    def build(self):
        self.layout = BoxLayout(orientation='vertical',
                           padding=[40, 20, 40, 20])

        self.lbl = Label(text='Teste Sullivan!')
        self.layout.add_widget(self.lbl)

        # Add checkbox, widget and labels
        self.layout.add_widget(Label(text='Male'))
        self.layout.active = CheckBox(active=True)
        self.layout.add_widget(self.layout.active)

        self.layout.add_widget(Label(text='Female'))
        self.layout.active = CheckBox(active=True)
        self.layout.add_widget(self.layout.active)

        self.btn = Button(text='Clique aqui!', size=(100, 50))
        self.btn.bind(on_press=self.pegar_cotacao)
        self.layout.add_widget(self.btn)

        return self.layout

    def on_checkbox_active(self, value):
        if value:
            print('The checkbox', self.checkbox, 'is active')
        else:
            print('The checkbox', self.checkbox, 'is inactive')

    def pegar_cotacao(self, event):
        moeda = self.vlr.upper()
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        req = requests.get(link).json()
        valor = req[f'{moeda}BRL']['bid']
        print(valor)
        self.lbl.text = valor
        self.btn.text = "Mudou"

if __name__ == '__main__':
    MeuApp().run()
