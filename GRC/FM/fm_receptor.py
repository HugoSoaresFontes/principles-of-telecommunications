#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: fm_receptor
# Author: Hugo Soares
# Generated: Tue Jul  3 11:42:42 2018
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
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
import time


class fm_receptor(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "fm_receptor")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("fm_receptor")
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

        self.settings = Qt.QSettings("GNU Radio", "fm_receptor")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.usrp_frequency = usrp_frequency = 98900000
        self.samp_rate = samp_rate = 500000
        self.rf_gain = rf_gain = 30
        self.fine_frequency = fine_frequency = 0

        ##################################################
        # Blocks
        ##################################################
        self._usrp_frequency_range = Range(88000000, 108000000, 100000, 98900000, 200)
        self._usrp_frequency_win = RangeWidget(self._usrp_frequency_range, self.set_usrp_frequency, "Central Frequency", "counter_slider", float)
        self.top_layout.addWidget(self._usrp_frequency_win)
        self._rf_gain_range = Range(0, 50, 1, 30, 200)
        self._rf_gain_win = RangeWidget(self._rf_gain_range, self.set_rf_gain, "RF GAIN", "counter_slider", float)
        self.top_layout.addWidget(self._rf_gain_win)
        self.janela = Qt.QTabWidget()
        self.janela_widget_0 = Qt.QWidget()
        self.janela_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.janela_widget_0)
        self.janela_grid_layout_0 = Qt.QGridLayout()
        self.janela_layout_0.addLayout(self.janela_grid_layout_0)
        self.janela.addTab(self.janela_widget_0, "R Channel")
        self.janela_widget_1 = Qt.QWidget()
        self.janela_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.janela_widget_1)
        self.janela_grid_layout_1 = Qt.QGridLayout()
        self.janela_layout_1.addLayout(self.janela_grid_layout_1)
        self.janela.addTab(self.janela_widget_1, "L Channel")
        self.top_layout.addWidget(self.janela)
        self._fine_frequency_range = Range(-250000, 250000, 500, 0, 200)
        self._fine_frequency_win = RangeWidget(self._fine_frequency_range, self.set_fine_frequency, "Fine Frequency", "counter_slider", float)
        self.top_layout.addWidget(self._fine_frequency_win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(usrp_frequency + fine_frequency, 0)
        self.uhd_usrp_source_0.set_gain(rf_gain, 0)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Espectro L", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.janela_layout_0.addWidget(self._qtgui_freq_sink_x_1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	98900000, #fc
        	samp_rate, #bw
        	"Espectro R", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
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
        self.janela_layout_1.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 115000, 30000, firdes.WIN_HANN, 6.76))
        self.analog_wfm_rcv_pll_0 = analog.wfm_rcv_pll(
        	demod_rate=500e3,
        	audio_decimation=10,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_pll_0, 1), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.analog_wfm_rcv_pll_0, 0), (self.qtgui_freq_sink_x_1, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_pll_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fm_receptor")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_usrp_frequency(self):
        return self.usrp_frequency

    def set_usrp_frequency(self, usrp_frequency):
        self.usrp_frequency = usrp_frequency
        self.uhd_usrp_source_0.set_center_freq(self.usrp_frequency + self.fine_frequency, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 115000, 30000, firdes.WIN_HANN, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(98900000, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.uhd_usrp_source_0.set_gain(self.rf_gain, 0)
        	

    def get_fine_frequency(self):
        return self.fine_frequency

    def set_fine_frequency(self, fine_frequency):
        self.fine_frequency = fine_frequency
        self.uhd_usrp_source_0.set_center_freq(self.usrp_frequency + self.fine_frequency, 0)


def main(top_block_cls=fm_receptor, options=None):

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
