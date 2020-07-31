def Email(lst):
    
    dic={}
    
    for i in lst:
        
        lst1=i.split('.')
        lst2=lst1[0].split('@')
        doamin=lst1[1]
        company_name=lst2[1]
        emp_name=lst2[0]
        if(doamin in dic):
            if(company_name in dic[doamin]):
                dic[doamin][company_name].append(emp_name)
            else:
                dic[doamin][company_name]=[]
                dic[doamin][company_name].append(emp_name)
           
        else:
            dic[doamin]={}
            dic[doamin][company_name]=[]
            dic[doamin][company_name].append(emp_name)
    return dic
def TotalNumOfEmployees(data):
    dic={}
    lst=data.keys()
    for i in lst:
        dic[i]=len( TotalEmployees(data,i))    
    return dic
   
   
lst=['sai@google.com','ravi@amazon.com','uday@amazon.in','kiran@salesforce.com','sunil@salesforce.com','maruthi@amazon.in','nawaz@google.io','madhu@microsoft.com','tharun@google.com']
data=Email(lst)
i=0

for domain in data:
    
    print("I belongs to this doamin---",domain)
    for comp in data[domain]:
        print("And we are from [",comp,"] and  employee details are as follow:")
        for emp in data[domain][comp]:
            i+=1
        print(i)
        i=0
        
print(data)

