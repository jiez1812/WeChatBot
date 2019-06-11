import itchat
from chatterbot import ChatBot

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    bot = ChatBot('LittleJie')
    print('{0} : {1}'.format(msg.user['NickName'], msg.text))
    response = bot.get_response(msg.text)
    return response

itchat.auto_login()
itchat.run()