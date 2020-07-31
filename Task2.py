def Email(lst):
    dic={}
    for i in lst:
        lst1=i.split('@')
        print(lst1[0],lst1[1])
        if(lst1[1] in dic):
            dic[lst1[1]].append(lst1[0])
        else:
            dic[lst1[1]]=[lst1[0]]
    return dic
# task1
def TotalEmployees(data,company_name):
    if(data[company_name]):
        return data[company_name]
    else:
        return "Employee details of "+company_name+" not found"
#task2
def TotalNumOfEmployees(data):
    dic={}
    lst=data.keys()
    for i in lst:
        dic[i]=len( TotalEmployees(data,i))    
    return dic
   
lst=['sai@google.com','ravi@amazon.com','uday@amazon.in','kiran@salesforce.com','sunil@salesforce.com','madhu@microsoft.com','tharun@google.com',]
data=Email(lst)

print(TotalNumOfEmployees(data))
