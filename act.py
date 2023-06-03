# 原书更新了一个插入的第二章，从第二章开始原来的文件名和链接都需要修改章节号（+1）

import os
import re

# 需要修改子目录编号的父级目录（先改好编号）
od = oprateing_dir = "8.图和图的算法"

# 本py文件所在目录（父级目录同级）
basedir = os.getcwd()

# 重命名子目录
def re_id(targetdir:str):

    # 被操作的父级目录的完整路径
    # oprateing_fullpath
    of = os.path.join(os.getcwd(),od)

    # 被操作父级目录所有子目录的列表
    dirs = os.listdir(of)
            
    for itm in dirs:

        # 每个子目录的完整路径
        itmpath = os.path.join(of,itm)

        # 如果完整路径是目录（而非文件的话）
        if os.path.isdir(itmpath)&1:
            
            # 将文件名以.切分以修改第一个章节编号
            dir_name_list = itm.split(".")

            # 如果子目录(itm)开头的编号数字不等于父级目录编号，则修改
            if dir_name_list[0] != targetdir.split(".")[0]:
                dir_name_list[0] = targetdir.split(".")[0]
                newname = ".".join(dir_name_list)
                if os.path.exists(itmpath):
                    # print(itm,newname)
                    os.rename(itmpath,os.path.join(of,newname)) 
                else:
                    print("ERR!")







def replace_str_infile(org:str,new:str,filename:str):
    with open (filename,"w+") as fff:
        filecontent = fff.read()
        rorg = "\.".join(org.split("."))
        re.sub(rorg,new,filecontent)
        fff.seek(0)
        fff.write(filecontent)


def list_sub(dirpath:str,filetype:str):
    li_withdir = []
    li_md = []
    if os.path.exists(dirpath):
        li_withdir = os.listdir(dirpath)

    for itm in li_withdir:
        itm_fullpath = os.path.join(dirpath,itm)
        if os.path.isdir(itm_fullpath):
            # dirpath2 = os.path.join(itm,dirpath)
            li_md += list_sub(itm_fullpath,filetype)
        else:
            itmtype = os.path.splitext(itm_fullpath)[1]
            if itmtype==filetype:
                li_md += [itm_fullpath]

    return li_md


def replace_orderid(target_dir:str,parent_dir:str):
    # list all dir name, repalece the names in md file

    # 要替换的字符串来自目标目录的目录名列表
    filenames = os.listdir(os.path.join(parent_dir,target_dir))
    
    words_old = filenames.copy()

    for ii in range(len(filenames)):
        if os.path.isdir(os.path.join(parent_dir,target_dir,filenames[ii])):
            itm = filenames[ii]
            li_file = itm.split(".")
            li_file[0] = "7"
            words_old[ii] = ".".join(li_file)
        else:
            filenames.pop(ii)
            words_old.pop(ii)


    mdfiles = []
    for itm in os.listdir(parent_dir):
        if os.path.isdir(os.path.join(parent_dir,itm)):
            mdfiles += list_sub(basedir,".md")


    for jj in range(len(mdfiles)):
        for ii in range(len(filenames)):
            # replace_str_infile(filenames[ii],words_old[ii],mdfiles[jj])
            with open (mdfiles[jj].replace('\\', '/'),"r",encoding="UTF-8") as fff:
                filecontent = fff.read()
                finded = filecontent.find(words_old[ii])
                # print(words_old[ii][1:]) if jj ==1 else None
            if finded!=-1:
                newcontent = filecontent.replace(words_old[ii],filenames[ii])
                print("---"*32)
                print(mdfiles[jj])
                print(filecontent[finded:12])
                print(newcontent[finded:12])
        
                with open (mdfiles[jj].replace('\\', '/'),"w",encoding="UTF-8") as fff:
                    fff.write(newcontent)
            
replace_orderid(od,basedir)
