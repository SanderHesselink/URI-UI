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

    output = tk.scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=50)
    output.grid(row=3)

    def convert():
        path = fileinput.get()
        if path:
            path = path.replace('\\', '/')
            output.insert(tk.END, image_to_uri(path))
        else:
            output.insert(tk.END, "No input!")

    convertbutton = tk.Button(root, text="Convert", command=convert)
    convertbutton.grid(row=2)




    root.mainloop()

if __name__ == "__main__":
    Main()