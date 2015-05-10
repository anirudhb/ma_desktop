from main import Timer
from gi.repository import Gtk as gtk

def lock():
    window = gtk.Window()
    window.connect("destroy", gtk.main_quit)
    window.set_keep_above(True)
    window.maximize()
    window.title("Gtk-Maximized-Always-On-Top-Restrictions")
    window.show_all()
    gtk.main()

t = Timer(60*30, 60*5)
t.start(lock)

