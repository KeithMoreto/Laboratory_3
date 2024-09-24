def check_loan_eligibility():
    #Getting customer details
    monthly_salary = float(input("Enter your monthly salary: "))
    loan_amount = float(input("Enter the loan amount you are requesting: "))
    
    #Check Loan Eligibility
    if monthly_salary >= 30000 and loan_amount <= 10 * monthly_salary:
        print("you are eligible for the loan.")
        monthls_to_pay = int(input("Enter the number of months you want to pay the loan"))
        total_amount = loan_amount * 1.10 #Adding 10% interest
        monthly_payment = total_amount / monthls_to_pay
        print(f"Your total loan amount with interest is: {total_amount:.2f}")
        print(f"Your monthly payment will be: {monthly_payment:.2f}")
        
    else:
        if monthly_salary < 30000:
            print("You are not eligible for the loan because your salary is too low. ")
        if loan_amount > 10 * monthly_salary:
            print("You are not eligible for the loan because the loan amount requested is too high" ) 
    
#Run the function
check_loan_eligibility()
        