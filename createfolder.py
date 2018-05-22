import os, errno,sys, fileinput

try:
    print('creating directory')
    # var = input("Please enter theme name ")
    filename = sys.argv[-1]
    magento_file_path = 'app/design/frontend/'
    os.makedirs(os.path.join(magento_file_path, filename))
except OSError as e:
    if e.errno != errno.EEXIST:
        raise


def main():
    filename = sys.argv[-1]
    print('creating file')
    f= open(filename,"w+")    
    
    f.close()
if __name__== "__main__":
  main()        