print("\t\tSPAM MAIL DETECTION\n")
spam_words = ["win", "free", "offer", "prize", "click", "urgent","Win", "Free", "Offer", "Prize", "Click", "Urgent","Lottery","lottery"]
n = int(input("Enter the number of emails: "))
i = 1
while i <= n:
    print("\nEmail", i)
    mail = input("Enter the email message: ")
    mail = mail.lower()
    spam = False
    for j in range(len(spam_words)):
        if spam_words[j] in mail:
            spam = True
            break
    if spam:
        print("Result : Spam Mail")
    else:
        print("Result : Not a Spam Mail")
    i = i + 1
