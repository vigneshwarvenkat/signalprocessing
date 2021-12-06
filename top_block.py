#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FM Radio
# Generated: Thu Aug 20 14:40:51 2020
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

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="FM Radio")
        _icon_path = "C:\Program Files\GNURadio-3.7-m\share\icons\hicolor\scalable/apps\gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.transition_width_selection = transition_width_selection = 1000000
        self.selected_station = selected_station = 93.3
        self.volume_slider = volume_slider = 1
        self.transition = transition = transition_width_selection
        self.samp_rate = samp_rate = 2000000
        self.quadrature = quadrature = 500000
        self.freq = freq = selected_station
        self.cutoff = cutoff = 100000
        self.audio_dec = audio_dec = 10

        ##################################################
        # Blocks
        ##################################################
        _volume_slider_sizer = wx.BoxSizer(wx.VERTICAL)
        self._volume_slider_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_volume_slider_sizer,
        	value=self.volume_slider,
        	callback=self.set_volume_slider,
        	label='volume_slider',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._volume_slider_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_volume_slider_sizer,
        	value=self.volume_slider,
        	callback=self.set_volume_slider,
        	minimum=0,
        	maximum=10,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_volume_slider_sizer)
        _transition_width_selection_sizer = wx.BoxSizer(wx.VERTICAL)
        self._transition_width_selection_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_transition_width_selection_sizer,
        	value=self.transition_width_selection,
        	callback=self.set_transition_width_selection,
        	label='transition_width_selection',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._transition_width_selection_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_transition_width_selection_sizer,
        	value=self.transition_width_selection,
        	callback=self.set_transition_width_selection,
        	minimum=1000,
        	maximum=2000000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_transition_width_selection_sizer)
        self._selected_station_chooser = forms.radio_buttons(
        	parent=self.GetWin(),
        	value=self.selected_station,
        	callback=self.set_selected_station,
        	label='Stations',
        	choices=[93.8, 93.3, 95.8, 97.2],
        	labels=["Symphony 92.4", "YES 93.3", "Capital 95.8", "Love 97.2"],
        	style=wx.RA_VERTICAL,
        )
        self.Add(self._selected_station_chooser)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(freq*1000000, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(True, 0)
        self.rtlsdr_source_0.set_gain(20, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)

        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=4,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=int(quadrature/1e3/audio_dec),
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, cutoff, transition, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume_slider, ))
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=quadrature,
        	audio_decimation=audio_dec,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.rational_resampler_xxx_0_0, 0))

    def get_transition_width_selection(self):
        return self.transition_width_selection

    def set_transition_width_selection(self, transition_width_selection):
        self.transition_width_selection = transition_width_selection
        self.set_transition(self.transition_width_selection)
        self._transition_width_selection_slider.set_value(self.transition_width_selection)
        self._transition_width_selection_text_box.set_value(self.transition_width_selection)

    def get_selected_station(self):
        return self.selected_station

    def set_selected_station(self, selected_station):
        self.selected_station = selected_station
        self.set_freq(self.selected_station)
        self._selected_station_chooser.set_value(self.selected_station)

    def get_volume_slider(self):
        return self.volume_slider

    def set_volume_slider(self, volume_slider):
        self.volume_slider = volume_slider
        self._volume_slider_slider.set_value(self.volume_slider)
        self._volume_slider_text_box.set_value(self.volume_slider)
        self.blocks_multiply_const_vxx_0.set_k((self.volume_slider, ))

    def get_transition(self):
        return self.transition

    def set_transition(self, transition):
        self.transition = transition
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.transition, firdes.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.transition, firdes.WIN_HAMMING, 6.76))

    def get_quadrature(self):
        return self.quadrature

    def set_quadrature(self, quadrature):
        self.quadrature = quadrature

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.rtlsdr_source_0.set_center_freq(self.freq*1000000, 0)

    def get_cutoff(self):
        return self.cutoff

    def set_cutoff(self, cutoff):
        self.cutoff = cutoff
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff, self.transition, firdes.WIN_HAMMING, 6.76))

    def get_audio_dec(self):
        return self.audio_dec

    def set_audio_dec(self, audio_dec):
        self.audio_dec = audio_dec


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
