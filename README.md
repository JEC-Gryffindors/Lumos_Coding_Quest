# Lumos Coding Quest

### Instructions - 
1. The coding quest contains a linked list that contains either jumbled or duplicate parts of a web link.
2. You need to figure out a way to solve the puzzled linked list and find the actual link to the metaverse whitelist.
3. Don't forget to post about your victory on social media, challenge your friends and earn early access to the Lumos Metaverse.


# Soution

The base given code is :-

```
from helper import *


def MyAnswer(self):
   # please put in your answer  here
   answer = ""
   print(answer)


MyAnswer(list)

```

- There are four functions in the newly constructed Modify module: listprint, get_prev_node, remove and remove_duplicates.

- Using the key for that node, we can get delete of an existing node. We find the preceding node of the node that has to be eliminated with the programme below. Then, point the subsequent node's pointer to the subsequent node of the removed node.

- Get the previous node of the linked list using the get_prev_node method.

- To remove a linked list node, use the remove function.

- The linked list's duplicates node is removed using the remove_duplicates method.

# MyAnswer Function
## it is employed to print out the proper link's output. Lumos Coding Quest provides this default function.
```
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

```