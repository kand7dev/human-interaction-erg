def hi():
    print("yes")
    
dict = {
    "Schedule" : hi,
    "Manage" : hi,
    "Appointments" : hi,
    "Calendar" : hi,
    "I want to make an appointment" : hi,
    "Show me my appointments" : hi,
    "email" :hi,
    "Send email" : hi,
    "Receive email" :hi,
    "Take a note" :hi,
    "Edit a note" :hi,
    "Delete a note" :hi,
    "Show me my notes" :hi,
    "Create a to-do list" :hi,
    "Show me my to-do list" :hi,
    "Alarm" :hi,
    "Reminder" :hi,
    "Clock" :hi,
    "Wake me up" :hi,
    "Set alarm" :hi,
    "Turn off the alarm" :hi,
    "Set Reminder" :hi,
    "Send notification" :hi,
    "Phone Call" :hi,
    "Message" :hi,
    "Send text message" :hi,
    "Call" :hi,
    "Task" :hi,
    "Task list" :hi,
    "Contacts" :hi,
    "Delete a contact" :hi,
    "Edit a contact" :hi,
    "Organize" :hi,
    "Organize files" :hi,
    "Create a new file" :hi,
    "Open an existing file" :hi,
    "Save the file" :hi,
    "Print the file" :hi,
    "Delete the file" :hi,
    "Find weather" : hi,
    "Weather" : hi,
    "What is the weather" : hi,
    "Traffic" :hi,
    "Traffic update" :hi,
    "Provide traffic situation" :hi,
    "Show me stock prices" :hi,
    "Music" :hi,
    "Play some music" :hi,
    "Open Spotify" :hi,
    "Open YouTube" :hi,
    "Open Google" :hi,
    "Open Facebook" :hi,
    "Open Instagram" :hi,
    "Open Twitter" :hi,
    "Open ICE Uniwa" :hi,
    "Open Settings" :hi,
    "Increase volume" :hi,
    "Reduce volume" :hi,
    "Increase Brightness" :hi,
    "Reduce Brightness" :hi,
    "Zoom in" :hi,
    "Zoom out" :hi,
    "Order" :hi,
    "Pay via PayPal" :hi,
    "Pay via Credit Card" :hi,
    "Pay via Debit Card" :hi,
    "Pay via Revolut" :hi,
    "Pay via Paysafe" :hi,
    "Shopping list" :hi,
    "Translate" :hi,
    "Open GPS" :hi,
    "Navigate me to" :hi,
    "How to get to" :hi,
    "Show me directions to" :hi,
    "Show me nearby restaurants" :hi,
    "Show me nearby bars" :hi,
    "Show me BBC" :hi,
    "Show me news about sports" :hi,
    "Show me general news" :hi,
    "Open Google" :hi,
    "Find" :hi,
    "Show me results for" :hi,
    "Open the light" :hi,
    "Close the light" :hi,
    "Turn on the light" : hi,
    "Turn off the light" :hi,
    "Increase the heat" :hi,
    "Reduce the heat" :hi,
    "Open the TV" :hi,
    "Close the TV" :hi,
    "Turn on the AC" :hi,
    "Turn off the AC" :hi,
    "Turn on the security alarm" :hi,
    "Turn off the alarm" :hi,
    "Open the door" :hi,
    "Close the door" :hi,
    "Lock the door" :hi,
    "Unlock the door" :hi,
    "Open the window" :hi,
    "Close the window" :hi,
    "Lock the window" :hi,
    "Unlock the window" :hi,
    "Open the garage" :hi,
    "Close the garage" :hi,
    "Lock the garage" :hi,
    "Unlock the garage" :hi,
    "Turn on the sprinkler" :hi,
    "Turn off the sprinkler" :hi,
    "Start the washing machine" :hi,
    "Stop the washing machine" :hi,
    "Start the dishwasher" :hi,
    "Stop the dishwasher" :hi,
    "Start the oven" :hi,
    "Stop the oven" :hi,
    "Start the microwave" :hi,
    "Stop the microwave" :hi,
    "Start the blender" :hi,
    "Stop the blender" :hi,
    "Start the vacuum cleaner" :hi,
    "Stop the vacuum cleaner" :hi,
    "Start the coffee maker" :hi,
    "Stop the coffee maker" :hi,
    "Turn on the fan" :hi,
    "Turn off the fan" :hi,

}

x = str(input("What are you searching for: "))
input_list = x.split()
for item in input_list:
    if item in dict:
        hi()
        break