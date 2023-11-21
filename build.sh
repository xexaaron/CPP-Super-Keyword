#!/usr/bin/bash

projName="Super"

#Define directories of script and project
scriptDir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
projDir="$scriptDir"
rsrcDir="$scriptDir/rsrc"
toolsDir="$scriptDir/Tools"

# SuperGen.py generates json data from the cpp and hpp files in the src directory of your project.
#   SuperImpl.py goes through the src directory again and replaces the 'Super' keyword
#   with the corresponding parent value from the json data file.
if [ -d "$toolsDir/Super" ]; then
    (
    cd "$toolsDir/Super" || exit
    python SuperGen.py
    python SuperImpl.py
  )
fi

# Export variables to be used in CMakeLists.txt Configuration
export CMProjName=$projName
export RsrcDir=$rsrcDir
export ToolsDir=$ToolsDir

cmake -S . -B build -G "Visual Studio 17 2022" -A x64 
cmake --build build --config Release

# Determine post-build state
if [ $? -eq 0 ]; then
    echo ""
    echo "Build successful"
    if [ -d "$toolsDir/Super" ]; then
      (
      cd "$toolsDir/Super" || exit
      python SuperLog.py
      )
    fi

    mv "$projDir"/build/Release/"$projName".exe "$projDir"
else
    echo "Build failed!"
fi

# SuperDestruct.py will launch after the build process and the executable
# has been generated, going through the src directory again and replacing 
# the value of parent from the json data file with the 'Super'
# It will not affect the word super if 'Super' has letters preceding it.
# It will also check to make sure their is two colons after it. 
if [ -d "$toolsDir/Super" ]; then
    (
    cd "$toolsDir/Super" || exit
    python SuperDestruct.py
  )
fi