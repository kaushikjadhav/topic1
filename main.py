import os
import random
## Number of days you want to make commits
for i in range(1,365*2 + 1):
	gap = random.randint(1,4)
	d = str(i) + str(gap) + ' day ago'
	## Open a text file and modify it
	with open('bot.txt', 'a') as file:
		file.write(d)
		## Add bot.txt to staging area
	os.system('git add bot.txt')
	## Commit it
	os.system('git commit --date="' + d + '" -m "first commit"')

## push the commit to github
os.system('git push -u origin master')