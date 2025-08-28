Python script to upload images on Jumble Nostr Client   
   
**How to run**:   
1 - pip install -r requirements.txt   
2 - export USER_NSEC=|your nsec|   
3 - python python main.py |file_path| |message|   

**Example**:   
python main.py "C:/Users/random_gui/Pictures/nostr.png" "This message was upload with Castiel's Jumble Image Upload Automation." or   
python main.py "C:/Users/random_gui/Pictures/nostr.png" ""   

**To Automate the Proccess:**   
**Linux users:** grant execute permission to the file **upload_image.sh** by doing **chmod +x upload_image.sh**   
**Windows users:** change bkg.py file to use **upload_image.bat** instead **upload_image.sh**   
**All users:**   
Change the **path** of the image directory in file **bkg.py** at **pic_path** variable   
Set the **hour** and **minute** to trigger the script at **expected_hour** and **expected_minute** variables   
**Execute:**   
python bkg.py   
