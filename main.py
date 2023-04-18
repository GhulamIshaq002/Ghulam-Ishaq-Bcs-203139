import requests                                             # Will Request API from Mentioned Website
import json                                                 # This will Loads According to Api id 
import tkinter as tk                                            # Library Used as per Assignment


api_endpoint = "https://openexchangerates.org/api/latest.json"          # Api Linked Using 1st Website Link 
app_id = "d6482a3c64f84a5fb77e2d4ccf5c2ada"                             # Api Id Generated 

                                                                         
response = requests.get(f"{api_endpoint}?app_id={app_id}")          # This will get Updated Rates 
exchange_rates = json.loads(response.text)["rates"]                 # Rates Might get differ Because of Free Account and Limited Number of Updation


root = tk.Tk()                                                       # This Will Create a New Window For Currency Converter
root.title("Currency Converter Using API of 1st Website")


def convert():                                                    # This Will Perform Currency Conversion
    
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = float(amount_entry.get())

   
    converted_amount = amount / exchange_rates[from_currency] * exchange_rates[to_currency]    #Convert The Amount to The Currency Of your Choice

   
    output_label.config(text=f"{converted_amount:.2f} {to_currency}")                  # Gives the Converted Amount 2 decimal places

def reset():                                                                            # Reset Function It will Reset all Enteries
    amount_entry.delete(0, tk.END)
    output_label.config(text="")


from_currency_var = tk.StringVar(value="PKR")                                          # Pre-Defined PKR and AUD (You Might Change This)
to_currency_var = tk.StringVar(value="AUD")
from_currency_menu = tk.OptionMenu(root, from_currency_var, *exchange_rates.keys())
to_currency_menu = tk.OptionMenu(root, to_currency_var, *exchange_rates.keys())
amount_label = tk.Label(root, text=" Enter Amount To be Converted:")
amount_entry = tk.Entry(root)


convert_button = tk.Button(root, text="Convert", command=convert)                   # This Will create Buttons For conversion and Reset
reset_button = tk.Button(root, text="Reset", command=reset)


output_label = tk.Label(root, font=("Calibri", 20))                                  # This Will Give the Output  ( FONTS MAY CHANGE )                


from_currency_menu.pack()                                                            # Pack the widgets into the window
to_currency_menu.pack()
amount_label.pack()
amount_entry.pack()
convert_button.pack()
reset_button.pack()
output_label.pack()


root.mainloop()
