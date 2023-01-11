from mailtm import Email
import requests
import time

FFweb = "https://www.farmfoods.co.uk/includes/mailing_list/join-club.php"


def verifyEmail():
    
    verlink = x[20]

    verlink = verlink.replace("[", "")
    verlink = verlink.replace("]", "")
    verlink = verlink.replace(".com.", ".com")
    
    #print(verlink)

    r = requests.get(verlink)
    #print(r)

def opencoup():

    coup = x[7]

    coup = coup.replace("[", "")
    coup = coup.replace("]", "")
    coup = coup.replace(".com.", ".com")

    #print(coup)

    r = requests.get(coup)
    #print(r)
    html = r.text
    html = html.split()
    #print(html)
    
    coup1 = html[323]
    coup1 = coup1.replace("class='text-center'>", "")
    coup1 = coup1.replace("<u>", "")
    coup1 = coup1.replace("</u>", "")
    coup1 = coup1.replace("</h3>", "")
    coup1 = coup1.replace("<h4", "")

    print("£2 off £25:" , coup1)

    coup1 = html[374]
    coup1 = coup1.replace("class='text-center'>", "")
    coup1 = coup1.replace("<u>", "")
    coup1 = coup1.replace("</u>", "")
    coup1 = coup1.replace("</h3>", "")
    coup1 = coup1.replace("<h4", "")

    print("£2 off £25:" , coup1)

    coup1 = html[425]
    coup1 = coup1.replace("class='text-center'>", "")
    coup1 = coup1.replace("<u>", "")
    coup1 = coup1.replace("</u>", "")
    coup1 = coup1.replace("</h3>", "")
    coup1 = coup1.replace("<h4", "")

    print("£5 off £60:" , coup1)

    coup1 = html[476]
    coup1 = coup1.replace("class='text-center'>", "")
    coup1 = coup1.replace("<u>", "")
    coup1 = coup1.replace("</u>", "")
    coup1 = coup1.replace("</h3>", "")
    coup1 = coup1.replace("<h4", "")

    print("£5 off £60:" , coup1)
    


def listener(message):
    global x 

    x = "Content: " + message['text'] if message['text'] else message['html']
    x = x.split()
    #print(x)

    if x[7] == "registering":
        verifyEmail()

    if x[5] == "click":
        opencoup()

    
    


for x in range(10):
    # Get Domains
    test = Email()
    #print("\nDomain: " + test.domain)

    # Make new email address
    test.register()
    #print("\nEmail Adress: " + str(test.address))
    test.address
    payload = {"email_address": test.address}
    r = requests.get(FFweb, params=payload)

    # Start listening
    test.start(listener, interval=1)
    #print("\nWaiting for new emails...")
