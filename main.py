from img_to_uri import image_to_uri
import pyperclip as pc
import tkinter as tk
from tkinter import filedialog

def Main():
    root = tk.Tk()
    root.title("Image to URI converter")
    root.geometry('600x600')

    tk.Label(root, text="Enter filepath:").grid(row=0)
    fileinput = tk.Entry(root, width=50)
    fileinput.grid(row=1)

    def dialogpopup():
        filepath = tk.filedialog.askopenfilename()
        fileinput.delete(0, tk.END)
        fileinput.insert(tk.END, filepath)

    fileexplorer = tk.Button(root, text="select file...", command=dialogpopup)
    fileexplorer.grid(row=1, column=1)

    output = tk.Label(root, text="")
    output.grid(row=3)

    def convert():
        filepath = fileinput.get()
        if filepath:
            filepath = filepath.replace('\\', '/')
            pc.copy(image_to_uri(filepath))
            output.configure(text="Copied to clipboard!")
        else:
            output.configure(text="No input!")

    convertbutton = tk.Button(root, text="Convert", command=convert)
    convertbutton.grid(row=2)




    root.mainloop()

if __name__ == "__main__":
    Main()