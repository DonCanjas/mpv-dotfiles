import vapoursynth as vs
import ccd 

core = vs.core

rgb = core.resize.Spline36(video_in, format=vs.RGBS)

derainbow = core.ccd.CCD(rgb, 25)

derainbow.set_output()
