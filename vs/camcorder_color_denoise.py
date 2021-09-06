import vapoursynth as vs
import ccd 

core = vs.core

derainbow = ccd.ccd(video_in, 10, "709")

derainbow.set_output()
