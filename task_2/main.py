n = int(input("Школьников: "))
k = int(input("Яблок: "))
yablok = k // n 
ost = k % n 
print(f"Все получат по {yablok}")
print(f"Останется лежать {ost}")