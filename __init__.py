# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#strarr="[\"1:[5]\", \"4:[5]\", \"3:[5]\", \"5:[1,4,3,2]\", \"2:[5,15,7]\", \"7:[2,8]\", \"8:[7,38]\", \"15:[2]\", \"38:[8]\"]"
strarr=input()
createdict={}
sorteddict={}
count=0
outputarr=[]
# create dictionaty from string
def create_dict(i,createdict):
    strarr=i.split(":")
    createdict[int(strarr[0])] = strarr[1]
    
def trimUnnecessary(strlst):   
   # trim unnecessary elements in string.
  global createdict
  for i in strlst:
    i=i.replace("[","").replace("]","").replace("\"","")
    #print(i)
    create_dict(i,createdict)

def sortDict():  
  # sort the dictionary
  global createdict
  global sorteddict
  for ele in sorted(createdict): 
    sorteddict[ele] = createdict[ele]
 


#print(sorteddict)
#print(createdict)
#recurvie iteration
def recursiveiteration(usednodes,ele):
    global count;
    #print(ele)
    subvalues = sorteddict.get(ele)
    #print(subvalues)
    split_subvalues = subvalues.split(",")
    for x in split_subvalues:
      if(usednodes.count(int(x)) <= 0): 
        #print("Next traversed is " +  x)
        usednodes.append(int(x))
        count = count + int(x)
        #print("count incremented is" +  str(count))
        recursiveiteration(usednodes,int(x))


def findmax(maxlist,ele):
    global outputarr
    value =  max(maxlist)
    outputarr.append(ele+":"+str(value))
    #print("Resultsofar" + str(outputarr))
    #return value

def processNodes():
    global sorteddict
    global count
    # find the number of nodes connected
    for ele in sorteddict:
        usednodes = []
        parentconn_nodes=sorteddict[ele].split(",")
        #print("Parent node is " + str(ele))
        maxlist=[]
        for nodes in parentconn_nodes:
            #print("immediate node is " + nodes)
            count = int(nodes)
            usednodes.append(int(ele))
            usednodes.append(int(nodes))
            recursiveiteration(usednodes,int(nodes))
            maxlist.append(count)
            usednodes.clear()
            #print(ele)
            #print("Total count is : " + str(count))
            count = 0
        findmax(maxlist,str(ele))
#print("Total max count " + str(max))
def processOutput():
    global outputarr
    strval=""
    for output in outputarr:
        strval=strval+output+","
    strval=strval[:len(strval)-1]
    print(strval)

def GraphChallenge(strArr):
    strlst=strarr.split("\", \"")
    trimUnnecessary(strlst)
    sortDict()
    processNodes()
    processOutput()


GraphChallenge(strarr)   
    