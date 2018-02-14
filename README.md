# Speechrec.py

## A command line tool for turning audio into text

This script uses the Google Cloud Speech API to perform simple speech transcription (speech-to-text) from .wav audio files. It supports all the [many languages the Google Cloud Speech API supports](https://cloud.google.com/speech/docs/languages) and it should support any .wav file.

### Cheaaap audio transcriptions!
The Google Cloud Speech API is free to use for [up to 60 minutes of audio per month](https://cloud.google.com/speech/pricing). After those 60 minutes, it costs $0.006 USD per 15 seconds of audio. That's 2.4 cents per minute, rounded up to the next 15 seconds. That's just $1.44 for an hour of audio. 
This code should probably support audio files that long, but also it might break, so let me know when that happens. Or when something else weird happens. Or if you want to help me improve my code. Feel free to submit issues or [tweet at me](http://www.twitter.com/woutervd).
## Set up:
1. You'll need to register with [Google Cloud Platform](https://console.cloud.google.com) and create a project
1. In the project, enable the Google Cloud Speech API
1. In the Credentials section of your Google Cloud Platform project, create a Service Account Key (JSON version)
1. Place the JSON file in the same folder as this code and rename it to `googlecredentials.json`
1. Install the required packages using `pip install -r requirements.txt`
1. You'll also need to install ffmpeg and set up a Google Cloud Storage bucket (these instructions TODO)

## Usage:
From the command line, run `python speechrec.py -i <path_to_input_file> -l <language_code>`. Make sure the input file is a .wav audio file. Use [this list](https://cloud.google.com/speech/docs/languages) to find the right code for your language. For quick reference:
* English (USA): en_US
* English (UK): en_UK
* Dutch: nl_NL
* French (France): fr_FR
* Etc...

## TODO:

 * Handle different GCS Bucket names (setup.py?)
 * Remove files from computer and Google Cloud Storage after use
 * Add Google Cloud Storage instructions to Readme
 * Clean up and refactor code
 * Add a check if file is supported
 * Add support for other audio file types
 * Someday create a web based version of this
 * Etc...
