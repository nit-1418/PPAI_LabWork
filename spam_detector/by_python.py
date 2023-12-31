############### spam detection ###############
def is_spam(email):
    spam_keywords = ['buy now', 'limited time', 'earn money', 'click here', 'subscribe', 'click below', 'order now', 'money back',
                      'free', 'offer', 'discount', 'trial', 'winner', 'prize', 'congratulations', 'dear friend', 'hello', 'dear', 'hello dear', 'dear sir', 'dear madam',
                        'dear customer', 'dear winner', 'dear lucky', 'dear selected', 'dear account', 'dear email',]
    
    for keyword in spam_keywords:
        if keyword in email.lower():
            return True
    
    return False

input_email = input("Enter your email: ")
result = is_spam(input_email)

if result:
    print("This email is likely spam.")
else:
    print("This email is not spam.")
