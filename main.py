import os
from os import sys
import samino
from time import sleep
from os import path
import pyfiglet
from colored import fore, back, style, attr
attr(0)
print(fore.GREEN + style.BOLD)
print(pyfiglet.figlet_format(" marshal", font="digital"))
print(pyfiglet.figlet_format("CoHost Spam", font="small"))
f='━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'
client = samino.Client()
e="k4puzx75@1secmail.org"
p="223344"
client.login(e,p)
print("\nLogin Successfully")
print(f)
#keep_alive()
client.headers
HostChatLink="http://aminoapps.com/p/uuszxa"
config_chat = client.get_from_link(HostChatLink).json #You have  host on chat
thread_id = config_chat["linkInfo"]["objectId"]
ndc_id = config_chat["linkInfo"]["ndcId"]
local = samino.Local(comId = ndc_id)
targetlink="http://aminoapps.com/p/wqql68"
remove = client.get_from_link(str(targetlink)).objectId
while True:
	print("boomm.......")
	try:
		local.remove_host(chatId=thread_id, userId=remove)
	except:
		pass
