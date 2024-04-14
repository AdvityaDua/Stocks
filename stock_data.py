# Importing the necessary files.

import yfinance as yf
import matplotlib.pyplot as pl
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from pandastable import Table, TableModel

# Creating required functions.


def max_period_chart(stock):
    window = Toplevel()
    stock_data = stock.history(period='max')
    figure1 = pl.Figure(figsize=(6, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    ax1.legend('Price')
    bar1 = FigureCanvasTkAgg(figure1, window)
    bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
    stock_data.plot.line(use_index=True, y='Close', ax=ax1)
    ax1.set_title('STOCK PRICE FROM 1996-2023')
    window.title('MAX PERIOD STOCK PRICE')
    window.configure(bg='white')
    window.resizable(0, 0)
    menu1 = Menu(window)
    window.config(menu=menu1)
    sub_menu_1 = Menu(menu1)
    menu1.add_cascade(label='File', menu=sub_menu_1)
    sub_menu_1.add_cascade(label='Exit', command=window.destroy)
    menu1.add_cascade(label='About', command=lambda: os.startfile('readme.txt'))
    img = ImageTk.PhotoImage(Image.open('icon.png'))
    window.iconphoto(False, img)


def one_month_details(stock):
    stock_data = stock.history()
    window = Toplevel()
    figure1 = pl.Figure(figsize=(6, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, window)
    bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
    stock_data.plot.line(use_index=True, y=['Close', 'Open'], ax=ax1)
    ax1.set_title('OPEN AND CLOSE PRICE OF LAST MONTH')
    window.title('1 MONTH OPEN AND CLOSE')
    window.configure(bg='white')
    window.resizable(0, 0)
    menu1 = Menu(window)
    window.config(menu=menu1)
    sub_menu_1 = Menu(menu1)
    menu1.add_cascade(label='File', menu=sub_menu_1)
    sub_menu_1.add_cascade(label='Exit', command=window.destroy)
    menu1.add_cascade(label='About', command=lambda: os.startfile('readme.txt'))
    p1 = ImageTk.PhotoImage(Image.open('icon.png'))
    window.iconphoto(False, p1)


def one_year_details(stock):
    stock_data = stock.history(period='12mo')
    window = Toplevel()
    figure1 = pl.Figure(figsize=(6, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, window)
    bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
    stock_data.plot.line(use_index=True, y=['Close', 'Open'], ax=ax1)
    ax1.set_title('OPEN AND CLOSE PRICE OF LAST YEAR')
    window.title('1 MONTH OPEN AND CLOSE')
    window.configure(bg='white')
    window.resizable(0, 0)
    menu1 = Menu(window)
    window.config(menu=menu1)
    sub_menu_1 = Menu(menu1)
    menu1.add_cascade(label='File', menu=sub_menu_1)
    sub_menu_1.add_cascade(label='Exit', command=window.destroy)
    menu1.add_cascade(label='About', command=lambda: os.startfile('/data/readme.txt'))
    p1 = ImageTk.PhotoImage(Image.open('icon.png'))
    window.iconphoto(False, p1)


def bar_price_up_or_down(stock):
    stock_data = stock.history(period='12mo')
    stock_data['Tomorrow'] = stock_data['Close'].shift(-1)
    stock_data['Target'] = (stock_data.Tomorrow > stock_data.Close).astype(int)
    window = Toplevel()
    figure1 = pl.Figure(figsize=(6, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, window)
    bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
    stock_data = stock_data['Target'].value_counts()
    stock_data.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('NUMBER OF PRICE UP AND DOWN IN LAST 1 YEAR')
    for bars in ax1.containers:
        ax1.bar_label(bars)
    window.title('1 MONTH OPEN AND CLOSE')
    window.configure(bg='white')
    window.resizable(0, 0)
    menu1 = Menu(window)
    window.config(menu=menu1)
    sub_menu_1 = Menu(menu1)
    menu1.add_cascade(label='File', menu=sub_menu_1)
    sub_menu_1.add_cascade(label='Exit', command=window.destroy)
    menu1.add_cascade(label='About', command=lambda: os.startfile('readme.txt'))
    p1 = ImageTk.PhotoImage(Image.open('/data/icon.png'))
    window.iconphoto(False, p1)


def price_hike_in_last_10_years(stock):
    stock_data = stock.history(period='max')
    one_day = stock_data.tail(1)
    one_day = one_day.Close
    one_day = one_day.values
    one_month = stock_data.tail(30)
    one_month = one_month.head(1)
    one_month = one_month.Close
    one_month = one_month.values
    one_year = stock_data.tail(365)
    one_year = one_year.head(1)
    one_year = one_year.Close
    one_year = one_year.values
    three_years = stock_data.tail(1095)
    three_years = three_years.head(1)
    three_years = three_years.Close
    three_years = three_years.values
    ten_years = stock_data.tail(3650)
    ten_years = ten_years.head(1)
    ten_years = ten_years.Close
    ten_years = ten_years.values
    one_day_value = 0
    one_month_value = 0
    one_year_value = 0
    three_years_value = 0
    ten_years_value = 0
    for i in one_day:
        one_day_value = i
    for i in one_month:
        one_month_value = i
    for i in one_year:
        one_year_value = i
    for i in three_years:
        three_years_value = i
    for i in ten_years:
        ten_years_value = i
    one_month_percentage = 100 * (one_day_value - one_month_value) / one_month_value
    one_year_percentage = 100 * (one_day_value - one_year_value) / one_year_value
    three_year_percentage = 100 * (one_day_value - three_years_value) / three_years_value
    ten_year_percentage = 100 * (one_day_value - ten_years_value) / ten_years_value
    series = pd.Series([one_month_percentage, one_year_percentage, three_year_percentage, ten_year_percentage],
                       index=['1 Month', '1 year', '3 years', '10 years'])
    window = Toplevel()
    figure1 = pl.Figure(figsize=(6, 6.5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, window)
    bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
    series.plot(kind='bar', legend=True, ax=ax1, use_index=True)
    for bars in ax1.containers:
        ax1.bar_label(bars)
    ax1.set_title('PERCENTAGE HIKE IN LAST MONTH, 1 YEAR, 3 YEARS, 10 YEARS')
    window.title('PERCENTAGE HIKE IN LAST 10 YEARS')
    window.configure(bg='white')
    window.resizable(0, 0)
    menu1 = Menu(window)
    window.config(menu=menu1)
    sub_menu_1 = Menu(menu1)
    menu1.add_cascade(label='File', menu=sub_menu_1)
    sub_menu_1.add_cascade(label='Exit', command=window.destroy)
    menu1.add_cascade(label='About', command=lambda: os.startfile('readme.txt'))
    p1 = ImageTk.PhotoImage(Image.open('icon.png'))
    window.iconphoto(False, p1)


def balance_sheet(stock):
    window = Toplevel()
    window.title('BALANCE SHEET OF LAST 4 YEARS')
    window.configure(bg='white')
    menu1 = Menu(window)
    window.config(menu=menu1)
    sub_menu_1 = Menu(menu1)
    menu1.add_cascade(label='File', menu=sub_menu_1)
    sub_menu_1.add_cascade(label='Exit', command=window.destroy)
    menu1.add_cascade(label='About', command=lambda: os.startfile('readme.txt'))
    p1 = ImageTk.PhotoImage(Image.open('icon.png'))
    window.iconphoto(False, p1)
    pt = Table(window, dataframe=stock.balancesheet, enable_menus=False)
    pt.show()
    pt.showIndex()


def get_data():
    try:
        stock = yf.Ticker(user_input.get())
        stock_data = stock.history()
        del stock_data['Dividends']
        del stock_data['Stock Splits']
    except KeyError:
        messagebox.showerror(title='NOT FOUND', message='No such stock found.')
    else:
        Label(text='History Price Chart from beginning of the stock', font=('Modern', 20), bg='white', padx=window.winfo_screenwidth() / 8).place(x=0, y=350)
        Button(text='Click Here', font=('Modern', 16), command=lambda: max_period_chart(stock)).place(x=window.winfo_screenwidth() * 6 / 8, y=350)
        Label(text='One month Opening and Closing price data', font=('Modern', 20), bg='white', padx=window.winfo_screenwidth() / 8).place(x=0, y=400)
        Button(text='Click Here', font=('Modern', 16), command=lambda: one_month_details(stock)).place(x=window.winfo_screenwidth() * 6 / 8, y=400)
        Label(text='One year Opening and closing price data', font=('Modern', 20), bg='white', padx=window.winfo_screenwidth() / 8).place(x=0, y=450)
        Button(text='Click Here', font=('Modern', 16), command=lambda: one_year_details(stock)).place(x=window.winfo_screenwidth() * 6 / 8, y=450)
        Label(text='How many times price went up and down the next day in last 1 year', font=('Modern', 20), bg='white', padx=window.winfo_screenwidth() / 8).place(x=0, y=500)
        Button(text='Click Here', font=('Modern', 16), command=lambda: bar_price_up_or_down(stock)).place(x=window.winfo_screenwidth() * 6 / 8, y=500)
        Label(text='Percentage price hike in Last 10 years', font=('Modern', 20), bg='white', padx=window.winfo_screenwidth() / 8).place(x=0, y=550)
        Button(text='Click Here', font=('Modern', 16), command=lambda: price_hike_in_last_10_years(stock)).place(x=window.winfo_screenwidth() * 6 / 8, y=550)
        Label(text='Last 4 Year Balance Sheet of the Company', font=('Modern', 20), bg='white', padx=window.winfo_screenwidth() / 8).place(x=0, y=600)
        Button(text='Click Here', font=('Modern', 16), command=lambda: balance_sheet(stock)).place(x=window.winfo_screenwidth() * 6 / 8, y=600)


window = Tk()
global size
# noinspection PyRedeclaration
size = window.winfo_geometry()
window.geometry(f'{window.winfo_geometry()}')
window.state('zoomed')
window.title('Main Menu')
window.configure(bg='white')
window.resizable(0, 0)
menu1 = Menu(window)
window.config(menu=menu1)
sub_menu_1 = Menu(menu1)
menu1.add_cascade(label='File', menu=sub_menu_1)
sub_menu_1.add_cascade(label='Exit', command=window.destroy)
menu1.add_cascade(label='About', command=lambda: os.startfile('icon.jpg'))

# Designing a menu bar

menu1 = Menu(window)
window.config(menu=menu1)
sub_menu_1 = Menu(menu1)
menu1.add_cascade(label='File', menu=sub_menu_1)
sub_menu_1.add_cascade(label='Exit', command=window.destroy)
menu1.add_cascade(label='About', command=lambda: os.startfile('readme.txt'))

# Setting the app icon and displaying it on the main screen.

p1 = ImageTk.PhotoImage(Image.open('icon.png'))
window.iconphoto(False, p1)
Label(padx=122, pady=121, image=p1, bg='white').place(relx=0.5, y=75, anchor=CENTER)

# Labelling the heading and statements of the project.
Label(text='Stock Data Analysis', font=('Modern', 36, 'bold'), anchor='w', bg='white').place(relx=0.5, y=175, anchor=CENTER)
Label(text='Enter the name of the stock you want to analyse:', font=('Modern', 20), bg='white', padx=window.winfo_screenwidth() / 8).place(x=0, y=210)
user_input = Entry(font=('Modern', 20), bg='white', border=2)
submit_button = Button(text='SUBMIT', font=('Modern', 16), command=get_data)
submit_button.place(relx=0.5, y=300, anchor=CENTER)
user_input.place(x=window.winfo_screenwidth() * 5 / 8, y=210)
window.mainloop()
