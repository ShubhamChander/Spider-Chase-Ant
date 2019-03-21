'''
This is an Spider Game with Artificial Intellgence Logic

Objective of the game is for the spider to eat the ant

'''
from random import randint
import queue 
from Stack import Stack
#import pygame


GRID = []


def InitPlayerLoc():
	#currLocSpiderXandY = []
	#currLocAntXandY = []
	loc = {'Spider_X' : 0, 'Spider_Y': 0, 'Ant_X' : 0, 'Ant_Y': 0}
	
	loc['Spider_X'] = randint(0,15)
	loc['Spider_Y'] = randint(0,15)
	
	while(True):
		loc['Ant_X'] = randint(0,15)
		loc['Ant_Y'] = randint(0,15)
		
		if(loc['Spider_X'] != loc['Ant_X'] and loc['Spider_Y'] != loc['Ant_Y']):
			break

	return loc
		
	
	
	

def ShowGrid():
	#To show the grid and the location of the spider and ant
	print("In showGrid function")
	global GRID
	print(len(GRID))
	for i in range(len(GRID)):
		print(GRID[i])


def generateSpiderMoves(x,y):
	#Generate options for spider
	#NOTE: Vertical axis is x-axis, and Horizontal axis is y-axis
	#Keep in minds the boundary of 16 and 16
	listOfoptions = []
	#print("x,y is ", x ," and ", y)
	
	#O1. two forward then right ======> x-2,y+1
	if(((x-2) <= 15 and (x-2) >= 0) and ((y+1) <= 15 and (y+1) >= 0)):
		listOfoptions.append([x-2,y+1])
		#g[x-2][y+1] = "1"
	#else:
	#	print("1 not possible")
	
	#O2. two forward then left ========> x-2,y-1
	if(((x-2) <= 15 and (x-2) >= 0) and ((y-1) <= 15) and (y-1) >= 0):
		listOfoptions.append([x-2,y-1])
		#g[x-2][y-1] = "2"
	#else:
	#	print("2 not possible")
	
	#O3. one forward then two right ========> x-1,y+2
	if(((x-1) <=15 and (x-1) >= 0) and ((y+2) <=15) and (y+2) >= 0):
		listOfoptions.append([x-1,y+2])
		#g[x-1][y+2] = "3"
	#else:
	#	print("3 not possible")
		
	#O4. one forward then two left =======> x-1, y-2
	if(((x-1) <=15 and (x-1) >= 0) and ((y-2) <=15) and (y-2) >= 0):
		listOfoptions.append([x-1,y-2])
		#g[x-1][y-2] = "4"
	#else:
	#	print("4 not possible")
	
	#O5. one left ======= > x,y-1
	if(((y-1) <=15) and (y-1) >= 0):
		listOfoptions.append([x,y-1])
		#g[x][y-1] = "5"
	#else:
	#	print("5 not possible")
	
	#O6. one right ======== > x y+1
	if(((y+1) <=15) and (y+1) >= 0):
		listOfoptions.append([x,y+1])
		#g[x][y+1] = "6"
	#else:
	#	print("6 not possible")
	
	#O7. one down =========== > x+1, y
	if(((x+1) <=15) and (x+1) >= 0):
		listOfoptions.append([x+1,y])
		#g[x+1][y] = "7"
	#else:
	#	print("7 not possible")
	#O8. one diagonal down leftside =====> x+1, y-1
	if(((x+1) <=15 and (x+1) >= 0) and ((y-1) <=15) and (y-1) >= 0):
		listOfoptions.append([x+1,y-1])
		#g[x+1][y-1] = "8"
	#else:
	#	print("8 not possible")
	
	#O9. one diagonal down rightside ======> x+1,y+1
	if(((x+1) <=15 and (x+1) >= 0) and ((y+1) <=15) and (y+1) >= 0):
		listOfoptions.append([x+1,y+1])
		#g[x+1][y+1] = "9"
	#else:
	#	print("9 not possible")
	
	#ShowGrid(g)
	#print("List of move options for spider is ", listOfoptions)
	return listOfoptions
	
	
def generateAntMoves(x,y,dir):
	#NOTE: Vertical axis is x-axis, and Horizontal axis is y-axis
	#Keep in minds the boundary of 16 and 16
	if(dir == "None"):
		direction = randint(0,7)
		if(direction == 0 or dir =="North"):
			print("North")
			#dir = "North"
			# x-1
			if(((x-1) <=15) and (x-1) >= 0):
				GRID[x-1][y] = "A0"
				
		elif(direction == 1 or dir =="South"):
			print("South")
			#dir = "South"
			# x+1
			if(((x+1) <=15) and (x+1) >= 0):
				GRID[x+1][y] = "A1"
		
		elif(direction == 2 or dir == "West"):
			print("West")
			#dir = "West"
			#y-1
			if(((y-1) <=15) and (y-1) >= 0):
				GRID[x][y-1] = "A2"
		elif(direction == 3):
			print("East")
			# y+1
			if(((y+1) <=15) and (y+1) >= 0):
				GRID[x][y+1] = "A3"
		elif(direction == 4):
			print("north east")
			#x-1,y+1
			if(((x-1) <= 15 and (x-1) >= 0) and ((y+1) <= 15 and (y+1) >= 0)):
				GRID[x-1][y+1] = "A4"
		elif(direction == 5):
			print("north west")
			#x-1,y-1
			if(((x-1) <= 15 and (x-1) >= 0) and ((y-1) <= 15 and (y-1) >= 0)):
				GRID[x-1][y-1] = "A5"
		elif(direction == 6):
			print("south west")
			#x+1,y-1
			if(((x+1) <= 15 and (x+1) >= 0) and ((y-1) <= 15 and (y-1) >= 0)):
				GRID[x+1][y-1] = "A6"
		elif(direction == 7):
			print("south east")
			#x+1,y+1
			if(((x+1) <= 15 and (x+1) >= 0) and ((y+1) <= 15 and (y+1) >= 0)):
				GRID[x+1][y+1] = "A7"
			
		return [direction]
	return[dir]
	
#visistedPath = []
def determinePath(goal,start,key,dict):
	global visistedPath
	print("In determinePath function")
	path = []
	print("Start state =====> ", start)
	print("Goal state =====> ", goal)
	#print("Production sys =====> ", dict)
	 
	#Removing root node to prevent any loops 
	for ke in dict:
		if(start in dict[ke]):
			(dict[ke]).remove(start)
		
	#use key list as k=value for dict, not the string key in dict itself
	i = (len(key))-1
	path.append(goal)
	while(i != -1):
		v = key[i]
		val = str(v[0]) + ", " + str(v[1])
		if(goal in dict[val]):
			path.append(v)
			goal = v
			
		i-=1	
	print("The path from goal to start is ", path)	
	goTo = len(path)-2
	return path[goTo]

	
def applyBFSLogic(spiderLoc,AntLoc):
	#generate spider possible moves and ant possible moves
	#For ant possible move, use generate direction ones and keep on that direction until boundary is reached
	#then use generate direction again if needed 
	visited = []
	visitedPath = []
	#pathToGoal = []
	parentChildDict={}
	q = queue.Queue()
	q.put(spiderLoc)
	#print(q.get())
	#child = []
	startLoc = spiderLoc
	key = []
	
	while((not q.empty())):
		v = q.get()
		spiderLoc = [v[0],v[1]]
		#print("Testing location ", spiderLoc, " for Ant")
		if(spiderLoc == AntLoc):
			#print("Spider has found the Ant in this moment in time")
			#print("Ant found at location ", spiderLoc)
			break
		possMoves = generateSpiderMoves(v[0],v[1])
		#send v and possMoves to function that keeps track of parent and child
		val = str(v[0]) + ", " + str(v[1])
		#parentChildDict[val] = possMoves
		key.append(spiderLoc)
		#child.clear()
		for i in range(len(possMoves)):
			#print("possible moves for spider at pos ", v," are ", possMoves[i])
					
			if(possMoves[i] not in visited):
				q.put(possMoves[i])
				visited.append(possMoves[i])
				visitedPath.append(possMoves[i])
				parentChildDict[val] = visitedPath
		
		print("visited Path is ", visitedPath)
		visitedPath.clear()
	
		#for key1 in parentChildDict:
		#	print(key1 + " children are ", parentChildDict[key1])
		
	print("spider location =====> ", spiderLoc)
	print("ant location ========> ", AntLoc)
	
	#send spiderLoc and parentChildDict to function that determines path for spider to take
	TileToGo = determinePath(spiderLoc,startLoc,key,parentChildDict)
	return TileToGo
	
	
	
'''	
def applyDFSLogic(g,spiderLoc,AntLoc):
	#generate spider possible moves and ant possible moves
	print("In Depth-First Search logic")
	stack = Stack()
	visited = []
	stack.push(spiderLoc)
	parentChildDict = {}
	key=[]
	startLoc = spiderLoc
	while(not stack.isEmpty()):
		v = stack.pop()
		spiderLoc = [v[0],v[1]]
		
		if(spiderLoc == AntLoc):
			print("Spider has found the ant")
			stack.push(possMoves[i])
			visited.append(possMoves[i])
			break
		possMoves = generateSpiderMoves(g,v[0],v[1])
		val = str(v[0]) + ", " + str(v[1])
		parentChildDict[val] = possMoves
		key.append(spiderLoc)
		for i in range(len(possMoves)):
			print("Possible moves for spider at pos ", v, " are ", possMoves[i])
			
			if(possMoves[i] not in visited):
				stack.push(possMoves[i])
				visited.append(possMoves[i])
				
	
	#while(not stack.isEmpty()):
	#	print("Stack element are ", stack.pop())
	
	print("spider location =====> ", spiderLoc)
	print("ant location ========> ", AntLoc)
	
	#send spiderLoc and parentChildDict to function that determines path for spider to take
	TileToGo = determinePath(spiderLoc,startLoc,key,parentChildDict)
	print(TileToGo)
	
'''	

def moveSpider(currLoc,nextLoc):
	print("Current location of spider is ", currLoc)
	print("Next location of spider is ", nextLoc)
	
	GRID[currLoc[0]][currLoc[1]] = "S"
	#g[nextLoc[0]][nextLoc[1]] = "S"
	#for i in range(len(nextLoc)):
	x = nextLoc[0]#[0]
	y = nextLoc[1]#[1]
	GRID[x][y]="S"
	
	return

def moveAnt(currLoc,direction):
	global GRID
	GRID[currLoc[0]][currLoc[1]] = ""
	x = currLoc[0]
	y = currLoc[1]
	newLoc = []
	if((x or y ==15) or (x or y == 0)):
		return currLoc
	if(direction == 0):
		print("North")
		#dir = "North"
		#if(((x-1) <=15) and (x-1) >= 0):
		GRID[x-1][y] = "A"
		newLoc = [x-1,y]
			
	elif(direction == 1):
		print("South")
		#dir = "South"
		# x+1
		#if(((x+1) <=15) and (x+1) >= 0):
		GRID[x+1][y] = "A"
		newLoc = [x+1,y]
	
	elif(direction == 2):
		print("West")
		#dir = "West"
		#y-1
		#if(((y-1) <=15) and (y-1) >= 0):
		GRID[x][y-1] = "A"
		newLoc = [x,y-1]
	elif(direction == 3):
		#print("East")
		# y+1
		#if(((y+1) <=15) and (y+1) >= 0):
		GRID[x][y+1] = "A"
		newLoc = [x,y+1]
	elif(direction == 4):
		print("north east")
		#x-1,y+1
		#if(((x-1) <= 15 and (x-1) >= 0) and ((y+1) <= 15 and (y+1) >= 0)):
		GRID[x-1][y+1] = "A"
		newLoc = [x-1,y+1]
	elif(direction == 5):
		print("north west")
		#x-1,y-1
		#if(((x-1) <= 15 and (x-1) >= 0) and ((y-1) <= 15 and (y-1) >= 0)):
		GRID[x-1][y-1] = "A"
		newLoc = [x-1,y-1]
	elif(direction == 6):
		print("south west")
		#x+1,y-1
		#if(((x+1) <= 15 and (x+1) >= 0) and ((y-1) <= 15 and (y-1) >= 0)):
		GRID[x+1][y-1] = "A"
		newLoc = [x+1,y-1]
	elif(direction == 7):
		print("south east")
		#x+1,y+1
		#if(((x+1) <= 15 and (x+1) >= 0) and ((y+1) <= 15 and (y+1) >= 0)):
		GRID[x+1][y+1] = "A"
		newLoc = [x+1,y+1]
		
	return newLoc

def InitializeGrid():
	xRange = 16
	yRange = 16
	global GRID 
	GRID = [["" for x in range(xRange)] for y in range(yRange)]
	##ShowGrid()
	#grid = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
	# NOTE: Vertical axis(grid[0]) is xRange, and Horizontal axis(grid[1]) is yRange

	#for y in range(len(grid)):
	#	for u in range(xRange):
	#		grid[y].append(" ")
		#print("\n")
	return 	

# Game starts here
def main():
	#First: Initialize grid and show initial grid
	global GRID
	InitializeGrid()
	#Second: Initialize the players location randomly on the grid
	locDir = InitPlayerLoc()
	dir = "None"
	print("Spider location is " + str(locDir['Spider_X']) + " , " + str(locDir['Spider_Y']))
	print("Ant location is " + str(locDir['Ant_X']) + " , " + str(locDir['Ant_Y']))
	visistedPath = []
	
	#Spider start location. This should be random
	GRID[locDir['Spider_X']][locDir['Spider_Y']] = "S"
	#Ant start location. This should be random
	GRID[locDir['Ant_X']][locDir['Ant_Y']] = "A"
	
	ShowGrid()
	
	#generateSpiderMoves
	#grid = generateSpiderMoves(grid,locDir['Spider_X'],locDir['Spider_Y'])
	
	#generateAntMoves
	#Still need to work on respawning the ant if goes off board
	listGrid_AntDir = generateAntMoves(locDir['Ant_X'], locDir['Ant_Y'],dir)
	#grid=listGrid_AntDir[0]
	dir = listGrid_AntDir[0]
	#print("\n")
	ShowGrid()
	print("\n")
	listStartSpider = [locDir['Spider_X'],locDir['Spider_Y']]
	listStartAnt    = [locDir['Ant_X'], locDir['Ant_Y']]
	
	
	while True:
		TileToGo = applyBFSLogic(listStartSpider,listStartAnt)
		print("TileToGo is ", TileToGo)
		while True:
			if(TileToGo not in visistedPath):
				visistedPath.append(TileToGo)
				break
			else:
				TileToGo = applyBFSLogic(listStartSpider,listStartAnt)
			
		#send current location of spider and TileToGo location to move spider
		moveSpider(listStartSpider,TileToGo)
		listStartSpider = [TileToGo[0],TileToGo[1]]
		#listStartAnt= generateAntMoves(listStartAnt[0],listStartAnt[1],dir)
		####listStartAnt = moveAnt(listStartAnt,dir)
		dist_X = abs(listStartSpider[0] - listStartAnt[0])
		dist_Y = abs(listStartSpider[1] - listStartAnt[1])
		if(dist_X <= 1 and dist_Y <=1):
			ShowGrid()
			return
		print("\n")
		ShowGrid()
	
	
	#applyDFSLogic(grid,listStartSpider,listStartAnt)
	
	
	
#FIX LOOPING BUG WHERE S IS SWITHCING TILES: GOING ONE TILE TO NEXT AND THEN BACK later
	
	
	
	
main()