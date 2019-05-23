#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 20:56:28 2019

@author: Vasanth
"""

# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.scrolledtext as tkst
import tkinter as tki
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter.ttk import *
import ctypes
import os, psutil, string
from subprocess import Popen

from oct2py import octave

import time, datetime
from datetime import *
from time import *
import ast

from tkinter.messagebox import *
import tkinter.messagebox

def mDoPlot(textDataF, textDataFs, textDataDCO, textDataAmp, textDataPhaseShift,
    textDataNcycles):
    
    f = textDataF.get(1.0, END)
    fs = textDataFs.get(1.0, END)
    dco = textDataDCO.get(1.0, END)
    amp = textDataAmp.get(1.0, END)
    ph = textDataPhaseShift.get(1.0, END)
    nc = textDataNcycles.get(1.0, END)

    pf = f.lstrip().rstrip()
    pfs = fs.lstrip().rstrip()
    pdco = dco.lstrip().rstrip()
    pamp = amp.lstrip().rstrip()
    pph = ph.lstrip().rstrip()
    pnc = nc.lstrip().rstrip()


    lf = list(map(float, f.lstrip().rstrip().split(",")))

    pfs = 30*max(lf)
    pdco = 0
    pamp = 1
    pph = 0
    pnc = 25
    
    xy = octave.mFsine(lf, pfs, pdco, pamp, pph, pnc)

    pass

def mSavePlot(textDataF, textDataFs, textDataDCO, textDataAmp, textDataPhaseShift,
    textDataNcycles):
    
    f = textDataF.get(1.0, END)
    fs = textDataFs.get(1.0, END)
    dco = textDataDCO.get(1.0, END)
    amp = textDataAmp.get(1.0, END)
    ph = textDataPhaseShift.get(1.0, END)
    nc = textDataNcycles.get(1.0, END)

    pf = f.lstrip().rstrip()
    pfs = fs.lstrip().rstrip()
    pdco = dco.lstrip().rstrip()
    pamp = amp.lstrip().rstrip()
    pph = ph.lstrip().rstrip()
    pnc = nc.lstrip().rstrip()


    lf = list(map(float, f.lstrip().rstrip().split(",")))

    pfs = 30*max(lf)
    pdco = 0
    pamp = 1
    pph = 0
    pnc = 25
    
    xy = octave.mSavePlot(lf, pfs, pdco, pamp, pph, pnc)

    pass

def mwriteWave(textDataF, textDataFs, textDataDCO, textDataAmp, textDataPhaseShift,
    textDataNcycles):
    
    f = textDataF.get(1.0, END)
    fs = textDataFs.get(1.0, END)
    dco = textDataDCO.get(1.0, END)
    amp = textDataAmp.get(1.0, END)
    ph = textDataPhaseShift.get(1.0, END)
    nc = textDataNcycles.get(1.0, END)

    pf = f.lstrip().rstrip()
    pfs = fs.lstrip().rstrip()
    pdco = dco.lstrip().rstrip()
    pamp = amp.lstrip().rstrip()
    pph = ph.lstrip().rstrip()
    pnc = nc.lstrip().rstrip()


    lf = list(map(float, f.lstrip().rstrip().split(",")))

    pfs = 30*max(lf)
    pdco = 0
    pamp = 1
    pph = 0
    pnc = 25
    
    xy = octave.mwriteWave(lf, pfs, pdco, pamp, pph, pnc)

    pass


def mSaveConfig(mtextDataF, mtextDataFs, mtextDataDCO, mtextDataAmp, mtextDataPhaseShift,
            mtextDataNcycles):
    
    f = mtextDataF.get(1.0, END)
    fs = mtextDataFs.get(1.0, END)
    dco = mtextDataDCO.get(1.0, END)
    amp = mtextDataAmp.get(1.0, END)
    ph = mtextDataPhaseShift.get(1.0, END)
    nc = mtextDataNcycles.get(1.0, END)
    
    dict1 = {}
    dict1['f'] = f
    dict1['fs'] = fs
    dict1['dco'] = dco
    dict1['amp'] = amp
    dict1['ps'] = ph
    dict1['nc'] = nc
    
    fo = open('msignalconfig.txt', 'w')
    fo.write(str(dict1))
    fo.close()
    
    pass

def mLoadConfig(mtextDataF, mtextDataFs, mtextDataDCO, mtextDataAmp, mtextDataPhaseShift,
            mtextDataNcycles):
    
    fi = open('msignalconfig.txt', "r")
    for line in fi:
        dict1 = ast.literal_eval(line)
    
    fi.close()

    mtextDataF.delete('1.0', END)
    mtextDataFs.delete('1.0', END)
    mtextDataDCO.delete('1.0', END)
    mtextDataAmp.delete('1.0', END)
    mtextDataPhaseShift.delete('1.0', END)
    mtextDataNcycles.delete('1.0', END)    
    
    mtextDataF.insert(INSERT, dict1['f'])
    mtextDataFs.insert(INSERT, dict1['fs'])
    mtextDataDCO.insert(INSERT, dict1['dco'])
    mtextDataAmp.insert(INSERT, dict1['amp'])
    mtextDataPhaseShift.insert(INSERT, dict1['ps'])
    mtextDataNcycles.insert(INSERT, dict1['nc'])
    
    pass

def mClearData(mtextDataF, mtextDataFs, mtextDataDCO, mtextDataAmp, mtextDataPhaseShift,
            mtextDataNcycles):
        
    mtextDataF.delete('1.0', END)
    mtextDataFs.delete('1.0', END)
    mtextDataDCO.delete('1.0', END)
    mtextDataAmp.delete('1.0', END)
    mtextDataPhaseShift.delete('1.0', END)
    mtextDataNcycles.delete('1.0', END)
    
    pass



def DoPlot(textDataF, textDataFs, textDataDCO, textDataAmp, textDataPhaseShift,
    textDataNcycles):
    
    f = textDataF.get(1.0, END)
    fs = textDataFs.get(1.0, END)
    dco = textDataDCO.get(1.0, END)
    amp = textDataAmp.get(1.0, END)
    ph = textDataPhaseShift.get(1.0, END)
    nc = textDataNcycles.get(1.0, END)

    pf = f.lstrip().rstrip()
    pfs = fs.lstrip().rstrip()
    pdco = dco.lstrip().rstrip()
    pamp = amp.lstrip().rstrip()
    pph = ph.lstrip().rstrip()
    pnc = nc.lstrip().rstrip()

    if pf == "":
        pf = 10.0
    if pfs =="":
        pfs = 200.0
    if pdco == "":
        pdco = 0.0
    if pamp == "":
        pamp = 1.0
    if pph == "":
        pph = 0.0
    if pnc == "":
        pnc = 25.0
    
    xy = octave.Fsine(float(pf), float(pfs), float(pdco), float(pamp), float(pph), float(pnc))

    pass


def SavePlot(textDataF, textDataFs, textDataDCO, textDataAmp, textDataPhaseShift,
    textDataNcycles):
    
    f = textDataF.get(1.0, END)
    fs = textDataFs.get(1.0, END)
    dco = textDataDCO.get(1.0, END)
    amp = textDataAmp.get(1.0, END)
    ph = textDataPhaseShift.get(1.0, END)
    nc = textDataNcycles.get(1.0, END)

    pf = f.lstrip().rstrip()
    pfs = fs.lstrip().rstrip()
    pdco = dco.lstrip().rstrip()
    pamp = amp.lstrip().rstrip()
    pph = ph.lstrip().rstrip()
    pnc = nc.lstrip().rstrip()

    if pf == "":
        pf = 10.0
    if pfs =="":
        pfs = 200.0
    if pdco == "":
        pdco = 0.0
    if pamp == "":
        pamp = 1.0
    if pph == "":
        pph = 0.0
    if pnc == "":
        pnc = 5.0

    xy = octave.SavePlot(float(pf), float(pfs), float(pdco), float(pamp), float(pph), float(pnc))

    pass

def writeWave(textDataF, textDataFs, textDataDCO, textDataAmp, textDataPhaseShift,
    textDataNcycles):
    
    f = textDataF.get(1.0, END)
    fs = textDataFs.get(1.0, END)
    dco = textDataDCO.get(1.0, END)
    amp = textDataAmp.get(1.0, END)
    ph = textDataPhaseShift.get(1.0, END)
    nc = textDataNcycles.get(1.0, END)

    pf = f.lstrip().rstrip()
    pfs = fs.lstrip().rstrip()
    pdco = dco.lstrip().rstrip()
    pamp = amp.lstrip().rstrip()
    pph = ph.lstrip().rstrip()
    pnc = nc.lstrip().rstrip()

    if pf == "":
        pf = 10.0
    if pfs =="":
        pfs = 200.0
    if pdco == "":
        pdco = 0.0
    if pamp == "":
        pamp = 1.0
    if pph == "":
        pph = 0.0
    if pnc == "":
        pnc = 5.0
    
    xy = octave.writeWave(float(pf), float(pfs), float(pdco), float(pamp), float(pph), float(pnc))

    pass

def SaveConfig(textDataF, textDataFs, textDataDCO, textDataAmp, textDataPhaseShift,
    textDataNcycles):
    
    f = textDataF.get(1.0, END)
    fs = textDataFs.get(1.0, END)
    dco = textDataDCO.get(1.0, END)
    amp = textDataAmp.get(1.0, END)
    ph = textDataPhaseShift.get(1.0, END)
    nc = textDataNcycles.get(1.0, END)
    
    dict1 = {}
    dict1['f'] = f
    dict1['fs'] = fs
    dict1['dco'] = dco
    dict1['amp'] = amp
    dict1['ps'] = ph
    dict1['nc'] = nc
    
    fo = open('signalconfig.txt', 'w')
    fo.write(str(dict1))
    fo.close()
    
    pass

def LoadConfig(textDataF, textDataFs, textDataDCO, textDataAmp, textDataPhaseShift,
    textDataNcycles):
    
    fi = open('signalconfig.txt', "r")
    for line in fi:
        dict1 = ast.literal_eval(line)
    
    fi.close()

    textDataF.delete('1.0', END)
    textDataFs.delete('1.0', END)
    textDataDCO.delete('1.0', END)
    textDataAmp.delete('1.0', END)
    textDataPhaseShift.delete('1.0', END)
    textDataNcycles.delete('1.0', END)    
    
    textDataF.insert(INSERT, dict1['f'])
    textDataFs.insert(INSERT, dict1['fs'])
    textDataDCO.insert(INSERT, dict1['dco'])
    textDataAmp.insert(INSERT, dict1['amp'])
    textDataPhaseShift.insert(INSERT, dict1['ps'])
    textDataNcycles.insert(INSERT, dict1['nc'])
    
    pass



def ClearData(textDataF, textDataFs, textDataDCO, textDataAmp, textDataPhaseShift,
    textDataNcycles):
    
    textDataF.delete('1.0', END)
    textDataFs.delete('1.0', END)
    textDataDCO.delete('1.0', END)
    textDataAmp.delete('1.0', END)
    textDataPhaseShift.delete('1.0', END)
    textDataNcycles.delete('1.0', END)
    
    pass


def openAndPlotWave():
    filename = askopenfilename(filetypes=[("Wave files","*.wav")])    
    ret = octave.plotwave(filename)    
    pass


def signal_mix_awgn_noise(snrDataval):
    
    snrval = snrDataval.get(1.0, END)
    
    if snrval.lstrip().rstrip() == "":
        snrval = 2.0
        
    filename = askopenfilename(filetypes=[("Wave files","*.wav")])    
    ret = octave.signal_mix_awgn_noise(filename, float(snrval))
    
    pass
    
def save_signal_mix_awgn_noise(snrDataval):
    
    snrval = snrDataval.get(1.0, END)
    
    if snrval.lstrip().rstrip() == "":
        snrval = 2.0
        
    filename = askopenfilename(filetypes=[("Wave files","*.wav")])    
    ret = octave.save_signal_mix_awgn_noise(filename, float(snrval))
    
    pass


def plot_fir_response(fpassData, fstopData, attenuationfsData, samplingrateData, 
                     f1Data, f2Data, filter_var):
    
    fpass = fpassData.get(1.0, END)
    fstop = fstopData.get(1.0, END)
    attenuationfs = attenuationfsData.get(1.0, END)
    fs = samplingrateData.get(1.0, END)
    f1 = f1Data.get(1.0, END)
    f2 = f2Data.get(1.0, END)
    
    
    filterDict = {1 : "low", 2 : "high", 3 : "pass", 4 : "stop"}
    filterChosen = filterDict[filter_var.get()]
    
    if f1.lstrip().rstrip() == "" or f2.lstrip().rstrip() == "":
        f1, f2 = 1, 2        
        
    if fpass.lstrip().rstrip() == "" or fstop.lstrip().rstrip() == "":
        fpass, fstop = 1, 2
    
    ret = octave.plot_fir_response(float(fpass), float(fstop), float(fs), float(attenuationfs), 
                                   filterChosen, float(f1), float(f2))

    pass


def save_plot_fir_response(fpassData, fstopData, attenuationfsData, samplingrateData, 
                     f1Data, f2Data, filter_var):
    
    fpass = fpassData.get(1.0, END)
    fstop = fstopData.get(1.0, END)
    attenuationfs = attenuationfsData.get(1.0, END)
    fs = samplingrateData.get(1.0, END)
    f1 = f1Data.get(1.0, END)
    f2 = f2Data.get(1.0, END)
    
    
    filterDict = {1 : "low", 2 : "high", 3 : "pass", 4 : "stop"}
    filterChosen = filterDict[filter_var.get()]
    
    if f1.lstrip().rstrip() == "" or f2.lstrip().rstrip() == "":
        f1, f2 = 1, 2        
        
    if fpass.lstrip().rstrip() == "" or fstop.lstrip().rstrip() == "":
        fpass, fstop = 1, 2
    
    ret = octave.save_plot_fir_response(float(fpass), float(fstop), float(fs), float(attenuationfs), 
                                   filterChosen, float(f1), float(f2))

    pass


def filterSaveConfig(fpassData, fstopData, attenuationfsData, samplingrateData, 
                     f1Data, f2Data, filter_var):
    fpass = fpassData.get(1.0, END)
    fstop = fstopData.get(1.0, END)
    attenuationfs = attenuationfsData.get(1.0, END)
    fs = samplingrateData.get(1.0, END)
    f1 = f1Data.get(1.0, END)
    f2 = f2Data.get(1.0, END)
    filter_type = filter_var.get()

    
    dict1 = {}
    dict1['fpass'] = fpass
    dict1['fstop'] = fstop
    dict1['attenuationfs'] = attenuationfs
    dict1['fs'] = fs
    dict1['f1'] = f1
    dict1['f2'] = f2
    dict1['filter_type'] = filter_type
    
    fo = open('filter_config.txt', 'w')
    fo.write(str(dict1))
    fo.close()
    
    pass


def filterLoadConfig(fpassData, fstopData, attenuationfsData, samplingrateData, 
                     f1Data, f2Data, filter_var, Rblow, Rbhigh, Rbpass, Rbstop):
    
    fi = open('filter_config.txt', "r")
    for line in fi:
        dict1 = ast.literal_eval(line)
    
    fi.close()

    fpassData.delete('1.0', END)
    fstopData.delete('1.0', END)
    attenuationfsData.delete('1.0', END)
    samplingrateData.delete('1.0', END)
    f1Data.delete('1.0', END)
    f2Data.delete('1.0', END)
    
    fpassData.insert(INSERT, dict1['fpass'])
    fstopData.insert(INSERT, dict1['fstop'])
    attenuationfsData.insert(INSERT, dict1['attenuationfs'])
    samplingrateData.insert(INSERT, dict1['fs'])
    f1Data.insert(INSERT, dict1['f1'])
    f2Data.insert(INSERT, dict1['f2'])
    
    if int(dict1['filter_type']) == 1:
        Rblow.invoke()
    elif int(dict1['filter_type']) == 2:
        Rbhigh.invoke()
    elif int(dict1['filter_type']) == 3:
        Rbpass.invoke()
    elif int(dict1['filter_type']) == 4:
        Rbstop.invoke()
    
    
    pass


def filter_wave_plot(fpassData, fstopData, attenuationfsData,
                     f1Data, f2Data, filter_var):
    
    filename = askopenfilename(filetypes=[("Wave files","*.wav")])  
    
    fpass = fpassData.get(1.0, END)
    fstop = fstopData.get(1.0, END)
    attenuationfs = attenuationfsData.get(1.0, END)    
    f1 = f1Data.get(1.0, END)
    f2 = f2Data.get(1.0, END)
    
    
    filterDict = {1 : "low", 2 : "high", 3 : "pass", 4 : "stop"}
    filterChosen = filterDict[filter_var.get()]
    
    if f1.lstrip().rstrip() == "" or f2.lstrip().rstrip() == "":
        f1, f2 = 1, 2        
        
    if fpass.lstrip().rstrip() == "" or fstop.lstrip().rstrip() == "":
        fpass, fstop = 1, 2
    
    ret = octave.filter_on_wave(filename, float(fpass), float(fstop), float(attenuationfs), 
                                   filterChosen, float(f1), float(f2))
    
    pass

def filter_wave_save(fpassData, fstopData, attenuationfsData,
                     f1Data, f2Data, filter_var):
    
    filename = askopenfilename(filetypes=[("Wave files","*.wav")])  
    
    fpass = fpassData.get(1.0, END)
    fstop = fstopData.get(1.0, END)
    attenuationfs = attenuationfsData.get(1.0, END)    
    f1 = f1Data.get(1.0, END)
    f2 = f2Data.get(1.0, END)
    
    
    filterDict = {1 : "low", 2 : "high", 3 : "pass", 4 : "stop"}
    filterChosen = filterDict[filter_var.get()]
    
    if f1.lstrip().rstrip() == "" or f2.lstrip().rstrip() == "":
        f1, f2 = 1, 2        
        
    if fpass.lstrip().rstrip() == "" or fstop.lstrip().rstrip() == "":
        fpass, fstop = 1, 2
    
    ret = octave.filter_on_wave_save(filename, float(fpass), float(fstop), float(attenuationfs), 
                                   filterChosen, float(f1), float(f2))
    
    pass






