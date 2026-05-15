m_num = (input("enter a number : "))
if len(m_num) == 10 and (m_num).isdigit():
    if (m_num)[0] in ['6', '7', '8', '9']:
        print("Valid Indian mobile number")
    else:
        print("Invalid Indian mobile number")
else:
    print("Mobile number must contain 10 digits")

print("----------------------------------------------")
