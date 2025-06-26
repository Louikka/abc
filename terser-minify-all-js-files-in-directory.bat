@echo off


setlocal EnableDelayedExpansion

for %%f in (*.js) do (
    set s=%%~nf
    if "!s:~-4!" neq ".min" (
        call terser !s!.js --config-file=terser-config.json -o !s!.min.js
    )
)

endlocal


pause