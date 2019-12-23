from modules.generation.generator_setup import setup_generator
from modules.generation.initialisation_rnn import init_melody_rnn
import magenta.music as mm
import time


def generate_continue_for(name, input_sequence, model_name, num_steps, temperature):
    start = time.time()
    melody_rnn = init_melody_rnn(model_name)
    generator_options = setup_generator(input_sequence, melody_rnn, num_steps, temperature)
    sequence = melody_rnn.generate(input_sequence, generator_options)
    filename = name + '_' + model_name + '_output.mid'
    mm.sequence_proto_to_midi_file(sequence, './output/' + filename)
    end = time.time()
    print(filename + " created")
    print("That took:" + (end - start).__str__())
