from tkinter import Tk, Frame
from container import Container

class Menu(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Registros/inventarios")
        self.resizable(False, False)
        self.configure(bg="#dddddd")
        self.geometry("500x350")

        self.container = Frame(self, bg="#dddddd")
        self.container.pack(fill="both", expand=True)

        self.frames = {
            Container: None
        }

        self.load_frames()
        self.show_frames(Container)
    
    def load_frames(self):
        for FrameClass in self.frames.keys():
            frame = FrameClass(self.container, self)
            self.frames[FrameClass] = frame

    def show_frames(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

def main():
    app = Menu()
    app.mainloop()

if __name__ == "__main__":
    main()