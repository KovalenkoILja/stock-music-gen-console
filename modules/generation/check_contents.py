import os

import magenta.music as mm


def init_contents():
    if os.path.exists("./content"):
        if not os.path.isfile("./content/polyphony_rnn.mag"):
            print("polyphony_rnn.mag doesnt find!")
            mm.notebook_utils.download_bundle('polyphony_rnn.mag', './content/')
            print("polyphony_rnn.mag successfully downloaded")
        if not os.path.isfile("./content/basic_rnn.mag"):
            print("basic_rnn.mag doesnt find!")
            mm.notebook_utils.download_bundle('basic_rnn.mag', './content/')
            print("basic_rnn.mag successfully downloaded")
        if not os.path.isfile("./content/mono_rnn.mag"):
            print("mono_rnn.mag doesnt find!")
            mm.notebook_utils.download_bundle('mono_rnn.mag', './content/')
            print("mono_rnn.mag successfully downloaded")
        if not os.path.isfile("./content/lookback_rnn.mag"):
            print("lookback_rnn.mag doesnt find!")
            mm.notebook_utils.download_bundle('lookback_rnn.mag', './content/')
            print("lookback_rnn.mag successfully downloaded")
        if not os.path.isfile("./content/attention_rnn.mag"):
            print("attention_rnn.mag doesnt find!")
            mm.notebook_utils.download_bundle('attention_rnn.mag', './content/')
            print("attention_rnn.mag successfully downloaded")
        if not os.path.isfile("./content/cat-mel_2bar_big.ckpt.data-00000-of-00001") \
                or not os.path.isfile("./content/cat-mel_2bar_big.ckpt.index"):
            print("models for interpolate doesnt find!")
    else:
        print("content folder doesnt find!")
        exit(1)
    print("all bundles set up")
