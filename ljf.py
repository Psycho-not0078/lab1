ready_queue=[]
ready=[]
output=[]

processes=[]

pids=[]
start_time={}
fin_time={}
mid_stops={}
arrival_times={}
burst_times={}

TAT={}
WT={}
RT={}


n=0

def get_info():#geting inputs
    n=int(input("enter the number of process:"))
    arrivaltime=0
    bursttime=0
    #total_time=0
    process={}

    for i in range(n):
        #print("\n "+str(i+1)+" process info:\n")
        process_id=int(input("enter the PID: "))
        arrivaltime=int(input("enter the arrival time: "))
        bursttime=int(input("enter the burst time: "))
        pids.append(process_id)
        process['PID']=process_id
        process['arrival_time']=arrivaltime
        arrival_times[process_id]=arrivaltime
        burst_times[process_id]=bursttime

        process['burst_time']=bursttime
        x=process.copy()
        processes.append(x)
        process.clear()
    return n
        #print(processes)
    #process1=processes[1]
    #print(processes)
n=get_info()

#print(processes)

for i in processes:
    print(i)

def sorte(lis):#sorting the ready queue
    return sorted(lis, key = lambda i: i['burst_time'],reverse=True) 



def checker(lis):#checking if all processes are done
    cc=n
    for i in lis:
        if(i['burst_time']==0):
            cc-=1
        else: 
            break
    
    if cc<=1:
        return False
    else:
        return True
time=0
start=0


while(checker(processes)):#mostly main functions
    for i in processes:
        if(i['arrival_time']<=time):
            ready.append(i)
    #print(ready)
    ready_queue=sorte(ready)

    #print(ready_queue)
    if(ready_queue):
        if(ready_queue[start]['burst_time']==0):
            for i in range(n):
                if(processes[i]['PID']==ready_queue[start]['PID']):
                    pid=processes[i]['PID']
            fin_time[pid]=time
            start+=1
        
        c=0
        output.append([ready_queue[start]['PID'],time])
        for i in range(n):
            if(processes[i]['PID']==ready_queue[start]['PID']):
                processes[i]['burst_time']-=1
                pid=processes[i]['PID']
            for k in output:
                if(k[0]==pid):
                    c+=1
            if(c==1):
                start_time[pid]=time
            else:
                mid_stops[pid]=time
                


    ready_queue.clear()
    ready.clear
    print(output)
    time+=1

total_time=time

for i in pids:
    TAT[i]=fin_time[i]-arrival_times[i]
    RT[i]=start_time[i]-arrival_times[i]


# _______   ________  ________ 
#|\  ___ \ |\   __  \|\  _____\
#\ \   __/|\ \  \|\  \ \  \__/ 
# \ \  \_|/_\ \  \\\  \ \   __\
#  \ \  \_|\ \ \  \\\  \ \  \_|
#   \ \_______\ \_______\ \__\ 
#    \|_______|\|_______|\|__| 
#        
# ________  ___             ___  ________ 
#|\   __  \|\  \           |\  \|\  _____\
#\ \  \|\  \ \  \          \ \  \ \  \__/ 
# \ \   ____\ \  \       __ \ \  \ \   __\
#  \ \  \___|\ \  \____ |\  \\_\  \ \  \_|
#   \ \__\    \ \_______\ \________\ \__\ 
#    \|__|     \|_______|\|________|\|__|                       
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              