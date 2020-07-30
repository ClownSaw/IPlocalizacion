#!usr/bin/bash
if which iplocalizacion >/dev/null; then
                sleep 0.25
    echo "[IPLLOCALIZACION]...........Installed [✓]"
else
                sleep 0.25
        echo "[IPLOCALIZACION]..........Not Installed [✗]"
                        sleep 1
                echo "Install IPLOCALIZACION "
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

fi
pip3 install -r requirements.txt

chmod +x iplocalizacion

mv iplocalizacion /usr/bin/

mv core /usr/bin

mv logs /usr/bin

