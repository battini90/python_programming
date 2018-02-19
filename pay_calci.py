hours = input("Enter number of hours")
hours = float(hours)
rate  = input("Enter rate per hour")
rate = float(rate)


def computePay(rate, hours):
    if hours > 40:
       pay = 40*rate + (hours-40)*1.5*rate
       return print(pay)
    else:
       pay = rate*hours
       return print(pay)

computePay(rate, hours)