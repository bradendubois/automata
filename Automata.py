#!/usr/bin/env python

import urwid

def main():

    urwid.set_encoding("utf8")

    delta_menu = urwid.LineBox(
        urwid.Text("Delta Menu")
    )

    transition_menu = urwid.LineBox(
        
        urwid.Pile([
            urwid.Text("A"),
            urwid.Text("B")
        ])
    )


    main_input_area = urwid.LineBox(
        
        urwid.ListBox(
            urwid.SimpleFocusListWalker([
                urwid.Text("Box3"),
                urwid.Text("Box4")
        ]))
    )

    mainframe = urwid.Pile([


        urwid.ListBox(

            urwid.SimpleFocusListWalker([

                delta_menu,

                transition_menu

            ])
        ),

        main_input_area
    ])

    def quit(*args, **kwargs):
        raise urwid.ExitMainLoop()
    
    def handle_key(key):
        if key in ("q", "Q"):
            quit()

    delta_menu.set_title("Delta Transitions")
    transition_menu.set_title("Transition Panel")
    main_input_area.set_title("Input Area")

    loop = urwid.MainLoop(
        mainframe,
        handle_mouse=False,
        unhandled_input=handle_key
    )

    loop.run()


if __name__ == "__main__":
    main()