from Tkinter import *
import threading
class CustomText(Text):
    '''A text widget with a new method, highlight_pattern()

    example:

    text = CustomText()
    text.tag_configure("red", foreground="#ff0000")
    text.highlight_pattern("this should be red", "red")

    The highlight_pattern method is a simplified python
    version of the tcl code at http://wiki.tcl.3246
    '''
    def __init__(self, *args, **kwargs):
        Text.__init__(self, *args, **kwargs)

    def highlight_pattern(self, pattern, tag, start="1.0", end="end",
                          regexp=True):
        '''Apply the given tag to all text that matches the given pattern

        If 'regexp' is set to True, pattern will be treated as a regular
        expression.
        '''

        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        count = IntVar()
        while True:
            index = self.search(pattern, "matchEnd","searchLimit",
                                count=count, regexp=regexp)
            if index == "": break
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")

root = Tk()
root.title("ColorText")
root.geometry("500x500")
text = CustomText(background="black", foreground="white", insertbackground="white")
text.pack(fill=BOTH, expand=1)
text.tag_configure("red", foreground="gray")
text.tag_configure("green", foreground="green")
text.tag_configure("purple", foreground="#9400D3")
text.tag_configure("yellow", foreground="#EEEE00")
text.tag_configure("black", foreground="#000000")
text.tag_configure("white", foreground="white")
# text.tag_configure("invert", background="black")
stmt = [
"print",
"in",
"for",
"while",
"with",
"import",
"from",
"as",
"is"
]
buin = dict(__builtins__.__dict__).keys()
def puts():
    while 1:
        # text.highlight_pattern("^.*$", "black")
        #text.mark_set("invS", 0.0)
        #text.mark_set("invE", -1.0)
        #text.tag_add("invert", "invS", "invE")
        text.highlight_pattern("'''.*'''", "green")
        text.highlight_pattern('""".*"""', "green")
        text.highlight_pattern("'.*.'", "green")
        text.highlight_pattern("\".*.\"", "green")
        for st in stmt:
            text.highlight_pattern(st, "yellow", regexp=False)
        for b in buin:
            text.highlight_pattern(b, "purple", regexp=False)
        text.highlight_pattern("#.*", "red")
        for word in text.get(0.0, END).split(" "):
            if word not in stmt and (not word.startswith("\"") and not word.endswith("\"")) or (not word.startswith("'") and not word.endswith("'")) and word not in buin:
                text.highlight_pattern(word, "white")
##            elif word not in buin:
##                text.highlight_pattern(word, "white")
##            elif (not word.startswith("\"") and not word.endswith("\"")) or (not word.startswith("'") and not word.endswith("'")):
##                text.highlight_pattern(word, "white")

t1 = threading.Thread(target=puts)
t1.daemon = True
t1.start()
root.mainloop()
t1.join(0)
