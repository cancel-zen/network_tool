# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:26:51 2019

@author: cs
"""

import os 
import tkinter as tk
def ping_the_net():
    abc = 'start cmd /k ping 223.5.5.5'
    ver=os.system(abc)
    
    
def rest_the_net():
    abc='start cmd /k netsh winsock reset'
    ver=os.system(abc)


def ipconfig_all():
    abc='start cmd /k ipconfig'
    ver=os.system(abc)
    
def ipconfig_flushdns():
    abc='start cmd /k ipconfig /flushdns'
    ver=os.system(abc)

def ipconfig_displaydns():
    abc='start cmd /k ipconfig /displaydns'
    ver=os.system(abc)
    
def tracert_ip():
    ip_and_site=input_bar.get()
    abc='start cmd /k tracert '+ip_and_site
    ver=os.system(abc)
    

window=tk.Tk()
window.title('网络工具 by今晚打老虎')
window.geometry('400x300')
button_ping_the_net=tk.Button(window,text='网络连通测试',command=ping_the_net)
button_ping_the_net.pack()

button_rest_the_net=tk.Button(window,text='网络重置',command=rest_the_net)
button_rest_the_net.pack()

button_ipconfig_all=tk.Button(window,text='网络查询',command=ipconfig_all)
button_ipconfig_all.pack()

button_flushdns=tk.Button(window,text='刷新dns',command=ipconfig_flushdns)
button_flushdns.pack()

button_displaydns=tk.Button(window,text='dns缓存',command=ipconfig_displaydns)
button_displaydns.pack()


lb_tracert=tk.Label(window,text='输入需要测试网络路径的ip或网址')
lb_tracert.pack()
input_bar=tk.Entry(window)
input_bar.pack()

button_tracert=tk.Button(window,text='测试ip路径',command=tracert_ip)
button_tracert.pack()

window.mainloop()

