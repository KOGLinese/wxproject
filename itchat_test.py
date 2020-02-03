import requests
import itchat

# 图灵机器人API
KEY = 'efe464b33e054496999bd8baa3bc4009'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl,data=data).json()
        print(r['text'])
        return r.get('text')
    except:
        return
# 测试
# get_response('你好')

@itchat.msg_register(itchat.content.TEXT,isFriendChat=True)
def text_reply(msg):
    # 获取好友发送的文本消息
    # 返回同样的文本消息
    content = msg['Content']
    # 将好友消息发送给机器人去处理，处理结果就是返回给好友的信息
    reply = get_response(content)
    return reply

# 微信官方已经现在不能登陆网页微信，因此测试失败
itchat.auto_login()
itchat.run()

# # 注册获取别人发来的信息方法
# @itchat.msg_register(['Text','Map', 'Card', 'Note', 'Sharing', 'Picture'])
# def tuling_reply(msg):
#     print(msg.User['NickName']+':'+msg['Text'])#这里输出给你发微信的人的名字和他发送的内容
#     reply = get_response(msg['Text'])  # 调取图灵机器人获取回复
#     print(reply + "\n")  # 打印机器人回复的消息
#     return reply
#
# @itchat.msg_register(itchat.content.TEXT, isGroupChat=True)    #群消息的处理
# def print_content(msg):
#     if msg.User["NickName"]=='家'or msg.User["NickName"]=='屌去哪了？':    #这里可以在后面加更多的or msg.User["NickName"]=='你希望自动回复群的名字'
#         print(msg.User['NickName'] +":"+ msg['Text'])     #打印哪个群给你发了什么消息
#         print(get_response(msg['Text'])+"\n")           #打印机器人回复的消息
#         return get_response(msg['Text'])
#     else:                                         #其他群聊直接忽略
#         pass
#
# itchat.auto_login(hotReload=True)
# itchat.run()