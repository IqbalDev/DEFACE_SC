import sys 
import time


def title():
    global title
    title = str(raw_input(" Masukkan Title: "))

def judul():
    global judul
    judul = str(raw_input(" Input Your Nick Name: "))


def background():
    try:
        global back
        print "+---------------+"
        print " [1] Black"
        print " [2] White"
        print " [3] red"
        print " [4] Abu2"
        print "+---------------+"
        back = str(raw_input(" Warna Background: "))
        if back is '1':
            back = '#000000' # black
        elif back is '2':
            back = '#ffffff' # white
        elif back is '3':
            back = '#f10909' # red
        elif back is '4':
            back = '#d1cbcb' # Abu2
        else:
            print ' '
    
    except KeyboardInterrupt:
        background()
def color_teks():
    try:
        global teks
        print "+---------------+"
        print " [1] White"
        print " [2] Black"
        print " [3] red"
        print " [4] Abu2"
        print "+---------------+"
        teks = str(raw_input(" Warna Text: "))
        if teks is '1':
            teks = '#ffffff' # white
        elif teks is '2':
            teks = '#000000' # black
        elif teks is '3':
            teks = '#f10909' # red
        elif teks is '4':
            teks = '#d1cbcb'
        else:
            print " "
    
    except KeyboardInterrupt:
        color_teks()
       
title()
judul()
background()
color_teks()

deface = open('deface.html', 'w')
deface.write('''
<!DOCTYPE html>
<html>
    <head>
        <title>'''+title+'''</title>
        <link href="https://fonts.googleapis.com/css?family=Indie+Flower" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Caveat|Macondo+Swash+Caps|Yeon+Sung" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Macondo+Swash+Caps|Yeon+Sung" rel="stylesheet">
        <script src="https://cdn.rawgit.com/FicriPebriyana/efek/0a935a6c/efek%20salju.js" type="text/javascript"></script>
        <script src="https://pastebin.com/raw/ynL2hpMe" type="text/javascript"></script>

        <style type="text/css">
            body {
                background-color: '''+back+''';
            }
            .conten {
                width: 700px;
                color: '''+teks+''';
                margin: auto;
                font-size: 60px;
                text-align: center;
                margin-top: 20px;
                font-family: Yeon Sung, Cursive;
            }
            .friends {
                margin: auto;
                color: '''+teks+''';
                font-size: 40px;
                text-align: center;
                margin-top: 30px;
                font-family: Yeon Sung, Cursive;
            }
        </style>
    </head>
    <body>
            <br><br><br><br>
            <center><img width="500" src="https://www.eannovate.com/admin/images/news/14769334601906521429garuda-berdarah.jpg"></center>
            <div class="conten">[ Hacked By <font color="red">'''+judul+'''</font> ]</div>
            <br>
            <div class="friends"><font color="red">Thanks To:</font> <br><font color="red">[</font> <marquee width='76%' behavior="alternate" scrollamount="20%">[+] Sultan<font color="red"> | </font>IqbalzNoobs <font color="red">| </font>Iqbal_Dev <font color="red">| 1V4L_D3V </font> [+]</marquee><font color="red"> ]</font></div>
            </br>
            <div id="Clock" align="center" style="font-size: 54px; font-family: Yeon Sung, Cursive; color: red;"></div>
            <br><center>
                <a href="mailto:iqbalziqbalz30@gmail.com"><font face="Caveat" size='7' color="#b8b3b3">  Contact Me</a></center>
            </br>
            <iframe width="0" height="0" loop="true" src="http://lagu123.eu/play/alan-walker-k-391-emelie-hollow-lily~lagu123.eu~kTJbE3sfvlI.mp3" frameborder="0" allowfullscreen></iframe>
    </body>
</html>
''')
deface.close()
