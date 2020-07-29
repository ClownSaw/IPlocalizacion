#!usr/bin/bash
pip3 install -r requirements.txt

chmod +x iplocalizacion

mv iplocalizacion /usr/bin/

mv core /usr/bin

mv logs /usr/bin

echo "[Desktop Entry]
Name=iplocalizacion
Encoding=UTF-8
Exec=/usr/share/kali-menu/exec-in-shell "iplocalizacion"
Icon=/usr/bin/core/iplocalizacion
StartupNotify=false
Terminal=true
Type=Application
Categories=01-info-gathering;
X-Kali-Package=iplocalizacion " >> /usr/share/applications/kali-iplocalizacion.desktop 
