@echo off
set "projName=Super"

REM Define directories of script and project
set "scriptDir=%~dp0"
set "projDir=%scriptDir%"
set "rsrcDir=%scriptDir%\rsrc"
set "toolsDir=%scriptDir%\Tools"

REM SuperGen.py generates json data from the cpp and hpp files in the src directory of your project.
REM SuperImpl.py goes through the src directory again and replaces the 'Super' keyword
REM with the corresponding parent value from the json data file.
if exist "%toolsDir%\Super" (
    pushd "%toolsDir%\Super" && (
        python SuperGen.py
        python SuperImpl.py
        popd
    )
)

REM Export variables to be used in CMakeLists.txt Configuration
set "CMProjName=%projName%"
set "RsrcDir=%rsrcDir%"
set "ToolsDir=%ToolsDir%"

cmake -S . -B build -G "Visual Studio 17 2022" -A x64 
cmake --build build --config Release

REM Determine post-build state
if %errorlevel% equ 0 (
    echo.
    echo Build successful
    move "%projDir%\build\Release\%projName%.exe" "%projDir%"
) else (
    echo Build failed!
)

REM SuperDestruct.py will launch after the build process and the executable
REM has been generated, going through the src directory again and replacing 
REM the value of parent from the json data file with the 'Super'
REM It will not affect the word super if 'Super' has letters preceding it.
REM It will also check to make sure their is two colons after it. 
if exist "%toolsDir%\Super" (
    pushd "%toolsDir%\Super" && (
        python SuperDestruct.py
        popd
    )
)