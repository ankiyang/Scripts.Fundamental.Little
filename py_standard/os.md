##os:


**os.getcwd()** 得到当前工作路径

**os.listdir()** 返回指定目录下所有文件,目录名

**os.remove()** 删除一个文件

**os.removedirs(r"/../.")** 删除多个目录

**os.rmdir()**  删除空文件夹

**os.path.isfile()** 检验给出的路径是否是一个文件

**os.path.isdir()** 检验给出的路径是否是一个目录

**os.path.isabs()** 判断是否是绝对路径

**os.path.exits()** 检验给出的路径是否真的存在

**os.path.split()** 返回一个路径的目录名和文件名

**shutil.rmtree()** 删除一个文件夹以及其中所有文件


###创建和管理进程 os.exec*()

**os.execvp(program, (program,)+args)**  
   example:  os.execvp("python", ("python",)+tuple(['xxx.py']))
    
    starts a new process, replacing the current one.
   it searches for the program xxx.py along the standard path, passes the contents of the second argument tuple as individual arguments to that program, and runs it with the current set of environment variables.
    
