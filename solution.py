from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n My message"
   endmsg = "\r\n.\r\n"

   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

   # Create socket called clientSocket and establish a TCP connection with mailserver and port

   # Fill in start
   serverName = 'nyu.edu'
   serverPort = 25
   clientSocket=socket(AF_INET,SOCK_STREAM)
   clientSocket.connect((serverName,serverPort))

   # Fill in end

   recv = clientSocket.recv(1024).decode()
   print(recv)
   if recv[:3] != '220':
       print('220 reply not received from server.')
       #print('220 reply not received from server.')

   # Send HELO command and print server response.
   heloCommand = 'HELO Alice\r\n'
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   print(recv1)
   if recv1[:3] != '250':
       print('250 reply not received from server.')
       #print('250 reply not received from server.')

   # Send MAIL FROM command and print server response.
   # Fill in start
   MailCommand = 'MAIL FROM: test@gmail.com\r\n'
   clientSocket.send(MailCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   print(recv1)
   if recv1[:3] != '250':
       print('250 reply not received from server.')
   # Fill in end

   # Send RCPT TO command and print server response.
   # Fill in start
   RcptCommand = 'RCPT TO: jm9556@nyu.edu\r\n'
   clientSocket.send(RcptCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   print(recv1)
   if recv1[:3] != '250':
       print('250 reply not received from server.')
   # Fill in end

   # Send DATA command and print server response.
   # Fill in start
   DataCommand = 'DATA\r\n'
   clientSocket.send(DataCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   print(recv1)
   if recv1[:3] != '250':
       print('250 reply not received from server.')
   # Fill in end

   # Send message data.
   # Fill in start
   MessageCommand = 'Testing my programming skills\r\n'
   
   # Fill in end

   # Message ends with a single period.
   # Fill in start
   messageEnd='\r\n.\r\n'
   clientSocket.send((MessageCommand + messageEnd).encode())
   recv1 = clientSocket.recv(1024).decode()
   print(recv1)
   if recv1[:3] != '250':
       print('250 reply not received from server.')
   # Fill in end

   # Send QUIT command and get server response.
   # Fill in start
   QuitCommand = 'QUIT\r\n'
   clientSocket.send(QuitCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   print(recv1)
   if recv1[:3] != '250':
       print('250 reply not received from server.')
   # Fill in end


if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')