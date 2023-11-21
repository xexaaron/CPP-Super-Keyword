# CMakeLists.txt

#SETUP
cmake_minimum_required(VERSION 3.27)
set (projName $ENV{CMprojName})
set(RSRC_DIR "$ENV{RsrcDir}/") 
set(TOOL_DIR "$ENV{ToolsDir}/")
project(${projName})


#VARIABLES
set(CMAKE_CXX_STANDARD 17)
set(SOURCE_FILES main.cpp 
				src/example/exampleParent.cpp
				src/example/exampleChild.hpp
				src/example/exampleGrandChild.hpp) 



add_executable(${PROJECT_NAME} ${SOURCE_FILES})
