with open('sales.txt', 'r') as sales_file:
    for line in sales_file:
        amount = float(line)
        print(format(amount, '.2f'))
        total_sales += amount
print(f"Total sales: (total_sales:.2f)")