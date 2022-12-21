# Welcome to the Lumos Coding Quest
# you have been given a linked list with duplicate values
# upon running this code, you will see a string that has been formed by collecting the data in the nodes of the linked list
# you need to complete the "MyAnswer" function and ensure that it removes the duplicate nodes from the linkedlist
# when you collate the string that this new linked list contains, you will get the link to the whitelist form

# Note:- "list" represents the said linked list

from helper import *

import webbrowser

class Modify_:
    def __init__(self,head : object ) -> None :
        self.headval : object = head

    def listprint(self) -> str:
        """For the terminal to display the node values"""

        printval: object = self.headval
        answer: str = ""

        while printval is not None:
            answer += printval.dataval
            printval = printval.nextval
        return answer

    def get_prev_node(self, ref_node: object) -> object:
        """Return the node's object after retrieving the previous node"""

        current: object = self.headval
        while current and current.nextval != ref_node:
            current = current.nextval
        return current

    def remove(self, node: object) -> None:
        """This function removes the node specified by the provided argument."""

        prev_node: object = self.get_prev_node(node)

        if prev_node is None:
            self.head: object = self.head.nextval
        else:
            prev_node.nextval: object = node.nextval

    def remove_duplicates(self) -> None:
        """The linked list's duplicate nodes are removed using this method"""

        current1: object = self.headval

        while current1:
            data: object = current1.dataval
            current2: object = current1.nextval
            while current2:
                if current2.dataval == data :
                    self.remove(current2)
                current2: object = current2.nextval
            current1: object = current1.nextval


def MyAnswer(self) -> None :
   # please put in your answer  here
   answer : str = ""
   obj : object = Modify_(self.headval)
   # remove duplicates 
   obj.remove_duplicates()
   # alter output string
   answer = "--"*40 + "\n" + obj.listprint() + "\n" + "--"*40 + "\n"
   print(answer)
   # open link at web browser
   webbrowser.open(obj.listprint(), new=2)

MyAnswer(list)




