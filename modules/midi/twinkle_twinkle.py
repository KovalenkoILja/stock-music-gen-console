from magenta.music.protobuf import music_pb2


def twinkle_twinkle():
    twinkle = music_pb2.NoteSequence()

    twinkle.notes.add(pitch=60, start_time=0.0, end_time=0.5, velocity=80)
    twinkle.notes.add(pitch=60, start_time=0.5, end_time=1.0, velocity=80)
    twinkle.notes.add(pitch=67, start_time=1.0, end_time=1.5, velocity=80)
    twinkle.notes.add(pitch=67, start_time=1.5, end_time=2.0, velocity=80)
    twinkle.notes.add(pitch=69, start_time=2.0, end_time=2.5, velocity=80)
    twinkle.notes.add(pitch=69, start_time=2.5, end_time=3.0, velocity=80)
    twinkle.notes.add(pitch=67, start_time=3.0, end_time=4.0, velocity=80)
    twinkle.notes.add(pitch=65, start_time=4.0, end_time=4.5, velocity=80)
    twinkle.notes.add(pitch=65, start_time=4.5, end_time=5.0, velocity=80)
    twinkle.notes.add(pitch=64, start_time=5.0, end_time=5.5, velocity=80)
    twinkle.notes.add(pitch=64, start_time=5.5, end_time=6.0, velocity=80)
    twinkle.notes.add(pitch=62, start_time=6.0, end_time=6.5, velocity=80)
    twinkle.notes.add(pitch=62, start_time=6.5, end_time=7.0, velocity=80)
    twinkle.notes.add(pitch=60, start_time=7.0, end_time=8.0, velocity=80)
    twinkle.total_time = 8
    twinkle.tempos.add(qpm=60)

    return twinkle
