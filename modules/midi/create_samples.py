import magenta.music as mm
from modules.common.create_dir import check_dir
from modules.midi.twinkle_twinkle import twinkle_twinkle
from modules.midi.teapot import teapot
from modules.midi.drums import drums


def create_midi_samples():
    tw_tw = twinkle_twinkle()
    tea = teapot()
    drm = drums()
    path = "./output"
    check_dir(path)
    mm.sequence_proto_to_midi_file(tw_tw, path + "/" + 'twinkle_twinkle_sample.mid')
    print("twinkle_twinkle_sample.mid created")
    mm.sequence_proto_to_midi_file(tea, path + "/" + 'teapot_sample.mid')
    print("teapot_sample.mid created")
    mm.sequence_proto_to_midi_file(drm, path + "/" + 'drums_sample.mid')
    print("drums_sample.mid created")
