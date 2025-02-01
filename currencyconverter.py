import tkinter as tk
from tkinter import ttk

def convert_currency():
    amount = float(entry_amount.get())
    from_currency = combo_from.get()
    to_currency = combo_to.get()
    
    exchange_rates = {
        'EUR': {'GBP': 0.85, 'USD': 1.10, 'EUR': 1.0},
        'GBP': {'EUR': 1.18, 'USD': 1.30, 'GBP': 1.0},
        'USD': {'EUR': 0.91, 'GBP': 0.77, 'USD': 1.0}
    }
    
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        converted_amount = amount * exchange_rates[from_currency][to_currency]
        label_result.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        label_result.config(text="Conversion not available")

# GUI Setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("300x200")

tk.Label(root, text="Amount:").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Label(root, text="From:").pack()
combo_from = ttk.Combobox(root, values=["EUR", "GBP", "USD"])
combo_from.pack()
combo_from.set("EUR")

tk.Label(root, text="To:").pack()
combo_to = ttk.Combobox(root, values=["EUR", "GBP", "USD"])
combo_to.pack()
combo_to.set("USD")

tk.Button(root, text="Convert", command=convert_currency).pack()
label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
