
import re
import argparse
import sys

# replace this comment with your implementation of
# Email class, Server class,
# main(), argparse()

import re

class Server(): 
    '''This class stores the data for all emails found in the emails_10k.txt file'''
    def __init__(self, path):
        f = open(path, "r")
        
        emails_list = f.read().split("End Email")  
         
        emails_list.pop()
        
        self.emails = []
        
        for e in emails_list:
            message_id_pattern = r"<(.+)>"
            message_id = re.search(message_id_pattern, e).group(1)

            date_pattern = r"Date:\s*(.+)"
            date = re.search(date_pattern, e).group(1)
    

            sender_pattern = r"From:\s*(.+)"
            sender = re.search(sender_pattern, e).group(1)

            receiver_pattern = r"To:\s*(.+)"
            receiver = re.search(receiver_pattern, e).group(1) 

            subject_pattern = r'Subject: (.*)'
            subject = re.search(subject_pattern, e).group(1) 

            body_pattern = r"(?<=\n\n).+"
            body = re.search(body_pattern, e, re.DOTALL).group(0)
          
            self.emails.append(Email(message_id, date, subject, sender, receiver, body))


class Email:
    '''The Email class will sore the data related to individual email messages;
    returns nothing'''
    def __init__(self, message_id, date, subject, sender, receiver, body):
        self.message_id = str(message_id)
        self.date = str(date)
        self.subject = str(subject)
        self. sender = str(sender)
        self.receiver = str(receiver)
        self.body = str(body)
        
def main(path):
    '''the main function will create an instance of the Server class and save it to a variabe;
    it will return the length of the emails attribute'''
    server = Server(path)
    return len(server.emails)

def parse_args(args_list):
    '''Will create an instance of the argumentparser class from the argesparse module
    (imported above)'''
    parser = argparse.ArgumentParser()
    
    parser.add_argument('path', type = str, help = 'The user cannot run the program without specifying these')
    return parser.parse_args(args_list)

if __name__ == "__main__":
    pass
    variable = parse_args(sys.argv[1:])
    print(main(input.path))
    
####You will need to write some code here 