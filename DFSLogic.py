from BFSLogic import BFSLogic
from Stack import Stack

class DFSLogic():
	
	
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
		print("The path from goal to start is ", path)	
		return path[len(path)-2]
	
	
	
	def applyDFS(self,spiderLoc,antLoc):
		BFS = BFSLogic()
		#print("In depth first search logic")
		#print("DFS LOGIC HAS RECIEVED ", spiderLoc)
		
		stack = Stack()
		visited = []
		treeKey = []
		treeDict = {}
		
		
		stack.push(spiderLoc)
		visited.append(spiderLoc)
		
		while(not stack.isEmpty()):
			v = stack.pop()
			if(v == antLoc):
				#print("Ant has been located at ", v)
				break
			possMoves = BFSLogic.generatePossMove(v)
			val = str(v[0]) +", " +str(v[1])
			treeKey.append(v)
			treeDict[val] = []
			
			for i in range(len(possMoves)):
				if(possMoves[i] not in visited):
					visited.append(possMoves[i])
					stack.push(possMoves[i])
					treeDict[val].append(possMoves[i])
					
		#for k in treeDict:
		#	print(k, "for DFS =======>", treeDict[k])

		TileToGo = DFSLogic.determinePath(treeDict,treeKey,spiderLoc,antLoc)
		return TileToGo
			
			
		
		