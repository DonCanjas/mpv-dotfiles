import vapoursynth as vs
core = vs.core

core.neo_f3kdb.Deband(video_in, range=30, y=64, cb=32, cr=32, grainy=64, grainc=0, dynamic_grain=True, sample_mode=2).set_output()
