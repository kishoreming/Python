with open("nfile1.txt","r+") as file:
   file.write("kob is hero")
   file.seek(0)
   print(file.read())