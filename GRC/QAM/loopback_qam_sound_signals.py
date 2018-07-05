#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Loopback QAM Modulation - Sound Signals
# Author: Hugo Soares
# Generated: Thu Jul  5 14:40:34 2018
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

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys


class loopback_qam_sound_signals(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Loopback QAM Modulation - Sound Signals")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Loopback QAM Modulation - Sound Signals")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "loopback_qam_sound_signals")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 400000

        ##################################################
        # Blocks
        ##################################################
        self.janela = Qt.QTabWidget()
        self.janela_widget_0 = Qt.QWidget()
        self.janela_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.janela_widget_0)
        self.janela_grid_layout_0 = Qt.QGridLayout()
        self.janela_layout_0.addLayout(self.janela_grid_layout_0)
        self.janela.addTab(self.janela_widget_0, "Frequency")
        self.janela_widget_1 = Qt.QWidget()
        self.janela_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.janela_widget_1)
        self.janela_grid_layout_1 = Qt.QGridLayout()
        self.janela_layout_1.addLayout(self.janela_grid_layout_1)
        self.janela.addTab(self.janela_widget_1, "Time ")
        self.janela_widget_2 = Qt.QWidget()
        self.janela_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.janela_widget_2)
        self.janela_grid_layout_2 = Qt.QGridLayout()
        self.janela_layout_2.addLayout(self.janela_grid_layout_2)
        self.janela.addTab(self.janela_widget_2, "QAM Signal (Frequency)")
        self.top_layout.addWidget(self.janela)
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_fff(
                interpolation=441,
                decimation=4000,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=441,
                decimation=4000,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=4000,
                decimation=441,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=4000,
                decimation=441,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Original Signal - Time", #name
        	4 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-2, 2)
        
        self.qtgui_time_sink_x_0_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0.disable_legend()
        
        labels = ["Original Signal 1", "Original Siginal 2", "Demodulated Signal 1", "Demodulated Signal 2", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 2, 2, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 0.8, 0.8, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(4):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.janela_layout_1.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_HAMMING, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Original Signal - Frequency", #name
        	4 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 0)
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.1)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)
        
        labels = ["Original Signal 1", "Original Signal 2", "Demodulated Signal 1", "Demodulated Signal 2", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 0.8, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(4):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.janela_layout_0.addWidget(self._qtgui_freq_sink_x_0_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Signal Modulated", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-160, 0)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["QAM Signal", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["magenta", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.janela_layout_2.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, 45.1e3, 100, firdes.WIN_HANN, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, 45.1e3, 100, firdes.WIN_HANN, 6.76))
        self.blocks_wavfile_source_0_0 = blocks.wavfile_source("/home/alunos/Área de Trabalho/principles-of-telecommunications/static/Electronic-Tom-4.wav", True)
        self.blocks_wavfile_source_0 = blocks.wavfile_source("/home/alunos/Área de Trabalho/principles-of-telecommunications/static/Electro-Tom.wav", True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_xx_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_add_xx_0_1 = blocks.add_vff(1)
        self.audio_sink_0 = audio.sink(44100, "", True)
        self.analog_sig_source_x_1_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 80000, 1, 0)
        self.analog_sig_source_x_1_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 80000, 1, 0)
        self.analog_sig_source_x_1_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 80000, 2, 0)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 80000, 2, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.analog_sig_source_x_1_0, 0), (self.blocks_multiply_xx_0_0, 1))    
        self.connect((self.analog_sig_source_x_1_0_0, 0), (self.blocks_multiply_xx_0_0_0_0, 0))    
        self.connect((self.analog_sig_source_x_1_1, 0), (self.blocks_multiply_xx_0_0_0, 0))    
        self.connect((self.blocks_add_xx_0_1, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0_1, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0_1, 1))    
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0_0_0, 0), (self.low_pass_filter_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_0_0_0, 1))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_0_0_0_0, 1))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.qtgui_freq_sink_x_0_0, 3))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.qtgui_time_sink_x_0_0_0, 3))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.blocks_wavfile_source_0_0, 0), (self.qtgui_freq_sink_x_0_0, 2))    
        self.connect((self.blocks_wavfile_source_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 2))    
        self.connect((self.blocks_wavfile_source_0_0, 0), (self.rational_resampler_xxx_0_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.rational_resampler_xxx_1_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_multiply_xx_0_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.audio_sink_0, 1))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.qtgui_freq_sink_x_0_0, 1))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.qtgui_time_sink_x_0_0_0, 1))    
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.qtgui_freq_sink_x_0_0, 0))    
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "loopback_qam_sound_signals")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_1.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 45.1e3, 100, firdes.WIN_HANN, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 45.1e3, 100, firdes.WIN_HANN, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)


def main(top_block_cls=loopback_qam_sound_signals, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
