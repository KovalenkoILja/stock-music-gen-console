from magenta.music.protobuf import music_pb2


def teapot():
    tpt = music_pb2.NoteSequence()

    tpt.notes.add(pitch=69, start_time=0, end_time=0.5, velocity=80)
    tpt.notes.add(pitch=71, start_time=0.5, end_time=1, velocity=80)
    tpt.notes.add(pitch=73, start_time=1, end_time=1.5, velocity=80)
    tpt.notes.add(pitch=74, start_time=1.5, end_time=2, velocity=80)
    tpt.notes.add(pitch=76, start_time=2, end_time=2.5, velocity=80)
    tpt.notes.add(pitch=81, start_time=3, end_time=4, velocity=80)
    tpt.notes.add(pitch=78, start_time=4, end_time=5, velocity=80)
    tpt.notes.add(pitch=81, start_time=5, end_time=6, velocity=80)
    tpt.notes.add(pitch=76, start_time=6, end_time=8, velocity=80)
    tpt.total_time = 8
    tpt.tempos.add(qpm=60)

    return tpt
