pyrcc5 resource.qrc -o resource_rc.py
cd designFiles
pyuic5 startUpWindow.ui -o startUpWindow.py
pyuic5 appMain.ui -o appMain.py
pyuic5 warning1.ui -o warning1.py
pyuic5 warning2.ui -o warning2.py
pyuic5 warning3.ui -o warning3.py
pyuic5 changePassword.ui -o changePassword.py