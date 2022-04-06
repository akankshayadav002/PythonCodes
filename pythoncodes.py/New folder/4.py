def linearsearch(stud,num):
    flag = 0
    count1 = 0
    key = int(input("\nEnter the Roll number to Search : "))
    for i in range (num) :
        count1+=2
        if stud[i] == key :
            flag = 1
            break
    count1 += 1         # last count of comparision in a for loop
    if flag == 0 :
        print("Student of Roll No.",key,"was not present in Training Program ")
    else :
        print("Student of Roll No.",key, "was present in Training Program ")
    print("Frequency Count : ",count1)
def sentinelsearch(stud,num) :
    count2 = 0
    key = int(input("\nEnter the Roll number to Search : "))
    last = stud[num-1]
    stud[num-1] = key
    i = 0
    while stud[i] != key :
        count2 += 1
        i+=1
    stud[num-1] = last
    count2 += 1+2   #  last count of comparision with while loop +
                    #  two comparision of if loop below
    if ( (i < (num-1)) or (stud[num-1]==key) ) :
        print("Student of Roll No.", key, "was present in Training Program ")
    else :
        print("Student of Roll No.", key, "was not present in Training Program ")
    print("Frequency Count : ",count2)

if __name__ == "__main__" :
    stud = []
    num = int(input("\nEnter the Total Number of Students who attended training Program  : "))
    for i in range (num) :
        s = int(input("Enter Roll No. : "))
        stud.append(s)
    print()
    print("1. Use Linear Search ")
    print("2. Use Sentinel Search ")
    print ("\nTo Exit Press 0 ")
    while (True) :
        ch = int(input("\nEnter your Choice To search : "))
        if ch == 1 :
            linearsearch(stud,num)
        if ch == 2:
            sentinelsearch(stud, num)
        if ch == 0 :
            break