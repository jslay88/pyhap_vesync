Etekcity Vesync HomeKit Bridge
==============================

This application was built to add HomeKit functionality to Etekcity's Vesync Outlets.

This application was built using [HAP-python](https://github.com/ikalchev/HAP-python),
and code from [python-vesync](https://github.com/tylergets/python-vesync).


Installation
============

This application requires Python 3.4+

Clone the repo, and install the requirements with pip or pip3, depending on your environment.


    git clone https://github.com/jslay88/pyhap_vesync.git
    cd pyhap_vesync
    pip install -r requirements.txt


Execute the application inside the pyhap_vesync folder.

    python pyhap_vesync/app.py -u username@domain.com -p totally_secure_password
    
On first run, you should get a QR code. Scan the QR code with your HomeKit app in iOS.
