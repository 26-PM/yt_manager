file=open("main.text","w")
try:
    text=file.write("heya!")
finally:
    file.close()        
