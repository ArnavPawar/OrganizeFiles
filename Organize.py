import os
import shutil

image= ".jpg" , ".jfif" , ".gif" , ".bmp" , ".pjp" , ".png" , ".cur" , ".jpeg" , ".ani", "svg"
app= ".exe" , ".apk" , ".bat" , ".bin" , ".cgi" , ".pl" , ".com" , ".gadget" , ".jar" , ".msi" , ".wsf"
document = ".text" , ".doc" , ".docx" , ".odt" , ".pdf" , ".rtf" , ".tex" , ".txt" , ".wpd", "log", "msg", "wps", "wpd","ppt","pps"
song= ".aif" , ".cda" , ".mid" , ".midi" , ".mp3" , ".mpa" , ".wav" , ".wma" , ".wpl" , "ogg" ,"iff","m4a","m3u"
video= ".3g2" , ".3gp" , ".avi" , ".flv" , ".h264" , ".m4v" , ".mkv" , ".mov" , ".mp4" , "mgp" , ".mpeg" , ".rm" , ".swf" , "vob" , "wmv"
zep= ".zip",".7z",".rar",".rmp",".zipx"
datas= ".cvs",".dat",".ged",".key",".keychain",".xml",".apk"
game= ".b",".dem",".gam",".nes",".rom",".sav"
webs=".asp",".cer",".css",".dcr",".htm",".html",".js",".jsp",".xhtml"
systems= ".cab",".cpl",".dll",".dmp",".drv",".ico",".lnk",".sys",".cfg",".ini",".prf"
codes= ".c",".class",".cs",".cpp",".java",".pl",".py",".vcxproj"

path = ("D:/Users/"YOUR USER"/Documents/Prgrms/PathForPrgm/")
names = os.listdir(path)
folder_name = ['images','apps','documents','songs','videos', 'zip','data','games','web','system','code']
for x in range(0,11):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])
for files in names:
    if files.endswith(image):# in files and not os.path.exists(path+'image/'+files):
        shutil.move(path+files,path+'images/'+files)
    # elif files.endswith(app):# in files and not os.path.exists(path+'image/'+files):
        # shutil.move(path+files,path+'apps/'+files)
    elif files.endswith(document):# in files and not os.path.exists(path+'image/'+files):
        shutil.move(path+files,path+'documents/'+files) 
    elif files.endswith(app):# in files and not os.path.exists(path+'image/'+files):
        shutil.move(path+files,path+'apps/'+files)
    elif files.endswith(song):# in files and not os.path.exists(path+'image/'+files):
        shutil.move(path+files,path+'songs/'+files)
    elif files.endswith(video):# in files and not os.path.exists(path+'image/'+files):
        shutil.move(path+files,path+'videos/'+files)
    elif files.endswith(zep):# in files and not os.path.exists(path+'image/'+files):
        shutil.move(path+files,path+'zip/'+files) 
    elif files.endswith(datas):# in files and not os.path.exists(path+'image/'+files):
        shutil.move(path+files,path+'data/'+files)
    elif files.endswith(game):# in files and not os.path.exists(path+'image/'+files):
        shutil.move(path+files,path+'games/'+files)
    elif files.endswith(webs):# in files and not os.path.exists(path+'image/'+files):
        shutil.move(path+files,path+'web/'+files)
    elif files.endswith(systems):# in files and not os.path.exists(path+'image/'+files):
        shutil.move(path+files,path+'system/'+files)
    elif files.endswith(codes):# in files and not os.path.exists(path+'image/'+files):
        shutil.move(path+files,path+'code/'+files)
