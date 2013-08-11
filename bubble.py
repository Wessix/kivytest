'''
Bubble
======

Test of the widget Bubble.
'''
#import main
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.bubble import Bubble

Builder.load_string('''
<cut_copy_paste>
    
    size_hint: (0.6, 0.2)
    #size: (260, 120)
    #pos_hint: {'center_x': .5, 'y': .6}
    #pos_hint: {'center_x': 0, 'y': 0}
    pos: 300,300
    BubbleButton:
        text: 'Storno'
    BubbleButton:
        text: 'Anzahl'
    BubbleButton:
        text: 'Favorit'
    BubbleButton:
        text: 'X'
''')


class cut_copy_paste(Bubble):
    pass


class BubbleShowcase(FloatLayout):

    def __init__(self, **kwargs):
        super(BubbleShowcase, self).__init__(**kwargs)
        self.but_bubble = Button(text='Press to show bubble')
        self.but_bubble.bind(on_release=self.show_bubble)
        self.add_widget(self.but_bubble)

    def show_bubble(self, widget_position, *l):
        print widget_position
        global widget_position_global
        widget_position_global = widget_position
        
        
        print 'hier ist eine Blase'
        if not hasattr(self, 'bubb'):
            self.bubb = bubb = cut_copy_paste()
            #self.add_widget(bubb)
            add_widget(bubb)
            
            self.bubb.pos = widget_position
           
            
        else:
            values = ('left_top', 'left_mid', 'left_bottom', 'top_left',
                'top_mid', 'top_right', 'right_top', 'right_mid',
                'right_bottom', 'bottom_left', 'bottom_mid', 'bottom_right')
            index = values.index(self.bubb.arrow_pos)
            self.bubb.arrow_pos = 'bottom_mid'#values[(index + 1) % len(values)]
            #self.bubb.background_color = (1, 0, 0, 1) 
            #self.bubb.border = [0.5, 0.5, 0.5, 0.5]
            #self.bubb.orientation = 'vertical'
        
class TestBubbleApp(App):

    def build(self):
        return BubbleShowcase()

if __name__ == '__main__':
    TestBubbleApp().run()
