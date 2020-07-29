def Email(lst):
    dic={}
    for i in lst:
        lst1=i.split('.')
        lst2=lst1[0].split('@')
        print(lst2[0],lst2[1])
        if(lst2[1] in dic):
            dic[lst2[1]].append(lst2[0])
        else:
            dic[lst2[1]]=[lst2[0]]
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
   
lst=['hello@dhruvsoft.com','john@dhruvsoft.com','bob@google.com', 'alice@amazon.com','william@salesforce.com', 'jhon@heroku.com','chiru@nestuite.com', 'venky@dhruvsoft.com', 'naveen@zoho.com', 'doe@zoho.com','aws@dhruvsoft.com','rgv@sivio.com','pawan@netsuite.com','welcome@dhruvsoft.com']
data=Email(lst)
print(TotalEmployees(data,"dhruvsoft"))
print(TotalNumOfEmployees(data))
