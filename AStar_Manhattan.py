from BFSLogic import BFSLogic
import math

class AStar_Manhattan():
	BFS = BFSLogic()
	
	
	def calcFValue(gValue, HValue):
		#print("gValue is ", gValue)
		#print("HValue is ", HValue)
		return gValue + HValue
	
	
	def calcHValue(spiderLocCurr, antLoc):
		#print("spiderLocCurr is ", spiderLocCurr)
		x1 = spiderLocCurr[0]
		y1 = spiderLocCurr[1]
		
		x2 = antLoc[0]
		y2 = antLoc[1]
		
		HValue = abs(x1-x2) + abs(y1-y2)
		return HValue
		
	
	def applyManhattanLogic(self,spiderLoc,antLoc):
		
		#print("Spider Location is ", spiderLoc)
		#print("Ant Location is ", antLoc)
		
		path = []
		AllHeuristicValues = []
		tempHeuristicValue = []
		
		#AllHeuristicValues.append([spiderLoc,0])
		path.append([spiderLoc,0])
		
		testValue = spiderLoc
		depth = 1
		while True:
			#Generate possible Moves
			possMoves = BFSLogic.generatePossMove(testValue)
			#print("Depth is ", depth)
			for i in range(len(possMoves)):
				succ = possMoves[i]
				ManhattanDist_H = AStar_Manhattan.calcHValue(succ,antLoc)
				#print("The depth used is ", depth)
				FValue = AStar_Manhattan.calcFValue(depth,ManhattanDist_H)
				AllHeuristicValues.append([succ,FValue])
				tempHeuristicValue.append([succ,FValue])
			
			#print("From point ", testValue, "possible moves are ", tempHeuristicValue)
			depth+=1
			smallF = tempHeuristicValue[0][1]
			#print("Smallf F is ", smallF)
			nextCoor = tempHeuristicValue[0][0]
			for j in range(len(tempHeuristicValue)):
				if(smallF > tempHeuristicValue[j][1]):
					smallF = tempHeuristicValue[j][1]
					nextCoor = tempHeuristicValue[j][0]
			
			#AllHeuristicValues.remove([nextCoor,smallF])
			
			'''
			for k in range(len(AllHeuristicValues)):
				if(nextCoor in AllHeuristicValues[k]):
					#print("\n")
					print("Another one found")
					#print("\n")
			'''		
			if(nextCoor == antLoc):
				path.append([nextCoor,smallF])
				break
			path.append([nextCoor,smallF])
					
			#print("The smallest F value is ", smallF)
			#print("The nextCoor is ", nextCoor)
			#print("Path is  ", path)
			#print("\n")
			tempHeuristicValue.clear()
			testValue = nextCoor
			
			
		#print("Path is  ", path)
		#print("The next coordinate to go to is ", path[1])
		return path[1][0]
