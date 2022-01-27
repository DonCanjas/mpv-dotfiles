import vapoursynth as vs
core = vs.core

core.neo_f3kdb.Deband(video_in, range=25, y=40, cb=0, cr=0, grainy=64, grainc=0, dynamic_grain=True, sample_mode=2).set_output()
