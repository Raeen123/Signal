import threading
import subprocess
import os
files = os.listdir('files')
files.remove("plugin")
files.remove("index.html")
diffault1 = '<!DOCTYPE html><html ><head><meta charset="UTF-8"><title>Signal</title><link rel="icon" href="plugin/signal.png"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css"><link rel="stylesheet" href="plugin/css/style.css"></head><body><center><img src="plugin/signal.png" style="width:5%"></center><h1>Signal</h1><p>Download Files</p><main><table><thead><tr><th>File Name</th><th>Size (MB)</th><th></th></tr></thead><tfoot><tr><th colspan='+'3'+'>RAEEN AHANI AZARI</th></tr></tfoot><tbody>'
diffault2 = '</tbody></table></main><script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script><script src="plugin/js/index.js"></script><script src="plugin/copy.js"></script><script>new ClipboardJS(".btn");</script></body></html>'
table= ""
for file in files:
    table += "<tr><td >"+file+"</td><td >"+str(os.path.getsize('files/'+file)/1000000)+"</td><td><div id='"+file+"'></div></td></tr><script>var OpenA = document.createElement('a');var Opentext = document.createTextNode('Open');OpenA.appendChild(Opentext);OpenA.href = location.href + '"+file+"';OpenA.className = 'button Openbtn btn';var downA = document.createElement('a');var downtext = document.createTextNode('Download');downA.appendChild(downtext);downA.href = location.href + '"+file+"';downA.download = '';downA.className = 'button downbtn btn';var CopyA = document.createElement('a');var Copytext = document.createTextNode('Copy Path');CopyA.appendChild(Copytext);CopyA.setAttribute('data-clipboard-text', location.href + '"+file+"');CopyA.href = '#';CopyA.className = 'button btn';var element = document.getElementById('"+file+"');element.appendChild(OpenA);element.appendChild(downA);element.appendChild(CopyA);</script>"
with open("files/index.html", "w") as f:
     f.write(diffault1 + table + diffault2) # write the new line before



def runlocal():
    subprocess.call('python -m http.server 8080 --directory files/')


def runhost():
    subprocess.call('ssh -R 80:localhost:8080 nokey@localhost.run')


if __name__ == "__main__":
    local = threading.Thread(target=runlocal)
    host = threading.Thread(target=runhost)

    local.start()
    host.start()
