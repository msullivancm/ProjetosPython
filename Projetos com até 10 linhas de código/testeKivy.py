import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical',
                           padding=[40, 20, 40, 20])

        layout.add_widget(Label(text='TESTE'))

        btn1 = Button(text='clique aqui')
        btn1.bind(on_press=self.tt())
        layout.add_widget(btn1)

        return layout

    def tt(self):
        t = "teste"
        print(t)
        return t

if __name__ in ('__android__', '__main__'):
    MyApp().run()