#!/usr/bin/env python

import urwid

class AutomataMenu(urwid.WidgetWrap):

    def __init__(self):

        self._w = urwid.LineBox(urwid.Text("Delta Menu"))
            
        super().__init__(self._w)
        self._w = self._w
        self._w.set_title("Automata Menu")
        
        self._w._sizing = "flow"
        self._sizing = "flow"
    
    def keypress(self, size, key):
        if key == "enter":
            self.tabs._set_active_by_tab(self)
        #elif key == "tab":
        #    self.tabs._set_active_next()
        #elif key == "shift tab":
        #    self.tabs._set_active_prev()
        else:
            return key

    def selectable(self):
        return True

class TransitionPanel(urwid.WidgetWrap):

    def __init__(self, w=None):
        
        self.show_text = urwid.Text("False")


        if w is None:
            w = urwid.LineBox(
                urwid.Pile([
                    urwid.Text("A"),
                    urwid.Text("B"),
                    self.show_text
                ]))

        super().__init__(w)
        self._w = w
        self._w.set_title("Transition Panel")
        self._w._sizing = "flow"
        self._w._selectable = True
        self._sizing = "flow"


    def keypress(self, size, key):
        if key in ["up", "down", "left", "right"]:
            return key
        self.show_text.set_text(key)
        self.input_area.edit_box.edit_text += key

    def selectable(self):
        return True
    
    def link_input_area(self, input_area):
        self.input_area = input_area

class InputArea(urwid.WidgetWrap):

    def __init__(self):

        self.edit_box = urwid.Edit("Enter: ")
        self._w = urwid.LineBox(   
            urwid.ListBox(
                urwid.SimpleFocusListWalker([
                    urwid.Text("Box3"),
                    urwid.Text("Box4"),
                    self.edit_box
            ])))

        super().__init__(self._w)
        self._w.set_title("Input Area")
        self._w._selectable = True
        self._sizing = "flow"
    
    def keypress(self, size, key):
        if key in ["up", "down", "left", "right"]:
            return key
        self.edit_box.edit_text = key

    def selectable(self):
        return True


class MainWindowFrame(urwid.WidgetWrap):

    def __init__(self):

        self.automata_menu = AutomataMenu()
        self.transition_panel = TransitionPanel()
        self.input_area = InputArea()

        self._w = urwid.Pile([
            
            urwid.ListBox(
                
                urwid.SimpleFocusListWalker([
                    self.automata_menu,
                    self.transition_panel
                ])
            ),
            
            self.input_area
        ])


        self.transition_panel.link_input_area(self.input_area)

        
        super().__init__(self._w)


def main():

    urwid.set_encoding("utf8")

    mainframe = MainWindowFrame()

    def quit(*args, **kwargs):
        raise urwid.ExitMainLoop()
    
    def handle_key(key):
        if key in ("q", "Q"):
            quit()

    loop = urwid.MainLoop(
        mainframe,
        handle_mouse=False,
        unhandled_input=handle_key
    )

    loop.run()


if __name__ == "__main__":
    main()
