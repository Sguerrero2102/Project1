from gui import *


def main():
    window = Tk()
    window.title('Lab 11')
    window.geometry('400x230')
    window.resizable(False, False)

    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()
