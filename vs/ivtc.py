import vapoursynth as vs
from typing import Optional
from vsutil import depth, get_depth

core = vs.core


def IVTC(clip: vs.VideoNode) -> vs.VideoNode:
    """"
        Experimental script for inverse telecining and deinterlacing.
        Forked from <https://github.com/LightArrowsEXE/dotfiles/blob/master/mpv/.config/mpv/vs/ivtc.vpy>

        Requires VapourSynth <http://www.vapoursynth.com/doc/about.html>

        Additional dependencies:
            * vsutil <https://pypi.org/project/vsutil/>
            * TIVTC <https://github.com/dubhater/vapoursynth-tivtc>		
				TIVTC's documentation <http://avisynth.nl/index.php/TIVTC/TFM>

        :param clip:         Input clip

        :return:             IVTC'd clip
    """

    down = depth(clip, 8)
    tfm = core.tivtc.TFM(down)
    return depth(tfm, get_depth(clip))


IVTC(video_in).set_output()
