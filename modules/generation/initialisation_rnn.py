from magenta.models.melody_rnn import melody_rnn_sequence_generator
from magenta.models.shared import sequence_generator_bundle


def init_melody_rnn(model_name):
    print("initializing generator...")
    bundle = sequence_generator_bundle.read_bundle_file('./content/' + model_name + '.mag')
    generator_map = melody_rnn_sequence_generator.get_generator_map()
    melody_rnn = generator_map[model_name](checkpoint=None, bundle=bundle)
    melody_rnn.initialize()
    print('🎉initializing done!')
    return melody_rnn
