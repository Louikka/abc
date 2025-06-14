@echo off


  :: name of the source file
set /p f=Enter name of the source file : 



  :: compile into assembly
::gcc %f%.c  -S

  :: compile into object file
::gcc %f%.c  -c  -Wall -O2

  :: linking object file into executable
::gcc %f%.o  -o %f%.exe  -s



  :: compiling without making any additional files
gcc %f%.c  -o %f%.exe  -O2 -s



echo Compiled successfully!

pause