from tkinter import *

class CarLoanCalculator:

    def __init__(self):
        window = Tk()  # Create a window
        window.title("CAR LOAN")  # Set title
        # create the input boxes.
        window.configure(background='white')

        Label(window, text="Number of Years",fg='green',font='bold').grid(row=1,column=1, sticky=W)

        Label(window, text="Car Price",fg='green',font='bold').grid(row=2,column=1, sticky=W)

        Label(window, text="Annual Interest Rate",fg='green',font='bold').grid(row=3,column=1, sticky=W)

        Label(window, text="Monthly Payment",fg='green',font='bold').grid(row=4,column=1, sticky=W)

        Label(window, text="Total Payment",fg='green',font='bold').grid(row=5,column=1, sticky=W)


        # for taking inputs
        # self.annualInterestRateVar = StringVar()
        # Entry(window, textvariable=self.annualInterestRateVar,justify=RIGHT).grid(row=1, column=2)

        self.numberOfYearsVar = StringVar()

        Entry(window, textvariable=self.numberOfYearsVar,justify=RIGHT).grid(row=1, column=2)
        self.loanAmountVar = StringVar()

        Entry(window, textvariable=self.loanAmountVar,justify=RIGHT).grid(row=2, column=2)

        self.annualintrestrateVar = StringVar()
        lblAnnualIntrestRate = Label(window,textvariable=self.annualintrestrateVar).grid(row=3,column=2,sticky=E)
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable=self.monthlyPaymentVar).grid(row=4,column=2, sticky=E)

        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable=self.totalPaymentVar).grid(row=5,column=2, sticky=E)

        # create the button
        btComputePayment = Button(window, text="Compute Payment",command=self.computePayment).grid(row=6, column=2, sticky=E)
        window.mainloop()  # Create an event loop

    # compute the total payment.
    def computePayment(self):
        fixedrate_peryear = 1.2
        self.annualintrestrate = float(self.numberOfYearsVar.get())*1.2
        self.annualintrestrateVar.set(self.annualintrestrate)
        monthlyPayment = self.getMonthlyPayment(float(self.loanAmountVar.get()),
                                                float(self.annualintrestrate) / 1200,
                                                int(self.numberOfYearsVar.get()))

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 * int(self.numberOfYearsVar.get())

        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        # compute the monthly payment.
        monthlyPayment = loanAmount * monthlyInterestRate / (1- 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))

        return monthlyPayment
        root = Tk()  # create the widget


# call the class to run the program.
CarLoanCalculator()