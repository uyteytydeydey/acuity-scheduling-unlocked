# Video Editing Script

This repository includes a Windows batch script (`video_edit.bat`) for creating promotional videos using FFmpeg.

## Prerequisites

1. **FFmpeg** - Must be installed and available in your system PATH
   - Download from: https://ffmpeg.org/download.html
   - Add to PATH: https://www.wikihow.com/Install-FFmpeg-on-Windows

2. **Video Files** - The following video files must be present in the same directory as the script:
   - `01_city.mp4`
   - `02_tower.mp4`
   - `03_king.mp4`
   - `04_motorcade.mp4`
   - `05_lights.mp4`
   - `06_life.mp4`
   - `07_street.mp4`
   - `08_aerial.mp4`

3. **Audio File** - Background music:
   - `music.mp3`

4. **Font File** - Arial Bold font (default Windows location):
   - `C:/Windows/Fonts/arialbd.ttf`

## Script Features

The script generates two video outputs:

### 1. 16:9 Aspect Ratio (Landscape)
- **Output:** `shorts_16x9_newlive.mp4`
- **Resolution:** 1920x1080 (Full HD)
- **Duration:** ~50 seconds
- **Frame Rate:** 60 FPS
- **Purpose:** Standard widescreen format for YouTube, web, presentations

### 2. 9:16 Aspect Ratio (Vertical/Portrait)
- **Output:** `shorts_9x16_newlive.mp4`
- **Resolution:** 1080x1920 (Vertical HD)
- **Duration:** ~30 seconds
- **Frame Rate:** 60 FPS
- **Purpose:** Social media shorts (TikTok, Instagram Reels, YouTube Shorts)

## Video Processing Details

Each video includes:
- **Scaling & Cropping** - Videos are scaled and cropped to fit the target aspect ratio
- **Frame Rate Conversion** - All clips converted to 60 FPS
- **Text Overlays** - Animated text with customizable messages:
  - "A city without a story..."
  - "NEW LIVE"
  - "This is not a game"
  - "This is life"
  - "NEW LIVE - Roleplay\NLife starts now"
- **Audio Processing** - Background music with volume adjustment (0.9 for 16:9, 0.95 for 9:16)
- **Video Encoding** - H.264 codec with CRF 18 (high quality)
- **Audio Encoding** - AAC codec at 192k bitrate

## Customization

### Changing Text
Edit the text variables at the top of the script:
```batch
set T1=Your custom text here
set T2=Another custom text
set T3=Yet another text
set T4=More text
set T5=Final text with \Nline breaks
```

Note: Use `\N` for line breaks in text overlays.

### Changing Music
Replace `music.mp3` with your desired audio file, or update the script:
```batch
set MUSIC=your_music_file.mp3
```

### Changing Font
Update the font path:
```batch
set FONT="C\:/Path/To/Your/Font.ttf"
```

Note: Use forward slashes (/) and escape colons (\:) in the path.

### Adjusting Clip Durations
Each video input has a trim parameter. For example:
```
trim=0:6  (6 seconds)
trim=0:9  (9 seconds)
trim=0:10 (10 seconds)
```

Modify these values in the filter_complex sections to change individual clip durations.

### Changing Video Quality
Adjust the CRF (Constant Rate Factor) value:
```batch
-crf 18  (current: high quality, larger file)
-crf 23  (balanced: good quality, medium file)
-crf 28  (lower quality, smaller file)
```

Lower CRF = Higher quality & larger file size (0-51 range, 18-28 recommended)

## Usage

1. Ensure all prerequisites are met
2. Place all required video and audio files in the same directory as `video_edit.bat`
3. Double-click `video_edit.bat` or run it from command prompt
4. Wait for processing to complete (may take several minutes depending on video length and system specs)
5. Find the output files:
   - `shorts_16x9_newlive.mp4`
   - `shorts_9x16_newlive.mp4`

## Troubleshooting

### "ffmpeg is not recognized as an internal or external command"
- FFmpeg is not installed or not in your PATH
- Install FFmpeg and add it to your system PATH

### "No such file or directory" errors
- Ensure all input video files (01_city.mp4, etc.) are present
- Check that `music.mp3` exists in the same directory

### Font rendering issues
- Verify the font path is correct
- Try using a different font (e.g., arial.ttf)
- Ensure font file has read permissions

### Script runs but produces no output
- Check that input videos are valid and not corrupted
- Ensure sufficient disk space for output files
- Review the console output for specific FFmpeg errors

## Technical Specifications

### Video Codec Settings
- **Codec:** libx264 (H.264)
- **Preset:** veryfast (good speed/quality balance)
- **CRF:** 18 (high quality)
- **Pixel Format:** yuv420p (maximum compatibility)

### Audio Codec Settings
- **Codec:** AAC
- **Bitrate:** 192 kbps (high quality)

### Processing Features
- Automatic aspect ratio handling
- Frame rate standardization to 60 FPS
- Sample aspect ratio correction (setsar=1)
- Synchronized audio/video timestamps

## License

This script is provided as-is for video editing purposes.
