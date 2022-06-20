from os import stat
import tkinter as tk
from tkinter.font import BOLD
import nltk  #natrual language toolkit
from textblob import TextBlob # process textual data like pharse extraction, sentment analysis, translate
from newspaper import Article #webScraping liberary to scrape information from any article

def summarize():
    url = utext.get('1.0','end').strip()
    article = Article(url)
    article.download()
    article.parse() #parse text into tokens and words
    article.nlp() #natrual language proccessiong
    
    #global vars
    global tit
    global summ

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentment.config(state='normal')

    tit = article.title
    title.delete('1.0','end')
    title.insert('1.0',tit)
 
    author.delete('1.0','end')
    if (article.authors):
        author.insert('1.0',article.authors)
    else:
        author.insert('1.0',"Not Detected")
          
    publication.delete('1.0','end')
    if (article.publish_date):
        publication.insert('1.0',article.publish_date)
    else:
        publication.insert('1.0',"Not Detected")
          
    summ = article.summary
    summary.delete('1.0','end')
    summary.insert('1.0',summ)

    analysis = TextBlob(article.text)
    sentment.delete('1.0','end')
    sentment.insert('1.0',f'Polarity: {analysis.polarity}, Sentiment: {"article is positive" if analysis.polarity > 0 else "article is negative" if analysis.polarity < 0 else "neutal"}')
 
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentment.config(state='disabled')
    
def save():
    file = open('article summary.txt', 'w')
    file.write(tit)
    file.write(summ)
    file.close()
    tk.messagebox.showinfo(title=None,message='Article summary was saved')  

            
root = tk.Tk()
root.title("Summary Any Article")
root.geometry('950x550')
root.config(bg='#262526')

tlabel = tk.Label(root, text="Title")
tlabel.config(fg='#f4f4f4', bg='#262526',font=("Helvetica", 13), padx=10,pady=5)
tlabel.pack()

title = tk.Text(root, height=1, width=110)
title.config(state='disabled', bg='#1e1e1e', fg='#f4f4f4')
title.pack()

alabel = tk.Label(root, text="Author")
alabel.config(fg='#f4f4f4', bg='#262526',font=("Helvetica", 13), padx=10,pady=5)
alabel.pack()

author = tk.Text(root, height=1, width=110)
author.config(state='disabled', bg='#1e1e1e', fg='#f4f4f4')
author.pack()

plabel = tk.Label(root, text="Published at")
plabel.config(fg='#f4f4f4', bg='#262526',font=("Helvetica", 13), padx=10,pady=5)
plabel.pack()

publication = tk.Text(root, height=1, width=110)
publication.config(state='disabled', bg='#1e1e1e', fg='#f4f4f4')
publication.pack()


slabel = tk.Label(root, text="Summary")
slabel.config(fg='#f4f4f4', bg='#262526',font=("Helvetica", 13), padx=10,pady=5)
slabel.pack()

summary = tk.Text(root, height=10, width=110)
summary.config(state='disabled', bg='#1e1e1e', fg='#f4f4f4')
summary.pack()

selabel = tk.Label(root, text="Sentment Analysis")
selabel.config(fg='#f4f4f4', bg='#262526',font=("Helvetica", 13), padx=10,pady=5)
selabel.pack()

sentment = tk.Text(root, height=1, width=110)
sentment.config(state='disabled', bg='#1e1e1e', fg='#f4f4f4')
sentment.pack()

ulabel = tk.Label(root, text="ENTER THE URL :")
ulabel.config(fg='#f4f4f4', bg='#262526',font=("Helvetica", 13), padx=10,pady=5)
ulabel.pack()

utext = tk.Text(root, height=1, width=110)
utext.config(bg='#1e1e1e', fg='#f4f4f4')
utext.pack()

btn = tk.Button(root, text='SUMARIZE', width=55,height=2 ,bg="#1b1b1b",command=summarize)
btn.config(fg='#f4f4f4',font=("Helvetica", 15, BOLD), borderwidth=2)
btn.pack(padx=35,pady=15,side='left')

btn2 = tk.Button(root, text='SAVE SUMMARY', width=15,height=2 ,bg="#1b1b1b",command=save)
btn2.config(fg='#f4f4f4',font=("Helvetica", 12, BOLD), borderwidth=2)
btn2.pack(padx=35,pady=15,side='right')


root.mainloop()