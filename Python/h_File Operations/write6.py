r1 = open("data6.txt","r")
above_50=[]
below_25=[]
bet_25_40=[]
from_ind=[]
doc=[]
eng=[]
from_uk=[]
doc_ind=[]
doc_uk=[]
pilot_above_40 = []
females=[]
from_kochi=[]
doc_num=0
prof={}
country={}
age=[]
last =[]
r1.split("]")
print(r1)
print("\nRecords of all people: ")
for i in r1:
    rec = i.rstrip().split(",")
    print(rec)
    if int(rec[3])>50:
        above_50.append(rec)

    if int(rec[3])<25:
        below_25.append(rec)

    if 25<int(rec[3])<40:
        bet_25_40.append(rec)

    if rec[6] == "India":
        from_ind.append(rec[1:3])

    if rec[-1]=="Doctor":
        doc.append(rec[1:3])

    if rec[-1]=="Engineer":
        eng.append(rec[1:3])

    if rec[-2]=="UK":
        from_uk.append(rec[1:3])

    if rec[-1]=="Doctor" and rec[-2]=="India":
        doc_ind.append(rec[1:3])

    if rec[-1]=="Doctor" and rec[-2]=="UK":
            doc_uk.append(rec[1:3])

    if rec[-1]=="Pilot" and int(rec[3])>40:
        pilot_above_40.append(rec[1:3])

    if rec[4]=="Female":
        females.append(rec[1]+" "+rec[3]+" "+rec[-1])

    if rec[-3]=="Kochi":
        from_kochi.append(rec[1:3])

    if rec[-1]=="Doctor":
        doc_num+=1

    if rec[-1] not in prof:
        prof[rec[-1]] = 1
    else:
        prof[rec[-1]] +=1

    if rec[-2] not in country:
        country[rec[-2]] = 1
    else:
        country[rec[-2]] +=1

    oldest = int(rec[3])
    if int(rec[3])>oldest:
        oldest=int(rec[3])

    youngest = int(rec[3])
    if int(rec[3])<youngest:
        youngest=int(rec[3])

    age.append(int(rec[3]))
    avg = sum(age)/len(age)

    if rec[-2]=="India" and int(rec[3])>30 and (rec[-1]=="Doctor" or rec[-1]=="Engineer"):
        last.append(rec[1:])

print("\nPeople above 50: ",above_50)
print("\nPeople below 25: ",below_25)
print("\nPeople people whose age is between 25 and 40: ",bet_25_40)
print("\nPeople who are from India: ",from_ind)
print("\nDoctors: ",doc)
print("\nEngineers: ",eng)
print("\nPeople who are from UK: ",from_uk)
print("\nDoctors from India: ",doc_ind)
print("\nDoctors from the UK: ",doc_uk)
print("\nPilots whose age is above 40: ",pilot_above_40)
print("\nFemales: ",females)
print("\nPeople living in Kochi: ",from_kochi)
print("\nTotal number of Doctors: ",doc_num)
print("\nCount of each profession: ",prof)
print("\nCount of each country: ",country)
print("\nThe oldest person: ",oldest)
print("\nThe youngest person: ",youngest)
print("\nAverage age of all people: ",age)
print("\nPeople who belong to India, are older than 30 and work as Engineer or Doctor: ",last)