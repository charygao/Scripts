import nuke
def nodePresetsStartup():
  nuke.setUserPreset("ColorCorrect", "SNJYW/EP05/01/HighlightAdjust", {'highlights.gain': '0.9274861813 1 0.9689226747 1', 'lookup': 'shadow {curve 1 s0 x0.03307496011 0 s0}\nmidtone {1-shadow-highlight}\nhighlight {curve x0.1837497354 0 s0 x0.3674994707 1 s0}', 'note_font': '\xe5\xbe\xae\xe8\xbd\xaf\xe9\x9b\x85\xe9\xbb\x91', 'highlights.saturation': '0.9', 'label': "SNJYW/EP05/01/HighlightAdjust\n\xe9\xa2\x84\xe8\xae\xbe\xe9\x94\x81\xe5\xae\x9a :[python {nuke.applyUserPreset('', 'SNJYW/EP05/01/HighlightAdjust', nuke.thisNode())}]\n"})
  nuke.setUserPreset("ColorCorrect", "SNJYW/EP05/01/Color_Soldier", {'saturation': '0.9', 'note_font': '\xe5\xbe\xae\xe8\xbd\xaf\xe9\x9b\x85\xe9\xbb\x91', 'label': "SNJYW/EP05/01/Color_Soldier\n\xe9\xa2\x84\xe8\xae\xbe\xe9\x94\x81\xe5\xae\x9a :[python {nuke.applyUserPreset('', 'SNJYW/EP05/01/Color_Soldier', nuke.thisNode())}]\n", 'mix': '0.935', 'gain': '0.5499999523 0.7554348707 1 1', 'indicators': '16'})
  nuke.setUserPreset("ColorCorrect", "SNJYW/EP05/01/Adj_Rooftop", {'indicators': '4', 'maskChannelInput': 'Rooftop.alpha', 'note_font': '\xe5\xbe\xae\xe8\xbd\xaf\xe9\x9b\x85\xe9\xbb\x91', 'gain': '2.6', 'label': "SNJYW/EP05/01/Adj_Rooftop\n\xe9\xa2\x84\xe8\xae\xbe\xe9\x94\x81\xe5\xae\x9a :[python {nuke.applyUserPreset('', 'SNJYW/EP05/01/Adj_Rooftop', nuke.thisNode())}]\n"})
  nuke.setUserPreset("ColorCorrect", "SNJYW/EP05/01/light_ground", {'saturation': '0.4', 'note_font': '\xe5\xbe\xae\xe8\xbd\xaf\xe9\x9b\x85\xe9\xbb\x91', 'label': "SNJYW/EP05/01/light_ground\n\xe9\xa2\x84\xe8\xae\xbe\xe9\x94\x81\xe5\xae\x9a :[python {nuke.applyUserPreset('', 'SNJYW/EP05/01/light_ground', nuke.thisNode())}]\n", 'contrast': '1.4', 'gamma': '0.6', 'gain': '13.19999886 14.56799984 15 6.099999905'})
  nuke.setUserPreset("ColorCorrect", "SNJYW/EP05/01/Color_Sky", {'note_font': '\xe5\xbe\xae\xe8\xbd\xaf\xe9\x9b\x85\xe9\xbb\x91', 'gain': '0.6718333364 0.8133032918 1.000833392 1', 'gamma': '1.1', 'label': "SNJYW/EP05/01/Color_Sky\n\xe9\xa2\x84\xe8\xae\xbe\xe9\x94\x81\xe5\xae\x9a :[python {nuke.applyUserPreset('', 'SNJYW/EP05/01/Color_Sky', nuke.thisNode())}]\n"})
  nuke.setUserPreset("ColorCorrect", "SNJYW/EP05/01/Light_Sky", {'note_font': '\xe5\xbe\xae\xe8\xbd\xaf\xe9\x9b\x85\xe9\xbb\x91', 'gain': '0.7360000014 1.288959861 1.600000024 3.049999952', 'gamma': '1.2', 'label': "SNJYW/EP05/01/Light_Sky\n\xe9\xa2\x84\xe8\xae\xbe\xe9\x94\x81\xe5\xae\x9a :[python {nuke.applyUserPreset('', 'SNJYW/EP05/01/Light_Sky', nuke.thisNode())}]\n"})
  nuke.setUserPreset("ColorCorrect", "SNJYW/EP05/01/color_shadows", {'shadows.gain': '0.6836920977 0.4399999976 1 1', 'note_font': '\xe5\xbe\xae\xe8\xbd\xaf\xe9\x9b\x85\xe9\xbb\x91', 'label': "SNJYW/EP05/01/color_shadows\n\xe9\xa2\x84\xe8\xae\xbe\xe9\x94\x81\xe5\xae\x9a :[python {nuke.applyUserPreset('', 'SNJYW/EP05/01/color_shadows', nuke.thisNode())}]\n"})
  nuke.setUserPreset("ColorCorrect", "SNJYW/EP05/01/Env_OutRoom_Day", {'gamma_panelDropped': 'true', 'note_font': '\xe5\xbe\xae\xe8\xbd\xaf\xe9\x9b\x85\xe9\xbb\x91', 'gamma': '0.842933 1.033333 1.123733 1', 'label': "SNJYW/EP05/01/Env_OutRoom_Day\n\xe9\xa2\x84\xe8\xae\xbe\xe9\x94\x81\xe5\xae\x9a :[python {nuke.applyUserPreset('', 'SNJYW/EP05/01/Env_OutRoom_Day', nuke.thisNode())}]\n"})
  nuke.setUserPreset("ColorCorrect", "SNJYW/EP05/01/Color_Fog", {'saturation': '0.8', 'note_font': '\xe5\xbe\xae\xe8\xbd\xaf\xe9\x9b\x85\xe9\xbb\x91', 'gamma_panelDropped': 'true', 'label': "SNJYW/EP05/01/Color_Fog\n\xe9\xa2\x84\xe8\xae\xbe\xe9\x94\x81\xe5\xae\x9a :[python {nuke.applyUserPreset('', 'SNJYW/EP05/01/Color_Fog', nuke.thisNode())}]\n", 'gain': '1.3 1.7 2.1 1', 'gamma': '1.023332 1.083333 1.043333 1.12', 'gain_panelDropped': 'true'})
  nuke.setUserPreset("ColorCorrect", "SNJYW/EP05/01/Color_Petal", {'saturation': '0.1', 'note_font': '\xe5\xbe\xae\xe8\xbd\xaf\xe9\x9b\x85\xe9\xbb\x91', 'gamma_panelDropped': 'true', 'label': "SNJYW/EP05/01/Color_Petal\n\xe9\xa2\x84\xe8\xae\xbe\xe9\x94\x81\xe5\xae\x9a :[python {nuke.applyUserPreset('', 'SNJYW/EP05/01/Color_Petal', nuke.thisNode())}]\n", 'gain': '1.8', 'gamma': '1.375000119 1.700000167 2.025000095 1.700000048'})
  nuke.setUserPreset("ColorCorrect", "SNJYW/EP05/01/color_cloth_deadbody", {'note_font': '\xe5\xbe\xae\xe8\xbd\xaf\xe9\x9b\x85\xe9\xbb\x91', 'gamma_panelDropped': 'true', 'maskChannelInput': 'mask_extra.cloth_deadbody', 'label': "SNJYW/EP05/01/color_cloth_deadbody\n\xe9\xa2\x84\xe8\xae\xbe\xe9\x94\x81\xe5\xae\x9a :[python {nuke.applyUserPreset('', 'SNJYW/EP05/01/color_cloth_deadbody', nuke.thisNode())}]\n", 'mix': '0.61', 'indicators': '20', 'gamma': '1.007429 0.983523 0.934485 1'})
  nuke.setUserPreset("ColorCorrect", "SNJYW/EP05/01/color_ground", {'saturation': '0.6', 'note_font': '\xe5\xbe\xae\xe8\xbd\xaf\xe9\x9b\x85\xe9\xbb\x91', 'gamma_panelDropped': 'true', 'maskChannelInput': 'mask_extra.ground', 'label': "SNJYW/EP05/01/color_ground\n\xe9\xa2\x84\xe8\xae\xbe\xe9\x94\x81\xe5\xae\x9a :[python {nuke.applyUserPreset('', 'SNJYW/EP05/01/color_ground', nuke.thisNode())}]\n", 'indicators': '4', 'gamma': '0.889642 0.986488 1.031667 1'})
  nuke.setUserPreset("ColorCorrect", "SNJYW/EP05/01/color_cloth_white", {'saturation': '0.5', 'note_font': '\xe5\xbe\xae\xe8\xbd\xaf\xe9\x9b\x85\xe9\xbb\x91', 'gamma_panelDropped': 'true', 'maskChannelInput': 'mask_extra.cloth_white', 'label': "SNJYW/EP05/01/color_cloth_white\n\xe9\xa2\x84\xe8\xae\xbe\xe9\x94\x81\xe5\xae\x9a :[python {nuke.applyUserPreset('', 'SNJYW/EP05/01/color_cloth_white', nuke.thisNode())}]\n", 'gain_panelDropped': 'true', 'indicators': '4', 'gamma': '0.823438 0.92356 1.073541 1', 'gain': '0.925365 1.028971 1.045663 1'})
  nuke.setUserPreset("Grade", "SNJYW/EP05/01/Fog_Lift", {'indicators': '4', 'maskChannelInput': 'rgba.alpha', 'black': '0.08241333067 0.05833334103 0.101333335 0.08500000089', 'note_font': '\xe5\xbe\xae\xe8\xbd\xaf\xe9\x9b\x85\xe9\xbb\x91', 'label': "SNJYW/EP05/01/Fog_Lift\n\xe9\xa2\x84\xe8\xae\xbe\xe9\x94\x81\xe5\xae\x9a :[python {nuke.applyUserPreset('', 'SNJYW/EP05/01/Fog_Lift', nuke.thisNode())}]\n\n"})
  nuke.setUserPreset("Group11214797875975229693", "SNJYW/EP05/01/Env_OutRoom_Day", {'Child-1 indicators': '16', 'Child18 black': '0 {parent.lift.g} 0 0', 'Child30 selected': 'true', 'Child23 mix': '0', 'Child-1 label': "SNJYW/EP05/01/Env_OutRoom_Day\n\xe9\xa2\x84\xe8\xae\xbe\xe9\x94\x81\xe5\xae\x9a :[python {nuke.applyUserPreset('', 'SNJYW/EP05/01/Env_OutRoom_Day', nuke.thisNode())}]\n[value in]\n[knob_default saturation 1]\n[knob_default gain 1]\n[knob_default gamma 1]\n[knob_default layer_mix 1]", 'Child23 disable': '{"\\[string is digit \\[input parent 0]]"}', 'Child28 saturation': '{parent.saturation.b}', 'Child27 saturation': '{parent.saturation.g}', 'Child25 alpha': 'depth.Z', 'Child1 channels': 'rgba', 'Child15 mix': '{1-parent.layer_mix}', 'Child26 channels': 'rgba.red -rgba.green -rgba.blue -rgba.alpha', 'Child18 white': '1 {parent.gain.g} 1 1', 'Child21 operation': 'copy', 'Child28 maskChannelMask': 'rgba.blue', 'Child19 black': '0 0 {parent.lift.b} 0', 'Child23 value': '0', 'Child17 maskChannelMask': 'rgba.red', 'Child21 Achannels': 'rgb', 'Child30 conversion': 'logarithmic compress', 'Child19 gamma': '1 1 {parent.gamma.b} 1', 'Child14 channels': 'none none none rgba.alpha', 'Child17 label': '[knob parent.Merge1.Achannels [value channels]]\n[knob parent.Merge1.Bchannels [value channels]]\n[knob parent.Merge1.output [value channels]]', 'Child29 in': 'SSS', 'Child17 gamma': '{parent.gamma.r} 1 1 1', 'Child-1 saturation': '0.8', 'Child-1 lift': '-0.04250000045 0 0.04250000045', 'Child-1 gain': '1', 'Child26 maskChannelMask': 'rgba.red', 'Child27 maskChannelMask': 'rgba.green', 'Child18 channels': '{{parent.R1.channels}}', 'Child17 white': '{parent.gain.r} 1 1 1', 'Child27 channels': '-rgba.red rgba.green -rgba.blue -rgba.alpha', 'Child19 channels': '{{parent.R1.channels}}', 'Child22 disable': '{1-parent.preview}', 'Child22 operation': 'copy', 'Child21 output': 'rgb', 'Child26 saturation': '{parent.saturation.r}', 'Child23 channels': 'rgba', 'Child-1 gamma': '0.2534665763 0.6184666157 0.8134665489', 'Child-1 layer_mix': '1', 'Child25 channels': 'alpha', 'Child-1 tile_color': '0x7aa9ffff', 'Child28 channels': '-rgba.red -rgba.green rgba.blue -rgba.alpha', 'Child21 Bchannels': 'rgb', 'Child14 whitepoint': '0.075', 'Child17 black': '{parent.lift.r} 0 0 0', 'Child15 whitepoint': '0.01', 'Child30 softclip_min': '0', 'Child18 gamma': '1 {parent.gamma.g} 1 1', 'Child19 white': '1 1 {parent.gain.b} 1', 'Child19 maskChannelMask': 'rgba.blue', 'Child18 maskChannelMask': 'rgba.green'})
  nuke.setUserPreset("Group17411436662440602462", "SNJYW/EP05/01/Lum_Sky", {'Child0 colorspace_out': 'HSV', 'Child6 maskChannelInput': '{{parent.Grade1.maskChannelMask}}', 'Child11 maskChannelInput': '{{parent.Grade1.maskChannelInput}}', 'Child1 channels': '{{parent.Colorspace1.channels}}', 'Child6 fringe': '{parent.Grade1.fringe}', 'Child-1 label': "SNJYW/EP05/01/Lum_Sky\n\xe9\xa2\x84\xe8\xae\xbe\xe9\x94\x81\xe5\xae\x9a :[python {nuke.applyUserPreset('', 'SNJYW/EP05/01/Lum_Sky', nuke.thisNode())}]\n[knob_default gain 1]\n[knob_default gamma 1]", 'Child5 maskChannelMask': '{{parent.MaskChannelChoose.alpha}}', 'Child12 which': '{"\\[string is digit \\[input parent 1]]"}', 'Child5 white': '{parent.gain}', 'Child11 maskChannelMask': '{{parent.MaskChannelChoose.alpha}}', 'Child10 alpha': 'none', 'Child-1 gain': '1', 'Child5 channels': 'none none none rgba.blue', 'Child8 number': '1', 'Child11 mix': '{parent.Grade1.mix}', 'Child-1 gamma': '0.8', 'Child11 fringe': '{parent.Grade1.fringe}', 'Child11 inject': '{parent.Grade1.inject}', 'Child5 black': '{parent.lift}', 'Child6 invert_mask': '{parent.Grade1.invert_mask}', 'Child-1 tile_color': '0x79a8ffff', 'Child11 invert_mask': '{parent.Grade1.invert_mask}', 'Child-1 help': '\xe5\x8f\xaa\xe8\xb0\x83\xe6\x95\xb4\xe4\xba\xae\xe5\xba\xa6\xe4\xb8\x8d\xe5\xbd\xb1\xe5\x93\x8d\xe9\xa5\xb1\xe5\x92\x8c\xe5\xba\xa6\xe5\x92\x8c\xe8\x89\xb2\xe7\x9b\xb8', 'Child6 white': '1.7', 'Child11 channels': '{{parent.Colorspace1.channels}}', 'Child1 colorspace_in': 'HSV', 'Child5 gamma': '{parent.gamma}', 'Child6 inject': '{parent.Grade1.inject}'})