# Hanoi.py
# A tower of Hanoi game
# By... YOU?
import os

# The biggest game size we'll allow. 
# Because '10' will take up more space in printDisk
maxGameSize = 9

# The biggest disk's size. We use this to choose
# how big to draw each item.
gameSize = -1

# These are the arrays for our pins.
# We'll add disks to the first one after we get the game size.
columns = [[],[],[]]

# This is how many turns we've done. Zero at first!
turn = 0

# This is a message we'll print if the user needs to be told something.
message = ''

# We'll keep playing until this is 0
playing = 1


#
# This gives us blank spaces
#
def spaces(size):
	result = ''
	for i in range(0,size):
		result = result + ' '
	return result


#
# This clears the screen. It will work on different computer types, too.
#
def cls():
	if os.name == 'posix':
		os.system('clear')
	else:
		os.system('cls')

# print a disk to the screen, of the right 'size'. 
# If size is 0, then there's no disk, just the pin.
# The disk is:
# "    [    4    ]    "
# "aaaabccccdcccceaaaa"
# where
#  a is outerspace
#  b is [ or blank
#  c is innerspace
#  d is a number, or |
#  e is ] or blank
def getDisk(size):
	left = '['
	right = ']'
	middle = str(size)						# get 'size' as text
	innerspace = spaces(size - 1) 			# spaces inside the disk
	outerspace = spaces(gameSize - size) 	# spaces outside the disk
	if size == 0:
		left = ''
		right = ''
		innerspace = spaces(gameSize)
		middle = '|'
		outerspace = ''
	
	return outerspace + left + innerspace + middle + innerspace + right + outerspace


#
# This prints a base for the game, which is the right size.
#
def getBase():
	sp = spaces(gameSize)
	sp2 = sp + sp
	return '[' + sp + 'A' + sp2 + 'B' + sp2 + 'C' + sp + ']'


#
# This prints all the disks represented by the 'columns' arrays
#
def printDisks():
	global columns
	for r in range(0, gameSize + 1):
		rowText = ' '
		rowsRemaining = gameSize + 1 - r
		for c in range(0, 3):
			# how many disks are there in this column?
			disks = len(columns[c])
			# is there no disk at this row?
			if (rowsRemaining > disks):
				rowText = rowText + getDisk(0)
				continue
			# which disk do we use?
			d = disks - rowsRemaining
			# add it
			rowText = rowText + getDisk(columns[c][d])
		print rowText


#
# This does keyboard commands that aren't moves
#
def doCommand(command):
	global message
	global playing
	if command == 'h':
		# You could add this later
		message = 'I don\'t know how to do hints yet!'
	elif command == 'q':
		print 'Bye!'
		playing = 0
	elif command == '?':
		message = getInstructions()
	else:
		message = 'That doesn\'t seem right.'


#
# This moves a disk from one column to another, if possible.
#
def doMove(fromCol, toCol):
	global columns
	global message
	global turn
	# get the difference between what they typed and 'a', giving us 0, 1 or 2
	iFrom = ord(fromCol) - ord('a')
	iTo = ord(toCol) - ord('a')
	# is there a disk in the From position?
	if len(columns[iFrom]) == 0:
		message = 'There is no disk at ' + fromCol.upper() + '!'
		return

	# is there a disk in the To position?
	if len(columns[iTo]) > 0:
		# then, if it's smaller than the From disk, we can't do this!
		sizeFrom = columns[iFrom][0] 
		sizeTo = columns[iTo][0]
		if sizeTo < sizeFrom:
			message = 'You cannot put a bigger disk onto a smaller disk!'
			return

	# move the disk
	disk = columns[iFrom][0]		# get it
	del columns[iFrom][0]			# delete it from the From list
	columns[iTo].insert(0, disk)	# insert it on top of the To list
	turn += 1


#
# This moves from the location the user entered, 
# and asks them where to move to
#
def doMoveFrom(command):
	global message
	print 'Move to? ',
	to = raw_input().lower()
	if to == command:
		message = 'Moved ' + command + ' to ' + to + ': Nothing to do!'
	elif to == 'a' or to == 'b' or to == 'c':
		doMove(command, to)
	else:
		doCommand(to)


#
# This prints the name of your game and your name
#
def printTitle():
	print 'TOWER OF HANOI v1.0'
	print 'by YOUR NAME GOES HERE'


#
# This asks the user for their next move, or command.
#
def doInput():
	print 'Your move? ',
	command = raw_input().lower()
	if command == 'a' or command == 'b' or command == 'c':
		doMoveFrom(command)
	else:
		doCommand(command)


#
# working out if we've won is really easy. Just check that
# column A is empty, and either column B or C is empty. If
# so, then the user moved everything to the third column!
#
def checkWon():
	global playing
	if len(columns[0]) != 0:
		return

	if len(columns[1]) == 0 or len(columns[2]) == 0:
		print 'Congratulations!'
		print 'You completed the Tower of Hanoi level', gameSize, 'in', turn, 'moves !!!'
		playing = 0


#
# Show the user how many moves they've made
#
def printTurn():
	if turn == 0:
		return

	print
	print 'You\'ve had', turn, 'moves.'
	print 


#
# This is what prints out the main game page, before asking for user input.
#
def printGame():
	global message
	cls()
	printTitle()
	printTurn()
	printDisks()
	print getBase()
	checkWon()
	print
	if message:
		print message + '\n'		


#
# These instructions will be helpful to new users!
#
def getInstructions():
	message = 'Type a command and press Enter.\n'
	message += 'To choose where to move from, press A, B or C.\n'
	message += 'To get a hint, press H.\n'
	message += 'To quit, press Q.\n'
	message += 'To see this help, press ?'
	return message


#
# Ask the user how big their tower should be. Big towers take a long time to play!!!
#
def getGameSize():
	global gameSize
	print 'How big do you want the game to be?'

	# Get a valid value
	while gameSize == -1:
		print 'Enter a number from 2 to 9:',
		entered = raw_input().lower()

		# They may want to quit, right now.
		if entered == 'q':
			playing = 0
			break

		# was it a numeric value?
		try:
			value = int(entered)
			# was it between 2 and 9?
			if value >= 2 and value <= 9:
				gameSize = value
				# add the disks to the first pin
				for d in range(0, gameSize):
					columns[0].append(d + 1)
		except TypeError:
			# it wasn't a number. Try again.
			gameSize = -1


#
# Start of the game. First, show the title and some instructions,
#
printTitle()
print
print getInstructions()
print

#
# Then ask how big the game should be
#
getGameSize()

#
# Now play - until the player wins or quits.
#
while (playing != 0):
	printGame()
	doInput()

### THE END ###