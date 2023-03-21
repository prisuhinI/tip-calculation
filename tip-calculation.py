def tip_calculation():
    total_bill = float(input("What's the total bill for today, please? "))
    how_many_percent = int(input("What percent of the tip would you like to leave? "))
    percent = round((total_bill / 100) * how_many_percent, 2)   
    print(f"{how_many_percent}% tip is {percent}, which brings your total to {round(percent + total_bill, 2)}")


tip_calculation()


