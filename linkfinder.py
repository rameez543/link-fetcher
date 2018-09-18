from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter import messagebox
import pandas as pd
window = Tk()
 
window.title("link extractor")
 
window.geometry('350x200')
 
lbl = Label(window, text="url")
lbl2= Label(window,text='')
 
lbl.grid(column=0, row=0) 
txt = Entry(window,width=20)

txt.grid(column=1, row=0)
txt.focus()
url=txt.get()


def func(url):
    ur=txt.get()
    
    r  = requests.get(url='http://'+ur)

    data = r.text

    soup = BeautifulSoup(data)
    links=[]
    for link in soup.find_all('a'):

        links.append((link.get('href')))
    my_df = pd.DataFrame(links)
    return(my_df)

def clicked():
	my_df=func(url)
	ur=txt.get()

	my_df.to_csv(txt.get()+'.csv', index=False, header=False)
	messagebox.showinfo("Succes","links extracted from http://www."+ur +" and saved as "+ur+".csv")
btn = Button(window, text="Click Me", command=clicked)
 
btn.grid(column=2, row=0)

window.mainloop()


    
 




