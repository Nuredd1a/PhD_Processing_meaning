/******************** 
 * Pilot_List1 Test *
 ********************/

import { PsychoJS } from './lib/core-2020.2.js';
import * as core from './lib/core-2020.2.js';
import { TrialHandler } from './lib/data-2020.2.js';
import { Scheduler } from './lib/util-2020.2.js';
import * as visual from './lib/visual-2020.2.js';
import * as sound from './lib/sound-2020.2.js';
import * as util from './lib/util-2020.2.js';
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
let expName = 'pilot_list1';  // from the Builder filename that created this script
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
flowScheduler.add(setting_JSRoutineBegin());
flowScheduler.add(setting_JSRoutineEachFrame());
flowScheduler.add(setting_JSRoutineEnd());
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
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'pilot_list1.xlsx', 'path': 'pilot_list1.xlsx'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.9';
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


var setting_JSClock;
var thisExp;
var win;
var event;
var shuffle;
var webbrowser;
var random;
var randint;
var loading_phrasesClock;
var condList;
var setting_parametersClock;
var trialsTraining;
var dimS;
var colorS;
var fontS;
var colorN;
var xPos1;
var xPos2;
var xPos3;
var xPos4;
var yPos;
var aux;
var aux_cond;
var startClock;
var start_txt;
var key_resp_2;
var waitClock;
var wait_img;
var fixationClock;
var aux_word;
var fix_txt;
var fix_resp;
var wordsClock;
var word_txt;
var words_resp;
var questionClock;
var item_check;
var question_resp;
var yes_rect;
var no_rect;
var yes;
var no;
var auxOut1;
var auxOut2;
var ratingClock;
var rating_question;
var rect1;
var rect2;
var rect3;
var rect4;
var rect5;
var g1;
var g2;
var g3;
var g4;
var g5;
var rating_resp;
var NadaSeguro;
var MuySeguro;
var pausaClock;
var pausa_txt;
var pausa_resp;
var check_practClock;
var pract_txt;
var pract_resp;
var intertrialClock;
var inter_img;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "setting_JS"
  setting_JSClock = new util.Clock();
  thisExp = psychoJS.experiment;
  win = psychoJS.window;
  event = psychoJS.eventManager;
  Array.prototype.append = [].push;
  shuffle = util.shuffle;
  webbrowser = window;
  random = Math.random;
  
  randint = function(min, maxplusone){
   return Math.floor(Math.random()*
          (maxplusone - min)) + min;
  }
  // Initialize components for Routine "loading_phrases"
  loading_phrasesClock = new util.Clock();
  condList = [];
  
  // Initialize components for Routine "setting_parameters"
  setting_parametersClock = new util.Clock();
  document.body.style.cursor='none';
  
  trialsTraining = 4;
  
  // dimensions elements of rating
  dimS = 0.1;
  colorS = 'blue';
  fontS = 0.05;
  colorN = 'white';
  xPos1 = -0.3;
  xPos2 = -0.15;
  xPos3 = 0;
  xPos4 = -0.5;
  yPos = 0;
  aux = [];
  aux_cond = [];
  
  // Initialize components for Routine "start"
  startClock = new util.Clock();
  start_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_txt',
    text: '¡Bienvenido!\n\nA continuación vas a leer unas frases y tendrás que decidir si son correctas o no. \n\nEn la pantalla aparecerá solo una palabra a la vez. Para ir leyendo la frase, pulsa la barra espaciadora y e irán apareciendo las siguientes palabras de la frase. Lee a la velocidad que leerías naturalmente.\n\nCuando la frase haya terminado, te preguntaremos si la frase que acabas de leer es correcta o no. Pulsa la tecla de la letra Q para indicar que SÍ y la tecla de la letra P para indicar que NO. Intenta responder lo más rápido que puedas, sin reflexionarlo mucho. Los errores que detectes pueden ser tanto de forma (que las frases no estén bien construidas) como de contenido (que tengan significados absurdos o imposibles).\n\nDespués, aparecerá una escala del 1 al 5 para que valores tu nivel de seguridad en tu respuesta, siendo 5 MUY SEGURO y 1 NADA SEGURO. \n\nVamos a empezar con una práctica. Pulsa la barra espaciadora para empezar. Cuando aparezca este símbolo +, pulsa la barra espaciadora. \n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "wait"
  waitClock = new util.Clock();
  wait_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'wait_img', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "fixation"
  fixationClock = new util.Clock();
  aux_word = []
  fix_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix_txt',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  fix_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "words"
  wordsClock = new util.Clock();
  word_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'word_txt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -1.0 
  });
  
  words_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "question"
  questionClock = new util.Clock();
  item_check = new visual.TextStim({
    win: psychoJS.window,
    name: 'item_check',
    text: '¿Era correcta la frase anterior?\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.05], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  question_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  yes_rect = new visual.Rect ({
    win: psychoJS.window, name: 'yes_rect', 
    width: [0.125, 0.05][0], height: [0.125, 0.05][1],
    ori: 0, pos: [(- 0.15), 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  no_rect = new visual.Rect ({
    win: psychoJS.window, name: 'no_rect', 
    width: [0.125, 0.05][0], height: [0.125, 0.05][1],
    ori: 0, pos: [0.15, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  yes = new visual.TextStim({
    win: psychoJS.window,
    name: 'yes',
    text: 'SÍ',
    font: 'Arial',
    units: undefined, 
    pos: [(- 0.15), 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -4.0 
  });
  
  no = new visual.TextStim({
    win: psychoJS.window,
    name: 'no',
    text: 'NO',
    font: 'Arial',
    units: undefined, 
    pos: [0.15, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -5.0 
  });
  
  auxOut1 = [];
  auxOut2 = [];
  
  // Initialize components for Routine "rating"
  ratingClock = new util.Clock();
  rating_question = new visual.TextStim({
    win: psychoJS.window,
    name: 'rating_question',
    text: 'Grado de seguridad de tu respuesta',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  rect1 = new visual.Rect ({
    win: psychoJS.window, name: 'rect1', 
    width: [dimS, dimS][0], height: [dimS, dimS][1],
    ori: 0, pos: [xPos1, yPos],
    lineWidth: 1, lineColor: new util.Color(colorS),
    fillColor: new util.Color(colorS),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  rect2 = new visual.Rect ({
    win: psychoJS.window, name: 'rect2', 
    width: [dimS, dimS][0], height: [dimS, dimS][1],
    ori: 0, pos: [xPos2, yPos],
    lineWidth: 1, lineColor: new util.Color(colorS),
    fillColor: new util.Color(colorS),
    opacity: 1, depth: -2, interpolate: true,
  });
  
  rect3 = new visual.Rect ({
    win: psychoJS.window, name: 'rect3', 
    width: [dimS, dimS][0], height: [dimS, dimS][1],
    ori: 0, pos: [xPos3, yPos],
    lineWidth: 1, lineColor: new util.Color(colorS),
    fillColor: new util.Color(colorS),
    opacity: 1, depth: -3, interpolate: true,
  });
  
  rect4 = new visual.Rect ({
    win: psychoJS.window, name: 'rect4', 
    width: [dimS, dimS][0], height: [dimS, dimS][1],
    ori: 0, pos: [(- xPos2), yPos],
    lineWidth: 1, lineColor: new util.Color(colorS),
    fillColor: new util.Color(colorS),
    opacity: 1, depth: -4, interpolate: true,
  });
  
  rect5 = new visual.Rect ({
    win: psychoJS.window, name: 'rect5', 
    width: [dimS, dimS][0], height: [dimS, dimS][1],
    ori: 0, pos: [(- xPos1), yPos],
    lineWidth: 1, lineColor: new util.Color(colorS),
    fillColor: new util.Color(colorS),
    opacity: 1, depth: -5, interpolate: true,
  });
  
  g1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'g1',
    text: '1',
    font: 'Arial',
    units: undefined, 
    pos: [xPos1, yPos], height: fontS,  wrapWidth: undefined, ori: 0,
    color: new util.Color(colorN),  opacity: 1,
    depth: -6.0 
  });
  
  g2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'g2',
    text: '2',
    font: 'Arial',
    units: undefined, 
    pos: [xPos2, yPos], height: fontS,  wrapWidth: undefined, ori: 0,
    color: new util.Color(colorN),  opacity: 1,
    depth: -7.0 
  });
  
  g3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'g3',
    text: '3',
    font: 'Arial',
    units: undefined, 
    pos: [xPos3, yPos], height: fontS,  wrapWidth: undefined, ori: 0,
    color: new util.Color(colorN),  opacity: 1,
    depth: -8.0 
  });
  
  g4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'g4',
    text: '4',
    font: 'Arial',
    units: undefined, 
    pos: [(- xPos2), yPos], height: fontS,  wrapWidth: undefined, ori: 0,
    color: new util.Color(colorN),  opacity: 1,
    depth: -9.0 
  });
  
  g5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'g5',
    text: '5',
    font: 'Arial',
    units: undefined, 
    pos: [(- xPos1), yPos], height: fontS,  wrapWidth: undefined, ori: 0,
    color: new util.Color(colorN),  opacity: 1,
    depth: -10.0 
  });
  
  rating_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  NadaSeguro = new visual.TextStim({
    win: psychoJS.window,
    name: 'NadaSeguro',
    text: 'Nada seguro',
    font: 'Arial',
    units: undefined, 
    pos: [xPos4, yPos], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -13.0 
  });
  
  MuySeguro = new visual.TextStim({
    win: psychoJS.window,
    name: 'MuySeguro',
    text: 'Muy seguro',
    font: 'Arial',
    units: undefined, 
    pos: [(- xPos4), yPos], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: -14.0 
  });
  
  // Initialize components for Routine "pausa"
  pausaClock = new util.Clock();
  pausa_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'pausa_txt',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  pausa_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "check_pract"
  check_practClock = new util.Clock();
  pract_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'pract_txt',
    text: 'Has acabado la práctica. \n\nPulsa la barra de espacio para empezar la tarea.\n\nCada ciertas frases tendrás una PAUSA en la que podrás tomarte unos segundos. Continúa enseguida que estés listo. ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  pract_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "intertrial"
  intertrialClock = new util.Clock();
  inter_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'inter_img', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var setting_JSComponents;
function setting_JSRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'setting_JS'-------
    t = 0;
    setting_JSClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    setting_JSComponents = [];
    
    for (const thisComponent of setting_JSComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


var continueRoutine;
function setting_JSRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'setting_JS'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = setting_JSClock.getTime();
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
    for (const thisComponent of setting_JSComponents)
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


function setting_JSRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'setting_JS'-------
    for (const thisComponent of setting_JSComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "setting_JS" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var load;
var currentLoop;
function loadLoopBegin(loadLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  load = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'pilot_list1.xlsx',
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
    trialsLoopScheduler.add(fixationRoutineBegin(snapshot));
    trialsLoopScheduler.add(fixationRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(fixationRoutineEnd(snapshot));
    const words_loopLoopScheduler = new Scheduler(psychoJS);
    trialsLoopScheduler.add(words_loopLoopBegin, words_loopLoopScheduler);
    trialsLoopScheduler.add(words_loopLoopScheduler);
    trialsLoopScheduler.add(words_loopLoopEnd);
    trialsLoopScheduler.add(questionRoutineBegin(snapshot));
    trialsLoopScheduler.add(questionRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(questionRoutineEnd(snapshot));
    trialsLoopScheduler.add(ratingRoutineBegin(snapshot));
    trialsLoopScheduler.add(ratingRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(ratingRoutineEnd(snapshot));
    const checkPausaLoopScheduler = new Scheduler(psychoJS);
    trialsLoopScheduler.add(checkPausaLoopBegin, checkPausaLoopScheduler);
    trialsLoopScheduler.add(checkPausaLoopScheduler);
    trialsLoopScheduler.add(checkPausaLoopEnd);
    const checkPractLoopScheduler = new Scheduler(psychoJS);
    trialsLoopScheduler.add(checkPractLoopBegin, checkPractLoopScheduler);
    trialsLoopScheduler.add(checkPractLoopScheduler);
    trialsLoopScheduler.add(checkPractLoopEnd);
    const interLoopLoopScheduler = new Scheduler(psychoJS);
    trialsLoopScheduler.add(interLoopLoopBegin, interLoopLoopScheduler);
    trialsLoopScheduler.add(interLoopLoopScheduler);
    trialsLoopScheduler.add(interLoopLoopEnd);
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var words_loop;
function words_loopLoopBegin(words_loopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  words_loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: totalWords, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'words_loop'
  });
  psychoJS.experiment.addLoop(words_loop); // add the loop to the experiment
  currentLoop = words_loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisWords_loop of words_loop) {
    const snapshot = words_loop.getSnapshot();
    words_loopLoopScheduler.add(importConditions(snapshot));
    words_loopLoopScheduler.add(wordsRoutineBegin(snapshot));
    words_loopLoopScheduler.add(wordsRoutineEachFrame(snapshot));
    words_loopLoopScheduler.add(wordsRoutineEnd(snapshot));
    words_loopLoopScheduler.add(endLoopIteration(words_loopLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function words_loopLoopEnd() {
  psychoJS.experiment.removeLoop(words_loop);

  return Scheduler.Event.NEXT;
}


var checkPausa;
function checkPausaLoopBegin(checkPausaLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  checkPausa = new TrialHandler({
    psychoJS: psychoJS,
    nReps: modePausa, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'checkPausa'
  });
  psychoJS.experiment.addLoop(checkPausa); // add the loop to the experiment
  currentLoop = checkPausa;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisCheckPausa of checkPausa) {
    const snapshot = checkPausa.getSnapshot();
    checkPausaLoopScheduler.add(importConditions(snapshot));
    checkPausaLoopScheduler.add(pausaRoutineBegin(snapshot));
    checkPausaLoopScheduler.add(pausaRoutineEachFrame(snapshot));
    checkPausaLoopScheduler.add(pausaRoutineEnd(snapshot));
    checkPausaLoopScheduler.add(endLoopIteration(checkPausaLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function checkPausaLoopEnd() {
  psychoJS.experiment.removeLoop(checkPausa);

  return Scheduler.Event.NEXT;
}


var checkPract;
function checkPractLoopBegin(checkPractLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  checkPract = new TrialHandler({
    psychoJS: psychoJS,
    nReps: modePract, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'checkPract'
  });
  psychoJS.experiment.addLoop(checkPract); // add the loop to the experiment
  currentLoop = checkPract;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisCheckPract of checkPract) {
    const snapshot = checkPract.getSnapshot();
    checkPractLoopScheduler.add(importConditions(snapshot));
    checkPractLoopScheduler.add(check_practRoutineBegin(snapshot));
    checkPractLoopScheduler.add(check_practRoutineEachFrame(snapshot));
    checkPractLoopScheduler.add(check_practRoutineEnd(snapshot));
    checkPractLoopScheduler.add(endLoopIteration(checkPractLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function checkPractLoopEnd() {
  psychoJS.experiment.removeLoop(checkPract);

  return Scheduler.Event.NEXT;
}


var interLoop;
function interLoopLoopBegin(interLoopLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  interLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: modeInter, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'interLoop'
  });
  psychoJS.experiment.addLoop(interLoop); // add the loop to the experiment
  currentLoop = interLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisInterLoop of interLoop) {
    const snapshot = interLoop.getSnapshot();
    interLoopLoopScheduler.add(importConditions(snapshot));
    interLoopLoopScheduler.add(intertrialRoutineBegin(snapshot));
    interLoopLoopScheduler.add(intertrialRoutineEachFrame(snapshot));
    interLoopLoopScheduler.add(intertrialRoutineEnd(snapshot));
    interLoopLoopScheduler.add(endLoopIteration(interLoopLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function interLoopLoopEnd() {
  psychoJS.experiment.removeLoop(interLoop);

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var loading_phrasesComponents;
function loading_phrasesRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'loading_phrases'-------
    t = 0;
    loading_phrasesClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    condList.append([n, cond, word1, word2, word3, word4, word5, word6, word7, word8, word9, target, length, trigger, correctKey, targetPos]);
    
    // keep track of which components have finished
    loading_phrasesComponents = [];
    
    for (const thisComponent of loading_phrasesComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function loading_phrasesRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'loading_phrases'-------
    let continueRoutine = true; // until we're told otherwise
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


var totalTrials;
var word;
var totalWords;
var lengthCol;
var corrAnsCol;
var targetCol;
var keyword;
var corrAns;
var nTrial;
var nRow;
var nWord;
var nInter;
var nPausa;
var auxInter;
var interDur;
var modePausa;
var modeInter;
var modePract;
var kk;
var i;
var setting_parametersComponents;
function setting_parametersRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'setting_parameters'-------
    t = 0;
    setting_parametersClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // TASK PARAMETERS
    // ---------------
    
    totalTrials = condList.length;
    console.log(totalTrials);
    word = "";
    
    // variable that takes the length of 
    // each sentence
    totalWords = 0;
    
    // variable that takes the length column
    lengthCol = 12;
    
    // variable that takes the correct answer column
    corrAnsCol = 14;
    
    // variable that takes the target word
    targetCol = 11;
    
    // variable that takes the keyword position
    keyword = 15
    
    corrAns = [];
    
    // counters
    nTrial = 0;
    nRow = -1;
    nWord = -1;
    nInter = -1;
    nPausa = 12;
    
    // array of possible intertrial durations
    auxInter = [0.75, 1, 1.25, 1.5, 1.75, 2];
    shuffle(auxInter);
    interDur = 0;
    
    modePausa = false;
    modeInter = true;
    modePract = false;
    
    aux = condList.slice(trialsTraining);
    shuffle(aux);
    for (let k = 0; k < aux.length; k++){
                condList[trialsTraining + k] = aux[k];
            }        
    
    kk = 0;
    i = trialsTraining + 2;
    while ((i <= (totalTrials - 1))) {
         aux = [];
        if (((condList[i][1] === condList[(i - 1)][1]) && (condList[i][1] === condList[(i - 2)][1]))) {
            aux = condList.slice(i);
            shuffle(aux);
            
            for (let k = 0; k < aux.length; k++){
                condList[i + k] = aux[k];
            }  
            kk = (kk + 1);
            i = (i - 1);
        } else {
            kk = 0;
        }
        if ((kk > 10)) {
            aux = condList.slice(trialsTraining);
            shuffle(aux);
            for (let k = 0; k < aux.length; k++){
                condList[trialsTraining + k] = aux[k];
            }        
            i = (trialsTraining  - 1);
        }
        i = (i + 1);
    }
    
    
    // keep track of which components have finished
    setting_parametersComponents = [];
    
    for (const thisComponent of setting_parametersComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function setting_parametersRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'setting_parameters'-------
    let continueRoutine = true; // until we're told otherwise
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


var _key_resp_2_allKeys;
var startComponents;
function startRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'start'-------
    t = 0;
    startClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    startComponents = [];
    startComponents.push(start_txt);
    startComponents.push(key_resp_2);
    
    for (const thisComponent of startComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function startRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'start'-------
    let continueRoutine = true; // until we're told otherwise
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

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
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
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
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
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    waitComponents = [];
    waitComponents.push(wait_img);
    
    for (const thisComponent of waitComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


var frameRemains;
function waitRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'wait'-------
    let continueRoutine = true; // until we're told otherwise
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

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((wait_img.status === PsychoJS.Status.STARTED || wait_img.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
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


var _fix_resp_allKeys;
var fixationComponents;
function fixationRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'fixation'-------
    t = 0;
    fixationClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    nWord = -1
    nTrial = nTrial + 1;
    nRow = nRow + 1;
    console.log(nRow)
    totalWords = condList[nRow][lengthCol];
    corrAns = condList[nRow][corrAnsCol];
    //console.log(totalWords)
    //console.log(condList[nRow][0]);
    //console.log(corrAns)
        
    aux_word = [];
    for (var i = 0, _pj_a = Number.parseInt((totalWords - 1)); (i < _pj_a); i += 1) {
        aux_word.append(condList[nRow][(i + 2)]);
    }
    aux_word.append(condList[nRow][targetCol]);
    
    //console.log(aux_word)
    
    fix_resp.keys = undefined;
    fix_resp.rt = undefined;
    _fix_resp_allKeys = [];
    nInter = (nInter + 1);
    if ((nInter === auxInter.length)) {
        shuffle(auxInter);
        nInter = 0;
    }
    
    interDur = auxInter[nInter];
    
    console.log(interDur);
    // keep track of which components have finished
    fixationComponents = [];
    fixationComponents.push(fix_txt);
    fixationComponents.push(fix_resp);
    
    for (const thisComponent of fixationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function fixationRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'fixation'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fix_txt* updates
    if (t >= 0.0 && fix_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_txt.tStart = t;  // (not accounting for frame time here)
      fix_txt.frameNStart = frameN;  // exact frame index
      
      fix_txt.setAutoDraw(true);
    }

    
    // *fix_resp* updates
    if (t >= 0.0 && fix_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fix_resp.tStart = t;  // (not accounting for frame time here)
      fix_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { fix_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { fix_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { fix_resp.clearEvents(); });
    }

    if (fix_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = fix_resp.getKeys({keyList: ['space'], waitRelease: false});
      _fix_resp_allKeys = _fix_resp_allKeys.concat(theseKeys);
      if (_fix_resp_allKeys.length > 0) {
        fix_resp.keys = _fix_resp_allKeys[_fix_resp_allKeys.length - 1].name;  // just the last key pressed
        fix_resp.rt = _fix_resp_allKeys[_fix_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of fixationComponents)
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


function fixationRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'fixation'-------
    for (const thisComponent of fixationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('fix_resp.keys', fix_resp.keys);
    if (typeof fix_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('fix_resp.rt', fix_resp.rt);
        routineTimer.reset();
        }
    
    fix_resp.stop();
    // the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _words_resp_allKeys;
var wordsComponents;
function wordsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'words'-------
    t = 0;
    wordsClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    nWord = nWord + 1
    word = aux_word[nWord];
    
    // adding presented item to the output
    words_loop.addData("item", word)
    
    // adding a 1 to column target to the output
    // when the key word is presented
    if (((nWord + 1) === condList[nRow][keyword])) {
        words_loop.addData("keyWord", 1);
    }
    
    //console.log(condList[nRow][11]);
    //console.log(nWord + 1);
    word_txt.setText(word);
    words_resp.keys = undefined;
    words_resp.rt = undefined;
    _words_resp_allKeys = [];
    // keep track of which components have finished
    wordsComponents = [];
    wordsComponents.push(word_txt);
    wordsComponents.push(words_resp);
    
    for (const thisComponent of wordsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function wordsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'words'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = wordsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *word_txt* updates
    if (t >= 0.0 && word_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      word_txt.tStart = t;  // (not accounting for frame time here)
      word_txt.frameNStart = frameN;  // exact frame index
      
      word_txt.setAutoDraw(true);
    }

    
    // *words_resp* updates
    if (t >= 0.0 && words_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      words_resp.tStart = t;  // (not accounting for frame time here)
      words_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { words_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { words_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { words_resp.clearEvents(); });
    }

    if (words_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = words_resp.getKeys({keyList: ['space'], waitRelease: false});
      _words_resp_allKeys = _words_resp_allKeys.concat(theseKeys);
      if (_words_resp_allKeys.length > 0) {
        words_resp.keys = _words_resp_allKeys[_words_resp_allKeys.length - 1].name;  // just the last key pressed
        words_resp.rt = _words_resp_allKeys[_words_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of wordsComponents)
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


function wordsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'words'-------
    for (const thisComponent of wordsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('words_resp.keys', words_resp.keys);
    if (typeof words_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('words_resp.rt', words_resp.rt);
        routineTimer.reset();
        }
    
    words_resp.stop();
    // the Routine "words" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _question_resp_allKeys;
var questionComponents;
function questionRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'question'-------
    t = 0;
    questionClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    question_resp.keys = undefined;
    question_resp.rt = undefined;
    _question_resp_allKeys = [];
    auxOut1 = condList[nRow][0]; 
    trials.addData("nSent", auxOut1);
    auxOut2 = condList[nRow][1]; 
    trials.addData("condition", auxOut2);
    // keep track of which components have finished
    questionComponents = [];
    questionComponents.push(item_check);
    questionComponents.push(question_resp);
    questionComponents.push(yes_rect);
    questionComponents.push(no_rect);
    questionComponents.push(yes);
    questionComponents.push(no);
    
    for (const thisComponent of questionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function questionRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'question'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = questionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *item_check* updates
    if (t >= 0.0 && item_check.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      item_check.tStart = t;  // (not accounting for frame time here)
      item_check.frameNStart = frameN;  // exact frame index
      
      item_check.setAutoDraw(true);
    }

    
    // *question_resp* updates
    if (t >= 0.0 && question_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      question_resp.tStart = t;  // (not accounting for frame time here)
      question_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { question_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { question_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { question_resp.clearEvents(); });
    }

    if (question_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = question_resp.getKeys({keyList: ['p', 'q'], waitRelease: false});
      _question_resp_allKeys = _question_resp_allKeys.concat(theseKeys);
      if (_question_resp_allKeys.length > 0) {
        question_resp.keys = _question_resp_allKeys[0].name;  // just the first key pressed
        question_resp.rt = _question_resp_allKeys[0].rt;
        // was this correct?
        if (question_resp.keys == corrAns) {
            question_resp.corr = 1;
        } else {
            question_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *yes_rect* updates
    if (t >= 0.0 && yes_rect.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      yes_rect.tStart = t;  // (not accounting for frame time here)
      yes_rect.frameNStart = frameN;  // exact frame index
      
      yes_rect.setAutoDraw(true);
    }

    
    // *no_rect* updates
    if (t >= 0.0 && no_rect.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      no_rect.tStart = t;  // (not accounting for frame time here)
      no_rect.frameNStart = frameN;  // exact frame index
      
      no_rect.setAutoDraw(true);
    }

    
    // *yes* updates
    if (t >= 0.0 && yes.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      yes.tStart = t;  // (not accounting for frame time here)
      yes.frameNStart = frameN;  // exact frame index
      
      yes.setAutoDraw(true);
    }

    
    // *no* updates
    if (t >= 0.0 && no.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      no.tStart = t;  // (not accounting for frame time here)
      no.frameNStart = frameN;  // exact frame index
      
      no.setAutoDraw(true);
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
    // was no response the correct answer?!
    if (question_resp.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         question_resp.corr = 1;  // correct non-response
      } else {
         question_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('question_resp.keys', question_resp.keys);
    psychoJS.experiment.addData('question_resp.corr', question_resp.corr);
    if (typeof question_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('question_resp.rt', question_resp.rt);
        routineTimer.reset();
        }
    
    question_resp.stop();
    // the Routine "question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _rating_resp_allKeys;
var ratingComponents;
function ratingRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'rating'-------
    t = 0;
    ratingClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    rating_resp.keys = undefined;
    rating_resp.rt = undefined;
    _rating_resp_allKeys = [];
    // keep track of which components have finished
    ratingComponents = [];
    ratingComponents.push(rating_question);
    ratingComponents.push(rect1);
    ratingComponents.push(rect2);
    ratingComponents.push(rect3);
    ratingComponents.push(rect4);
    ratingComponents.push(rect5);
    ratingComponents.push(g1);
    ratingComponents.push(g2);
    ratingComponents.push(g3);
    ratingComponents.push(g4);
    ratingComponents.push(g5);
    ratingComponents.push(rating_resp);
    ratingComponents.push(NadaSeguro);
    ratingComponents.push(MuySeguro);
    
    for (const thisComponent of ratingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function ratingRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'rating'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ratingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rating_question* updates
    if (t >= 0.0 && rating_question.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rating_question.tStart = t;  // (not accounting for frame time here)
      rating_question.frameNStart = frameN;  // exact frame index
      
      rating_question.setAutoDraw(true);
    }

    
    // *rect1* updates
    if (t >= 0.0 && rect1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rect1.tStart = t;  // (not accounting for frame time here)
      rect1.frameNStart = frameN;  // exact frame index
      
      rect1.setAutoDraw(true);
    }

    
    // *rect2* updates
    if (t >= 0.0 && rect2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rect2.tStart = t;  // (not accounting for frame time here)
      rect2.frameNStart = frameN;  // exact frame index
      
      rect2.setAutoDraw(true);
    }

    
    // *rect3* updates
    if (t >= 0.0 && rect3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rect3.tStart = t;  // (not accounting for frame time here)
      rect3.frameNStart = frameN;  // exact frame index
      
      rect3.setAutoDraw(true);
    }

    
    // *rect4* updates
    if (t >= 0.0 && rect4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rect4.tStart = t;  // (not accounting for frame time here)
      rect4.frameNStart = frameN;  // exact frame index
      
      rect4.setAutoDraw(true);
    }

    
    // *rect5* updates
    if (t >= 0.0 && rect5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rect5.tStart = t;  // (not accounting for frame time here)
      rect5.frameNStart = frameN;  // exact frame index
      
      rect5.setAutoDraw(true);
    }

    
    // *g1* updates
    if (t >= 0.0 && g1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      g1.tStart = t;  // (not accounting for frame time here)
      g1.frameNStart = frameN;  // exact frame index
      
      g1.setAutoDraw(true);
    }

    
    // *g2* updates
    if (t >= 0.0 && g2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      g2.tStart = t;  // (not accounting for frame time here)
      g2.frameNStart = frameN;  // exact frame index
      
      g2.setAutoDraw(true);
    }

    
    // *g3* updates
    if (t >= 0.0 && g3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      g3.tStart = t;  // (not accounting for frame time here)
      g3.frameNStart = frameN;  // exact frame index
      
      g3.setAutoDraw(true);
    }

    
    // *g4* updates
    if (t >= 0.0 && g4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      g4.tStart = t;  // (not accounting for frame time here)
      g4.frameNStart = frameN;  // exact frame index
      
      g4.setAutoDraw(true);
    }

    
    // *g5* updates
    if (t >= 0.0 && g5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      g5.tStart = t;  // (not accounting for frame time here)
      g5.frameNStart = frameN;  // exact frame index
      
      g5.setAutoDraw(true);
    }

    
    // *rating_resp* updates
    if (t >= 0.0 && rating_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rating_resp.tStart = t;  // (not accounting for frame time here)
      rating_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rating_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rating_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rating_resp.clearEvents(); });
    }

    if (rating_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = rating_resp.getKeys({keyList: ['1', '2', '3', '4', '5'], waitRelease: false});
      _rating_resp_allKeys = _rating_resp_allKeys.concat(theseKeys);
      if (_rating_resp_allKeys.length > 0) {
        rating_resp.keys = _rating_resp_allKeys[_rating_resp_allKeys.length - 1].name;  // just the last key pressed
        rating_resp.rt = _rating_resp_allKeys[_rating_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *NadaSeguro* updates
    if (t >= 0.0 && NadaSeguro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      NadaSeguro.tStart = t;  // (not accounting for frame time here)
      NadaSeguro.frameNStart = frameN;  // exact frame index
      
      NadaSeguro.setAutoDraw(true);
    }

    
    // *MuySeguro* updates
    if (t >= 0.0 && MuySeguro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MuySeguro.tStart = t;  // (not accounting for frame time here)
      MuySeguro.frameNStart = frameN;  // exact frame index
      
      MuySeguro.setAutoDraw(true);
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
    for (const thisComponent of ratingComponents)
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


var pausa_msg;
function ratingRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'rating'-------
    for (const thisComponent of ratingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('rating_resp.keys', rating_resp.keys);
    if (typeof rating_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rating_resp.rt', rating_resp.rt);
        routineTimer.reset();
        }
    
    rating_resp.stop();
    // checking end of training
    if ((nRow === trialsTraining - 1)) {
        modePract = true;
        nTrial = 0;
    }
    
    // checking pause
    if ((nTrial > 1)) {
        if (((nTrial % nPausa) === 0)) {
            pausa_msg = 'PAUSA';
            modePausa = true;
        }
    }
    
    // checking end of task
    if ((nRow === condList.length - 1)){
         pausa_msg = '¡Ya has acabado!\nGracias por tu participación.\n\n Pulsa la barra de ESPACIO para acabar';
         modePausa = true;
         modeInter = false;
    }     
    // the Routine "rating" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _pausa_resp_allKeys;
var pausaComponents;
function pausaRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'pausa'-------
    t = 0;
    pausaClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    pausa_txt.setText(pausa_msg);
    pausa_resp.keys = undefined;
    pausa_resp.rt = undefined;
    _pausa_resp_allKeys = [];
    // keep track of which components have finished
    pausaComponents = [];
    pausaComponents.push(pausa_txt);
    pausaComponents.push(pausa_resp);
    
    for (const thisComponent of pausaComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function pausaRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'pausa'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = pausaClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pausa_txt* updates
    if (t >= 1 && pausa_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pausa_txt.tStart = t;  // (not accounting for frame time here)
      pausa_txt.frameNStart = frameN;  // exact frame index
      
      pausa_txt.setAutoDraw(true);
    }

    
    // *pausa_resp* updates
    if (t >= 1 && pausa_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pausa_resp.tStart = t;  // (not accounting for frame time here)
      pausa_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { pausa_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { pausa_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { pausa_resp.clearEvents(); });
    }

    if (pausa_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = pausa_resp.getKeys({keyList: ['space'], waitRelease: false});
      _pausa_resp_allKeys = _pausa_resp_allKeys.concat(theseKeys);
      if (_pausa_resp_allKeys.length > 0) {
        pausa_resp.keys = _pausa_resp_allKeys[_pausa_resp_allKeys.length - 1].name;  // just the last key pressed
        pausa_resp.rt = _pausa_resp_allKeys[_pausa_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of pausaComponents)
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


function pausaRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'pausa'-------
    for (const thisComponent of pausaComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('pausa_resp.keys', pausa_resp.keys);
    if (typeof pausa_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('pausa_resp.rt', pausa_resp.rt);
        routineTimer.reset();
        }
    
    pausa_resp.stop();
    modePausa = false;
    
    // the Routine "pausa" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _pract_resp_allKeys;
var check_practComponents;
function check_practRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'check_pract'-------
    t = 0;
    check_practClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    pract_resp.keys = undefined;
    pract_resp.rt = undefined;
    _pract_resp_allKeys = [];
    // keep track of which components have finished
    check_practComponents = [];
    check_practComponents.push(pract_txt);
    check_practComponents.push(pract_resp);
    
    for (const thisComponent of check_practComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function check_practRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'check_pract'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = check_practClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pract_txt* updates
    if (t >= 1.0 && pract_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pract_txt.tStart = t;  // (not accounting for frame time here)
      pract_txt.frameNStart = frameN;  // exact frame index
      
      pract_txt.setAutoDraw(true);
    }

    
    // *pract_resp* updates
    if (t >= 1.0 && pract_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pract_resp.tStart = t;  // (not accounting for frame time here)
      pract_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { pract_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { pract_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { pract_resp.clearEvents(); });
    }

    if (pract_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = pract_resp.getKeys({keyList: ['space'], waitRelease: false});
      _pract_resp_allKeys = _pract_resp_allKeys.concat(theseKeys);
      if (_pract_resp_allKeys.length > 0) {
        pract_resp.keys = _pract_resp_allKeys[_pract_resp_allKeys.length - 1].name;  // just the last key pressed
        pract_resp.rt = _pract_resp_allKeys[_pract_resp_allKeys.length - 1].rt;
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
    for (const thisComponent of check_practComponents)
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


function check_practRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'check_pract'-------
    for (const thisComponent of check_practComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('pract_resp.keys', pract_resp.keys);
    if (typeof pract_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('pract_resp.rt', pract_resp.rt);
        routineTimer.reset();
        }
    
    pract_resp.stop();
    modePract = false;
    
    // the Routine "check_pract" was not non-slip safe, so reset the non-slip timer
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
    // update component parameters for each repeat
    // keep track of which components have finished
    intertrialComponents = [];
    intertrialComponents.push(inter_img);
    
    for (const thisComponent of intertrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
  };
}


function intertrialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'intertrial'-------
    let continueRoutine = true; // until we're told otherwise
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
    if ((inter_img.status === PsychoJS.Status.STARTED || inter_img.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
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
