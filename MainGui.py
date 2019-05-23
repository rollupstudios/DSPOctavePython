# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.scrolledtext as tkst
import tkinter as tki
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter.ttk import *
from tkinter.messagebox import *


from subprocess import Popen
from datetime import *
from time import *

from matfuncs import *


REF_ROW_COUNT = 1080.0
REF_COL_COUNT = 1920.0
FIRST_COL_X = 50.0
FIRST_COL_Y = 70.0
COL_INC = 350
ROW_INC = 50
COL_INC_CHILD = 75
ROW_INC_CHILD = 30



def Design_Tab1():

    textTitle = Label(tab1,text="Single Sine Wave Generator",font=("Arial", 10, "bold"))
    textTitle.place(x=((FIRST_COL_Y+(0*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(0*ROW_INC))/REF_ROW_COUNT)*b)

    buttonPlot = Button(tab1, text='Plot', width="15",
        command=lambda: DoPlot(textDataF, textDataFs, textDataDCO, textDataAmp, textDataPhaseShift,
            textDataNcycles))
    buttonPlot.place(x=((FIRST_COL_Y+(1*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(1*ROW_INC))/REF_ROW_COUNT)*b)

    buttonSave = Button(tab1, text='Save Plot', width="15",
        command=lambda: SavePlot(textDataF, textDataFs, textDataDCO, textDataAmp, textDataPhaseShift,
            textDataNcycles))

    buttonSave.place(x=((FIRST_COL_Y+(1*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(2*ROW_INC))/REF_ROW_COUNT)*b)

    buttonSaveSignal = Button(tab1, text='Save Signal', width="15",
        command=lambda: writeWave(textDataF, textDataFs, textDataDCO, textDataAmp, textDataPhaseShift,
            textDataNcycles))

    buttonSaveSignal.place(x=((FIRST_COL_Y+(1*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(3*ROW_INC))/REF_ROW_COUNT)*b)
    
    buttonSaveConfig = Button(tab1, text='Save Config', width="15",
        command=lambda: SaveConfig(textDataF, textDataFs, textDataDCO, textDataAmp, textDataPhaseShift,
            textDataNcycles))
    buttonSaveConfig.place(x=((FIRST_COL_Y+(1*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(4*ROW_INC))/REF_ROW_COUNT)*b)

    buttonLoadConfig = Button(tab1, text='Open Config', width="15",
        command=lambda: LoadConfig(textDataF, textDataFs, textDataDCO, textDataAmp, textDataPhaseShift,
            textDataNcycles))
    buttonLoadConfig.place(x=((FIRST_COL_Y+(1*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(5*ROW_INC))/REF_ROW_COUNT)*b)

    buttonClear = Button(tab1, text='Clear all', width="15",
        command=lambda: ClearData(textDataF, textDataFs, textDataDCO, textDataAmp, textDataPhaseShift,
            textDataNcycles))
    buttonClear.place(x=((FIRST_COL_Y+(1*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(6*ROW_INC))/REF_ROW_COUNT)*b)

    textF = Label(tab1,text="Signal Frequency",font=("Arial", 10, "bold"))    
    textF.place(x=((FIRST_COL_Y+(0*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(1*ROW_INC))/REF_ROW_COUNT)*b)

    textDataF = Text(tab1, undo=True, width=10, height=0)
    textDataF['font'] = ('consolas', '12')
    textDataF.place(x=((FIRST_COL_Y+(0.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(1*ROW_INC))/REF_ROW_COUNT)*b)

    
    textFs = Label(tab1,text="Sampling Frequency",font=("Arial", 10, "bold"))
    textFs.place(x=((FIRST_COL_Y+(0*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(2*ROW_INC))/REF_ROW_COUNT)*b)

    textDataFs = Text(tab1, undo=True, width=10, height=0)
    textDataFs['font'] = ('consolas', '12')
    textDataFs.place(x=((FIRST_COL_Y+(0.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(2*ROW_INC))/REF_ROW_COUNT)*b)

    textDCO = Label(tab1,text="DC Offset",font=("Arial", 10, "bold"))
    textDCO.place(x=((FIRST_COL_Y+(0*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(3*ROW_INC))/REF_ROW_COUNT)*b)

    textDataDCO = Text(tab1, undo=True, width=10, height=0)
    textDataDCO['font'] = ('consolas', '12')
    textDataDCO.place(x=((FIRST_COL_Y+(0.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(3*ROW_INC))/REF_ROW_COUNT)*b)

    textAmp = Label(tab1,text="Amplitude",font=("Arial", 10, "bold"))
    textAmp.place(x=((FIRST_COL_Y+(0*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(4*ROW_INC))/REF_ROW_COUNT)*b)

    textDataAmp = Text(tab1, undo=True, width=10, height=0)
    textDataAmp['font'] = ('consolas', '12')
    textDataAmp.place(x=((FIRST_COL_Y+(0.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(4*ROW_INC))/REF_ROW_COUNT)*b)

    textPhaseShift = Label(tab1,text="Phase Shift",font=("Arial", 10, "bold"))
    textPhaseShift.place(x=((FIRST_COL_Y+(0*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(5*ROW_INC))/REF_ROW_COUNT)*b)

    textDataPhaseShift = Text(tab1, undo=True, width=10, height=0)
    textDataPhaseShift['font'] = ('consolas', '12')
    textDataPhaseShift.place(x=((FIRST_COL_Y+(0.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(5*ROW_INC))/REF_ROW_COUNT)*b)

    textNcycles = Label(tab1,text="Cycle count",font=("Arial", 10, "bold"))
    textNcycles.place(x=((FIRST_COL_Y+(0*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(6*ROW_INC))/REF_ROW_COUNT)*b)

    textDataNcycles = Text(tab1, undo=True, width=10, height=0)
    textDataNcycles['font'] = ('consolas', '12')
    textDataNcycles.place(x=((FIRST_COL_Y+(0.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(6*ROW_INC))/REF_ROW_COUNT)*b)





    # multi sine wave generator

    mtextTitle = Label(tab1,text="Multi Sine Wave Generator",font=("Arial", 10, "bold"))
    mtextTitle.place(x=((FIRST_COL_Y+(2*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(0*ROW_INC))/REF_ROW_COUNT)*b)

    mbuttonPlot = Button(tab1, text='Plot', width="15",
        command=lambda: mDoPlot(mtextDataF, mtextDataFs, mtextDataDCO, mtextDataAmp, mtextDataPhaseShift,
            mtextDataNcycles))
    mbuttonPlot.place(x=((FIRST_COL_Y+(3.75*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(1*ROW_INC))/REF_ROW_COUNT)*b)

    mbuttonSave = Button(tab1, text='Save Plot', width="15",
        command=lambda: mSavePlot(mtextDataF, mtextDataFs, mtextDataDCO, mtextDataAmp, mtextDataPhaseShift,
            mtextDataNcycles))

    mbuttonSave.place(x=((FIRST_COL_Y+(3.75*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(2*ROW_INC))/REF_ROW_COUNT)*b)
    
    mbuttonSaveSignal = Button(tab1, text='Save Signal', width="15",
        command=lambda: mwriteWave(mtextDataF, mtextDataFs, mtextDataDCO, mtextDataAmp, mtextDataPhaseShift,
            mtextDataNcycles))

    mbuttonSaveSignal.place(x=((FIRST_COL_Y+(3.75*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(3*ROW_INC))/REF_ROW_COUNT)*b)



    mbuttonSaveConfig = Button(tab1, text='Save Config', width="15",
        command=lambda: mSaveConfig(mtextDataF, mtextDataFs, mtextDataDCO, mtextDataAmp, mtextDataPhaseShift,
            mtextDataNcycles))
    mbuttonSaveConfig.place(x=((FIRST_COL_Y+(3.75*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(4*ROW_INC))/REF_ROW_COUNT)*b)

    mbuttonOpenConfig = Button(tab1, text='Open Config', width="15",
        command=lambda: mLoadConfig(mtextDataF, mtextDataFs, mtextDataDCO, mtextDataAmp, mtextDataPhaseShift,
            mtextDataNcycles))
    mbuttonOpenConfig.place(x=((FIRST_COL_Y+(3.75*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(5*ROW_INC))/REF_ROW_COUNT)*b)

    mbuttonClear = Button(tab1, text='Clear all', width="15",
        command=lambda: mClearData(mtextDataF, mtextDataFs, mtextDataDCO, mtextDataAmp, mtextDataPhaseShift,
            mtextDataNcycles))
    mbuttonClear.place(x=((FIRST_COL_Y+(3.75*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(6*ROW_INC))/REF_ROW_COUNT)*b)
    
    mtextF = Label(tab1,text="Signal Frequency",font=("Arial", 10, "bold"))    
    mtextF.place(x=((FIRST_COL_Y+(2*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(1*ROW_INC))/REF_ROW_COUNT)*b)

    mtextDataF = Text(tab1, undo=True, width=30, height=0)
    mtextDataF['font'] = ('consolas', '12')
    mtextDataF.place(x=((FIRST_COL_Y+(2.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(1*ROW_INC))/REF_ROW_COUNT)*b)
    
    
    mtextFs = Label(tab1,text="Sampling Frequency",font=("Arial", 10, "bold"))
    mtextFs.place(x=((FIRST_COL_Y+(2*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(2*ROW_INC))/REF_ROW_COUNT)*b)

    mtextDataFs = Text(tab1, undo=True, width=30, height=0)
    mtextDataFs['font'] = ('consolas', '12')
    mtextDataFs.place(x=((FIRST_COL_Y+(2.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(2*ROW_INC))/REF_ROW_COUNT)*b)

    mtextDCO = Label(tab1,text="DC Offset",font=("Arial", 10, "bold"))
    mtextDCO.place(x=((FIRST_COL_Y+(2*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(3*ROW_INC))/REF_ROW_COUNT)*b)

    mtextDataDCO = Text(tab1, undo=True, width=30, height=0)
    mtextDataDCO['font'] = ('consolas', '12')
    mtextDataDCO.place(x=((FIRST_COL_Y+(2.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(3*ROW_INC))/REF_ROW_COUNT)*b)

    mtextAmp = Label(tab1,text="Amplitude",font=("Arial", 10, "bold"))
    mtextAmp.place(x=((FIRST_COL_Y+(2*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(4*ROW_INC))/REF_ROW_COUNT)*b)

    mtextDataAmp = Text(tab1, undo=True, width=30, height=0)
    mtextDataAmp['font'] = ('consolas', '12')
    mtextDataAmp.place(x=((FIRST_COL_Y+(2.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(4*ROW_INC))/REF_ROW_COUNT)*b)

    mtextPhaseShift = Label(tab1,text="Phase Shift",font=("Arial", 10, "bold"))
    mtextPhaseShift.place(x=((FIRST_COL_Y+(2*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(5*ROW_INC))/REF_ROW_COUNT)*b)

    mtextDataPhaseShift = Text(tab1, undo=True, width=30, height=0)
    mtextDataPhaseShift['font'] = ('consolas', '12')
    mtextDataPhaseShift.place(x=((FIRST_COL_Y+(2.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(5*ROW_INC))/REF_ROW_COUNT)*b)

    mtextNcycles = Label(tab1,text="Cycle count",font=("Arial", 10, "bold"))
    mtextNcycles.place(x=((FIRST_COL_Y+(2*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(6*ROW_INC))/REF_ROW_COUNT)*b)

    mtextDataNcycles = Text(tab1, undo=True, width=30, height=0)
    mtextDataNcycles['font'] = ('consolas', '12')
    mtextDataNcycles.place(x=((FIRST_COL_Y+(2.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(6*ROW_INC))/REF_ROW_COUNT)*b)


    
    # noise mix block
    
    ntextTitle = Label(tab1,text="AWGN Noise mix with Signal",font=("Arial", 10, "bold"))
    ntextTitle.place(x=((FIRST_COL_Y+(0*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(8*ROW_INC))/REF_ROW_COUNT)*b)
   
    
    buttonOpenWave = Button(tab1, text='Open & Plot Wave', width="20",
        command=lambda: openAndPlotWave())
    buttonOpenWave.place(x=((FIRST_COL_Y+(0*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(9*ROW_INC))/REF_ROW_COUNT)*b)

    snrval = Label(tab1,text="SNR (dB)",font=("Arial", 10, "bold"))
    snrval.place(x=((FIRST_COL_Y+(0*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(10*ROW_INC))/REF_ROW_COUNT)*b)

    snrDataval = Text(tab1, undo=True, width=5, height=0)
    snrDataval['font'] = ('consolas', '12')
    snrDataval.place(x=((FIRST_COL_Y+(0.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(10*ROW_INC))/REF_ROW_COUNT)*b)

    b1 = Button(tab1, text='Plot Wave + AWGN Noise', width="25",
        command=lambda: signal_mix_awgn_noise(snrDataval))
    b1.place(x=((FIRST_COL_Y+(0*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(11*ROW_INC))/REF_ROW_COUNT)*b)

    b1 = Button(tab1, text='Save Wave + AWGN Noise', width="25",
        command=lambda: save_signal_mix_awgn_noise(snrDataval))
    b1.place(x=((FIRST_COL_Y+(0*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(12*ROW_INC))/REF_ROW_COUNT)*b)    
    
    
    # filter operation

    ntextTitle = Label(tab1,text="Filter Operations",font=("Arial", 10, "bold"))
    ntextTitle.place(x=((FIRST_COL_Y+(2*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(8*ROW_INC))/REF_ROW_COUNT)*b)
    
    Rblow = Radiobutton(tab1, text="low", variable=filter_var, value=1, command=sel)
    Rblow.place(x=((FIRST_COL_Y+(2*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(9*ROW_INC))/REF_ROW_COUNT)*b)    

    Rbhigh = Radiobutton(tab1, text="high", variable=filter_var, value=2, command=sel)
    Rbhigh.place(x=((FIRST_COL_Y+(2.25*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(9*ROW_INC))/REF_ROW_COUNT)*b)

    Rbpass = Radiobutton(tab1, text="pass", variable=filter_var, value=3, command=sel)
    Rbpass.place(x=((FIRST_COL_Y+(2.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(9*ROW_INC))/REF_ROW_COUNT)*b)

    Rbstop = Radiobutton(tab1, text="stop", variable=filter_var, value=4, command=sel)
    Rbstop.place(x=((FIRST_COL_Y+(2.75*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(9*ROW_INC))/REF_ROW_COUNT)*b)

    fpass = Label(tab1,text="fp (Hz)",font=("Arial", 10, "bold"))
    fpass.place(x=((FIRST_COL_Y+(2*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(10*ROW_INC))/REF_ROW_COUNT)*b)

    fpassData = Text(tab1, undo=True, width=10, height=0)
    fpassData['font'] = ('consolas', '12')
    fpassData.place(x=((FIRST_COL_Y+(2.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(10*ROW_INC))/REF_ROW_COUNT)*b)

    fstop = Label(tab1,text="fs (Hz)",font=("Arial", 10, "bold"))
    fstop.place(x=((FIRST_COL_Y+(2*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(11*ROW_INC))/REF_ROW_COUNT)*b)

    fstopData = Text(tab1, undo=True, width=10, height=0)
    fstopData['font'] = ('consolas', '12')
    fstopData.place(x=((FIRST_COL_Y+(2.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(11*ROW_INC))/REF_ROW_COUNT)*b)
    
    attenuationfs = Label(tab1,text="attemuation stop (dB)",font=("Arial", 10, "bold"))
    attenuationfs.place(x=((FIRST_COL_Y+(2*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(12*ROW_INC))/REF_ROW_COUNT)*b)

    attenuationfsData = Text(tab1, undo=True, width=10, height=0)
    attenuationfsData['font'] = ('consolas', '12')
    attenuationfsData.place(x=((FIRST_COL_Y+(2.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(12*ROW_INC))/REF_ROW_COUNT)*b)  
    
    samplingrate = Label(tab1,text="Sampling Frequency",font=("Arial", 10, "bold"))
    samplingrate.place(x=((FIRST_COL_Y+(3*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(10*ROW_INC))/REF_ROW_COUNT)*b)

    samplingrateData = Text(tab1, undo=True, width=10, height=0)
    samplingrateData['font'] = ('consolas', '12')
    samplingrateData.place(x=((FIRST_COL_Y+(3.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(10*ROW_INC))/REF_ROW_COUNT)*b)    
    
    f1 = Label(tab1,text="f1 (Hz)",font=("Arial", 10, "bold"))
    f1.place(x=((FIRST_COL_Y+(3*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(11*ROW_INC))/REF_ROW_COUNT)*b)

    f1Data = Text(tab1, undo=True, width=10, height=0)
    f1Data['font'] = ('consolas', '12')
    f1Data.place(x=((FIRST_COL_Y+(3.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(11*ROW_INC))/REF_ROW_COUNT)*b)

    f2 = Label(tab1,text="f2 (Hz)",font=("Arial", 10, "bold"))
    f2.place(x=((FIRST_COL_Y+(3*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(12*ROW_INC))/REF_ROW_COUNT)*b)

    f2Data = Text(tab1, undo=True, width=10, height=0)
    f2Data['font'] = ('consolas', '12')
    f2Data.place(x=((FIRST_COL_Y+(3.5*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(12*ROW_INC))/REF_ROW_COUNT)*b) 
    
    bfilter_resp = Button(tab1, text='Plot filter response', width="25",
        command=lambda: plot_fir_response(fpassData, fstopData, attenuationfsData, samplingrateData, 
                                         f1Data, f2Data, filter_var))
    bfilter_resp.place(x=((FIRST_COL_Y+(2*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(13*ROW_INC))/REF_ROW_COUNT)*b)

    bsave_filter_resp = Button(tab1, text='Save plot filter response', width="25",
        command=lambda: save_plot_fir_response(fpassData, fstopData, attenuationfsData, samplingrateData, 
                                         f1Data, f2Data, filter_var))
    bsave_filter_resp.place(x=((FIRST_COL_Y+(3*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(13*ROW_INC))/REF_ROW_COUNT)*b)    

    bfilter_save_config = Button(tab1, text='Save filter config', width="25",
        command=lambda: filterSaveConfig(fpassData, fstopData, attenuationfsData, samplingrateData, 
                                         f1Data, f2Data, filter_var))
    bfilter_save_config.place(x=((FIRST_COL_Y+(2*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(14*ROW_INC))/REF_ROW_COUNT)*b)

    bfilter_load_config = Button(tab1, text='Load filter config', width="25",
        command=lambda: filterLoadConfig(fpassData, fstopData, attenuationfsData, samplingrateData, 
                                         f1Data, f2Data, filter_var, Rblow, Rbhigh, Rbpass, Rbstop))
    bfilter_load_config.place(x=((FIRST_COL_Y+(3*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(14*ROW_INC))/REF_ROW_COUNT)*b)

    bplot_filter_wave = Button(tab1, text='Plot filter on wave', width="25",
        command=lambda: filter_wave_plot(fpassData, fstopData, attenuationfsData, 
                                         f1Data, f2Data, filter_var))
    bplot_filter_wave.place(x=((FIRST_COL_Y+(2*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(15*ROW_INC))/REF_ROW_COUNT)*b)

    bsave_filter_wave = Button(tab1, text='Save filter on wave', width="25",
        command=lambda: filter_wave_save(fpassData, fstopData, attenuationfsData, 
                                         f1Data, f2Data, filter_var))
    bsave_filter_wave.place(x=((FIRST_COL_Y+(3*COL_INC))/REF_COL_COUNT)*a,y=((FIRST_COL_X+(15*ROW_INC))/REF_ROW_COUNT)*b)
    
    pass

def sel():
    pass

if __name__ == "__main__":

    root = Tk()
    root.tk.call('encoding', 'system', 'utf-8')
    root.resizable(0,0)

    a = root.winfo_screenwidth()
    b = root.winfo_screenheight()    

    note = Notebook(root,width=a,height=b)
    filter_var = IntVar()
    tab1 = Frame(note)
    
    note.add(tab1, text = "Octave Operations by Python 3.x:: Vasanth")

    Tab2_Data = Design_Tab1()    

    note.pack()
    root.mainloop()
    