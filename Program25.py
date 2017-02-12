#Password strength indicator
def checkpassword(pw):
    #very weak
    hasletter = False
    hasnumber = False
    hasspecial = False
    for i in pw:
        if i.isalpha() == True:
            hasletter = True
        elif i.isdigit():
            hasnumber = True
        elif i.isalpha() == False and i.isdigit() == False:
            hasspecial = True
    if len(pw) >= 8 and hasnumber and hasletter and hasspecial:
        return "very Strong"
    if len(pw) >= 8 and hasnumber and hasletter:
        return "strong"
    elif len(pw) < 8 and pw.isalpha():
        return "weak"
    if len(pw) < 8 and pw.isdigit():
        return "very weak"
    return "very very weak"

userpw = input("Enter your password:")
print("Your password " + userpw + " is " + checkpassword(userpw))
