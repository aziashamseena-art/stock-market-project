#to provie a nice user inerface for the took 
#user input like salary, expenses, age and provide the output in a nice way
#convert it into an application using tkinter
from app import get_investment_allocation,convert_percentage_to_cash
import tkinter as tk
root = tk.Tk()
root.title("stock market app") #for title
root.geometry("500x500") #for default length and width of the app wondow

def calculate():
    age = int(age_entry.get())
    salary = int(salary_entry.get())
    expence = int(expence_entry.get())
    investible_amount = salary - expence
    print(investible_amount)
    equity, large_cap, mid_cap, small_cap, debt, gold = get_investment_allocation(age)
    result = f"""
Investible amount ₹{investible_amount}
--------------------------------------------------------------------
Based on your age, we recommend the following investment allocation:
--------------------------------------------------------------------
  Equity: {equity}%
    Large Cap: {large_cap}%
    Mid Cap: {mid_cap}%
    Small Cap: {small_cap}%
  Debt: {debt}%
  Gold: {gold}%
-----------------------------------------------------------
 we recommend the following investment allocation in cash:
----------------------------------------------------------
    Equity: ₹{convert_percentage_to_cash(investible_amount, equity)}
      Large Cap: ₹{convert_percentage_to_cash(investible_amount, large_cap)}
      Mid Cap: ₹{convert_percentage_to_cash(investible_amount, mid_cap)}
      Small Cap: ₹{convert_percentage_to_cash(investible_amount, small_cap)}
    Debt: ₹{convert_percentage_to_cash(investible_amount, debt)}
    Gold: ₹{convert_percentage_to_cash(investible_amount, gold)}""" # triple quote id to diplay the text how we type no need of \n.it will display how we type
       
    result_full.config(text=result)  #to display the result that we have to already exsisting lable


label = tk.Label(root, text="Enter your details for the best recomendations", font=("Arial", 14,"bold")) #tk.Label for a label
label.pack() #pack() is for display without pach() nothing diaplay
frame = tk.Frame()
frame.pack()

#user inputs
age_label = tk.Label(frame, text="Age :",font=("Arial",12)) #tk.Label for a label
age_label.grid(row=0,column=0,sticky="w")# for arrange in grid 
age_entry = tk.Entry(frame)
age_entry.grid(row=0,column=1,pady=10)

salary_label = tk.Label(frame, text="Monthly salary :",font=("Arial",12)) 
salary_label.grid(row=1,column=0,sticky="w")# sticky is to align the text to any side east,west,north,south
salary_entry = tk.Entry(frame)
salary_entry.grid(row=1,column=1,pady=10)

expence_label = tk.Label(frame, text="Monthly expence :",font=("Arial",12)) 
expence_label.grid(row=2,column=0,sticky="w")
expence_entry = tk.Entry(frame)
expence_entry.grid(row=2,column=1,pady=10)

#buttom for calculate investemnt
investment_button = tk.Button(root, text="calculate the investment" ,font=("Arial",12), command=calculate)
investment_button.pack(pady=10)

result_full = tk.Label(root,text="",justify="left",font=("Arial",12))
result_full.pack(pady=10)
root.mainloop() #to run the app
