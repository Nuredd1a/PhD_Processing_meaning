/******************************* 
 * Training_Temps_Lectura Test *
 *******************************/

import { PsychoJS } from './lib/core-2021.1.4.js';
import * as core from './lib/core-2021.1.4.js';
import { TrialHandler } from './lib/data-2021.1.4.js';
import { Scheduler } from './lib/util-2021.1.4.js';
import * as visual from './lib/visual-2021.1.4.js';
import * as sound from './lib/sound-2021.1.4.js';
import * as util from './lib/util-2021.1.4.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'training_temps_lectura';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const loadLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(loadLoopBegin, loadLoopScheduler);
flowScheduler.add(loadLoopScheduler);
flowScheduler.add(loadLoopEnd);
flowScheduler.add(setting_parametersRoutineBegin());
flowScheduler.add(setting_parametersRoutineEachFrame());
flowScheduler.add(setting_parametersRoutineEnd());
flowScheduler.add(startRoutineBegin());
flowScheduler.add(startRoutineEachFrame());
flowScheduler.add(startRoutineEnd());
flowScheduler.add(waitRoutineBegin());
flowScheduler.add(waitRoutineEachFrame());
flowScheduler.add(waitRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(end_trainingRoutineBegin());
flowScheduler.add(end_trainingRoutineEachFrame());
flowScheduler.add(end_trainingRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'Prac4_semsyn.wav', 'path': 'Prac4_semsyn.wav'},
    {'name': 'Prac2_corr.wav', 'path': 'Prac2_corr.wav'},
    {'name': 'Prac6_syn.wav', 'path': 'Prac6_syn.wav'},
    {'name': 'Prac3_sem.wav', 'path': 'Prac3_sem.wav'},
    {'name': 'Prac1_corr.wav', 'path': 'Prac1_corr.wav'},
    {'name': 'Prac5_semsyn.wav', 'path': 'Prac5_semsyn.wav'},
    {'name': 'Trigers_Práctica.xlsx', 'path': 'Trigers_Práctica.xlsx'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var loading_phrasesClock;
var setting_parametersClock;
var startClock;
var start_txt;
var start_resp;
var waitClock;
var wait_img;
var setting_trialClock;
var mainClock;
var fix;
var stim_phrase;
var questionClock;
var item_check;
var yes_rect;
var no_rect;
var yes;
var no;
var blinkClock;
var blink_txt;
var intertrialClock;
var inter_img;
var end_trainingClock;
var end_t;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "loading_phrases"
  loading_phrasesClock = new util.Clock();
  // Initialize components for Routine "setting_parameters"
  setting_parametersClock = new util.Clock();
  // Initialize components for Routine "start"
  startClock = new util.Clock();
  start_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_txt',
    text: 'INSTRUCCIONS\n\nVamos a empezar la tarea.\n\nPulsa la barra espaciadora para empezar',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  start_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "wait"
  waitClock = new util.Clock();
  wait_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'wait_img', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "setting_trial"
  setting_trialClock = new util.Clock();
  // Initialize components for Routine "main"
  mainClock = new util.Clock();
  fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  stim_phrase = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  stim_phrase.setVolume(1.0);
  // Initialize components for Routine "question"
  questionClock = new util.Clock();
  item_check = new visual.TextStim({
    win: psychoJS.window,
    name: 'item_check',
    text: '¿Era correcta la frase anterior?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.05], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  yes_rect = new visual.Rect ({
    win: psychoJS.window, name: 'yes_rect', 
    width: [0.125, 0.05][0], height: [0.125, 0.05][1],
    ori: 0.0, pos: [(- 0.15), 0],
    lineWidth: 1.0, lineColor: new util.Color([0.9216, 0.9216, 0.7255]),
    fillColor: new util.Color([0.9216, 0.9216, 0.7255]),
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  no_rect = new visual.Rect ({
    win: psychoJS.window, name: 'no_rect', 
    width: [0.125, 0.05][0], height: [0.125, 0.05][1],
    ori: 0.0, pos: [0.15, 0],
    lineWidth: 1.0, lineColor: new util.Color([0.9216, 0.9216, 0.7255]),
    fillColor: new util.Color([0.9216, 0.9216, 0.7255]),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  yes = new visual.TextStim({
    win: psychoJS.window,
    name: 'yes',
    text: 'Sí',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.15), 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  no = new visual.TextStim({
    win: psychoJS.window,
    name: 'no',
    text: 'No',
    font: 'Arial',
    units: undefined, 
    pos: [0.15, 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "blink"
  blinkClock = new util.Clock();
  blink_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'blink_txt',
    text: '****',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "intertrial"
  intertrialClock = new util.Clock();
  inter_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'inter_img', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "end_training"
  end_trainingClock = new util.Clock();
  end_t = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_t',
    text: 'El entrenamiento se ha acabado.\n\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var load;
var currentLoop;
function loadLoopBegin(loadLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  load = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'Trigers_Práctica.xlsx',
    seed: undefined, name: 'load'
  });
  psychoJS.experiment.addLoop(load); // add the loop to the experiment
  currentLoop = load;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisLoad of load) {
    const snapshot = load.getSnapshot();
    loadLoopScheduler.add(importConditions(snapshot));
    loadLoopScheduler.add(loading_phrasesRoutineBegin(snapshot));
    loadLoopScheduler.add(loading_phrasesRoutineEachFrame(snapshot));
    loadLoopScheduler.add(loading_phrasesRoutineEnd(snapshot));
    loadLoopScheduler.add(endLoopIteration(loadLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function loadLoopEnd() {
  psychoJS.experiment.removeLoop(load);

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: totalTrials, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    const snapshot = trials.getSnapshot();
    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(setting_trialRoutineBegin(snapshot));
    trialsLoopScheduler.add(setting_trialRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(setting_trialRoutineEnd(snapshot));
    trialsLoopScheduler.add(mainRoutineBegin(snapshot));
    trialsLoopScheduler.add(mainRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(mainRoutineEnd(snapshot));
    trialsLoopScheduler.add(questionRoutineBegin(snapshot));
    trialsLoopScheduler.add(questionRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(questionRoutineEnd(snapshot));
    trialsLoopScheduler.add(blinkRoutineBegin(snapshot));
    trialsLoopScheduler.add(blinkRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(blinkRoutineEnd(snapshot));
    const loopInterLoopScheduler = new Scheduler(psychoJS);
    trialsLoopScheduler.add(loopInterLoopBegin, loopInterLoopScheduler);
    trialsLoopScheduler.add(loopInterLoopScheduler);
    trialsLoopScheduler.add(loopInterLoopEnd);
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var loopInter;
function loopInterLoopBegin(loopInterLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  loopInter = new TrialHandler({
    psychoJS: psychoJS,
    nReps: modeInter, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'loopInter'
  });
  psychoJS.experiment.addLoop(loopInter); // add the loop to the experiment
  currentLoop = loopInter;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisLoopInter of loopInter) {
    const snapshot = loopInter.getSnapshot();
    loopInterLoopScheduler.add(importConditions(snapshot));
    loopInterLoopScheduler.add(intertrialRoutineBegin(snapshot));
    loopInterLoopScheduler.add(intertrialRoutineEachFrame(snapshot));
    loopInterLoopScheduler.add(intertrialRoutineEnd(snapshot));
    loopInterLoopScheduler.add(endLoopIteration(loopInterLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function loopInterLoopEnd() {
  psychoJS.experiment.removeLoop(loopInter);

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var loading_phrasesComponents;
function loading_phrasesRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'loading_phrases'-------
    t = 0;
    loading_phrasesClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    loading_phrasesComponents = [];
    
    for (const thisComponent of loading_phrasesComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function loading_phrasesRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'loading_phrases'-------
    // get current time
    t = loading_phrasesClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of loading_phrasesComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function loading_phrasesRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'loading_phrases'-------
    for (const thisComponent of loading_phrasesComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "loading_phrases" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var setting_parametersComponents;
function setting_parametersRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'setting_parameters'-------
    t = 0;
    setting_parametersClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    setting_parametersComponents = [];
    
    for (const thisComponent of setting_parametersComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function setting_parametersRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'setting_parameters'-------
    // get current time
    t = setting_parametersClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of setting_parametersComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function setting_parametersRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'setting_parameters'-------
    for (const thisComponent of setting_parametersComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "setting_parameters" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _start_resp_allKeys;
var startComponents;
function startRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'start'-------
    t = 0;
    startClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    start_resp.keys = undefined;
    start_resp.rt = undefined;
    _start_resp_allKeys = [];
    // keep track of which components have finished
    startComponents = [];
    startComponents.push(start_txt);
    startComponents.push(start_resp);
    
    for (const thisComponent of startComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function startRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'start'-------
    // get current time
    t = startClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *start_txt* updates
    if (t >= 0.0 && start_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_txt.tStart = t;  // (not accounting for frame time here)
      start_txt.frameNStart = frameN;  // exact frame index
      
      start_txt.setAutoDraw(true);
    }

    
    // *start_resp* updates
    if (t >= 0.0 && start_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_resp.tStart = t;  // (not accounting for frame time here)
      start_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { start_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { start_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { start_resp.clearEvents(); });
    }

    if (start_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = start_resp.getKeys({keyList: ['space'], waitRelease: false});
      _start_resp_allKeys = _start_resp_allKeys.concat(theseKeys);
      if (_start_resp_allKeys.length > 0) {
        start_resp.keys = _start_resp_allKeys[_start_resp_allKeys.length - 1].name;  // just the last key pressed
        start_resp.rt = _start_resp_allKeys[_start_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of startComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function startRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'start'-------
    for (const thisComponent of startComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('start_resp.keys', start_resp.keys);
    if (typeof start_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('start_resp.rt', start_resp.rt);
        routineTimer.reset();
        }
    
    start_resp.stop();
    // the Routine "start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var waitComponents;
function waitRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'wait'-------
    t = 0;
    waitClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    waitComponents = [];
    waitComponents.push(wait_img);
    
    for (const thisComponent of waitComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function waitRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'wait'-------
    // get current time
    t = waitClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *wait_img* updates
    if (t >= 0.0 && wait_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      wait_img.tStart = t;  // (not accounting for frame time here)
      wait_img.frameNStart = frameN;  // exact frame index
      
      wait_img.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (wait_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      wait_img.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of waitComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function waitRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'wait'-------
    for (const thisComponent of waitComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var nTrial;
var nRow;
var soundF;
var soundDur;
var fixDur;
var onset_keyw_2;
var onset_keyw_1;
var onset_keyw;
var onset_keyw_plus1;
var onset_endingw;
var trig_onset_stim;
var corrAns;
var interDur;
var setting_trialComponents;
function setting_trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'setting_trial'-------
    t = 0;
    setting_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    nTrial = (nTrial + 1);
    nRow = (nRow + 1);
    soundF = condList[trials.thisN][1];
    soundDur = condList[trials.thisN][3];
    fixDur = (delayFix + soundDur);
    console.log(soundF);
    console.log(fixDur);
    onset_keyw_2 = (delayFix + condList[trials.thisN][4]);
    onset_keyw_1 = (delayFix + condList[trials.thisN][5]);
    onset_keyw = (delayFix + condList[trials.thisN][6]);
    onset_keyw_plus1 = (delayFix + condList[trials.thisN][7]);
    onset_endingw = (delayFix + condList[trials.thisN][8]);
    trig_onset_stim = condList[trials.thisN][3];
    corrAns = condList[trials.thisN][9];
    random.shuffle(auxInter);
    interDur = auxInter[0];
    
    // keep track of which components have finished
    setting_trialComponents = [];
    
    for (const thisComponent of setting_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function setting_trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'setting_trial'-------
    // get current time
    t = setting_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of setting_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function setting_trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'setting_trial'-------
    for (const thisComponent of setting_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "setting_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var mainComponents;
function mainRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'main'-------
    t = 0;
    mainClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    stim_phrase = new sound.Sound({
    win: psychoJS.window,
    value: soundF,
    secs: -1,
    });
    stim_phrase.setVolume(1.0);
    // keep track of which components have finished
    mainComponents = [];
    mainComponents.push(fix);
    mainComponents.push(stim_phrase);
    
    for (const thisComponent of mainComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function mainRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'main'-------
    // get current time
    t = mainClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix* updates
    if (t >= 0.0 && fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix.tStart = t;  // (not accounting for frame time here)
      fix.frameNStart = frameN;  // exact frame index
      
      fix.setAutoDraw(true);
    }

    frameRemains = 0.0 + fixDur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fix.setAutoDraw(false);
    }
    // start/stop stim_phrase
    if (t >= delayFix && stim_phrase.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stim_phrase.tStart = t;  // (not accounting for frame time here)
      stim_phrase.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ stim_phrase.play(); });  // screen flip
      stim_phrase.status = PsychoJS.Status.STARTED;
    }
    if (t >= (stim_phrase.getDuration() + stim_phrase.tStart)     && stim_phrase.status === PsychoJS.Status.STARTED) {
      stim_phrase.stop();  // stop the sound (if longer than duration)
      stim_phrase.status = PsychoJS.Status.FINISHED;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of mainComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function mainRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'main'-------
    for (const thisComponent of mainComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    stim_phrase.stop();  // ensure sound has stopped at end of routine
    // the Routine "main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var questionComponents;
function questionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'question'-------
    t = 0;
    questionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    questionComponents = [];
    questionComponents.push(item_check);
    questionComponents.push(yes_rect);
    questionComponents.push(no_rect);
    questionComponents.push(yes);
    questionComponents.push(no);
    
    for (const thisComponent of questionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function questionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'question'-------
    // get current time
    t = questionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *item_check* updates
    if (t >= start_q && item_check.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item_check.tStart = t;  // (not accounting for frame time here)
      item_check.frameNStart = frameN;  // exact frame index
      
      item_check.setAutoDraw(true);
    }

    frameRemains = start_q + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (item_check.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      item_check.setAutoDraw(false);
    }
    
    // *yes_rect* updates
    if (t >= start_q && yes_rect.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      yes_rect.tStart = t;  // (not accounting for frame time here)
      yes_rect.frameNStart = frameN;  // exact frame index
      
      yes_rect.setAutoDraw(true);
    }

    frameRemains = start_q + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (yes_rect.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      yes_rect.setAutoDraw(false);
    }
    
    // *no_rect* updates
    if (t >= start_q && no_rect.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      no_rect.tStart = t;  // (not accounting for frame time here)
      no_rect.frameNStart = frameN;  // exact frame index
      
      no_rect.setAutoDraw(true);
    }

    frameRemains = start_q + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (no_rect.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      no_rect.setAutoDraw(false);
    }
    
    // *yes* updates
    if (t >= start_q && yes.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      yes.tStart = t;  // (not accounting for frame time here)
      yes.frameNStart = frameN;  // exact frame index
      
      yes.setAutoDraw(true);
    }

    frameRemains = start_q + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (yes.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      yes.setAutoDraw(false);
    }
    
    // *no* updates
    if (t >= start_q && no.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      no.tStart = t;  // (not accounting for frame time here)
      no.frameNStart = frameN;  // exact frame index
      
      no.setAutoDraw(true);
    }

    frameRemains = start_q + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (no.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      no.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of questionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function questionRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'question'-------
    for (const thisComponent of questionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var blinkComponents;
function blinkRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'blink'-------
    t = 0;
    blinkClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    blinkComponents = [];
    blinkComponents.push(blink_txt);
    
    for (const thisComponent of blinkComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function blinkRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'blink'-------
    // get current time
    t = blinkClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blink_txt* updates
    if (t >= start_q && blink_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blink_txt.tStart = t;  // (not accounting for frame time here)
      blink_txt.frameNStart = frameN;  // exact frame index
      
      blink_txt.setAutoDraw(true);
    }

    frameRemains = start_q + blinkDur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (blink_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blink_txt.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of blinkComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blinkRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'blink'-------
    for (const thisComponent of blinkComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "blink" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var intertrialComponents;
function intertrialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'intertrial'-------
    t = 0;
    intertrialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    intertrialComponents = [];
    intertrialComponents.push(inter_img);
    
    for (const thisComponent of intertrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function intertrialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'intertrial'-------
    // get current time
    t = intertrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *inter_img* updates
    if (t >= 0.0 && inter_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      inter_img.tStart = t;  // (not accounting for frame time here)
      inter_img.frameNStart = frameN;  // exact frame index
      
      inter_img.setAutoDraw(true);
    }

    frameRemains = 0.0 + interDur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (inter_img.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      inter_img.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of intertrialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function intertrialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'intertrial'-------
    for (const thisComponent of intertrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "intertrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var end_trainingComponents;
function end_trainingRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'end_training'-------
    t = 0;
    end_trainingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    end_trainingComponents = [];
    end_trainingComponents.push(end_t);
    
    for (const thisComponent of end_trainingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function end_trainingRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'end_training'-------
    // get current time
    t = end_trainingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_t* updates
    if (t >= 0.0 && end_t.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_t.tStart = t;  // (not accounting for frame time here)
      end_t.frameNStart = frameN;  // exact frame index
      
      end_t.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_t.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_t.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of end_trainingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_trainingRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'end_training'-------
    for (const thisComponent of end_trainingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
