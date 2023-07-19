# 原书更新了一个插入的第二章，从第二章开始原来的文件名和链接都需要修改章节号（+1）

# todo:
# - 理清楚修改一个章节号都需要哪几步?
#   - 第一轮:
#       - 更新目标章 所有子节的 目录名
#       - 更新全书文本内容中 所有该章的             [章名] 及其 [连接]
#       - 修改全书文本内容中 该章下面 [子节] 的     [节名] 和 [连接]
#   - 第二轮:
#       - 修改图片 连接(ASCII码) 和 文件名 上的章节号
#   - 
#   - 

import os
import re

# 需要修改子目录编号的父级目录（先改好编号）

# 本py文件所在目录（父级目录同级）
basedir = os.getcwd()

def isIntSeriously(number):
    result = False
    try:
        n = float(number)
        if n.is_integer() and str(number).count('.') == 0:
            result =True
    except :
        # print('非数字')
        pass

    return result


def update_all1typefiles_in_wholebook(book_path:str,chapterpath:str,oldstr:str,newstr:str,filetype=".md"):
    # 没用上
    # 更新全书所有文本内容 (md文件) 中的指定字符串 (章节名) 
    #   应该给出 新\旧章名 \ 整书的完整路径(修改全书文本内容即所有md文件) \ 目标章的完整路径(修改子目录名)
    #   检查章目录名是不是新的章名, 不是就修改
    # 每次应该只修改一章

    if os.path.isdir(book_path) & os.path.isdir(chapterpath) & False:

        all_typed_fileslist = list_sub(book_path,filetype)

        for jj in range(len(all_typed_fileslist)):
            with open (all_typed_fileslist[jj].replace('\\', '/'),"r",encoding="UTF-8") as fff:
                filecontent = fff.read()
                finded = filecontent.find(oldstr)

            if finded!=-1:
                newcontent = filecontent.replace(oldstr,newstr)
                print("---"*32)
                print(all_typed_fileslist[jj])
                print(filecontent[finded:12])
                print(newcontent[finded:12])
        
                with open (all_typed_fileslist[jj].replace('\\', '/'),"w",encoding="UTF-8") as fff:
                    fff.write(newcontent)

def replace_str_in1file(org:str,new:str,filename:str):
    with open (filename,"w+") as fff:
        filecontent = fff.read()
        rorg = "\.".join(org.split("."))
        re.sub(rorg,new,filecontent)
        fff.seek(0)
        fff.write(filecontent)

def list_sub(dirpath:str,filetype:str):
    # dirpath: os.getcwd()
    # filetype: ".md"
    # list_sub(os.getcwd(),".md")
    
    if (filetype=="dir"):
        li_withdir = []
        li_res = []
        if os.path.exists(dirpath):
            li_withdir = os.listdir(dirpath)

        for itm in li_withdir:
            itm_fullpath = os.path.join(dirpath,itm)
            if (os.path.isdir(itm_fullpath)&(isIntSeriously(itm.split(".")[0]))):
                li_res += [os.path.basename(itm_fullpath)]
                li_res += list_sub(itm_fullpath,filetype)

    else:

        li_withdir = []
        li_res = []
        if os.path.exists(dirpath):
            li_withdir = os.listdir(dirpath)

        for itm in li_withdir:
            itm_fullpath = os.path.join(dirpath,itm)
            if os.path.isdir(itm_fullpath):
                # dirpath2 = os.path.join(itm,dirpath)
                li_res += list_sub(itm_fullpath,filetype)
            else:
                itmtype = os.path.splitext(itm_fullpath)[1]
                if itmtype==filetype:
                    li_res += [itm_fullpath]

    return li_res

# 修改章目录名 (根据newstr)
def update_tgtchapter_dirsname(book_path:str,chapterpath:str,oldstr:str,newstr:str):
    # 重命名章目录.
    
    if os.path.isdir(book_path) & os.path.isdir(chapterpath) & 1:

        if chapterpath != os.path.join(book_path,newstr):
            # 重命名章目录, 如果章目录名不符合新章名 (newstr)
            os.rename(chapterpath,os.path.join(book_path,newstr)) 
    
    if os.path.isdir(os.path.join(book_path,newstr)):
        return os.path.join(book_path,newstr)

def update_tgtchapter_subdirsname(chapterpath:str):
    # 更新所有子目录章节号与父目录一致

    # 被操作父级目录所有子目录的列表
    chapter_subdirs = os.listdir(chapterpath)
    chapter_name = os.path.basename(chapterpath)

    for subdir in chapter_subdirs:

        # 每个子目录的完整路径
        subpath = os.path.join(chapterpath,subdir)

        # 如果完整路径是目录（而非文件的话）
        if os.path.isdir(subpath)&1:
            
            # 将文件名以.切分以修改第一个章节编号
            dir_name_list = subdir.split(".")

            # 如果子目录(subdir)开头的编号数字不等于父级目录编号，则修改
            if dir_name_list[0] != chapter_name.split(".")[0]:
                dir_name_list[0] = chapter_name.split(".")[0]
                newname = ".".join(dir_name_list)
                if os.path.exists(subpath):
                    os.rename(subpath,os.path.join(chapterpath,newname)) 
                else:
                    print("ERR!")

def update_chapter_number(book_path:str,chapterpath:str,oldnum:str,newnum:str,filetype=".md"):
    # 更新全书指定章的章节号, 包括章名和节名在文本及连接中的章节号

    # 列出所有需要处理的原字段(章名, 节名), 先把章名填进去
    titles_list = [os.path.basename(chapterpath)]
    titles_list += list_sub(chapterpath,"dir")
    print(titles_list)


    if os.path.isdir(book_path) & os.path.isdir(chapterpath) & 1:

        all_typed_fileslist = list_sub(book_path,filetype)

        for tt in titles_list:

            ttlst = tt.split(".")

            ttlst[0] = oldnum
            oldstr = ".".join(ttlst)

            ttlst[0] = newnum
            newstr = ".".join(ttlst)

            # update_all1typefiles_in_wholebook(book_path,chapterpath,oldstr,newstr)    # 这个函数应该可以替换下面的循环段, 但是不好使, 先用不着了下次再说

            for jj in range(len(all_typed_fileslist)):
                with open (all_typed_fileslist[jj].replace('\\', '/'),"r",encoding="UTF-8") as fff:
                    filecontent = fff.read()
                    finded = filecontent.find(oldstr)

                if finded!=-1:
                    newcontent = filecontent.replace(oldstr,newstr)
                    print("---"*32)
                    print(all_typed_fileslist[jj])
                    print(filecontent[finded:12])
                    print(newcontent[finded:12])
            
                    with open (all_typed_fileslist[jj].replace('\\', '/'),"w",encoding="UTF-8") as fff:
                        fff.write(newcontent)


def main():
    
    # 准备变量
    book_path = r"C:\Users\lukel\Documents\study\Training_Python\self_learn\python-data-structure-cn"
    tgt_chapter_name = "2.算法分析"
    oldnum = 2
    newnum = oldnum+1

    tgt_chapter_path = os.path.join(book_path,tgt_chapter_name)
    tgt_str = [tgt_chapter_name,tgt_chapter_name.replace(str(oldnum)+".",str(newnum)+".")]
    
    # 1.修改章目录名 (根据 newstr )
    new_chapter_path = update_tgtchapter_dirsname(book_path, tgt_chapter_path, tgt_str[0], tgt_str[1])

    # 2.修改节目录名 (根据 章目录名 )
    update_tgtchapter_subdirsname(new_chapter_path)
    
    # 3.在全书范围内, 修改目标章号 (根据)
    update_chapter_number(book_path, os.path.join(book_path,new_chapter_path), str(oldnum), str(newnum))

    print(tgt_str)

if __name__=="__main__":
    # main(tgt_chapter_name)
    # print(list_sub(os.getcwd(),".md"))
    main()
