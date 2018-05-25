
import sys, os, urllib2, fileinput
from shutil import copyfile

# magento directory path which will is already present, if not, will create dir
magento_dir_path = 'app/design/frontend/'
# If you are using python3, change raw_input to input
# Input from console where user will enter Vendor name
vendor_name = raw_input('Enter vendor name where you want your theme to be created:')
# Input from console where user will enter theme name
theme_name = raw_input('Enter theme name which you want to create :')
# var which joins the magento dir path, vendor name and theme name 
theme_folder_path = os.path.join(magento_dir_path,vendor_name, theme_name)

# if the magento directory path does not exsist, it will create the dir 
if not os.path.exists(magento_dir_path):
    # this wil create dir    
    os.makedirs(magento_dir_path)
        
# if the above path exsist's, then it join the above dir path, vendor name and theme name    
if not os.path.exists(theme_folder_path):
    # this will create dir with vendor name, theme name and magento root path to theme
    os.makedirs(os.path.join(theme_folder_path))
    
    # this will create Inner folders of theme
    web_folders = ['css','Images']
    theme_folders = ['media', 'etc', 'Magento_Theme']

    print('Do keep your theme preview Image in media folder')

    # web folders
    for webfolder in web_folders:        
        os.makedirs(os.path.join(theme_folder_path, 'web', webfolder))    
    # theme folders
    for themefolder in theme_folders:        
        os.makedirs(os.path.join(theme_folder_path,themefolder))    

  
def download_theme_files():
    # Magento version
    version_input = raw_input('Magento Version:')
    # Download default theme file from Magento latest version URL
    downloadable_files = [ 'theme.xml', 'composer.json',  'registration.php', 'etc/view.xml']
    for url_folders in downloadable_files:         
        magento_file_url = 'https://raw.githubusercontent.com/magento/magento2/'+ version_input +'-develop/app/design/frontend/Magento/blank/'                
        try:
            theme_xml = os.path.join(magento_file_url + url_folders)
            print "Downloading...........", url_folders    
            filedata = urllib2.urlopen(theme_xml)          
            datatowrite = filedata.read()
            with open(os.path.join(theme_folder_path, url_folders) ,'wb') as f:  
                f.write(datatowrite)
        except urllib2.HTTPError as err:
            if err.code == 404:
                print "Please enter Valid Magento Version" 
                break                
if __name__== "__main__":
    download_theme_files()

# Opnen file and replace the required content in it

filein = os.path.join( theme_folder_path, 'theme.xml')
theme_title = os.path.join(vendor_name + ' ' + theme_name)
print filein
f = open(filein,'r')
filedata = f.read()
f.close()

newdata = filedata.replace("Magento Blank",theme_title)

f = open(filein,'w')
f.write(newdata)
f.close()

