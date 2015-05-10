import chat
chat.init()
server = chat.ChatServer('main_thread')
server.start()
server.quit()
del server
