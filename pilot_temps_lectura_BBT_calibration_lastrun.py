#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on enero 24, 2022, at 16:06
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'sounddevice'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'temps_lectura'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Brainvitge\\Desktop\\Clara\\pilot_eeg_Mundet\\pilot_temps_lectura_BBT_calibration_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1024, 768], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "loading_phrases"
loading_phrasesClock = core.Clock()
condList = []
corrAns = []

# Initialize components for Routine "setting_parameters"
setting_parametersClock = core.Clock()
import random

event.Mouse(visible = False)

# sentence file
soundF = ''

# variables for the onsets of words 
onset_keyw_2 = 0
onset_keyw_1 = 0
onset_keyw = 0
onset_keyw_plus1 = 0
onset_endingw = 0

pausa_msg = ''

# trigger pulse duration
pulseDur = 0.01


aux = []
aux_cond = []

# Initialize components for Routine "start"
startClock = core.Clock()
start_txt = visual.TextStim(win=win, name='start_txt',
    text='Vamos a empezar la tarea.\n\nPulsa la barra espaciadora para empezar',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
start_resp = keyboard.Keyboard()
port_start = parallel.ParallelPort(address='0xC100')

# Initialize components for Routine "wait"
waitClock = core.Clock()
wait_img = visual.ImageStim(
    win=win,
    name='wait_img', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "setting_trial"
setting_trialClock = core.Clock()

# Initialize components for Routine "main"
mainClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
stim_phrase = sound.Sound('A', secs=-1, stereo=True, hamming=False,
    name='stim_phrase')
stim_phrase.setVolume(1.0)
keyw_2 = parallel.ParallelPort(address='0xC100')
keyw_1 = parallel.ParallelPort(address='0xC100')
keyw = parallel.ParallelPort(address='0xC100')
keyw_plus1 = parallel.ParallelPort(address='0xC100')
endingw = parallel.ParallelPort(address='0xC100')
port_onset_stim = parallel.ParallelPort(address='0xC100')
port_fix = parallel.ParallelPort(address='0xC100')

# Initialize components for Routine "question"
questionClock = core.Clock()
item_check = visual.TextStim(win=win, name='item_check',
    text='¿Era correcta la frase anterior?',
    font='Arial',
    pos=(0, 0.05), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
question_resp = keyboard.Keyboard()
yes_rect = visual.Rect(
    win=win, name='yes_rect',
    width=(0.125, 0.05)[0], height=(0.125, 0.05)[1],
    ori=0.0, pos=(-0.15, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=(0.9216, 0.9216, 0.7255), fillColor=(0.9216, 0.9216, 0.7255),
    opacity=None, depth=-2.0, interpolate=True)
no_rect = visual.Rect(
    win=win, name='no_rect',
    width=(0.125, 0.05)[0], height=(0.125, 0.05)[1],
    ori=0.0, pos=(0.15, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=(0.9216, 0.9216, 0.7255), fillColor=(0.9216, 0.9216, 0.7255),
    opacity=None, depth=-3.0, interpolate=True)
yes = visual.TextStim(win=win, name='yes',
    text='Sí',
    font='Arial',
    pos=(-.15, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
no = visual.TextStim(win=win, name='no',
    text='No',
    font='Arial',
    pos=(0.15, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
auxOut1 = []
auxOut2 = []
port_q = parallel.ParallelPort(address='0xC100')

# Initialize components for Routine "blink"
blinkClock = core.Clock()
blink_txt = visual.TextStim(win=win, name='blink_txt',
    text='****',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
port_blink = parallel.ParallelPort(address='0xC100')

# Initialize components for Routine "pausa"
pausaClock = core.Clock()
pausa_txt = visual.TextStim(win=win, name='pausa_txt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
pausa_resp = keyboard.Keyboard()
port_pausa = parallel.ParallelPort(address='0xC100')

# Initialize components for Routine "intertrial"
intertrialClock = core.Clock()
inter_img = visual.ImageStim(
    win=win,
    name='inter_img', 
    image=None, mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
load = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Triggers_list1.xlsx'),
    seed=None, name='load')
thisExp.addLoop(load)  # add the loop to the experiment
thisLoad = load.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoad.rgb)
if thisLoad != None:
    for paramName in thisLoad:
        exec('{} = thisLoad[paramName]'.format(paramName))

for thisLoad in load:
    currentLoop = load
    # abbreviate parameter names if possible (e.g. rgb = thisLoad.rgb)
    if thisLoad != None:
        for paramName in thisLoad:
            exec('{} = thisLoad[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "loading_phrases"-------
    continueRoutine = True
    # update component parameters for each repeat
    condList.append([nSent, stim, cond, length, onset_keyw_2, onset_keyw_1, onset_keyw, onset_keyw_plus1, onset_endingw, corrAns])
    # keep track of which components have finished
    loading_phrasesComponents = []
    for thisComponent in loading_phrasesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    loading_phrasesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "loading_phrases"-------
    while continueRoutine:
        # get current time
        t = loading_phrasesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=loading_phrasesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in loading_phrasesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "loading_phrases"-------
    for thisComponent in loading_phrasesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "loading_phrases" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'load'


# ------Prepare to start Routine "setting_parameters"-------
continueRoutine = True
# update component parameters for each repeat
# TASK PARAMETERS
# ---------------

totalTrials = len(condList)

# triggers
trig_start = 0
trig_fix = 1
trig_onset_stim = 1
trig_keyw_2 = 0
trig_keyw_1 = 0
trig_keyw = 0
trig_keyw_plus1 = 0
trig_endingw = 0
trig_question = 0
trig_blink = 0
trig_pausa = 0

corrAns = []

# counters
nTrial = 0
nRow = -1
nInter = -1
nPausa = 12

# stim durations
start_q = 0.5 # blank period before question 
              # blank period before blink window
delayFix = 0.5 # duration of silence before onset audio stim with fixation on screen
blinkDur = 1.0 # blink window

# array of possible intertrial durations
auxInter = [1.5, 1.75, 2, 2.25, 2.5]
interDur = 0

modePausa = False
modeInter = True


# print(condList)
random.shuffle(condList)

kk = 0
i = 2
while i <= totalTrials - 1:
    #print(i)
    '''
    print(i)
    print(condList[i][1])
    print(condList[i-1][1])
    print(condList[i-2][1])
    '''
    aux = []
    if condList[i][1] == condList[i-1][1] and condList[i][1] == condList[i-2][1]:
        aux = condList[i:]
        random.shuffle(aux)
        condList[i:] = aux[:]
        kk = kk + 1
        i = i- 1
    else:
        kk = 0
    
    if kk > 10:
        random.shuffle(condList)
        i = 1   
    
    i = i + 1 

for i in range(totalTrials):
    print(condList[i][0])
 
# print(condList) 
# keep track of which components have finished
setting_parametersComponents = []
for thisComponent in setting_parametersComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setting_parametersClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setting_parameters"-------
while continueRoutine:
    # get current time
    t = setting_parametersClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setting_parametersClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setting_parametersComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setting_parameters"-------
for thisComponent in setting_parametersComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setting_parameters" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start"-------
continueRoutine = True
# update component parameters for each repeat
start_resp.keys = []
start_resp.rt = []
_start_resp_allKeys = []
# keep track of which components have finished
startComponents = [start_txt, start_resp, port_start]
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start"-------
while continueRoutine:
    # get current time
    t = startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_txt* updates
    if start_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_txt.frameNStart = frameN  # exact frame index
        start_txt.tStart = t  # local t and not account for scr refresh
        start_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_txt, 'tStartRefresh')  # time at next scr refresh
        start_txt.setAutoDraw(True)
    
    # *start_resp* updates
    waitOnFlip = False
    if start_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_resp.frameNStart = frameN  # exact frame index
        start_resp.tStart = t  # local t and not account for scr refresh
        start_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_resp, 'tStartRefresh')  # time at next scr refresh
        start_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_resp.status == STARTED and not waitOnFlip:
        theseKeys = start_resp.getKeys(keyList=['space'], waitRelease=False)
        _start_resp_allKeys.extend(theseKeys)
        if len(_start_resp_allKeys):
            start_resp.keys = _start_resp_allKeys[-1].name  # just the last key pressed
            start_resp.rt = _start_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # *port_start* updates
    if port_start.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        port_start.frameNStart = frameN  # exact frame index
        port_start.tStart = t  # local t and not account for scr refresh
        port_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(port_start, 'tStartRefresh')  # time at next scr refresh
        port_start.status = STARTED
        win.callOnFlip(port_start.setData, int(trig_start))
    if port_start.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > port_start.tStartRefresh + pulseDur-frameTolerance:
            # keep track of stop time/frame for later
            port_start.tStop = t  # not accounting for scr refresh
            port_start.frameNStop = frameN  # exact frame index
            win.timeOnFlip(port_start, 'tStopRefresh')  # time at next scr refresh
            port_start.status = FINISHED
            win.callOnFlip(port_start.setData, int(0))
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('start_txt.started', start_txt.tStartRefresh)
thisExp.addData('start_txt.stopped', start_txt.tStopRefresh)
# check responses
if start_resp.keys in ['', [], None]:  # No response was made
    start_resp.keys = None
thisExp.addData('start_resp.keys',start_resp.keys)
if start_resp.keys != None:  # we had a response
    thisExp.addData('start_resp.rt', start_resp.rt)
thisExp.addData('start_resp.started', start_resp.tStartRefresh)
thisExp.addData('start_resp.stopped', start_resp.tStopRefresh)
thisExp.nextEntry()
if port_start.status == STARTED:
    win.callOnFlip(port_start.setData, int(0))
thisExp.addData('port_start.started', port_start.tStart)
thisExp.addData('port_start.stopped', port_start.tStop)
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "wait"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
waitComponents = [wait_img]
for thisComponent in waitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
waitClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "wait"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = waitClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=waitClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *wait_img* updates
    if wait_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        wait_img.frameNStart = frameN  # exact frame index
        wait_img.tStart = t  # local t and not account for scr refresh
        wait_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(wait_img, 'tStartRefresh')  # time at next scr refresh
        wait_img.setAutoDraw(True)
    if wait_img.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > wait_img.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            wait_img.tStop = t  # not accounting for scr refresh
            wait_img.frameNStop = frameN  # exact frame index
            win.timeOnFlip(wait_img, 'tStopRefresh')  # time at next scr refresh
            wait_img.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in waitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait"-------
for thisComponent in waitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('wait_img.started', wait_img.tStartRefresh)
thisExp.addData('wait_img.stopped', wait_img.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=totalTrials, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "setting_trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    nTrial = nTrial + 1
    nRow = nRow + 1
    
    # setting the stim to present
    soundF = "rythm_v2.wav"
    
    soundDur = condList[trials.thisN][3]
    fixDur = delayFix + soundDur
    
    print(fixDur)
    
    onset_keyw_2 = delayFix + condList[trials.thisN][4]
    onset_keyw_1 = delayFix + condList[trials.thisN][5]
    onset_keyw = delayFix + condList[trials.thisN][6]
    onset_keyw_plus1 = delayFix + condList[trials.thisN][7]
    onset_endingw = delayFix + condList[trials.thisN][8]
    
    #trig_onset_stim = condList[trials.thisN][2]
    print(trig_onset_stim)
    
    # setting the intertrial duration
    random.shuffle(auxInter)
    interDur = auxInter[0]
    
    # setting the correct answer for this trials
    corrAns = condList[trials.thisN][9]
    # keep track of which components have finished
    setting_trialComponents = []
    for thisComponent in setting_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    setting_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "setting_trial"-------
    while continueRoutine:
        # get current time
        t = setting_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=setting_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in setting_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "setting_trial"-------
    for thisComponent in setting_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "setting_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "main"-------
    continueRoutine = True
    # update component parameters for each repeat
    stim_phrase.setSound(soundF, hamming=False)
    stim_phrase.setVolume(1.0, log=False)
    # keep track of which components have finished
    mainComponents = [fix, stim_phrase, keyw_2, keyw_1, keyw, keyw_plus1, endingw, port_onset_stim, port_fix]
    for thisComponent in mainComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    mainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "main"-------
    while continueRoutine:
        # get current time
        t = mainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=mainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            fix.setAutoDraw(True)
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + fixDur-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                fix.setAutoDraw(False)
        # start/stop stim_phrase
        if stim_phrase.status == NOT_STARTED and tThisFlip >= delayFix-frameTolerance:
            # keep track of start time/frame for later
            stim_phrase.frameNStart = frameN  # exact frame index
            stim_phrase.tStart = t  # local t and not account for scr refresh
            stim_phrase.tStartRefresh = tThisFlipGlobal  # on global time
            stim_phrase.play(when=win)  # sync with win flip
        # *keyw_2* updates
        if keyw_2.status == NOT_STARTED and t >= onset_keyw_2-frameTolerance:
            # keep track of start time/frame for later
            keyw_2.frameNStart = frameN  # exact frame index
            keyw_2.tStart = t  # local t and not account for scr refresh
            keyw_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyw_2, 'tStartRefresh')  # time at next scr refresh
            keyw_2.status = STARTED
            win.callOnFlip(keyw_2.setData, int(trig_keyw_2))
        if keyw_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > keyw_2.tStartRefresh + pulseDur-frameTolerance:
                # keep track of stop time/frame for later
                keyw_2.tStop = t  # not accounting for scr refresh
                keyw_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(keyw_2, 'tStopRefresh')  # time at next scr refresh
                keyw_2.status = FINISHED
                win.callOnFlip(keyw_2.setData, int(0))
        # *keyw_1* updates
        if keyw_1.status == NOT_STARTED and t >= onset_keyw_1-frameTolerance:
            # keep track of start time/frame for later
            keyw_1.frameNStart = frameN  # exact frame index
            keyw_1.tStart = t  # local t and not account for scr refresh
            keyw_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyw_1, 'tStartRefresh')  # time at next scr refresh
            keyw_1.status = STARTED
            win.callOnFlip(keyw_1.setData, int(trig_keyw_1))
        if keyw_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > keyw_1.tStartRefresh + pulseDur-frameTolerance:
                # keep track of stop time/frame for later
                keyw_1.tStop = t  # not accounting for scr refresh
                keyw_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(keyw_1, 'tStopRefresh')  # time at next scr refresh
                keyw_1.status = FINISHED
                win.callOnFlip(keyw_1.setData, int(0))
        # *keyw* updates
        if keyw.status == NOT_STARTED and t >= onset_keyw-frameTolerance:
            # keep track of start time/frame for later
            keyw.frameNStart = frameN  # exact frame index
            keyw.tStart = t  # local t and not account for scr refresh
            keyw.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyw, 'tStartRefresh')  # time at next scr refresh
            keyw.status = STARTED
            win.callOnFlip(keyw.setData, int(trig_keyw))
        if keyw.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > keyw.tStartRefresh + pulseDur-frameTolerance:
                # keep track of stop time/frame for later
                keyw.tStop = t  # not accounting for scr refresh
                keyw.frameNStop = frameN  # exact frame index
                win.timeOnFlip(keyw, 'tStopRefresh')  # time at next scr refresh
                keyw.status = FINISHED
                win.callOnFlip(keyw.setData, int(0))
        # *keyw_plus1* updates
        if keyw_plus1.status == NOT_STARTED and t >= onset_keyw_plus1-frameTolerance:
            # keep track of start time/frame for later
            keyw_plus1.frameNStart = frameN  # exact frame index
            keyw_plus1.tStart = t  # local t and not account for scr refresh
            keyw_plus1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyw_plus1, 'tStartRefresh')  # time at next scr refresh
            keyw_plus1.status = STARTED
            win.callOnFlip(keyw_plus1.setData, int(trig_keyw_plus1))
        if keyw_plus1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > keyw_plus1.tStartRefresh + pulseDur-frameTolerance:
                # keep track of stop time/frame for later
                keyw_plus1.tStop = t  # not accounting for scr refresh
                keyw_plus1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(keyw_plus1, 'tStopRefresh')  # time at next scr refresh
                keyw_plus1.status = FINISHED
                win.callOnFlip(keyw_plus1.setData, int(0))
        # *endingw* updates
        if endingw.status == NOT_STARTED and t >= onset_endingw-frameTolerance:
            # keep track of start time/frame for later
            endingw.frameNStart = frameN  # exact frame index
            endingw.tStart = t  # local t and not account for scr refresh
            endingw.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endingw, 'tStartRefresh')  # time at next scr refresh
            endingw.status = STARTED
            win.callOnFlip(endingw.setData, int(trig_endingw))
        if endingw.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > endingw.tStartRefresh + pulseDur-frameTolerance:
                # keep track of stop time/frame for later
                endingw.tStop = t  # not accounting for scr refresh
                endingw.frameNStop = frameN  # exact frame index
                win.timeOnFlip(endingw, 'tStopRefresh')  # time at next scr refresh
                endingw.status = FINISHED
                win.callOnFlip(endingw.setData, int(0))
        # *port_onset_stim* updates
        if port_onset_stim.status == NOT_STARTED and t >= delayFix-frameTolerance:
            # keep track of start time/frame for later
            port_onset_stim.frameNStart = frameN  # exact frame index
            port_onset_stim.tStart = t  # local t and not account for scr refresh
            port_onset_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(port_onset_stim, 'tStartRefresh')  # time at next scr refresh
            port_onset_stim.status = STARTED
            win.callOnFlip(port_onset_stim.setData, int(trig_onset_stim))
        if port_onset_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > port_onset_stim.tStartRefresh + pulseDur-frameTolerance:
                # keep track of stop time/frame for later
                port_onset_stim.tStop = t  # not accounting for scr refresh
                port_onset_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(port_onset_stim, 'tStopRefresh')  # time at next scr refresh
                port_onset_stim.status = FINISHED
                win.callOnFlip(port_onset_stim.setData, int(0))
        # *port_fix* updates
        if port_fix.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            port_fix.frameNStart = frameN  # exact frame index
            port_fix.tStart = t  # local t and not account for scr refresh
            port_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(port_fix, 'tStartRefresh')  # time at next scr refresh
            port_fix.status = STARTED
            win.callOnFlip(port_fix.setData, int(trig_fix))
        if port_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > port_fix.tStartRefresh + pulseDur-frameTolerance:
                # keep track of stop time/frame for later
                port_fix.tStop = t  # not accounting for scr refresh
                port_fix.frameNStop = frameN  # exact frame index
                win.timeOnFlip(port_fix, 'tStopRefresh')  # time at next scr refresh
                port_fix.status = FINISHED
                win.callOnFlip(port_fix.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mainComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "main"-------
    for thisComponent in mainComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fix.started', fix.tStartRefresh)
    trials.addData('fix.stopped', fix.tStopRefresh)
    stim_phrase.stop()  # ensure sound has stopped at end of routine
    trials.addData('stim_phrase.started', stim_phrase.tStartRefresh)
    trials.addData('stim_phrase.stopped', stim_phrase.tStopRefresh)
    if keyw_2.status == STARTED:
        win.callOnFlip(keyw_2.setData, int(0))
    trials.addData('keyw_2.started', keyw_2.tStart)
    trials.addData('keyw_2.stopped', keyw_2.tStop)
    if keyw_1.status == STARTED:
        win.callOnFlip(keyw_1.setData, int(0))
    trials.addData('keyw_1.started', keyw_1.tStart)
    trials.addData('keyw_1.stopped', keyw_1.tStop)
    if keyw.status == STARTED:
        win.callOnFlip(keyw.setData, int(0))
    trials.addData('keyw.started', keyw.tStart)
    trials.addData('keyw.stopped', keyw.tStop)
    if keyw_plus1.status == STARTED:
        win.callOnFlip(keyw_plus1.setData, int(0))
    trials.addData('keyw_plus1.started', keyw_plus1.tStart)
    trials.addData('keyw_plus1.stopped', keyw_plus1.tStop)
    if endingw.status == STARTED:
        win.callOnFlip(endingw.setData, int(0))
    trials.addData('endingw.started', endingw.tStart)
    trials.addData('endingw.stopped', endingw.tStop)
    if port_onset_stim.status == STARTED:
        win.callOnFlip(port_onset_stim.setData, int(0))
    trials.addData('port_onset_stim.started', port_onset_stim.tStart)
    trials.addData('port_onset_stim.stopped', port_onset_stim.tStop)
    if port_fix.status == STARTED:
        win.callOnFlip(port_fix.setData, int(0))
    trials.addData('port_fix.started', port_fix.tStart)
    trials.addData('port_fix.stopped', port_fix.tStop)
    # the Routine "main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "question"-------
    continueRoutine = True
    # update component parameters for each repeat
    question_resp.keys = []
    question_resp.rt = []
    _question_resp_allKeys = []
    auxOut1 = condList[nRow][0]
    trials.addData("nSent", auxOut1)
    auxOut2 = condList[nRow][1] 
    trials.addData("condition", auxOut2)
    # keep track of which components have finished
    questionComponents = [item_check, question_resp, yes_rect, no_rect, yes, no, port_q]
    for thisComponent in questionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "question"-------
    while continueRoutine:
        # get current time
        t = questionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=questionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *item_check* updates
        if item_check.status == NOT_STARTED and tThisFlip >= start_q-frameTolerance:
            # keep track of start time/frame for later
            item_check.frameNStart = frameN  # exact frame index
            item_check.tStart = t  # local t and not account for scr refresh
            item_check.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(item_check, 'tStartRefresh')  # time at next scr refresh
            item_check.setAutoDraw(True)
        
        # *question_resp* updates
        waitOnFlip = False
        if question_resp.status == NOT_STARTED and tThisFlip >= start_q-frameTolerance:
            # keep track of start time/frame for later
            question_resp.frameNStart = frameN  # exact frame index
            question_resp.tStart = t  # local t and not account for scr refresh
            question_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(question_resp, 'tStartRefresh')  # time at next scr refresh
            question_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(question_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(question_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if question_resp.status == STARTED and not waitOnFlip:
            theseKeys = question_resp.getKeys(keyList=['p', 'q'], waitRelease=False)
            _question_resp_allKeys.extend(theseKeys)
            if len(_question_resp_allKeys):
                question_resp.keys = _question_resp_allKeys[-1].name  # just the last key pressed
                question_resp.rt = _question_resp_allKeys[-1].rt
                # was this correct?
                if (question_resp.keys == str(corrAns)) or (question_resp.keys == corrAns):
                    question_resp.corr = 1
                else:
                    question_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *yes_rect* updates
        if yes_rect.status == NOT_STARTED and tThisFlip >= start_q-frameTolerance:
            # keep track of start time/frame for later
            yes_rect.frameNStart = frameN  # exact frame index
            yes_rect.tStart = t  # local t and not account for scr refresh
            yes_rect.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(yes_rect, 'tStartRefresh')  # time at next scr refresh
            yes_rect.setAutoDraw(True)
        
        # *no_rect* updates
        if no_rect.status == NOT_STARTED and tThisFlip >= start_q-frameTolerance:
            # keep track of start time/frame for later
            no_rect.frameNStart = frameN  # exact frame index
            no_rect.tStart = t  # local t and not account for scr refresh
            no_rect.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(no_rect, 'tStartRefresh')  # time at next scr refresh
            no_rect.setAutoDraw(True)
        
        # *yes* updates
        if yes.status == NOT_STARTED and tThisFlip >= start_q-frameTolerance:
            # keep track of start time/frame for later
            yes.frameNStart = frameN  # exact frame index
            yes.tStart = t  # local t and not account for scr refresh
            yes.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(yes, 'tStartRefresh')  # time at next scr refresh
            yes.setAutoDraw(True)
        
        # *no* updates
        if no.status == NOT_STARTED and tThisFlip >= start_q-frameTolerance:
            # keep track of start time/frame for later
            no.frameNStart = frameN  # exact frame index
            no.tStart = t  # local t and not account for scr refresh
            no.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(no, 'tStartRefresh')  # time at next scr refresh
            no.setAutoDraw(True)
        # *port_q* updates
        if port_q.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            port_q.frameNStart = frameN  # exact frame index
            port_q.tStart = t  # local t and not account for scr refresh
            port_q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(port_q, 'tStartRefresh')  # time at next scr refresh
            port_q.status = STARTED
            win.callOnFlip(port_q.setData, int(trig_question))
        if port_q.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > port_q.tStartRefresh + pulseDur-frameTolerance:
                # keep track of stop time/frame for later
                port_q.tStop = t  # not accounting for scr refresh
                port_q.frameNStop = frameN  # exact frame index
                win.timeOnFlip(port_q, 'tStopRefresh')  # time at next scr refresh
                port_q.status = FINISHED
                win.callOnFlip(port_q.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in questionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "question"-------
    for thisComponent in questionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('item_check.started', item_check.tStartRefresh)
    trials.addData('item_check.stopped', item_check.tStopRefresh)
    # check responses
    if question_resp.keys in ['', [], None]:  # No response was made
        question_resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           question_resp.corr = 1;  # correct non-response
        else:
           question_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('question_resp.keys',question_resp.keys)
    trials.addData('question_resp.corr', question_resp.corr)
    if question_resp.keys != None:  # we had a response
        trials.addData('question_resp.rt', question_resp.rt)
    trials.addData('question_resp.started', question_resp.tStartRefresh)
    trials.addData('question_resp.stopped', question_resp.tStopRefresh)
    trials.addData('yes_rect.started', yes_rect.tStartRefresh)
    trials.addData('yes_rect.stopped', yes_rect.tStopRefresh)
    trials.addData('no_rect.started', no_rect.tStartRefresh)
    trials.addData('no_rect.stopped', no_rect.tStopRefresh)
    trials.addData('yes.started', yes.tStartRefresh)
    trials.addData('yes.stopped', yes.tStopRefresh)
    trials.addData('no.started', no.tStartRefresh)
    trials.addData('no.stopped', no.tStopRefresh)
    if port_q.status == STARTED:
        win.callOnFlip(port_q.setData, int(0))
    trials.addData('port_q.started', port_q.tStart)
    trials.addData('port_q.stopped', port_q.tStop)
    # the Routine "question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blink"-------
    continueRoutine = True
    # update component parameters for each repeat
    # checking pause
    if nTrial > 1:
        if nTrial % nPausa == 0:
            pausa_msg = 'PAUSA'
            modePausa = True
              
    
    # checking end of task
    if trials.thisN == len(condList)-1:        
        pausa_msg = '¡Ya has acabado!\nGracias por tu participación.\n\n Pulsa la barra de ESPACIO salir' 
        modePausa = True
        modeInter = False
    
    # keep track of which components have finished
    blinkComponents = [blink_txt, port_blink]
    for thisComponent in blinkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blinkClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blink"-------
    while continueRoutine:
        # get current time
        t = blinkClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blinkClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blink_txt* updates
        if blink_txt.status == NOT_STARTED and tThisFlip >= start_q-frameTolerance:
            # keep track of start time/frame for later
            blink_txt.frameNStart = frameN  # exact frame index
            blink_txt.tStart = t  # local t and not account for scr refresh
            blink_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blink_txt, 'tStartRefresh')  # time at next scr refresh
            blink_txt.setAutoDraw(True)
        if blink_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blink_txt.tStartRefresh + blinkDur-frameTolerance:
                # keep track of stop time/frame for later
                blink_txt.tStop = t  # not accounting for scr refresh
                blink_txt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blink_txt, 'tStopRefresh')  # time at next scr refresh
                blink_txt.setAutoDraw(False)
        # *port_blink* updates
        if port_blink.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            port_blink.frameNStart = frameN  # exact frame index
            port_blink.tStart = t  # local t and not account for scr refresh
            port_blink.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(port_blink, 'tStartRefresh')  # time at next scr refresh
            port_blink.status = STARTED
            win.callOnFlip(port_blink.setData, int(trig_blink))
        if port_blink.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > port_blink.tStartRefresh + pulseDur-frameTolerance:
                # keep track of stop time/frame for later
                port_blink.tStop = t  # not accounting for scr refresh
                port_blink.frameNStop = frameN  # exact frame index
                win.timeOnFlip(port_blink, 'tStopRefresh')  # time at next scr refresh
                port_blink.status = FINISHED
                win.callOnFlip(port_blink.setData, int(0))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blinkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blink"-------
    for thisComponent in blinkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('blink_txt.started', blink_txt.tStartRefresh)
    trials.addData('blink_txt.stopped', blink_txt.tStopRefresh)
    if port_blink.status == STARTED:
        win.callOnFlip(port_blink.setData, int(0))
    trials.addData('port_blink.started', port_blink.tStart)
    trials.addData('port_blink.stopped', port_blink.tStop)
    # the Routine "blink" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    check_pausa = data.TrialHandler(nReps=modePausa, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='check_pausa')
    thisExp.addLoop(check_pausa)  # add the loop to the experiment
    thisCheck_pausa = check_pausa.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCheck_pausa.rgb)
    if thisCheck_pausa != None:
        for paramName in thisCheck_pausa:
            exec('{} = thisCheck_pausa[paramName]'.format(paramName))
    
    for thisCheck_pausa in check_pausa:
        currentLoop = check_pausa
        # abbreviate parameter names if possible (e.g. rgb = thisCheck_pausa.rgb)
        if thisCheck_pausa != None:
            for paramName in thisCheck_pausa:
                exec('{} = thisCheck_pausa[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "pausa"-------
        continueRoutine = True
        # update component parameters for each repeat
        pausa_txt.setText(pausa_msg)
        pausa_resp.keys = []
        pausa_resp.rt = []
        _pausa_resp_allKeys = []
        # keep track of which components have finished
        pausaComponents = [pausa_txt, pausa_resp, port_pausa]
        for thisComponent in pausaComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        pausaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "pausa"-------
        while continueRoutine:
            # get current time
            t = pausaClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=pausaClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *pausa_txt* updates
            if pausa_txt.status == NOT_STARTED and tThisFlip >= start_q-frameTolerance:
                # keep track of start time/frame for later
                pausa_txt.frameNStart = frameN  # exact frame index
                pausa_txt.tStart = t  # local t and not account for scr refresh
                pausa_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pausa_txt, 'tStartRefresh')  # time at next scr refresh
                pausa_txt.setAutoDraw(True)
            
            # *pausa_resp* updates
            waitOnFlip = False
            if pausa_resp.status == NOT_STARTED and tThisFlip >= start_q-frameTolerance:
                # keep track of start time/frame for later
                pausa_resp.frameNStart = frameN  # exact frame index
                pausa_resp.tStart = t  # local t and not account for scr refresh
                pausa_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pausa_resp, 'tStartRefresh')  # time at next scr refresh
                pausa_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(pausa_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(pausa_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if pausa_resp.status == STARTED and not waitOnFlip:
                theseKeys = pausa_resp.getKeys(keyList=['space'], waitRelease=False)
                _pausa_resp_allKeys.extend(theseKeys)
                if len(_pausa_resp_allKeys):
                    pausa_resp.keys = _pausa_resp_allKeys[-1].name  # just the last key pressed
                    pausa_resp.rt = _pausa_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            # *port_pausa* updates
            if port_pausa.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                port_pausa.frameNStart = frameN  # exact frame index
                port_pausa.tStart = t  # local t and not account for scr refresh
                port_pausa.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(port_pausa, 'tStartRefresh')  # time at next scr refresh
                port_pausa.status = STARTED
                win.callOnFlip(port_pausa.setData, int(trig_pausa))
            if port_pausa.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > port_pausa.tStartRefresh + pulseDur-frameTolerance:
                    # keep track of stop time/frame for later
                    port_pausa.tStop = t  # not accounting for scr refresh
                    port_pausa.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(port_pausa, 'tStopRefresh')  # time at next scr refresh
                    port_pausa.status = FINISHED
                    win.callOnFlip(port_pausa.setData, int(0))
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pausaComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "pausa"-------
        for thisComponent in pausaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        check_pausa.addData('pausa_txt.started', pausa_txt.tStartRefresh)
        check_pausa.addData('pausa_txt.stopped', pausa_txt.tStopRefresh)
        # check responses
        if pausa_resp.keys in ['', [], None]:  # No response was made
            pausa_resp.keys = None
        check_pausa.addData('pausa_resp.keys',pausa_resp.keys)
        if pausa_resp.keys != None:  # we had a response
            check_pausa.addData('pausa_resp.rt', pausa_resp.rt)
        check_pausa.addData('pausa_resp.started', pausa_resp.tStartRefresh)
        check_pausa.addData('pausa_resp.stopped', pausa_resp.tStopRefresh)
        modePausa = False
        if port_pausa.status == STARTED:
            win.callOnFlip(port_pausa.setData, int(0))
        check_pausa.addData('port_pausa.started', port_pausa.tStart)
        check_pausa.addData('port_pausa.stopped', port_pausa.tStop)
        # the Routine "pausa" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed modePausa repeats of 'check_pausa'
    
    
    # set up handler to look after randomisation of conditions etc
    loopInter = data.TrialHandler(nReps=modeInter, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='loopInter')
    thisExp.addLoop(loopInter)  # add the loop to the experiment
    thisLoopInter = loopInter.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoopInter.rgb)
    if thisLoopInter != None:
        for paramName in thisLoopInter:
            exec('{} = thisLoopInter[paramName]'.format(paramName))
    
    for thisLoopInter in loopInter:
        currentLoop = loopInter
        # abbreviate parameter names if possible (e.g. rgb = thisLoopInter.rgb)
        if thisLoopInter != None:
            for paramName in thisLoopInter:
                exec('{} = thisLoopInter[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "intertrial"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        intertrialComponents = [inter_img]
        for thisComponent in intertrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        intertrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "intertrial"-------
        while continueRoutine:
            # get current time
            t = intertrialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=intertrialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *inter_img* updates
            if inter_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                inter_img.frameNStart = frameN  # exact frame index
                inter_img.tStart = t  # local t and not account for scr refresh
                inter_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(inter_img, 'tStartRefresh')  # time at next scr refresh
                inter_img.setAutoDraw(True)
            if inter_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > inter_img.tStartRefresh + interDur-frameTolerance:
                    # keep track of stop time/frame for later
                    inter_img.tStop = t  # not accounting for scr refresh
                    inter_img.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(inter_img, 'tStopRefresh')  # time at next scr refresh
                    inter_img.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in intertrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "intertrial"-------
        for thisComponent in intertrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loopInter.addData('inter_img.started', inter_img.tStartRefresh)
        loopInter.addData('inter_img.stopped', inter_img.tStopRefresh)
        # the Routine "intertrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed modeInter repeats of 'loopInter'
    
    thisExp.nextEntry()
    
# completed totalTrials repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
