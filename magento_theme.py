
import sys, os, urllib2


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

    # Download theme.xml file from Magento latest version URL
    theme_xml = 'https://raw.githubusercontent.com/magento/magento2/2.2-develop/app/design/frontend/Magento/blank/theme.xml'
    composer_json =  'https://raw.githubusercontent.com/magento/magento2/2.2-develop/app/design/frontend/Magento/blank/composer.json'
    registration_php = 'https://raw.githubusercontent.com/magento/magento2/2.2-develop/app/design/frontend/Magento/blank/registration.php'
    view_xml = 'https://raw.githubusercontent.com/magento/magento2/2.2-develop/app/design/frontend/Magento/blank/etc/view.xml'


    # theme.xml file download
    filedata = urllib2.urlopen(theme_xml)  
    datatowrite = filedata.read()
    with open(os.path.join(theme_folder_path, 'theme.xml') ,'wb') as f:  
        f.write(datatowrite)

     # composer.json file download
    filedata = urllib2.urlopen(composer_json)  
    datatowrite = filedata.read()
    with open(os.path.join(theme_folder_path, 'composer.json') ,'wb') as f:  
        f.write(datatowrite)   

    # registratoin.php file download
    filedata = urllib2.urlopen(composer_json)  
    datatowrite = filedata.read()
    with open(os.path.join(theme_folder_path, 'registration.php') ,'wb') as f:  
        f.write(datatowrite)                 

      # view.xml in etc folder file download
    filedata = urllib2.urlopen(view_xml)  
    datatowrite = filedata.read()
    with open(os.path.join(theme_folder_path,'etc', 'view.xml') ,'wb') as f:  
        f.write(datatowrite)     