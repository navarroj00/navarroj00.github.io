@ECHO OFF
ECHO This batch file was written by Jordan M. Navarro and a partner who chooses to remain anonymous. This file requires you to have ffmpeg.exe and RAD Video Tools installed. You can configure the parameters of this file through the file directly. This file must be placed in the same directory as ffmpeg.exe in order to run properly.
ECHO.
PAUSE

REM Input the name of the Bink Video here, without the file extension.
set filename=

REM Convert Bink 1 Video (.bik) into a Bink 2 Video (.bk2).
copy %filename%.bik %filename%.bk2

ECHO.
ECHO Make sure the new Bink 2 Video (.bk2) has the correct audio and is playable.
ECHO.
PAUSE

REM Convert the new Bink 2 Video into an Audio Video Interleave (.avi). Select Microsoft Video 1, Compression Quality: 75.
ECHO.
ECHO Select Microsoft Video 1, Compression Quality: 75.
"C:\Program Files (x86)\RADVideo\binkconv.exe" %filename%.bk2 %filename%.avi /N0 /#

REM Encode the new AVI (.avi) into MP4 (.mp4) format and save as an MP4 File.
ffmpeg -i %filename%.avi -c:v libx264 -crf 19 -preset slow -c:a aac -strict experimental -b:a 192k -ac 2 %filename%.mp4

ECHO.
ECHO Ensure that the quality of the new MP4 File is acceptable.
ECHO.
ECHO If the quality on the MP4 File is not acceptable, change the "19" in "-crf 19" instruction to a smaller integer.
ECHO.
PAUSE