import os

import input
from modules.common.create_dir import check_dir
from modules.common.print_version import print_versions
from modules.common.user_input import wait_for_user_input
from modules.generation.check_contents import init_contents
from modules.generation.generate_continue import generate_continue_for
from modules.generation.generate_interpolation import generate_interpolation_for
from modules.generation.initialisation_vae import init_music_vae
from modules.midi.create_samples import create_midi_samples
from modules.midi.teapot import teapot
from modules.midi.twinkle_twinkle import twinkle_twinkle


class Application:

    def start(self):

        init_contents()

        while True:
            self.print_controls()
            wait_for_user_input()

            if input.user_input == "empty":
                continue

            if input.user_input == "1":
                print()
                create_midi_samples()

            elif input.user_input == "2":
                print()

                input_sequence = twinkle_twinkle()
                num_steps = 128
                temperature = 1.0
                model_name = 'basic_rnn'
                generate_continue_for("twinkle_twinkle", input_sequence, model_name, num_steps, temperature)
                model_name = 'attention_rnn'
                generate_continue_for("twinkle_twinkle", input_sequence, model_name, num_steps, temperature)
                model_name = 'lookback_rnn'
                generate_continue_for("twinkle_twinkle", input_sequence, model_name, num_steps, temperature)
                model_name = 'mono_rnn'
                generate_continue_for("twinkle_twinkle", input_sequence, model_name, num_steps, temperature)

            elif input.user_input == "3":
                print()

                input_sequence = teapot()
                num_steps = 128
                temperature = 1.0
                model_name = 'basic_rnn'
                generate_continue_for("teapot", input_sequence, model_name, num_steps, temperature)
                model_name = 'attention_rnn'
                generate_continue_for("teapot", input_sequence, model_name, num_steps, temperature)
                model_name = 'lookback_rnn'
                generate_continue_for("teapot", input_sequence, model_name, num_steps, temperature)
                model_name = 'mono_rnn'
                generate_continue_for("teapot", input_sequence, model_name, num_steps, temperature)

            elif input.user_input == "4":
                print()

                if not os.path.isfile("./content/cat-mel_2bar_big.ckpt.data-00000-of-00001") \
                        or not os.path.isfile("./content/cat-mel_2bar_big.ckpt.index"):
                    print("models for interpolate doesnt find!")
                    return
                else:

                    model_name = 'cat-mel_2bar_big'

                    music_vae = init_music_vae(model_name)

                    num_steps = 8
                    length = 32
                    generate_interpolation_for(model_name, music_vae, num_steps, length, twinkle_twinkle(), teapot())

            elif input.user_input == "5":
                print("5 input")
                path = "./input"
                check_dir(path)

            # elif input.user_input == "6":
            #     print("6 input")
            # elif input.user_input == "7":
            #     print("7 input")
            # elif input.user_input == "8":
            #     print("8 input")
            # elif input.user_input == "9":
            #     print("9 input")
            elif input.user_input == "0":
                print()
                print_versions()
            elif input.user_input == "esc":
                print("ESC pressed, exit")
                break

    @staticmethod
    def print_controls():
        print("Press key:")
        print("1: create sample midi files")
        print("2: generate continue for twinkle_twinkle")
        print("3: generate continue for teapot")
        print("4: generate interpolating between twinkle_twinkle and teapot")
        print("5: generate continue for files in input folder")
        # print("6: ")
        # print("7: ")
        # print("8: ")
        # print("9: ")
        print("0: show tools version")
        print("ESC: exit")
