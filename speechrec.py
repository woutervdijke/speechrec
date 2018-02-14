#!/usr/bin/python

def uploadwav(filenamein):
    import os
    from google.cloud import storage
    from pydub import AudioSegment

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "googlecredentials.json"

    storage_client = storage.Client()

    bucket_name = 'voicerecwsvd'
    file_path = filenamein

    file_name = file_path.split("/")[-1]
    file_name_mono = file_name.replace(".wav","")+"mono"+'.wav'
    path_no_file = '/'.join(file_path.split("/")[:-1])
    file_path_mono = path_no_file+"/"+file_name_mono

    AudioSegment.converter = "/usr/local/bin/ffmpeg"
    sound = AudioSegment.from_wav(file_path)
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(44100)
    sound.export(file_path_mono,format="wav",
                           bitrate="44k")

    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_name_mono)
    blob.upload_from_filename(file_path_mono)

    return "gs://"+bucket_name+"/"+file_name_mono

def transcribe_gcs(gcs_uri, language):
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code=language)

    operation = client.long_running_recognize(config, audio)

    print('Waiting for operation to complete...')
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print('Transcript: {}'.format(result.alternatives[0].transcript))
        print('Confidence: {}'.format(result.alternatives[0].confidence))


def main():
    import argparse
    parser = argparse.ArgumentParser()
    requiredNamed = parser.add_argument_group('required arguments')
    requiredNamed.add_argument("-i", "--ifile", help="select the input WAV file")
    requiredNamed.add_argument("-l", "--lang", help="choose the language of your audio (e.g. en_US)")
    args = parser.parse_args()
    filein = args.ifile
    language = args.lang
    if filein == None and language == None:
        print("Please specify your input file with -i and your language with -l. Use -h for help")
    elif filein == None:
        print("Please specify your input file with -i")
    elif language == None:
        print("Please specify your language with -l")
    else:
        print(transcribe_gcs(uploadwav(filein), language))

if __name__ == "__main__":
   main()
