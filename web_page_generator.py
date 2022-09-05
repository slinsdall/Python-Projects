import tkinter as tk
from tkinter import *
import webbrowser



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        #Creates button for HTML page
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=1, padx=(10,10) , pady=(10,10))

        #Creates label for user input
        UserInput_label = tk.Label(root, text = "Enter custom text or select Default HTML Page")
        UserInput_label.grid(row=0, column=0, padx=(10,10), pady=(20,0))

        #Creates user input section
        self.User_input = Entry(width=75)
        self.User_input.grid(row=1, column=0, padx=(20,10), pady=(30,0))

        
        

        #Creates button for custom text submit
        self.btn = Button(self.master, text="Submit custom text", width=30, height=2, command=self.customText)
        self.btn.grid(row=2, column=2, padx=(10,10) , pady=(10,10))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customText(self):
        htmlText = self.User_input.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
