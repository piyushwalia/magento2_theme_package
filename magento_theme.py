
import sys, os
# Input from console where user will enter theme name
theme_name = raw_input('Enter theme name which you want to create:')
# magento directory path which will is already present, if not, will create dir
magento_dir_path = 'app/design/frontend/'
# if the magento directory path does not exsist, it will create the dir 
if not os.path.exists(magento_dir_path):
    # this wil create dir    
    os.makedirs(magento_dir_path)
# if the above path exsist's, then it join the above dir path and theme name    
if not os.path.exists(os.path.join(magento_dir_path, theme_name)):
    # this will create dir with theme name and magento root path to theme
    os.makedirs(os.path.join(magento_dir_path, theme_name))

    