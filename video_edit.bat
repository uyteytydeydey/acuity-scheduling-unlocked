@echo off
setlocal enabledelayedexpansion

REM ===== SETTINGS =====
set FONT="C\:/Windows/Fonts/arialbd.ttf"
set MUSIC=music.mp3

REM ===== TEXTS =====
set T1=A city without a story...
set T2=NEW LIVE
set T3=This is not a game
set T4=This is life
set T5=NEW LIVE - Roleplay\NLife starts now

REM ===== COMMON FILTER (each clip trimmed) =====
REM You can adjust each duration with -t per input if needed.

REM ===== BUILD 16:9 =====
ffmpeg -y ^
-i 01_city.mp4 ^
-i 02_tower.mp4 ^
-i 03_king.mp4 ^
-i 04_motorcade.mp4 ^
-i 05_lights.mp4 ^
-i 06_life.mp4 ^
-i 07_street.mp4 ^
-i 08_aerial.mp4 ^
-i %MUSIC% ^
-filter_complex ^
"
[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60,trim=0:6,setpts=PTS-STARTPTS,drawtext=fontfile=%FONT%:text='%T1%':x=(w-text_w)/2:y=h*0.12:fontsize=54:box=1:boxborderw=18:alpha=0.95[v0];
[1:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60,trim=0:6,setpts=PTS-STARTPTS[v1];
[2:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60,trim=0:9,setpts=PTS-STARTPTS,drawtext=fontfile=%FONT%:text='%T2%':x=(w-text_w)/2:y=(h-text_h)/2:fontsize=120:box=1:boxborderw=22:alpha=0.98[v2];
[3:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60,trim=0:6,setpts=PTS-STARTPTS[v3];
[4:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60,trim=0:10,setpts=PTS-STARTPTS[v4];
[5:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60,trim=0:7,setpts=PTS-STARTPTS,drawtext=fontfile=%FONT%:text='%T3%':x=(w-text_w)/2:y=h*0.14:fontsize=64:box=1:boxborderw=18:alpha=0.95[v5];
[6:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60,trim=0:7,setpts=PTS-STARTPTS,drawtext=fontfile=%FONT%:text='%T4%':x=(w-text_w)/2:y=h*0.14:fontsize=64:box=1:boxborderw=18:alpha=0.95[v6];
[7:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1,fps=60,trim=0:5,setpts=PTS-STARTPTS,drawtext=fontfile=%FONT%:text='%T5%':x=(w-text_w)/2:y=(h-text_h)/2:fontsize=72:box=1:boxborderw=22:alpha=0.98[v7];

[v0][v1][v2][v3][v4][v5][v6][v7]concat=n=8:v=1:a=0[v];
[8:a]atrim=0:50,asetpts=PTS-STARTPTS,volume=0.9[a]
" ^
-map "[v]" -map "[a]" ^
-c:v libx264 -preset veryfast -crf 18 -pix_fmt yuv420p ^
-c:a aac -b:a 192k ^
shorts_16x9_newlive.mp4

REM ===== BUILD 9:16 (vertical) =====
ffmpeg -y ^
-i 01_city.mp4 ^
-i 02_tower.mp4 ^
-i 03_king.mp4 ^
-i 04_motorcade.mp4 ^
-i 05_lights.mp4 ^
-i 06_life.mp4 ^
-i 07_street.mp4 ^
-i 08_aerial.mp4 ^
-i %MUSIC% ^
-filter_complex ^
"
[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=60,trim=0:3,setpts=PTS-STARTPTS,drawtext=fontfile=%FONT%:text='%T1%':x=(w-text_w)/2:y=h*0.12:fontsize=64:box=1:boxborderw=18:alpha=0.95[v0];
[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=60,trim=0:4,setpts=PTS-STARTPTS[v1];
[2:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=60,trim=0:4,setpts=PTS-STARTPTS,drawtext=fontfile=%FONT%:text='%T2%':x=(w-text_w)/2:y=(h-text_h)/2:fontsize=140:box=1:boxborderw=24:alpha=0.98[v2];
[3:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=60,trim=0:4,setpts=PTS-STARTPTS[v3];
[4:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=60,trim=0:7,setpts=PTS-STARTPTS[v4];
[5:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=60,trim=0:4,setpts=PTS-STARTPTS,drawtext=fontfile=%FONT%:text='%T3%':x=(w-text_w)/2:y=h*0.14:fontsize=72:box=1:boxborderw=18:alpha=0.95[v5];
[6:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=60,trim=0:4,setpts=PTS-STARTPTS,drawtext=fontfile=%FONT%:text='%T4%':x=(w-text_w)/2:y=h*0.14:fontsize=72:box=1:boxborderw=18:alpha=0.95[v6];
[7:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=60,trim=0:3,setpts=PTS-STARTPTS,drawtext=fontfile=%FONT%:text='%T5%':x=(w-text_w)/2:y=(h-text_h)/2:fontsize=80:box=1:boxborderw=22:alpha=0.98[v7];

[v0][v1][v2][v3][v4][v5][v6][v7]concat=n=8:v=1:a=0[v];
[8:a]atrim=0:30,asetpts=PTS-STARTPTS,volume=0.95[a]
" ^
-map "[v]" -map "[a]" ^
-c:v libx264 -preset veryfast -crf 18 -pix_fmt yuv420p ^
-c:a aac -b:a 192k ^
shorts_9x16_newlive.mp4

echo Done!
pause
