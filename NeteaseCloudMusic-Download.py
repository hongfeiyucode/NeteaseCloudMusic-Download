# -*- coding:UTF-8 -*-
# Author：hongfeiyu
import os
path=raw_input(u'请完整输入缓存文件目录并彻底退出播放器： ')#.strip()
path=path+"/Cache"
#print path
files = os.listdir(path)
for f in files:
    file_name, file_extname = f.split('.')
    print file_name, file_extname
    if file_extname == 'uc':
    	os.chdir(path)#切记要到目录下来修改
        os.rename(f, '%s.mp3' %file_name)
print u'文件下载完成！请打开播放器手动上传到云端！'