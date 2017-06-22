# -*- coding=UTF-8 -*-
import nuke

def set_knob_default():
    def vectorblur2():
        nuke.knobDefault("VectorBlur2.uv", "motion")
        nuke.knobDefault("VectorBlur2.blur_uv", "uniform")
        nuke.knobDefault("VectorBlur2.uv_offset", "-0.5")
        nuke.knobDefault("VectorBlur2.scale", "30")
        nuke.knobDefault("VectorBlur2.soft_lines", "True")
        nuke.knobDefault("VectorBlur2.normalize", "True")

    def root():
        nuke.knobDefault("Root.fps", "25")
        nuke.knobDefault("Root.format", "1920 1080 0 0 1920 1080 1 HD_1080")
        nuke.knobDefault("Root.project_directory", "[python {nuke.script_directory()}]")
        # nuke.knobDefault("Root.free_type_font_path", "//SERVER/scripts/NukePlugins/Fonts")

    def zdefocus2():
        nuke.knobDefault("ZDefocus2.blur_dof", "0")
        nuke.knobDefault("ZDefocus2.math", "depth")

    root()
    vectorblur2()
    zdefocus2()
    nuke.knobDefault("LayerContactSheet.showLayerNames", "1")
    nuke.knobDefault("note_font", u"微软雅黑".encode('utf8'))
    nuke.knobDefault("Switch.which", "1")
    nuke.knobDefault("Viewer.input_process", "False")
    nuke.knobDefault("SoftClip.conversion", "3")
    