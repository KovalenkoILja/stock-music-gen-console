from magenta.music.protobuf import generator_pb2

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


def generate_continue_for_polyphony(input_sequence, model_name, name, num_steps, polyphony_rnn, temperature):
    start = time.time()
    last_end_time = (max(n.end_time for n in input_sequence.notes)
                     if input_sequence.notes else 0)
    qpm = input_sequence.tempos[0].qpm
    seconds_per_step = 60.0 / qpm / polyphony_rnn.steps_per_quarter
    total_seconds = num_steps * seconds_per_step
    generator_options = generator_pb2.GeneratorOptions()
    generator_options.args['temperature'].float_value = temperature
    generate_section = generator_options.generate_sections.add(
        start_time=last_end_time + seconds_per_step,
        end_time=total_seconds)
    filename = name + '_' + model_name + '_output.mid'
    sequence = polyphony_rnn.generate(input_sequence, generator_options)
    mm.sequence_proto_to_midi_file(sequence, './output/' + filename)
    end = time.time()
    print(filename + " created")
    print("That took:" + (end - start).__str__())
