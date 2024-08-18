import base64
import pyperclip as pc
import tkinter as tk
from tkinter import filedialog

def image_to_uri(path):
    with open(path, 'rb') as f:
        img = f.read()
    return base64.b64encode(img).decode("utf-8")

def Main():
    root = tk.Tk()
    root.title("Image to URI converter")
    root.geometry('600x200')

    tk.Label(root, text="Enter filepath:").grid(row=0)
    fileinput = tk.Entry(root, width=50)
    fileinput.grid(row=1)

    def dialogpopup():
        filepath = tk.filedialog.askopenfilename()
        if filepath:
            fileinput.delete(0, tk.END)
            fileinput.insert(tk.END, filepath)

    fileexplorer = tk.Button(root, text="select file...", command=dialogpopup)
    fileexplorer.grid(row=1, column=1)

    output = tk.Label(root, text="")
    output.grid(row=4)

    # Tkinter checkbuttons seem rather convoluted... is this really the simplest way?
    extvar = tk.IntVar(value=1)
    extcheck = tk.Checkbutton(root, text="Add prefix", variable=extvar, onvalue=1, offvalue=0)
    extcheck.grid(row=2)

    def convert():
        filepath = fileinput.get()
        if filepath:
            filepath = filepath.replace('\\', '/')
            # Very elegant exception handling: just throw it all into one big try/except. But hey, it works
            try:
                result = image_to_uri(filepath)
                if extvar.get() == 1:
                    ext = filepath.split('.')[-1]
                    result = "data:image/" + ext + ";base64," + result
                pc.copy(result)
                output.configure(text="Copied to clipboard!")
            except:
                output.configure(text="Bad input!")
        else:
            output.configure(text="No input!")


    convertbutton = tk.Button(root, text="Convert", command=convert)
    convertbutton.grid(row=3)


    root.mainloop()

if __name__ == "__main__":
    Main()