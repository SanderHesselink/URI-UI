from img_to_uri import image_to_uri
import pyperclip as pc
import tkinter as tk
import tkinter.scrolledtext

def Main():
    root = tk.Tk()
    root.title("Image to URI converter")
    root.geometry('600x600')

    tk.Label(root, text="Enter filepath:").grid(row=0)
    fileinput = tk.Entry(root, width=100)
    fileinput.grid(row=1)

    output = tk.Label(root, text="")
    output.grid(row=3)

    def convert():
        path = fileinput.get()
        if path:
            path = path.replace('\\', '/')
            pc.copy(image_to_uri(path))
            output.configure(text="Copied to clipboard!")
        else:
            output.configure(text="No input!")

    convertbutton = tk.Button(root, text="Convert", command=convert)
    convertbutton.grid(row=2)




    root.mainloop()

if __name__ == "__main__":
    Main()