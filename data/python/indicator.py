import appindicator
import pynotify
import pygtk
pygtk.require("2.0")
import gtk
import time

a = appindicator.Indicator('notify_example', 'info-indicator', appindicator.CATEGORY_APPLICATION_STATUS)
a.set_status(appindicator.STATUS_ACTIVE)
def quit(item):
    gtk.main_quit()
m = gtk.Menu()
ci = gtk.MenuItem('Extract Archive...')
def check(item):
    class Error(Exception):
        pass
    pynotify.init('proc')
    return pynotify.Notification('<b>Archive extract error</b>',
         str(Error('Failed to extract archive')), 'error-icon').show()

ci.connect('activate', check)
qi = gtk.MenuItem('Quit')
qi.connect('activate', quit)
m.append(ci)
m.append(qi)
a.set_menu(m)
ci.show()
qi.show()
gtk.main()
