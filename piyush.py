
import sys, os, urllib2, fileinput, shutil


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


# copy file from Magento theme directory to our theme
core_files = [ 'theme.xml', 'composer.json',  'registration.php']
magento_root_initial = 'Magento/vendor/magento/theme-frontend-blank/'
theme_etc_file = 'etc/view.xml'
shutil.copy2(os.path.join(magento_root_initial + theme_etc_file), os.path.join(theme_folder_path , theme_etc_file)) 
for copy_files in core_files:         
    shutil.copy2(os.path.join(magento_root_initial + copy_files), theme_folder_path) 
  


# Opnen file and replace the required content in it
# open theme file
theme_xml = os.path.join( theme_folder_path, 'theme.xml')
# theme name 
theme_title = os.path.join("<title>" + vendor_name + ' ' + theme_name + "</title>\n")
blank_theme = "<parent>Magento/blank</parent>"
theme_name_parent = theme_title + blank_theme
f = open(theme_xml,'r')
filedata = f.read()
f.close()
theme_xml_data = filedata.replace("<title>Magento Blank</title>",theme_name_parent)
f = open(theme_xml,'w')
f.write(theme_xml_data)
f.close()



reg_php = os.path.join( theme_folder_path, 'registration.php')
reg_title = os.path.join('frontend/' + vendor_name + '/' + theme_name)

print reg_title
f = open(reg_php,'r')
filedata = f.read()
f.close()
reg_php_data = filedata.replace("frontend/Magento/blank", reg_title)
f = open(reg_php,'w')
f.write(reg_php_data)
f.close()

     

print("Theme created successfully.")


