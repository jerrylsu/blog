Status: published
Date: 2019-04-13 06:35:27
Author: Jerry Su
Slug: Auto-generated-subtitles-for-any-video
Title: Auto-generated subtitles for any video
Category: 
Tags: Tools

[TOC]

## Autosub
[Autosub](https://github.com/agermanidis/autosub) is a utility for automatic speech recognition and subtitle generation. It takes a video or an audio file as input, performs voice activity detection to find speech regions, makes parallel requests to Google Web Speech API to generate transcriptions for those regions, (optionally) translates them to a different language, and finally saves the resulting subtitles to disk. It supports a variety of input and output languages (to see which, run the utility with the argument --list-languages) and can currently produce subtitles in either the SRT format or simple JSON.

## Install ffmpeg
- `sudo add-apt-repository ppa:djcj/hybrid`
- `sudo apt-get update`
- `sudo apt-get install ffmpeg`

## Install autosub
- `pip install autosub`

## Usage
- `autosub -S en -D en file_path`

