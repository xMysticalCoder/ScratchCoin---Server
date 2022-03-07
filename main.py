

# -----IMPORTS-----
import sys
from better_profanity import profanity
import scratchconnect
import os
from replit import db
import keep_alive
# import ScratchEncoder
# --------SETUP---------

username = os.environ['USERNAME']
password = os.environ['PASSWORD']

user = scratchconnect.ScratchConnect(username, password)
project = user.connect_project(project_id=651500530)
variables = project.connect_cloud_variables()
# ---------FUNCTIONS--------
def readVar(name):
    return variables.get_cloud_variable_value(variable_name=name)[0]
  
def setVar(name, value):
  
    return variables.set_cloud_variable(variable_name=name, value=value)
  
    
  
  
def delAll():
  for q in list(db.keys()):
    print(f"Deleting {q}")
    del db[q]
  


# --------MAIN------------
#delAll()
keep_alive.keep_alive()
while True:
  try:
  
  
    if readVar("getVotes") != "0":
      user = variables.decode(readVar("getVotes"))
      if user in db.keys():
        setVar("recieveVotes", db[user])
        setVar("getVotes", 0)
      else:
        db[user] = 1000
        setVar("recieveVotes", db[user])
        setVar("getVotes", 0)
    if readVar("giveToUser") != "0":
      decoded = variables.decode(readVar("giveToUser"))
      decoded = decoded.split(":")
      user = decoded[0]
      amount = decoded[1]
      giving = decoded[2]
      print(user)
      print(amount)
      print(giving)
      
      
      file = open('transactionsHistory.txt','a')
      
      try:
        int(amount)
      except:
        setVar("giveStatus", "1")
        setVar("giveToUser", "0")
        continue
      if db[giving] >= int(amount):
        db[giving] -= int(amount)
        if user in db.keys():
          db[user] += int(amount)
          setVar("giveStatus", "0")
          setVar("giveToUser", "0")
          file.write(f"{giving} gave {amount} coin(s) to {user}.\n")
          file.close()
        else:
          db[user] = int(amount) + 1000
          setVar("giveStatus", "0")
          setVar("giveToUser", "0")
          file.write(f"{giving} gave {amount} coin(s) to {user}.\n")
          file.close()
      else:
        setVar("giveStatus", "1")
        setVar("giveToUser", "0")
        file.write(f"{giving} tried to give {amount} coin(s) to {user}.\n")
        file.close()
  except:
    print("failed loop")
    user = scratchconnect.ScratchConnect(username, password)
    project = user.connect_project(project_id=651500530)
    variables = project.connect_cloud_variables()

      
        
      
    
  
    
  
  