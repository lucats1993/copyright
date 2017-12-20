#coding:utf-8
import os
from co_name import CoName
path='C:/Users/wll/Desktop/simple/2017-09-14-16h35m17s'#文件夹目录source_test
#path='C:/Users/wll/Desktop/simple/test'
if __name__ == '__main__':
    file_names = os.listdir(path)  # 得到文件夹下的所有文件名称
    i=0
    for file in file_names:
        file_path =path+'/'+file
        with open(file_path, 'r') as f:
            html=f.read()
            try:
                co = CoName(html)
                copyright=co.get_copyright()
                # if copyright:
                #     copyright =copyright.decode('utf-8')[:150].encode('utf-8')
                co_name =co.get_co_name(copyright)
            except Exception as e:
                print e
            else:
                if copyright:
                    print co_name
                    # print("%s %s"%(copyright,file_path))
                    i=i+1
    print i





