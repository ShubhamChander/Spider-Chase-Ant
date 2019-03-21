#Variables to be used
GRID = []
GRID_SIZE = 30
from random import randint
from BFSLogic import BFSLogic
from DFSLogic import DFSLogic
from AStar_Euclidean import AStar_Euclidean
from AStar_Manhattan import AStar_Manhattan
from AStar_FourDir import AStar_FourDir
from AStar_Average import AStar_Average

def ShowGrid():
	#To show the grid and the location of the spider and ant
	#print("In showGrid function")
	global GRID
	#print("The length of the grid is ",len(GRID))
	for i in range(len(GRID)):
		print(GRID[i])


def InitializeGrid():
	xRange = 16
	yRange = 16
	global GRID
	global GRID_SIZE
	GRID = [["" for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
	return 	

def SpawnSpider():
	global GRID_SIZE
	N = GRID_SIZE - 1
	spiderXY = []
	x = randint(0,N)
	y = randint(0,N)
	spiderXY = [x,y]
	return spiderXY
	
def SpawnAnt():
	global GRID_SIZE
	N = GRID_SIZE - 1
	antXY = []
	x = randint(0,N)
	y = randint(0,N)
	antXY = [x,y]
	return antXY

def moveSpider(currLoc,nextLoc):
	print("Current location of spider is ", currLoc)
	print("Next location of spider is ", nextLoc)
	global GRID
	GRID[currLoc[0]][currLoc[1]] = ""
	x = nextLoc[0]
	y = nextLoc[1]
	GRID[x][y]="S"
	
	return
	
def moveAnt(currLocAnt,nextLocAnt):
	print("Current location of Ant is ", currLocAnt)
	print("Next location of Ant is ", nextLocAnt)
	global GRID
	GRID[currLocAnt[0]][currLocAnt[1]] = ""
	x = nextLocAnt[0]
	y = nextLocAnt[1]
	GRID[x][y]="A"
	
	return

def determineDirAnt():
	return randint(0,7)

def generateAntNextMove(dir,currLoc):
	global GRID_SIZE
	N = GRID_SIZE - 1
	ANT_SPEED = 1
	nextMove = []
	x = currLoc[0]
	y = currLoc[1]
	if(dir== 0):
		if(((x-ANT_SPEED) <=N) and (x-ANT_SPEED) >= 0):
			nextMove = [x-ANT_SPEED,y]	
		else: 
			nextMove = SpawnAnt()
			dir = determineDirAnt()
	elif(dir == 1):
		if(((x+ANT_SPEED) <=N) and (x+ANT_SPEED) >= 0):
			nextMove = [x+ANT_SPEED,y] 
		else: 
			nextMove = SpawnAnt()
			dir = determineDirAnt()
	elif(dir==2):
		if(((y-ANT_SPEED) <=N) and (y-ANT_SPEED) >= 0):
			nextMove = [x,y-ANT_SPEED] 
		else: 
			nextMove = SpawnAnt()
			dir = determineDirAnt()
	elif(dir == 3):
		if(((y+ANT_SPEED) <=N) and (y+ANT_SPEED) >= 0):
			nextMove = [x,y+ANT_SPEED] 
		else: 
			nextMove = SpawnAnt()
			dir = determineDirAnt()
	elif(dir == 4):
		if(((x-ANT_SPEED) <= N and (x-ANT_SPEED) >= 0) and ((y+ANT_SPEED) <= N and (y+ANT_SPEED) >= 0)):
			nextMove = [x-ANT_SPEED,y+ANT_SPEED] 
		else: 
			nextMove = SpawnAnt()
			dir = determineDirAnt()
	elif(dir == 5):
		if(((x-ANT_SPEED) <= N and (x-ANT_SPEED) >= 0) and ((y-ANT_SPEED) <= N and (y-ANT_SPEED) >= 0)):
			nextMove = [x-ANT_SPEED,y-ANT_SPEED] 
		else: 
			nextMove = SpawnAnt()
			dir = determineDirAnt()
	elif(dir == 6):
		if(((x+ANT_SPEED) <= N and (x+ANT_SPEED) >= 0) and ((y-ANT_SPEED) <= N and (y-ANT_SPEED) >= 0)):
			nextMove = [x+ANT_SPEED,y-ANT_SPEED] 
		else: 
			nextMove = SpawnAnt()
			dir = determineDirAnt()
	elif(dir == 7):
		if(((x+ANT_SPEED) <= N and (x+ANT_SPEED) >= 0) and ((y+ANT_SPEED) <= N and (y+ANT_SPEED) >= 0)):
			nextMove = [x+ANT_SPEED,y+ANT_SPEED] 
		else: 
			nextMove = SpawnAnt()
			dir = determineDirAnt()
			
	return [nextMove,dir]


def main():
	global GRID
	BFS = BFSLogic()
	DFS = DFSLogic()
	AStarE = AStar_Euclidean()
	AStarM = AStar_Manhattan()
	AStarFour = AStar_FourDir()
	AStarAv = AStar_Average()
	#Initialize Grid
	InitializeGrid()
	##ShowGrid()
	
	#Intialize Player locations and show on Grid
	while True:
		spiderLocation = SpawnSpider()
		antLocation = SpawnAnt()
		if(spiderLocation != antLocation):
			break
	#print("Spider Location is ", spiderLocation)
	#print("Ant Location is ", antLocation)
	
	GRID[spiderLocation[0]][spiderLocation[1]] = "S"
	GRID[antLocation[0]][antLocation[1]] = "A"
	ShowGrid()
	
	#Apply BFS logic of Game here 
	###spiderLocationNext ====> will be determined by BFS logic 
	####spiderLocationNext= BFS.applyBFS(spiderLocation,antLocation)
	
	#Apply DFS logic of Game here
	####spiderLocationNext = DFS.applyDFS(spiderLocation,antLocation)
	####print("Spider's next location is ", spiderLocationNext[0])
	
	#Apply Euclidean logic of Game here
	###spiderLocationNext = AStarE.applyEuclideanLogic(spiderLocation,antLocation)
	#####print("Spider's next location is ", spiderLocationNext[0])
	
	#Apply Manhattan logic of Game here
	spiderLocationNext = AStarM.applyManhattanLogic(spiderLocation,antLocation)
	#####print("Spider's next location is ", spiderLocationNext[0])
	
	#Apply Four direction logic of Game here
	###spiderLocationNext = AStarFour.applyFourDir(spiderLocation,antLocation)
	#####print("Spider's next location is ", spiderLocationNext[0])
	
	
	#Apply Average of two heuristic logic of Game here
	
	antDir = determineDirAnt()
	
	# FOR BFS 
	'''
	while True:
		listMoveAndDir = generateAntNextMove(antDir,antLocation)
		antLocationNext = listMoveAndDir[0]
		antDir = listMoveAndDir[1]
		#print("The direction of the ant is ", antDir)
		#Move Spider from one tile to another
		moveSpider(spiderLocation,spiderLocationNext)
		spiderLocation = spiderLocationNext
		spiderLocationNext= BFS.applyBFS(spiderLocation,antLocation)
		#######spiderLocationNext= DFS.applyDFS(spiderLocation,antLocation)
		##BFS/DFS logic here spiderLocationNext = BFS/DFS
		#Move Ant from one tile to another
		moveAnt(antLocation, antLocationNext)
		antLocation = antLocationNext
		ShowGrid()
		if(spiderLocation == antLocation):
			print("=================GAME OVER========================")
			break
	'''
	
	'''
	#FOR DFS --- FIGURE THIS OUT LATER
	while True:
		listMoveAndDir = generateAntNextMove(antDir,antLocation)
		antLocationNext = listMoveAndDir[0]
		antDir = listMoveAndDir[1]
		#print("The direction of the ant is ", antDir)
		#Move Spider from one tile to another
		#i = len(spiderLocationNext)-2
		#while(i != 1):
			#print("The index value is ",i)
		moveSpider(spiderLocation,spiderLocationNext)#[i]
		spiderLocation = spiderLocationNext#[i]
		spiderLocationNext= DFS.applyDFS(spiderLocation,antLocation)
		moveAnt(antLocation, antLocationNext)
		antLocation = antLocationNext
		ShowGrid()
			#i-=1
			
		#######spiderLocationNext= BFS.applyBFS(spiderLocation,antLocation)
		#######spiderLocationNext= DFS.applyDFS(spiderLocation,antLocation)
		##BFS/DFS logic here spiderLocationNext = BFS/DFS
		#Move Ant from one tile to another
		####moveAnt(antLocation, antLocationNext)
		####antLocation = antLocationNext
		print("\n")
		#ShowGrid()
		if(spiderLocation == antLocation):
			print("=================GAME OVER========================")
			break
	'''
	
	'''
	#For first A* --- Euclidean
	while True:
		listMoveAndDir = generateAntNextMove(antDir,antLocation)
		antLocationNext = listMoveAndDir[0]
		antDir = listMoveAndDir[1]
		
		moveSpider(spiderLocation,spiderLocationNext)
		spiderLocation = spiderLocationNext
		spiderLocationNext= AStarE.applyEuclideanLogic(spiderLocation,antLocation)
	
		moveAnt(antLocation, antLocationNext)
		antLocation = antLocationNext
		ShowGrid()
		if(spiderLocation == antLocation):
			print("=================GAME OVER========================")
			break
	
	'''
	'''
	#For second A* --- Manhattan
	#import os
	#import time
	#clear = lambda: os.system('cls')
	
	while True:
		#clear()
		#time.sleep(0.1)
		listMoveAndDir = generateAntNextMove(antDir,antLocation)
		antLocationNext = listMoveAndDir[0]
		antDir = listMoveAndDir[1]
		
		moveSpider(spiderLocation,spiderLocationNext)
		spiderLocation = spiderLocationNext
		spiderLocationNext= AStarM.applyManhattanLogic(spiderLocation,antLocation)
	
		moveAnt(antLocation, antLocationNext)
		antLocation = antLocationNext
		ShowGrid()
		if(spiderLocation == antLocation):
			print("=================GAME OVER========================")
			break
			#Spawn spider and ant location here
	
	'''
	#For third A* ----- smallest x or y difference
	'''
	while True:
		listMoveAndDir = generateAntNextMove(antDir,antLocation)
		antLocationNext = listMoveAndDir[0]
		antDir = listMoveAndDir[1]
		
		moveSpider(spiderLocation,spiderLocationNext)
		spiderLocation = spiderLocationNext
		spiderLocationNext= AStarFour.applyFourDir(spiderLocation,antLocation)
	
		moveAnt(antLocation, antLocationNext)
		antLocation = antLocationNext
		ShowGrid()
		if(spiderLocation == antLocation):
			print("=================GAME OVER========================")
			break
	
	'''
	#For Average A* ------ average of first euclidean and manhattan
	
	while True:
		listMoveAndDir = generateAntNextMove(antDir,antLocation)
		antLocationNext = listMoveAndDir[0]
		antDir = listMoveAndDir[1]
		
		moveSpider(spiderLocation,spiderLocationNext)
		spiderLocation = spiderLocationNext
		spiderLocationNext= AStarAv.applyAverageLogic(spiderLocation,antLocation)
	
		moveAnt(antLocation, antLocationNext)
		antLocation = antLocationNext
		ShowGrid()
		if(spiderLocation == antLocation):
			print("=================GAME OVER========================")
			break
	
	
	
	
main()










