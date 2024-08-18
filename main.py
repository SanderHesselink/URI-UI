from img_to_uri import image_to_uri
import pyperclip as pc
import tkinter as tk

def Main():
    root = tk.Tk()
    root.title("Image to URI converter")
    root.geometry('600x600')

    # REFERENCE CODE
    # label = tk.Label(root, text="hello")
    # label.grid()
    # entry = tk.Entry(root, width=10)
    # entry.grid()
    #
    # def click():
    #     value = entry.get()
    #     label.configure(text=value)
    #
    # button = tk.Button(root, text="Click", command=click)
    # button.grid(column=1, row=0)

    tk.Label(root, text="Enter filepath:").grid(row=0)
    fileinput = tk.Entry(root, width=100)
    fileinput.grid(row=1)

    output = tk.Label(root, text="")
    output.grid(row=3)

    def convert():
        path = fileinput.get()
        if path:
            output.configure(text=path)
        else:
            output.configure(text="No input!")

    convertbutton = tk.Button(root, text="Convert", command=convert)
    convertbutton.grid(row=2)




    root.mainloop()

if __name__ == "__main__":
    Main()