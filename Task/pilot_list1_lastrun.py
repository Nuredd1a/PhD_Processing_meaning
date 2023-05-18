#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on noviembre 23, 2022, at 16:38
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
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
psychopyVersion = '2021.2.3'
expName = 'SLangexp'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\clara\\OneDrive\\Escritorio\\Curso 2020-2021\\ERPs\\PilotTempsLectura\\pilot_list1\\pilot_list1_lastrun.py',
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
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "setting_JS"
setting_JSClock = core.Clock()

# Initialize components for Routine "loading_phrases"
loading_phrasesClock = core.Clock()
condList = []


# Initialize components for Routine "setting_parameters"
setting_parametersClock = core.Clock()
import random

event.Mouse(visible = False)

trialsTraining = 4

# dimensions elements of rating
dimS = 0.1
colorS = 'blue'
fontS = 0.05
colorN = 'white'
xPos1 = -0.3
xPos2 = -0.15
xPos3 = 0
xPos4 = -0.5
yPos = -0.05



aux = []
aux_cond = []

# Initialize components for Routine "start"
startClock = core.Clock()
start_txt = visual.TextStim(win=win, name='start_txt',
    text='¡Bienvenido!\n\nA continuación vas a leer unas frases y tendrás que decidir si son correctas o no. \n\nEn la pantalla aparecerá solo una palabra a la vez. Para ir leyendo la frase, pulsa la barra espaciadora y e irán apareciendo las siguientes palabras de la frase. Lee a la velocidad que leerías naturalmente.\n\nCuando la frase haya terminado, te preguntaremos si la frase que acabas de leer es correcta o no. Pulsa la tecla de la letra Q para indicar que SÍ y la tecla de la letra P para indicar que NO. Intenta responder lo más rápido que puedas, sin reflexionarlo mucho. Los errores que detectes pueden ser tanto de forma (que las frases no estén bien construidas) como de contenido (que tengan significados absurdos o imposibles).\n\nDespués, aparecerá una escala del 1 al 5 para que valores tu nivel de seguridad en tu respuesta, siendo 5 MUY SEGURO y 1 NADA SEGURO. \n\nVamos a empezar con una práctica. Pulsa la barra espaciadora para empezar. Cuando aparezca este símbolo +, pulsa la barra espaciadora. \n',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "wait"
waitClock = core.Clock()
wait_img = visual.ImageStim(
    win=win,
    name='wait_img', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
aux_word = []
fix_txt = visual.TextStim(win=win, name='fix_txt',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
fix_resp = keyboard.Keyboard()

# Initialize components for Routine "words"
wordsClock = core.Clock()
word_txt = visual.TextStim(win=win, name='word_txt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
words_resp = keyboard.Keyboard()

# Initialize components for Routine "question"
questionClock = core.Clock()
item_check = visual.TextStim(win=win, name='item_check',
    text='¿Era correcta la frase anterior?\n',
    font='Arial',
    pos=(0, 0.05), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
question_resp = keyboard.Keyboard()
yes_rect = visual.Rect(
    win=win, name='yes_rect',
    width=(0.125, 0.05)[0], height=(0.125, 0.05)[1],
    ori=0, pos=(-0.15, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-2.0, interpolate=True)
no_rect = visual.Rect(
    win=win, name='no_rect',
    width=(0.125, 0.05)[0], height=(0.125, 0.05)[1],
    ori=0, pos=(0.15, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-3.0, interpolate=True)
yes = visual.TextStim(win=win, name='yes',
    text='SÍ',
    font='Arial',
    pos=(-0.15, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
no = visual.TextStim(win=win, name='no',
    text='NO',
    font='Arial',
    pos=(0.15, 0), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
auxOut1 = []
auxOut2 = []

# Initialize components for Routine "rating"
ratingClock = core.Clock()
rating_question = visual.TextStim(win=win, name='rating_question',
    text='Grado de seguridad de tu respuesta',
    font='Arial',
    pos=(0, 0.1), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rect1 = visual.Rect(
    win=win, name='rect1',
    width=(dimS, dimS)[0], height=(dimS, dimS)[1],
    ori=0, pos=(xPos1, yPos),
    lineWidth=1,     colorSpace='rgb',  lineColor=colorS, fillColor=colorS,
    opacity=1, depth=-1.0, interpolate=True)
rect2 = visual.Rect(
    win=win, name='rect2',
    width=(dimS, dimS)[0], height=(dimS, dimS)[1],
    ori=0, pos=(xPos2, yPos),
    lineWidth=1,     colorSpace='rgb',  lineColor=colorS, fillColor=colorS,
    opacity=1, depth=-2.0, interpolate=True)
rect3 = visual.Rect(
    win=win, name='rect3',
    width=(dimS, dimS)[0], height=(dimS, dimS)[1],
    ori=0, pos=(xPos3, yPos),
    lineWidth=1,     colorSpace='rgb',  lineColor=colorS, fillColor=colorS,
    opacity=1, depth=-3.0, interpolate=True)
rect4 = visual.Rect(
    win=win, name='rect4',
    width=(dimS, dimS)[0], height=(dimS, dimS)[1],
    ori=0, pos=(-xPos2, yPos),
    lineWidth=1,     colorSpace='rgb',  lineColor=colorS, fillColor=colorS,
    opacity=1, depth=-4.0, interpolate=True)
rect5 = visual.Rect(
    win=win, name='rect5',
    width=(dimS, dimS)[0], height=(dimS, dimS)[1],
    ori=0, pos=(-xPos1, yPos),
    lineWidth=1,     colorSpace='rgb',  lineColor=colorS, fillColor=colorS,
    opacity=1, depth=-5.0, interpolate=True)
g1 = visual.TextStim(win=win, name='g1',
    text='1',
    font='Arial',
    pos=(xPos1, yPos), height=fontS, wrapWidth=None, ori=0, 
    color=colorN, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
g2 = visual.TextStim(win=win, name='g2',
    text='2',
    font='Arial',
    pos=(xPos2, yPos), height=fontS, wrapWidth=None, ori=0, 
    color=colorN, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
g3 = visual.TextStim(win=win, name='g3',
    text='3',
    font='Arial',
    pos=(xPos3, yPos), height=fontS, wrapWidth=None, ori=0, 
    color=colorN, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
g4 = visual.TextStim(win=win, name='g4',
    text='4',
    font='Arial',
    pos=(-xPos2, yPos), height=fontS, wrapWidth=None, ori=0, 
    color=colorN, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
g5 = visual.TextStim(win=win, name='g5',
    text='5',
    font='Arial',
    pos=(-xPos1, yPos), height=fontS, wrapWidth=None, ori=0, 
    color=colorN, colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
rating_resp = keyboard.Keyboard()
NadaSeguro = visual.TextStim(win=win, name='NadaSeguro',
    text='Nada seguro',
    font='Arial',
    pos=(xPos4, yPos), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-13.0);
MuySeguro = visual.TextStim(win=win, name='MuySeguro',
    text='Muy seguro',
    font='Arial',
    pos=(-xPos4, yPos), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);

# Initialize components for Routine "pausa"
pausaClock = core.Clock()
pausa_txt = visual.TextStim(win=win, name='pausa_txt',
    text='',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
pausa_resp = keyboard.Keyboard()

# Initialize components for Routine "check_pract"
check_practClock = core.Clock()
pract_txt = visual.TextStim(win=win, name='pract_txt',
    text='Has acabado la práctica. \n\nPulsa la barra de espacio para empezar la tarea.\n\nCada ciertas frases tendrás una PAUSA en la que podrás tomarte unos segundos. Continúa enseguida que estés listo. ',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
pract_resp = keyboard.Keyboard()

# Initialize components for Routine "intertrial"
intertrialClock = core.Clock()
inter_img = visual.ImageStim(
    win=win,
    name='inter_img', 
    image=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setting_JS"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
setting_JSComponents = []
for thisComponent in setting_JSComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setting_JSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setting_JS"-------
while continueRoutine:
    # get current time
    t = setting_JSClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setting_JSClock)
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
    for thisComponent in setting_JSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setting_JS"-------
for thisComponent in setting_JSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setting_JS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
load = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pilot_list1.xlsx'),
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
    condList.append([n, cond, word1, word2, word3, word4, word5, word6, word7, word8, word9, target, length, trigger, correctKey, targetPos])
    
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
# completed 1 repeats of 'load'


# ------Prepare to start Routine "setting_parameters"-------
continueRoutine = True
# update component parameters for each repeat
# TASK PARAMETERS
# ---------------

totalTrials = len(condList)
word = ''

# variable that takes the length of 
# each sentence
totalWords = 0

# variable that takes the length column
lengthCol = 12

# variable that takes the correct answer column
corrAnsCol = 14

# variable that takes the target word
targetCol = 11

# variable that takes the keyword position
keyword = 15

corrAns = []

# counters
nTrial = 0;
nRow = -1;
nWord = -1;
nInter = -1;
nPausa = 12;

# array of possible intertrial durations
auxInter = [0.75, 1, 1.25, 1.5, 1.75, 2]
random.shuffle(auxInter)
interDur = 0

modePausa = False
modeInter = True
modePract = False
# print(condList)
aux = condList[trialsTraining:]
random.shuffle(aux)
condList[trialsTraining:] = aux[:]
kk = 0
i = trialsTraining + 2
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
        aux = condList[trialsTraining:]
        random.shuffle(aux)
        condList[trialsTraining:] = aux[:]
        i = trialsTraining - 1     
    
    i = i + 1 

# for i in range(totalTrials):
#    print(condList[i][0])
 
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
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
startComponents = [start_txt, key_resp_2]
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
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
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
        if tThisFlipGlobal > wait_img.tStartRefresh + 2-frameTolerance:
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
    
    # ------Prepare to start Routine "fixation"-------
    continueRoutine = True
    # update component parameters for each repeat
    nWord = -1
    nTrial = nTrial + 1;
    nRow = nRow + 1
    
    totalWords = condList[trials.thisN][lengthCol]
    
    corrAns = condList[trials.thisN][corrAnsCol]
    print(corrAns)
    
    #print(condList[trials.thisN][0])
    
    aux_word = []
    for i in range(int(totalWords - 1)):
        aux_word.append(condList[trials.thisN][i+2])
        
    aux_word.append(condList[trials.thisN][targetCol]) 
    
    print(aux_word)
    
    
    fix_resp.keys = []
    fix_resp.rt = []
    _fix_resp_allKeys = []
    nInter = nInter + 1
    if nInter == len(auxInter):
        random.shuffle(auxInter)
        nInter = 0
        
    interDur = auxInter[nInter]    
    
    print(interDur)
    
    # keep track of which components have finished
    fixationComponents = [fix_txt, fix_resp]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation"-------
    while continueRoutine:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix_txt* updates
        if fix_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_txt.frameNStart = frameN  # exact frame index
            fix_txt.tStart = t  # local t and not account for scr refresh
            fix_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_txt, 'tStartRefresh')  # time at next scr refresh
            fix_txt.setAutoDraw(True)
        
        # *fix_resp* updates
        waitOnFlip = False
        if fix_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix_resp.frameNStart = frameN  # exact frame index
            fix_resp.tStart = t  # local t and not account for scr refresh
            fix_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix_resp, 'tStartRefresh')  # time at next scr refresh
            fix_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(fix_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(fix_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if fix_resp.status == STARTED and not waitOnFlip:
            theseKeys = fix_resp.getKeys(keyList=['space'], waitRelease=False)
            _fix_resp_allKeys.extend(theseKeys)
            if len(_fix_resp_allKeys):
                fix_resp.keys = _fix_resp_allKeys[-1].name  # just the last key pressed
                fix_resp.rt = _fix_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fix_txt.started', fix_txt.tStartRefresh)
    trials.addData('fix_txt.stopped', fix_txt.tStopRefresh)
    # check responses
    if fix_resp.keys in ['', [], None]:  # No response was made
        fix_resp.keys = None
    trials.addData('fix_resp.keys',fix_resp.keys)
    if fix_resp.keys != None:  # we had a response
        trials.addData('fix_resp.rt', fix_resp.rt)
    trials.addData('fix_resp.started', fix_resp.tStartRefresh)
    trials.addData('fix_resp.stopped', fix_resp.tStopRefresh)
    # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    words_loop = data.TrialHandler(nReps=totalWords, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='words_loop')
    thisExp.addLoop(words_loop)  # add the loop to the experiment
    thisWords_loop = words_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisWords_loop.rgb)
    if thisWords_loop != None:
        for paramName in thisWords_loop:
            exec('{} = thisWords_loop[paramName]'.format(paramName))
    
    for thisWords_loop in words_loop:
        currentLoop = words_loop
        # abbreviate parameter names if possible (e.g. rgb = thisWords_loop.rgb)
        if thisWords_loop != None:
            for paramName in thisWords_loop:
                exec('{} = thisWords_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "words"-------
        continueRoutine = True
        # update component parameters for each repeat
        word = aux_word[words_loop.thisN]
        
        # adding presented item to the output
        words_loop.addData("item", word)
        
        # adding a 1 to column target to the output
        # when the key word is presented
        if (words_loop.thisN + 1) == condList[trials.thisN][keyword]:
            words_loop.addData("keyWord", 1)
        
        word_txt.setText(word)
        words_resp.keys = []
        words_resp.rt = []
        _words_resp_allKeys = []
        # keep track of which components have finished
        wordsComponents = [word_txt, words_resp]
        for thisComponent in wordsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        wordsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "words"-------
        while continueRoutine:
            # get current time
            t = wordsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=wordsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *word_txt* updates
            if word_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                word_txt.frameNStart = frameN  # exact frame index
                word_txt.tStart = t  # local t and not account for scr refresh
                word_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(word_txt, 'tStartRefresh')  # time at next scr refresh
                word_txt.setAutoDraw(True)
            
            # *words_resp* updates
            waitOnFlip = False
            if words_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                words_resp.frameNStart = frameN  # exact frame index
                words_resp.tStart = t  # local t and not account for scr refresh
                words_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(words_resp, 'tStartRefresh')  # time at next scr refresh
                words_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(words_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(words_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if words_resp.status == STARTED and not waitOnFlip:
                theseKeys = words_resp.getKeys(keyList=['space'], waitRelease=False)
                _words_resp_allKeys.extend(theseKeys)
                if len(_words_resp_allKeys):
                    words_resp.keys = _words_resp_allKeys[-1].name  # just the last key pressed
                    words_resp.rt = _words_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in wordsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "words"-------
        for thisComponent in wordsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        words_loop.addData('word_txt.started', word_txt.tStartRefresh)
        words_loop.addData('word_txt.stopped', word_txt.tStopRefresh)
        # check responses
        if words_resp.keys in ['', [], None]:  # No response was made
            words_resp.keys = None
        words_loop.addData('words_resp.keys',words_resp.keys)
        if words_resp.keys != None:  # we had a response
            words_loop.addData('words_resp.rt', words_resp.rt)
        words_loop.addData('words_resp.started', words_resp.tStartRefresh)
        words_loop.addData('words_resp.stopped', words_resp.tStopRefresh)
        # the Routine "words" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed totalWords repeats of 'words_loop'
    
    
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
    questionComponents = [item_check, question_resp, yes_rect, no_rect, yes, no]
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
        if item_check.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            item_check.frameNStart = frameN  # exact frame index
            item_check.tStart = t  # local t and not account for scr refresh
            item_check.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(item_check, 'tStartRefresh')  # time at next scr refresh
            item_check.setAutoDraw(True)
        
        # *question_resp* updates
        waitOnFlip = False
        if question_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
                question_resp.keys = _question_resp_allKeys[0].name  # just the first key pressed
                question_resp.rt = _question_resp_allKeys[0].rt
                # was this correct?
                if (question_resp.keys == str(corrAns)) or (question_resp.keys == corrAns):
                    question_resp.corr = 1
                else:
                    question_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *yes_rect* updates
        if yes_rect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            yes_rect.frameNStart = frameN  # exact frame index
            yes_rect.tStart = t  # local t and not account for scr refresh
            yes_rect.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(yes_rect, 'tStartRefresh')  # time at next scr refresh
            yes_rect.setAutoDraw(True)
        
        # *no_rect* updates
        if no_rect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            no_rect.frameNStart = frameN  # exact frame index
            no_rect.tStart = t  # local t and not account for scr refresh
            no_rect.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(no_rect, 'tStartRefresh')  # time at next scr refresh
            no_rect.setAutoDraw(True)
        
        # *yes* updates
        if yes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            yes.frameNStart = frameN  # exact frame index
            yes.tStart = t  # local t and not account for scr refresh
            yes.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(yes, 'tStartRefresh')  # time at next scr refresh
            yes.setAutoDraw(True)
        
        # *no* updates
        if no.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            no.frameNStart = frameN  # exact frame index
            no.tStart = t  # local t and not account for scr refresh
            no.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(no, 'tStartRefresh')  # time at next scr refresh
            no.setAutoDraw(True)
        
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
    # the Routine "question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rating"-------
    continueRoutine = True
    # update component parameters for each repeat
    rating_resp.keys = []
    rating_resp.rt = []
    _rating_resp_allKeys = []
    # keep track of which components have finished
    ratingComponents = [rating_question, rect1, rect2, rect3, rect4, rect5, g1, g2, g3, g4, g5, rating_resp, NadaSeguro, MuySeguro]
    for thisComponent in ratingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ratingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rating"-------
    while continueRoutine:
        # get current time
        t = ratingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ratingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rating_question* updates
        if rating_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating_question.frameNStart = frameN  # exact frame index
            rating_question.tStart = t  # local t and not account for scr refresh
            rating_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_question, 'tStartRefresh')  # time at next scr refresh
            rating_question.setAutoDraw(True)
        
        # *rect1* updates
        if rect1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rect1.frameNStart = frameN  # exact frame index
            rect1.tStart = t  # local t and not account for scr refresh
            rect1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect1, 'tStartRefresh')  # time at next scr refresh
            rect1.setAutoDraw(True)
        
        # *rect2* updates
        if rect2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rect2.frameNStart = frameN  # exact frame index
            rect2.tStart = t  # local t and not account for scr refresh
            rect2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect2, 'tStartRefresh')  # time at next scr refresh
            rect2.setAutoDraw(True)
        
        # *rect3* updates
        if rect3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rect3.frameNStart = frameN  # exact frame index
            rect3.tStart = t  # local t and not account for scr refresh
            rect3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect3, 'tStartRefresh')  # time at next scr refresh
            rect3.setAutoDraw(True)
        
        # *rect4* updates
        if rect4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rect4.frameNStart = frameN  # exact frame index
            rect4.tStart = t  # local t and not account for scr refresh
            rect4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect4, 'tStartRefresh')  # time at next scr refresh
            rect4.setAutoDraw(True)
        
        # *rect5* updates
        if rect5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rect5.frameNStart = frameN  # exact frame index
            rect5.tStart = t  # local t and not account for scr refresh
            rect5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rect5, 'tStartRefresh')  # time at next scr refresh
            rect5.setAutoDraw(True)
        
        # *g1* updates
        if g1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            g1.frameNStart = frameN  # exact frame index
            g1.tStart = t  # local t and not account for scr refresh
            g1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(g1, 'tStartRefresh')  # time at next scr refresh
            g1.setAutoDraw(True)
        
        # *g2* updates
        if g2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            g2.frameNStart = frameN  # exact frame index
            g2.tStart = t  # local t and not account for scr refresh
            g2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(g2, 'tStartRefresh')  # time at next scr refresh
            g2.setAutoDraw(True)
        
        # *g3* updates
        if g3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            g3.frameNStart = frameN  # exact frame index
            g3.tStart = t  # local t and not account for scr refresh
            g3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(g3, 'tStartRefresh')  # time at next scr refresh
            g3.setAutoDraw(True)
        
        # *g4* updates
        if g4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            g4.frameNStart = frameN  # exact frame index
            g4.tStart = t  # local t and not account for scr refresh
            g4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(g4, 'tStartRefresh')  # time at next scr refresh
            g4.setAutoDraw(True)
        
        # *g5* updates
        if g5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            g5.frameNStart = frameN  # exact frame index
            g5.tStart = t  # local t and not account for scr refresh
            g5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(g5, 'tStartRefresh')  # time at next scr refresh
            g5.setAutoDraw(True)
        
        # *rating_resp* updates
        waitOnFlip = False
        if rating_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rating_resp.frameNStart = frameN  # exact frame index
            rating_resp.tStart = t  # local t and not account for scr refresh
            rating_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rating_resp, 'tStartRefresh')  # time at next scr refresh
            rating_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(rating_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(rating_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if rating_resp.status == STARTED and not waitOnFlip:
            theseKeys = rating_resp.getKeys(keyList=['1', '2', '3', '4', '5'], waitRelease=False)
            _rating_resp_allKeys.extend(theseKeys)
            if len(_rating_resp_allKeys):
                rating_resp.keys = _rating_resp_allKeys[-1].name  # just the last key pressed
                rating_resp.rt = _rating_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *NadaSeguro* updates
        if NadaSeguro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NadaSeguro.frameNStart = frameN  # exact frame index
            NadaSeguro.tStart = t  # local t and not account for scr refresh
            NadaSeguro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NadaSeguro, 'tStartRefresh')  # time at next scr refresh
            NadaSeguro.setAutoDraw(True)
        
        # *MuySeguro* updates
        if MuySeguro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MuySeguro.frameNStart = frameN  # exact frame index
            MuySeguro.tStart = t  # local t and not account for scr refresh
            MuySeguro.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MuySeguro, 'tStartRefresh')  # time at next scr refresh
            MuySeguro.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ratingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rating"-------
    for thisComponent in ratingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('rating_question.started', rating_question.tStartRefresh)
    trials.addData('rating_question.stopped', rating_question.tStopRefresh)
    trials.addData('rect1.started', rect1.tStartRefresh)
    trials.addData('rect1.stopped', rect1.tStopRefresh)
    trials.addData('rect2.started', rect2.tStartRefresh)
    trials.addData('rect2.stopped', rect2.tStopRefresh)
    trials.addData('rect3.started', rect3.tStartRefresh)
    trials.addData('rect3.stopped', rect3.tStopRefresh)
    trials.addData('rect4.started', rect4.tStartRefresh)
    trials.addData('rect4.stopped', rect4.tStopRefresh)
    trials.addData('rect5.started', rect5.tStartRefresh)
    trials.addData('rect5.stopped', rect5.tStopRefresh)
    trials.addData('g1.started', g1.tStartRefresh)
    trials.addData('g1.stopped', g1.tStopRefresh)
    trials.addData('g2.started', g2.tStartRefresh)
    trials.addData('g2.stopped', g2.tStopRefresh)
    trials.addData('g3.started', g3.tStartRefresh)
    trials.addData('g3.stopped', g3.tStopRefresh)
    trials.addData('g4.started', g4.tStartRefresh)
    trials.addData('g4.stopped', g4.tStopRefresh)
    trials.addData('g5.started', g5.tStartRefresh)
    trials.addData('g5.stopped', g5.tStopRefresh)
    # check responses
    if rating_resp.keys in ['', [], None]:  # No response was made
        rating_resp.keys = None
    trials.addData('rating_resp.keys',rating_resp.keys)
    if rating_resp.keys != None:  # we had a response
        trials.addData('rating_resp.rt', rating_resp.rt)
    trials.addData('rating_resp.started', rating_resp.tStartRefresh)
    trials.addData('rating_resp.stopped', rating_resp.tStopRefresh)
    # checking end of training
    if trials.thisN == (trialsTraining - 1): 
        modePract = True
        nTrial = 0
    
    # checking pause
    if nTrial > 1:
        if nTrial % nPausa == 0:
            pausa_msg = 'PAUSA'
            modePausa = True
    
    # checking end of task
    if trials.thisN == len(condList)-1:        
        pausa_msg = '¡Ya has acabado!\nGracias por tu participación.\n\n Pulsa la barra de ESPACIO para acabar' 
        modePausa = True
        modeInter = False
    trials.addData('NadaSeguro.started', NadaSeguro.tStartRefresh)
    trials.addData('NadaSeguro.stopped', NadaSeguro.tStopRefresh)
    trials.addData('MuySeguro.started', MuySeguro.tStartRefresh)
    trials.addData('MuySeguro.stopped', MuySeguro.tStopRefresh)
    # the Routine "rating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    checkPausa = data.TrialHandler(nReps=modePausa, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='checkPausa')
    thisExp.addLoop(checkPausa)  # add the loop to the experiment
    thisCheckPausa = checkPausa.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCheckPausa.rgb)
    if thisCheckPausa != None:
        for paramName in thisCheckPausa:
            exec('{} = thisCheckPausa[paramName]'.format(paramName))
    
    for thisCheckPausa in checkPausa:
        currentLoop = checkPausa
        # abbreviate parameter names if possible (e.g. rgb = thisCheckPausa.rgb)
        if thisCheckPausa != None:
            for paramName in thisCheckPausa:
                exec('{} = thisCheckPausa[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "pausa"-------
        continueRoutine = True
        # update component parameters for each repeat
        pausa_txt.setText(pausa_msg)
        pausa_resp.keys = []
        pausa_resp.rt = []
        _pausa_resp_allKeys = []
        # keep track of which components have finished
        pausaComponents = [pausa_txt, pausa_resp]
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
            if pausa_txt.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                pausa_txt.frameNStart = frameN  # exact frame index
                pausa_txt.tStart = t  # local t and not account for scr refresh
                pausa_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pausa_txt, 'tStartRefresh')  # time at next scr refresh
                pausa_txt.setAutoDraw(True)
            
            # *pausa_resp* updates
            waitOnFlip = False
            if pausa_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
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
        checkPausa.addData('pausa_txt.started', pausa_txt.tStartRefresh)
        checkPausa.addData('pausa_txt.stopped', pausa_txt.tStopRefresh)
        # check responses
        if pausa_resp.keys in ['', [], None]:  # No response was made
            pausa_resp.keys = None
        checkPausa.addData('pausa_resp.keys',pausa_resp.keys)
        if pausa_resp.keys != None:  # we had a response
            checkPausa.addData('pausa_resp.rt', pausa_resp.rt)
        checkPausa.addData('pausa_resp.started', pausa_resp.tStartRefresh)
        checkPausa.addData('pausa_resp.stopped', pausa_resp.tStopRefresh)
        modePausa = False
        # the Routine "pausa" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed modePausa repeats of 'checkPausa'
    
    
    # set up handler to look after randomisation of conditions etc
    checkPract = data.TrialHandler(nReps=modePract, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='checkPract')
    thisExp.addLoop(checkPract)  # add the loop to the experiment
    thisCheckPract = checkPract.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCheckPract.rgb)
    if thisCheckPract != None:
        for paramName in thisCheckPract:
            exec('{} = thisCheckPract[paramName]'.format(paramName))
    
    for thisCheckPract in checkPract:
        currentLoop = checkPract
        # abbreviate parameter names if possible (e.g. rgb = thisCheckPract.rgb)
        if thisCheckPract != None:
            for paramName in thisCheckPract:
                exec('{} = thisCheckPract[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "check_pract"-------
        continueRoutine = True
        # update component parameters for each repeat
        pract_resp.keys = []
        pract_resp.rt = []
        _pract_resp_allKeys = []
        # keep track of which components have finished
        check_practComponents = [pract_txt, pract_resp]
        for thisComponent in check_practComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        check_practClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "check_pract"-------
        while continueRoutine:
            # get current time
            t = check_practClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=check_practClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *pract_txt* updates
            if pract_txt.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                pract_txt.frameNStart = frameN  # exact frame index
                pract_txt.tStart = t  # local t and not account for scr refresh
                pract_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pract_txt, 'tStartRefresh')  # time at next scr refresh
                pract_txt.setAutoDraw(True)
            
            # *pract_resp* updates
            waitOnFlip = False
            if pract_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                pract_resp.frameNStart = frameN  # exact frame index
                pract_resp.tStart = t  # local t and not account for scr refresh
                pract_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pract_resp, 'tStartRefresh')  # time at next scr refresh
                pract_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(pract_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(pract_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if pract_resp.status == STARTED and not waitOnFlip:
                theseKeys = pract_resp.getKeys(keyList=['space'], waitRelease=False)
                _pract_resp_allKeys.extend(theseKeys)
                if len(_pract_resp_allKeys):
                    pract_resp.keys = _pract_resp_allKeys[-1].name  # just the last key pressed
                    pract_resp.rt = _pract_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in check_practComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "check_pract"-------
        for thisComponent in check_practComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        checkPract.addData('pract_txt.started', pract_txt.tStartRefresh)
        checkPract.addData('pract_txt.stopped', pract_txt.tStopRefresh)
        # check responses
        if pract_resp.keys in ['', [], None]:  # No response was made
            pract_resp.keys = None
        checkPract.addData('pract_resp.keys',pract_resp.keys)
        if pract_resp.keys != None:  # we had a response
            checkPract.addData('pract_resp.rt', pract_resp.rt)
        checkPract.addData('pract_resp.started', pract_resp.tStartRefresh)
        checkPract.addData('pract_resp.stopped', pract_resp.tStopRefresh)
        modePract = False
        # the Routine "check_pract" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed modePract repeats of 'checkPract'
    
    
    # set up handler to look after randomisation of conditions etc
    interLoop = data.TrialHandler(nReps=modeInter, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='interLoop')
    thisExp.addLoop(interLoop)  # add the loop to the experiment
    thisInterLoop = interLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInterLoop.rgb)
    if thisInterLoop != None:
        for paramName in thisInterLoop:
            exec('{} = thisInterLoop[paramName]'.format(paramName))
    
    for thisInterLoop in interLoop:
        currentLoop = interLoop
        # abbreviate parameter names if possible (e.g. rgb = thisInterLoop.rgb)
        if thisInterLoop != None:
            for paramName in thisInterLoop:
                exec('{} = thisInterLoop[paramName]'.format(paramName))
        
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
        interLoop.addData('inter_img.started', inter_img.tStartRefresh)
        interLoop.addData('inter_img.stopped', inter_img.tStopRefresh)
        # the Routine "intertrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed modeInter repeats of 'interLoop'
    
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
