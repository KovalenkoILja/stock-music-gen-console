from magenta.models.music_vae import configs
from magenta.models.music_vae.trained_model import TrainedModel


def init_music_vae(model_name):
    print("initializing generator...")
    music_vae = TrainedModel(
        configs.CONFIG_MAP[model_name],
        batch_size=4,
        checkpoint_dir_or_path='./content/' + model_name + '.ckpt')
    print('initializing🎉 done!')
    return music_vae
