# CPP-Super-Keyword
--------------------------------------------------------------------------------------------------
# build.sh / build.bat
  * Run build command to generate cmake project files.
  * Running the build script subsequently runs the necessary python scripts to
    handle the implementation of the Super keyword in the C++ project.
--------------------------------------------------------------------------------------------------
# SuperGen.py
  * SuperGen.py is the first python script to be executed by the build script and it runs
    before the project is built.
  * Upon executing it takes the .hpp and .cpp files inside your project root directory's
    'src' directory and outputs a json file where each object is the filepath of the .cpp/.hpp
    file and each object contains the child and parent class names.
  
--------------------------------------------------------------------------------------------------
# SuperImpl.py
  * SuperImpl.py is the second python script to be executed by the build script and it runs
    before the project is built.
  * Upon executing it reads the json data file created by SuperGen.py, goes to the file listed
    in the json data and replaces instances of the keyword 'Super' with the name of the parent
    data listed in the json object.
  * SuperImpl.py logs all instances of replacement inside a file called change_log.txt located
    in the same directory as this script (Root/Tools/Super).
--------------------------------------------------------------------------------------------------
# SuperLog.py
  * SuperLog.py is the third python script to be executed by the build script and it runs after
    the build has completed succesfully. 
  * Upon executing it reads the change_log.txt generated by the SuperImpl.py script and then
    logs the amount of classes that use the 'Super' keyword.
--------------------------------------------------------------------------------------------------
# SuperDestruct.py
  * SuperDestruct.py is the fourth python script to be executed by the build script.
  * After the project has been built SuperDestruct.py rereads the json data file and reverses
    the changes made by SuperImpl.py.
  * SuperDestruct.py logs all instances of replacement inside a file called reverse_change_log.txt
    located in the same directory as this script (Root/Tools/Super).
    
