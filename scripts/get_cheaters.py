"""
Lists all users who have made multiple accounts from same IP address
"""

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
	sys.path.append(BASE_DIR)

if __name__=="__main__":
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'checkmate.settings')
	print("Setting up Django...")
	import django
	django.setup()

from main.models import Player
import json
from pprint import pprint

def get_cheaters():
	players = list(Player.objects.order_by('ip_address').values_list('ip_address','user__username','score'))
	if len(players)<=1:
		return []
	cheaters = []
	ip_index=0
	if players[0][ip_index]==players[1][ip_index]:
		cheaters.append(players[0])
	for i in range(1,len(players)-1):
		if players[i-1][ip_index]==players[i][ip_index] or players[i+1][ip_index]==players[i][ip_index]:
			cheaters.append(players[i])
	if players[-1][ip_index]==players[-2][ip_index]:
		cheaters.append(players[-1])
	return cheaters

if __name__=="__main__":
#	print(json.dumps(get_cheaters(),indent=2))
	pprint(get_cheaters())
