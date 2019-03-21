
import queue

class BFSLogic():

	def generatePossMove(coorSpider):
		x = coorSpider[0]
		y = coorSpider[1]
		listOfoptions = []
		#Actual grid size -1
		GRID_SIZE = 29

		#O1. two forward then right ======> x-2,y+1
		if(((x-2) <= GRID_SIZE and (x-2) >= 0) and ((y+1) <= GRID_SIZE and (y+1) >= 0)):
			listOfoptions.append([x-2,y+1])
			
		#O2. two forward then left ========> x-2,y-1
		if(((x-2) <= GRID_SIZE and (x-2) >= 0) and ((y-1) <= GRID_SIZE) and (y-1) >= 0):
			listOfoptions.append([x-2,y-1])
			
		#O3. one forward then two right ========> x-1,y+2
		if(((x-1) <=GRID_SIZE and (x-1) >= 0) and ((y+2) <=GRID_SIZE) and (y+2) >= 0):
			listOfoptions.append([x-1,y+2])

		#O4. one forward then two left =======> x-1, y-2
		if(((x-1) <=GRID_SIZE and (x-1) >= 0) and ((y-2) <=GRID_SIZE) and (y-2) >= 0):
			listOfoptions.append([x-1,y-2])
	
		#O5. one left ======= > x,y-1
		if(((y-1) <=GRID_SIZE) and (y-1) >= 0):
			listOfoptions.append([x,y-1])
	
		#O6. one right ======== > x y+1
		if(((y+1) <=GRID_SIZE) and (y+1) >= 0):
			listOfoptions.append([x,y+1])
		
		#O7. one down =========== > x+1, y
		if(((x+1) <=GRID_SIZE) and (x+1) >= 0):
			listOfoptions.append([x+1,y])
		
		#O8. one diagonal down leftside =====> x+1, y-1
		if(((x+1) <=GRID_SIZE and (x+1) >= 0) and ((y-1) <=GRID_SIZE) and (y-1) >= 0):
			listOfoptions.append([x+1,y-1])
	
	
		#O9. one diagonal down rightside ======> x+1,y+1
		if(((x+1) <=GRID_SIZE and (x+1) >= 0) and ((y+1) <=GRID_SIZE) and (y+1) >= 0):
			listOfoptions.append([x+1,y+1])
			
		return listOfoptions
		
		
	def determinePath(dict,key,start,goal):
		#print("Spider start location in determinePath  is ", start)
		#print("Ant start location in determinePath is ", goal)
		path = []
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
		#print("The path from goal to start is ", path)	
		return path[len(path)-2]
		
	

	def applyBFS(self,spiderLoc,antLoc):
		#print("Spider start location in BFS logic  is ", spiderLoc)
		#print("Ant start location in BFS logic  is ", antLoc)
		
		treeDict = {}
		treeKey = []
		q = queue.Queue()
		visited = []
		visitedPath = []
		#visitedPath2 = []
		
		q.put(spiderLoc)
		visited.append(spiderLoc)
		
		while(not q.empty()):
			v = q.get()
			if(v == antLoc):
				print("Ant has been located at ", v)
				break
			possMoves = BFSLogic.generatePossMove(v)
			#print("PossMoves at ", v , " are ", possMoves)
			
			#### THIS CODE IS FOR CREATING THE TREE IN DICTIONARY FORM
			val = str(v[0]) +", " +str(v[1])
			treeKey.append(v)
			treeDict[val] = []
			
			for i in range(len(possMoves)):
				if(possMoves[i] not in visited):
					visited.append(possMoves[i])
					q.put(possMoves[i])
					visitedPath.append(possMoves[i])
					treeDict[val].append(possMoves[i])
			
			visitedPath.clear()
			
		#for k in treeDict:
		#	print(k, "=======>", treeDict[k])
		
		TileToGo = BFSLogic.determinePath(treeDict,treeKey,spiderLoc,antLoc)
		return TileToGo
			
			
			
			
			
		
	