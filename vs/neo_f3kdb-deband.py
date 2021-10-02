import vapoursynth as vs
core = vs.core()

core.neo_f3kdb.Deband(video_in, range=15, y=64, cb=16, cr=16, grainy=64, grainc=0, dynamic_grain=True, sample_mode=2).set_output()
