NumberOfProcesses = int(input("Enter Number of Processes:  "))
def CompletionTime(TotalTime):  
    index = 0
    i = Process[0][1]  
    while (1):  
        if (i <= NumberOfProcesses): 
            index = LargestArrivalTime(i)  
        else: 
            index = LargestArrivalTime(NumberOfProcesses)  
        print("Process execute at time ", 
                    TotalTime, end = " ") 
        print(" is: P", index + 1,  
                        sep = "", end = " ") 
        Process[index][2] -= 1
        TotalTime += 1
        i += 1
        if (Process[index][2] == 0):  
                Process[index][6] = TotalTime 
                print("Process P", Process[index][0],  
                           sep = "", end = " ") 
                print(" is completed at ",  
                     TotalTime, end = " ") 
        print() 
        if (TotalTime== PreTotalBurstTime):  
            break
def LargestArrivalTime(ArrivalTime): 
    maximum = 0
    for i in range(NumberOfProcesses): 
        if (Process[i][1] <= ArrivalTime): 
            if (Process[i][2] > Process[maximum][2]) : 
                maximum = i      
    return maximum
Process = []
for i in range(NumberOfProcesses): 
    Process.append([0, 0, 0, 0, 0, 0, 0]) 
TotalTime = 0
PreTotalBurstTime = 0
for i in range(NumberOfProcesses):  
    Process[i][0] = i + 1
for i in range(NumberOfProcesses): 
    Process[i][1] = int(input("Enter arrival time for process "+str(i+1)+"  "))
for i in range(NumberOfProcesses):  
    Process[i][2] = int(input("Enter burst time for process "+str(i+1)+"  ")) 
    Process[i][3] = Process[i][2]  
    PreTotalBurstTime += Process[i][2]
print("Process ID        Arrival Time        Burst Time") 
for i in range(NumberOfProcesses):  
    print(Process[i][0], "                ",Process[i][1], "                ", Process[i][2])
print(" ")
Process = sorted(Process, key = lambda Process:Process[1])  

TotalTime = TotalTime + Process[0][1] 
PreTotalBurstTime  = PreTotalBurstTime + Process[0][1]  

print("GANT CHART")
CompletionTime(TotalTime)  
WaitingTime = 0
TurnAroundTime = 0
for i in range(NumberOfProcesses): 
    Process[i][5] = Process[i][6]- Process[i][1]  
    Process[i][4] = Process[i][5] - Process[i][3]  
    WaitingTime += Process[i][4]  
    TurnAroundTime += Process[i][5]  
  
print("After completion of all processes in queue ... ") 
print("Process ID    Arrival Time    Burst Time    Completion Time    Turn Around Time    Waiting Time") 
 
for i in range(NumberOfProcesses):  
    print(Process[i][0], "        ", Process[i][1], "        ",Process[i][3], "        ", end = " ") 
    print(Process[i][6], "        ",  Process[i][5], "        ", Process[i][4]) 
print(" ") 
print("Total turn around time is = ", TurnAroundTime) 
print("Average turn around time is = ", TurnAroundTime / 4.0) 
print("Total waiting time is  = ", WaitingTime) 
print("Average waiting time is  = ", WaitingTime / 4.0) 


