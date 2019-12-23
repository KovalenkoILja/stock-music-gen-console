import magenta.music as mm
import time


def generate_interpolation_for(model_name, music_vae, num_steps, length, first_sequence, second_sequence):
    start = time.time()
    note_sequences = music_vae.interpolate(
        first_sequence,
        second_sequence,
        num_steps=num_steps,
        length=length)
    interp_seq = mm.sequences_lib.concatenate_sequences(note_sequences)
    filename = model_name + '_output.mid'
    mm.sequence_proto_to_midi_file(interp_seq, './output/' + filename)
    end = time.time()
    print(filename + " created")
    print("That took:" + (end - start).__str__())
