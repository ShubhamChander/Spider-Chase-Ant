from BFSLogic import BFSLogic
from AStar_Euclidean import AStar_Euclidean
from AStar_Manhattan import AStar_Manhattan

import math

class AStar_Average():
	BFS = BFSLogic()
	AStarE = AStar_Euclidean()
	AStarM = AStar_Manhattan()
	
	
	def calcFValue(gValue, HValue):
		#print("gValue is ", gValue)
		#print("HValue is ", HValue)
		return gValue + HValue
	
	def applyAverageLogic(self,spiderLoc,antLoc):

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
				
				#Euclidean distance 
				EuclideanDist_H = AStar_Euclidean.calcHValue(succ,antLoc)
				#print("The depth used is ", depth)
				FValueE = AStar_Euclidean.calcFValue(depth,EuclideanDist_H)
				
				#Manhattan distance
				ManhattanDist_H = AStar_Manhattan.calcHValue(succ,antLoc)
				#print("The depth used is ", depth)
				FValueM = AStar_Manhattan.calcFValue(depth,ManhattanDist_H)
				
				FValue = (FValueE + FValueM) / 2
				
				AllHeuristicValues.append([succ,FValue])
				tempHeuristicValue.append([succ,FValue])
			
			#print("From point ", testValue, "possible moves are ", tempHeuristicValue)
			depth+=1
			smallF = tempHeuristicValue[0][1]
			nextCoor = tempHeuristicValue[0][0]
			for j in range(len(tempHeuristicValue)):
				if(smallF > tempHeuristicValue[j][1]):
					smallF = tempHeuristicValue[j][1]
					nextCoor = tempHeuristicValue[j][0]
			
			AllHeuristicValues.remove([nextCoor,smallF])
			
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
		
