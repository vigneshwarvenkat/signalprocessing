#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Chat App
# Generated: Thu Jan  7 09:56:35 2021
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import EE2033
import pmt
import wx


class chat_app(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Chat App")
        _icon_path = "C:\Program Files\GNURadio-3.7-m\share\icons\hicolor\scalable/apps\gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.preambleOut = preambleOut = "1000000101010101"
        self.msg_str = msg_str = "Shannon"
        self.fsym = fsym = 200
        self.fs_out = fs_out = 4e6
        self.fs_in = fs_in = 4e6

        ##################################################
        # Blocks
        ##################################################
        self._preambleOut_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.preambleOut,
        	callback=self.set_preambleOut,
        	label='Preamble Output',
        	converter=forms.str_converter(),
        )
        self.Add(self._preambleOut_text_box)
        self._msg_str_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.msg_str,
        	callback=self.set_msg_str,
        	label='msg_str',
        	converter=forms.str_converter(),
        )
        self.GridAdd(self._msg_str_text_box, 1, 1, 3, 18)
        self._fsym_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.fsym,
        	callback=self.set_fsym,
        	label='Symbol Rate (Symbols per second)',
        	choices=[80, 100, 160, 200, 320, 400],
        	labels=["80k", "100k", "160k", "200k", "320k", "400k"],
        )
        self.GridAdd(self._fsym_chooser, 4, 12, 1, 5)
        self.wxgui_scopesink2_0_0_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Scope Plot1',
        	sample_rate=fs_out,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_0_0_0.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Scope Plot',
        	sample_rate=fs_in,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=True,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=int(fs_out/1e5),
                decimation=int(fs_in/1e5),
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	100, fs_in, 300e3, 100e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, 'C:\\Users\\com2p\\Desktop\\TA\\EE2033\\2020_21 sem 2\\Miniproject\\LTSPICE\\testspice.dat', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.EE2033_ook_text_b_sink_0 = EE2033.ook_text_b_sink(msg_str, preambleOut, fsym*1000, int(fs_out))



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_file_source_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.EE2033_ook_text_b_sink_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.wxgui_scopesink2_0_0_0, 0))

    def get_preambleOut(self):
        return self.preambleOut

    def set_preambleOut(self, preambleOut):
        self.preambleOut = preambleOut
        self._preambleOut_text_box.set_value(self.preambleOut)
        self.EE2033_ook_text_b_sink_0.set_preamble(self.preambleOut)

    def get_msg_str(self):
        return self.msg_str

    def set_msg_str(self, msg_str):
        self.msg_str = msg_str
        self._msg_str_text_box.set_value(self.msg_str)
        self.EE2033_ook_text_b_sink_0.set_matched_text(self.msg_str)

    def get_fsym(self):
        return self.fsym

    def set_fsym(self, fsym):
        self.fsym = fsym
        self._fsym_chooser.set_value(self.fsym)

    def get_fs_out(self):
        return self.fs_out

    def set_fs_out(self, fs_out):
        self.fs_out = fs_out
        self.wxgui_scopesink2_0_0_0.set_sample_rate(self.fs_out)

    def get_fs_in(self):
        return self.fs_in

    def set_fs_in(self, fs_in):
        self.fs_in = fs_in
        self.wxgui_scopesink2_0.set_sample_rate(self.fs_in)
        self.low_pass_filter_0.set_taps(firdes.low_pass(100, self.fs_in, 300e3, 100e3, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=chat_app, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
