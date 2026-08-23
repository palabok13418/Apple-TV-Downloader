
# __Apple TV 4K SDR/HDR/Dolby Vision & Atmos Downloader__

 <div size='20px'> A Tool To download 4K HDR DV SDR from Apple TV
</div>

```
usage: python bad37.py [-h] [--url URL_SEASON] [--tqdm] [--nv] [--na] [--ns] [--all-season] [-e EPISODESTART] [-s SEASON]
                [--tag TAG] [-q CUSTOMQUALITY] [-o OUTPUT] [--keep] [--info] [--no-mux] [--only-2ch-audio]
                [--alang [AUDIOLANG ...]] [--slang [SUBLANG ...]] [--flang [FORCEDLANG ...]] [--no-cleansubs] [--hevc]
                [--uhd] [--license] [-licenses-as-json] [--debug] [--aformat-51ch AFORMAT_51CH] [--nc]
                [-c {widevine,playready}] [--ap {aac,ac3,atmos}] [--atmos] [--ad] [--hdr] [-r {la,us}]
                [--vp {h264,hevc,hdr}] [--m3u8] [--file TXTPATH] [--tlang TITLELANG] [--scenario1 SCENARIODSNP]
                [--scenario2 SCENARIOSTAR] [--proxy PROXY]
                [content]
```

# __About This Repo__
This repo is from https://github.com/TDenisM/APPLE-TV-4K-Downloader and https://github.com/weapon121/APPLE-TV-4K-Downloader (They are the same)

They both have a 41 rating score for scanrepo.dev
<img src="https://raw.githubusercontent.com/palabok13418/Apple-TV-Downloader/refs/heads/main/photos/Screenshot%202026-08-23%20015116.png">
<img src="https://raw.githubusercontent.com/palabok13418/Apple-TV-Downloader/refs/heads/main/photos/Screenshot%202026-08-23%20020611.png">

Scanned with bandit removed all High and Medium Severity things only leaving 17 Low

Scan this repo with scanrepo.dev and with the bandit pip 

```
pip install bandit
 python -m bandit -r [PATH TO THIS REPO]
```
  The command above is to verify this repo does have 17 Low

  The only error I can't fix is, Error: Could not extract Apple TV authorization token from webpage HTML.
<br>
 <p>
  Final Video can be in 
  <picture style="display: inline-block; vertical-align: middle;">
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/palabok13418/Apple-TV-Downloader/refs/heads/main/photos/4k_black.png">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/palabok13418/Apple-TV-Downloader/refs/heads/main/photos/4k_white.png">
    <img src="https://raw.githubusercontent.com/palabok13418/Apple-TV-Downloader/refs/heads/main/photos/4k_white.png" alt="4K" width="37" height="21" style="vertical-align: middle;">
  </picture>, 
  <picture style="display: inline-block; vertical-align: middle;">
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/palabok13418/Apple-TV-Downloader/refs/heads/main/photos/hdr_black.png">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/palabok13418/Apple-TV-Downloader/refs/heads/main/photos/hdr_white.png">
    <img src="https://raw.githubusercontent.com/palabok13418/Apple-TV-Downloader/refs/heads/main/photos/hdr_white.png" alt="HDR" width="48" height="21" style="vertical-align: middle;">
  </picture>, 
  <picture style="display: inline-block; vertical-align: middle;">
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/palabok13418/Apple-TV-Downloader/refs/heads/main/photos/dolbyatmos_vision_black.png">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/palabok13418/Apple-TV-Downloader/refs/heads/main/photos/dolbyatmos_vision_white.png">
    <img src="https://raw.githubusercontent.com/palabok13418/Apple-TV-Downloader/refs/heads/main/photos/dolbyatmos_vision_white.png" alt="Dolby Atmos & Vision" width="74" height="34" style="vertical-align: middle;">
  </picture>
</p>
