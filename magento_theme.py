"""
piyush

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/piyushwalia/m2_automate
"""

import os, json

# urllib2 bug fix
# see https://stackoverflow.com/questions/6594620/python-3-2-unable-to-import-urllib2-importerror-no-module-named-urllib2#6594775
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

# magento_file_url = 'https://raw.githubusercontent.com/magento/magento2/' + version_input + '-develop/app/design/frontend/Magento/blank/'

REMOTE_URL_PART1 = 'https://raw.githubusercontent.com/magento/magento2/'
REMOTE_URL_PART2 = '/app/design/frontend/Magento/blank/'

# this will create Inner folders of theme
WEB_FOLDERS = ['css', 'Images']
THEME_FOLDERS = ['media', 'etc', 'Magento_Theme']

# Download default theme file from Magento latest version URL
DOWNLOADABLE_FILES = ['theme.xml', 'composer.json', 'registration.php', 'etc/view.xml']

# magento directory path which will is already present, if not, will create dir
MAGENTO_DIR_PATH = 'app/design/frontend/'

GITHUB_MAGENTO_URL = "https://api.github.com/repos/magento/magento2/tags"
# If you are using python3, change raw_input to input
# Input from console where user will enter Vendor name
try:
    vendor_name = raw_input('Enter vendor name(where you want your theme to be created):')
except NameError:
    vendor_name = input('Enter vendor name (where you want your theme to be created):')

# Input from console where user will enter theme name
try:
    theme_name = raw_input('Enter theme name (which you want to create):')
except NameError:
    theme_name = input('Enter theme name (which you want to create):')
# var which joins the magento dir path, vendor name and theme name
theme_folder_path = os.path.join(MAGENTO_DIR_PATH, vendor_name, theme_name)

# if the magento directory path does not exsist, it will create the dir
if not os.path.exists(MAGENTO_DIR_PATH):
    # this wil create dir
    os.makedirs(MAGENTO_DIR_PATH)
# if the above path exsist's, then it join the above dir path, vendor name and theme name
if not os.path.exists(theme_folder_path):
    # this will create dir with vendor name, theme name and magento root path to theme
    os.makedirs(os.path.join(theme_folder_path))

    print('Do keep your theme preview Image in media folder')

    # web folders
    for webfolder in WEB_FOLDERS:
        os.makedirs(os.path.join(theme_folder_path, 'web', webfolder))
        # theme folders
    for themefolder in THEME_FOLDERS:
        os.makedirs(os.path.join(theme_folder_path, themefolder))

    # Magento version
    print('')
    print('Downloading available magento version:')
    r = urllib2.urlopen(GITHUB_MAGENTO_URL)
    data = json.load(r)
    versions = []
    for d in data:
        n = d['name'].replace('u', '')
        versions.append(n)
    print(versions)
    print('')

    try:
        version_input = raw_input('Enter Magento Version(use full name):')
    except NameError:
        version_input = input('Enter Magento Version(use full name):')

    try:
        for url_folders in DOWNLOADABLE_FILES:
            magento_file_url = REMOTE_URL_PART1 + version_input + REMOTE_URL_PART2
            theme_xml = os.path.join(magento_file_url + url_folders)
            print("Downloading...." + url_folders)
            fileData = urllib2.urlopen(theme_xml)
            dataToWrite = fileData.read()
            with open(os.path.join(theme_folder_path, url_folders), 'wb') as f:
                f.write(dataToWrite)
                print("Download complete")

        print("Theme created successfully.")
    except Exception:
        print("Unable to download the file: " + theme_xml)
        print("Please check the you have entered:  " + version_input)