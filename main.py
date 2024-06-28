import tkinter as tk
from tkinter import messagebox

def calculate_returns():
    investment = selected_investment.get()
    if investment == "":
        messagebox.showerror("Error", "Please select an investment!")
        return

    amount_val = amount.get()
    if amount_val <= 0:
        messagebox.showerror("Error", "Please enter a valid amount!")
        return

    annual_return = investments[investment]["Annual Return"]
    three_year_return = investments[investment]["3yr Return"]
    five_year_return = investments[investment]["5yr Return"]
    ten_year_return = investments[investment]["10yr Return"]

    annual_returns = amount_val * (1 + annual_return / 100)
    three_year_returns = amount_val * (1 + three_year_return / 100)
    five_year_returns = amount_val * (1 + five_year_return / 100)
    ten_year_returns = amount_val * (1 + ten_year_return / 100)

    messagebox.showinfo("Returns",
                        f"Estimated Returns:\n"
                        f"1 Year: {annual_returns:.2f}\n"
                        f"3 Year: {three_year_returns:.2f}\n"
                        f"5 Year: {five_year_returns:.2f}\n"
                        f"10 Year: {ten_year_returns:.2f}")

def main():
    root = tk.Tk()
    root.title("WealthTracker")

    # Initialize variables
    global investments, selected_investment, amount
    investments = {
        "Stocks": {"Annual Return": 10, "3yr Return": 30, "5yr Return": 50, "10yr Return": 100},
        "Bonds": {"Annual Return": 5, "3yr Return": 15, "5yr Return": 25, "10yr Return": 50},
        "Real Estate": {"Annual Return": 8, "3yr Return": 24, "5yr Return": 40, "10yr Return": 80}
    }
    selected_investment = tk.StringVar(root)
    amount = tk.DoubleVar(root)

    # Create GUI elements
    tk.Label(root, text="Select Investment:").grid(row=0, column=0, padx=10, pady=5)
    investment_menu = tk.OptionMenu(root, selected_investment, *investments.keys())
    investment_menu.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Enter Amount:").grid(row=1, column=0, padx=10, pady=5)
    amount_entry = tk.Entry(root, textvariable=amount)
    amount_entry.grid(row=1, column=1, padx=10, pady=5)

    calculate_button = tk.Button(root, text="Calculate Returns", command=calculate_returns)
    calculate_button.grid(row=2, columnspan=2, padx=10, pady=5)

    quit_button = tk.Button(root, text="Quit", command=root.quit)
    quit_button.grid(row=3, columnspan=2, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
