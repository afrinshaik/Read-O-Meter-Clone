#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 12:53:11 2017

@author: afrin
"""

import tkinter as tk
import read_o_meter as rom
import random_quote as rq

def main():
    window = tk.Tk()
    window.title("Read-O-Meter")
    window.geometry("860x800+0+0")
    
    header = tk.Frame(window, width=800, bg="white",padx=20, pady=20)
    header.pack(side=tk.TOP, fill="both", expand=False)
    
    body = tk.Frame(window, width=800, height=400, bg="white",padx=40, pady=20)
    body.pack(side=tk.BOTTOM, fill="both", expand=True)
    
    heading = tk.Label(header, text="READ-O-METER", font=('arial',50,'bold'), justify=tk.LEFT, fg="steel blue")
    heading.grid(row=0, column=0)
    
    small_heading = tk.Label(header, text="so many posts, so little time", font=('arial',15,''), justify=tk.RIGHT, bg="white", fg="black")
    small_heading.grid(row=1, column=0)
    
    info_1_var = tk.StringVar()
    info_1_var.set("Please enter/paste your text to estimate the reading time.")
    info_1 = tk.Label(header, textvariable = info_1_var, font=('arial', 15, ''), bg="white", 
                      fg="black", padx=10, pady=10, justify=tk.LEFT, borderwidth=2, relief="ridge").grid(row=2, column=0)
    
    info_2_var = tk.StringVar()
    random_quote = rq.Quote()
    info_2_var.set(random_quote.get_quote())
    info_2 = tk.Label(header, textvariable=info_2_var, font=('arial', 12, ''), bg="#bedebe", 
                      fg="black", padx=10, pady=10, justify=tk.RIGHT, borderwidth=2, relief="ridge").grid(row=2, column=1)
    
    
    post_text = tk.Text(body, width=100, borderwidth=2, relief="ridge")
    post_text.grid(row=0, column=0, columnspan=2)
    
    #post_text.delete('1.0', tk.END)
    #post_text.insert(tk.END, post)
    
    def ert():
        post = post_text.get(1.0,tk.END)
        post1 = rom.ReadPost(post)
        time = post1.wpm()
        mins = int(time/60)
        secs = int(time%60)
        words = post1.count_words()
        data = "Estimated reading time: " + str(mins) + " minutes, " + str(secs) + " seconds. Contains " + str(words) + " words"
        info_1_var.set(data)
    
    ert_button = tk.Button(body, text="Estimate Reading Time!", font=('arial',15,'bold'), padx=10, pady=20, bg="#333333", 
                           fg="powder blue", borderwidth=2, relief="groove", command=ert).grid(row=1, column=0)
    
    def reset():
        post_text.delete("1.0", tk.END)
    reset_button = tk.Button(body, text="Reset", font=('arial',15,'bold'), padx=10, pady=20, bg="white", 
                           fg="black", borderwidth=2, relief=tk.RAISED, command=reset).grid(row=1, column=1)
    footer = tk.Label(body, text= "**Calculation is based on the average reading speed that around 200 words per minute (wpm)",pady=20).grid(row=3,column=0)
    
    window.mainloop()

if __name__ == '__main__':
    main()