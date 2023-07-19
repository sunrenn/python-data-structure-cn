

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

    # mdfiles应该是列出全书所有指定类型的文件
    mdfiles = []
    for itm in os.listdir(parent_dir):
        if os.path.isdir(os.path.join(parent_dir,itm)):
            mdfiles += list_sub(os.getcwd(),".md")


    for jj in range(len(mdfiles)):
        for ii in range(len(filenames)):
            # replace_str_in1file(filenames[ii],words_old[ii],mdfiles[jj])
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
           