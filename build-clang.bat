@echo off


  :: name of the source file
set /p f=Enter name of the source file : 


  :: compile into assembly
:: gcc %f%.c  -S

  :: compile into object file
gcc %f%.c  -c  -Wall -O2

  :: linking into executable
gcc %f%.o  -o %f%.exe  -s


echo Compiled successfully!


pause