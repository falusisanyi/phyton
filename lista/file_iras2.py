import sys
oldout = sys.stdout
print("képernyőre ír.")
wr = open("test2.txt",'w')
sys.stdout = wr
print("fájlba ír.")
wr.close()
sys.stdout = oldout
print("Képernyőre ír ismét.")