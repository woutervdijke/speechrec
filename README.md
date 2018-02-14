# Speechrec.py

## A command line tool for turning audio into text

This script uses the Google Cloud Speech API to perform simple speech transcription (speech-to-text) from .wav audio files. It supports all the [many languages the Google Cloud Speech API supports](https://cloud.google.com/speech/docs/languages) and it should support any .wav file.

## Set up:
1. You'll need to register with [Google Cloud Platform](https://console.cloud.google.com) and create a project
1. In the project, enable the Google Cloud Speech API
1. In the Credentials section of your Google Cloud Platform project, create a Service Account Key (JSON version)
1. Place the JSON file in the same folder as this code and rename it to `googlecredentials.json`
1. Install the required packages using `pip install -r requirements.txt`

## Usage:
From the command line, run `python speechrec.py -i <path_to_input_file> -l <language_code>`. Make sure the input file is a .wav audio file. Use [this list](https://cloud.google.com/speech/docs/languages) to find the right code for your language. For quick reference:
* English (USA): en_US
* English (UK): en_UK
* Dutch: nl_NL
* French (France): fr_FR
* Etc...

## TODO:
 * Clean up and refactor code
 * Add a check if file is supported
 * Add upport for other audio files
 * Someday create a web based version of this
 * Etc...
