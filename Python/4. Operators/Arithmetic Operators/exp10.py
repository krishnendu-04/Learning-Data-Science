n = int(input("Enter the seconds: "))
hrs = n//3600
remain_sec = n%3600
mins = remain_sec//60
sec = remain_sec%60
print(hrs,"hrs:",mins,"mins:",sec,"secs")