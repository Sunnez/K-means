import time
import math
import copy
from Tkinter import *
from PIL import Image, ImageDraw
posx=0
posy=0
infinite=1000000007
pointflag=1	#1:getting points 0:getting clustervector
started=0
clusterCount=0
pointCount=0
pointsx=[]
pointsy=[]
clusterx=[]
clustery=[]
dummy_clusterx=[]
dummy_clustery=[]
cluster_member_count=[]
point_belongs_to_cluster=[]
point_dist_from_cluster=[]
color_list=['yellow','blue','green','pink','brown']
point_belongs_to_cluster,point_dist_from_cluster
def motion(event):
	global posx,posy,pointflag,started,clusterCount,pointCount,pointsx,pointsy,clusterx,clustery,canvas,infinite,point_belongs_to_cluster,point_dist_from_cluster,cluster_member_count,color_list,dummy_clusterx,dummy_clustery
	posx=event.x
	posy=event.y
	#print posx,posy
	return
	
def singleClick(event):
	global posx,posy,pointflag,started,clusterCount,pointCount,pointsx,pointsy,clusterx,clustery,canvas,infinite,point_belongs_to_cluster,point_dist_from_cluster,cluster_member_count,color_list,dummy_clusterx,dummy_clustery	
	if(started==0):
		if(pointflag==1):
			pointsx.append(posx)
			pointsy.append(posy)
			canvas.create_oval(posx+3,posy+3,posx-3,posy-3, fill="red")
			canvas.addtag_closest("point"+str(pointCount), posx, posy, halo=None, start=None)
			pointCount+=1
		else:
			
			clusterx.append(posx)
			clustery.append(posy)
			canvas.create_oval(posx+3,posy+3,posx-3,posy-3, fill="white")
			canvas.addtag_closest("cluster"+str(clusterCount), posx, posy, halo=None, start=None)
			clusterCount+=1
		#print "CLICK:",posx,posy
	

def task():
	global posx,posy,pointflag,started,clusterCount,pointCount,pointsx,pointsy,clusterx,clustery,canvas,infinite,point_belongs_to_cluster,point_dist_from_cluster,cluster_member_count,color_list,dummy_clusterx,dummy_clustery

	#print("hello")
	for i in range(len(pointsx)):
		point_dist_from_cluster[i]=infinite
		point_belongs_to_cluster[i]=0
		for j in range(len(clusterx)):
			local_dist=math.pow((clusterx[j]-pointsx[i]),2)+math.pow((clustery[j]-pointsy[i]),2)	
			if local_dist<point_dist_from_cluster[i]:
				point_dist_from_cluster[i]=local_dist
				point_belongs_to_cluster[i]=j
	
	for i in range(len(pointsx)):
		#change color
		temp=point_belongs_to_cluster[i]
			
			
	for i in range(len(clusterx)):
		#init
		cluster_member_count[i]=0
		dummy_clusterx[i]=0
		dummy_clustery[i]=0
	for i in range(len(pointsx)):
		temp=point_belongs_to_cluster[i]
		cluster_member_count[temp]+=1
		dummy_clusterx[temp]+=pointsx[i]
		dummy_clustery[temp]+=pointsy[i]
		canvas.itemconfig("point"+str(i), fill=color_list[temp])
	for i in range(len(clusterx)):
		dummy_clusterx[i]=dummy_clusterx[i]/cluster_member_count[i]
		dummy_clustery[i]=dummy_clustery[i]/cluster_member_count[i]	
		canvas.move("cluster"+str(i),dummy_clusterx[i]-clusterx[i],dummy_clustery[i]-clustery[i])
		
	#print "clusterx,clustery:",clusterx,clustery
	#print "dummy_clusterx:",dummy_clusterx,dummy_clustery
	
	
	if(clusterx==dummy_clusterx and clustery==dummy_clustery):
		#print "done"
		root.after_cancel(task)
		return 0
	else:
		#print "next"
		#root.after(200,task)
		return 0
	
	
	
def startFunc():
	global posx,posy,pointflag,started,clusterCount,pointCount,pointsx,pointsy,clusterx,clustery,canvas,infinite,point_belongs_to_cluster,point_dist_from_cluster,cluster_member_count,color_list,dummy_clusterx,dummy_clustery
	started=1
	local_dist=0
	dummy_clusterx=[]
	dummy_clustery=[]
	#print "started"
	for i in range(len(clusterx)):
		#init
		cluster_member_count.append(0)
		dummy_clusterx.append(0)
		dummy_clustery.append(0)
	for i in range(len(pointsx)):
		point_dist_from_cluster.append(infinite)
		point_belongs_to_cluster.append(0)
	
	#for iteration in range(0,3):
	root.after(2000,task)
	#print "super done!"
	
	return 0
	
		
		
		
def getPoints():
	global posx,posy,pointflag,started,clusterCount,pointCount,pointsx,pointsy,clusterx,clustery,canvas,infinite,point_belongs_to_cluster,point_dist_from_cluster,cluster_member_count,color_list,dummy_clusterx,dummy_clustery
	pointflag=1

def getClusterVector():
	global posx,posy,pointflag,started,clusterCount,pointCount,pointsx,pointsy,clusterx,clustery,canvas,infinite,point_belongs_to_cluster,point_dist_from_cluster,cluster_member_count,color_list,dummy_clusterx,dummy_clustery
	pointflag=0

	
root=Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.wm_title("K-means clustering")


canvas = Canvas(root,width=w,height=h-100)
canvas.bind('<Motion>',motion)
canvas.bind('<Button-1>',singleClick)
canvas.pack()


start = Button(root, text="Start",command=startFunc)
start.pack()

points = Button(root, text="Points",command=getPoints)
points.pack()

clusterVector = Button(root, text="Cluster Vector",command=getClusterVector)
clusterVector.pack()





root.mainloop()




