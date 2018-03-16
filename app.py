from wxpy import *

# start the bot machine 
# scan the QR code using mobile to login
# cache_path is set True so user don't have scan QR code every time
bot = Bot(cache_path=True,console_qr=2)

xiaoi = XiaoI('xiaoi key','xiaoi secret')

honey = bot.friends().search('Honey')[0]
family_group1 = bot.groups().search('一家人')[0]
mother = family_group1.search('母上')[0]
family_group2 = bot.groups().search('茄宝宝由我们来罩')[0]
jiqizhixin_mp = bot.mps().search('机器之心')[0]


@bot.register(family_group1)
def forward_mother_message(msg):
	if msg.member == mother:
		msg.forward(bot.file_helper,prefix='母上发言')

@bot.register(family_group2)
def forward_mother_message(msg):
	if msg.member == honey:
		msg.forward(bot.file_helper,prefix='老婆发言')

# send messge
def send_message(msg):
	bot.file_helper.send(msg)

# respond to messages
@bot.register()
def print_others(msg):
	print(msg)

@bot.register(honey)
def print_honey(msg):
	print('From Honey:', msg.text)
	xiaoi.do_reply(msg)
	# return "I am busy now, call me if it's emergency. Love you."

# # 自动接受新的好友请求
# @bot.register(msg_types=FRIENDS)
# def auto_accept_friends(msg):
#     # 接受好友请求
#     new_friend = msg.card.accept()
#     # 向新的好友发送消息
#     new_friend.send('哈哈，我自动接受了你的好友请求')

# keep app running
embed()