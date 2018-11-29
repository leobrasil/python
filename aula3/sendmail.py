import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
server.login("leobrasil@gmail.com", "Wssmbmlpn77!")

#Send the mail
msg = "Hello!" # The /n separates the message from the headers
server.sendmail("you@gmail.com", "leobrasil@example.com", msg)