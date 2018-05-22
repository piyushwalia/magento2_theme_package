def main():
    f= open("./magento/guru99.txt","w+")
    #f=open("guru99.txt","a+")
    
    f.close()
    #Open the file back and read the contents
    #f=open("guru99.txt", "r")
    #if f.mode == 'r':
    #   contents =f.read()
    #    print (contents)
    #or, readlines reads the individual line into a list
    #fl =f.readlines()
    #for x in fl:
    #print(x)
if __name__== "__main__":
  main()