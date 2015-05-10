import chat
chat.init()
client = chat.ChatClient(raw_input('Name:'))
client.start()
client.quit()
del client
