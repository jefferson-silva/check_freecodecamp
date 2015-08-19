'''
Description: Script to check if FreeCodeCamp.com is online.
Author: Jefferson Silva (github.com/jefferson-silva)
'''

if __name__ == "__main__":
	import sys
	import time
	import requests

	# time in seconds to wait before requests
	wait = 30

	while True:
		try:
			fcc = requests.get("http://www.freecodecamp.com")

			if fcc.status_code == 200:
				print("FreeCodeCamp is live now!")
				sys.exit()

		except Exception:
			print("FreeCodeCamp is still offline.\nWaiting {} seconds...\n".format(wait))
			time.sleep(wait)
