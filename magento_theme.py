
import sys, os


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
    subfolder_names = ['css','Images']
    for subfolder_name in subfolder_names:
        os.makedirs(os.path.join(theme_folder_path, subfolder_name))
    

