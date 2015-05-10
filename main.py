import kivy
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.app import App

Builder.load_string('''
<CounterMixUpScreen>:
    orientation: 'all'
    cols: 1
    Label:
        text: 'You are at %d' % root.counter
    Button:
        text: 'Press me to increment by 1!'
        on_press: root.increment()
    Button:
        text: "Press me to decrement by 1!"
        on_press: root.decrement()
    Button:
        text: "Press me to increment by 10!"
        on_press: root.increment(10)
    Button:
        text: "Press me to decrement by 10!"
        on_press: root.decrement(10)
    Button:
        text: "Press me to increment by 100!"
        on_press: root.increment(100)
    Button:
        text: "Press me to decrement by 100!"
        on_press: root.decrement(100)
    Button:
        text: "Press me to increment by 1000!"
        on_press: root.increment(1000)
    Button:
        text: "Press me to decrement by 1000!"
        on_press: root.decrement(1000)
    Button:
        text: "Press me to increment by 10000!"
        on_press: root.increment(10000)
    Button:
        text: "Press me to decrement by 10000!"
        on_press: root.decrement(10000)
    Button:
        text: "Press me to increment by 100000!"
        on_press: root.increment(100000)
    Button:
        text: "Press me to decrement by 100000!"
        on_press: root.decrement(100000)
    Button:
        text: "Press me to reset the counter!"
        on_press: root.reset()
''')

class CounterMixUpScreen(GridLayout):
    counter = NumericProperty(0)
    def increment(self, num=1):
        self.counter += num
    def decrement(self, num=1):
        self.counter -= num
    def reset(self):
        self.counter = 0
    

class CounterMixUpApp(App):
    def build(self):
        return CounterMixUpScreen()

if __name__ == '__main__':
    CounterMixUpApp().run()
