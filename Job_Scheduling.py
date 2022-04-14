# Simple Job Scheduling Python Assignment

class Job:
    # This class is a template for creating Job objects
    # properties : job_id, deadline, profit
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit


def main():
    Job1 = Job(1,3,50)
    Job2 = Job(2,1,40)
    Job3 = Job(3,3,70)
    Job4 = Job(4,1,20)
    
    # Job objects are hard coded
    
    Jobs = [Job1, Job2, Job3, Job4] # unsorted list
    sorted = []                     # sotring sorted list
    min = Jobs[0]                   # variable to store minimum value to facilitate sorting
    

    # sorting Jobs using selection sort
    for k in range(4):
        min = Jobs[0] # re-assigning min to the 0th element in current truncated list
        
        for i in Jobs:
    #        print('\n i\'s profit is ',i.profit)
            
            if(min.profit > i.profit):
                # updating minimum value
                min = i
        # for i ends
    #    print('kth iteration ',k,'\n minimum of ',k,'th is',min.profit)
        sorted.append(min) # appending minimum value of this iteration to sorted list  
        Jobs.remove(min)    # removing minimum value of this iteration from Jobs list
        # removal is required so that minimum for remaining list is computed in next iteration 
        # otherwise same value will be minimum for all iterations
    # for k endsd
    
    #sorting done in ascending order
    
        
    sorted.reverse() #for descending order
 
    #printing sorted list of jobs

    print('sorted list [printing job profits in descending order]')    
    for i in sorted:
        print(i.profit)
    
    slot = [None] * 3 #creating slot list of size same as maximum deadline
    
    #now we need to add jobs as per their profit into slots list
    
    for i in sorted:
        
        if slot[i.deadline - 1 ] == None:
            #empty space
            slot[i.deadline -1 ] = i
        else:
            #pre-occupied
        #    print('else is triggered for i with job id',i.job_id)
            for j in range(i.deadline - 1 , 0, -1):
            #    print('for j is triggered for slot index',j)
                if slot[j] == None :
                #    print('if is triggered for slot index',j)
                    slot[j] = i
                    break
    
       
    for i in range(5):
        #adding some hyphens for separation
        print('-')
        
    print('Result Array : ')    
    for i in slot:
        if i != None:
            print('for index : ',slot.index(i) + 1,'| entry : Job ID = ',i.job_id)
    
if __name__=="__main__":
    main()
