from tkinter import Tk
from Controllers.RootController import RootController


def main():
    root = Tk()
    RootController(root)
    root.mainloop()


if __name__ == "__main__":
    main()
