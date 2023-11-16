"""Class to store a message (operator overload, union types, default parameters)"""

class Message:

    to: str
    content: str
    important: bool

    def __init__(self, recipient: str | int, message_content: str = "", importance_flag: bool = False):
        """Construct a message"""
        self.to = recipient
        self.content = message_content
        self.important = importance_flag


    def __str__(self) -> str:
        output: str = f"Message to {self.to}:\n"
        output += f"Important? {self.important}:\n"
        output += f'"{self.content}"'
        return output
    

    def __mul__(self, factor: int):
        """Multiplication operator overload"""
        copy_val: str = self.content
        for loop_number in range(0, factor):
            self.content += "" + copy_val

        

#msg: Message = Message("erin", "Great job?", False)
#msg * 10
msg_to_myself:Message = Message("me,", "You are the best!", True)
#print(msg)
#msg_to_myself * 100
print(msg_to_myself)
msg_to_camilla: Message = Message("camilla", "You inspire the students!")
print(msg_to_camilla)
msg_to_bear: Message = Message("Bear")
msg_to_bear.content = "Good boy!"
msg_to_bear.important = True
print(msg_to_bear)