@echo off

set "pasta=ambiente-dev"

call "%pasta%"\Scripts\deactivate

rd /S /Q "%pasta%"

exit


