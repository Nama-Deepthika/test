registered = input()
fee_paid = input()
identity_verified = input()
system_check = input()

# Check the student can access the online exam.
if registered == "yes":
    if fee_paid and identity_verified == "yes":
        if system_check == "pass":
            print("Access Granted")
        else:
            print("Access Denied: system check failed")
    else:
        print("Access Denied: Verification Pending")
else:
    print("Access Denied: Registration Incomplete")