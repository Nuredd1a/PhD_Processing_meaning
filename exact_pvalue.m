clear all
clc
eeglab
%% load STUDY
[STUDY ALLEEG] = pop_loadstudy('filename', 'KW_030223.study', 'filepath', 'C:\Users\clara\OneDrive\Escritorio\EEG ES\Analysis\EEG\DATA\Studies\KW_34_suj_clean\KW_ERP_070223\');
CURRENTSTUDY = 1; EEG = ALLEEG; CURRENTSET = [1:length(EEG)];
eeglab redraw;
%% CORR vs SEM -ERPs
STUDY = std_selectdesign(STUDY, ALLEEG, 2);

STUDY = pop_statparams(STUDY, 'effect','main','groupstats','off','mode','fieldtrip','fieldtripmethod','montecarlo','fieldtripmcorrect','cluster','fieldtripclusterparam','''clusterstatistic'',''maxsum''');
STUDY = pop_statparams(STUDY, 'fieldtripnaccu',10000);
STUDY = pop_erpparams(STUDY, 'averagechan','off'); 
[STUDY erpdata erptimes pgroup pcond pinter] = std_erpplot(STUDY,ALLEEG,'channels',{'Fp1','Fz','F3','F7','FT9','FC5','FC1','C3','T7','CP5','CP1','Pz','P3','P7','O1','O2','P4','P8','CP6','CP2','Cz','C4','TP8','FT10','FC6','FC2','F4','F8','Fp2'}, 'design', 2);
CORR_SEMpval_exact = pcond % Modify alpha: STUDY = pop_statparams(STUDY, 'fieldtripalpha',0.05); Exact pvalue that I will not save because I don't need it for the grid
%CORR_SEMpval_grid = pcond 

save CORR_SEMpval_exact
%% CORR v GRAM - ERPs

STUDY = std_selectdesign(STUDY, ALLEEG, 3);


STUDY = pop_statparams(STUDY, 'effect','main','groupstats','off','mode','fieldtrip','fieldtripmethod','montecarlo','fieldtripmcorrect','cluster','fieldtripclusterparam','''clusterstatistic'',''maxsum''');
STUDY = pop_statparams(STUDY, 'fieldtripnaccu',10000);
STUDY = pop_erpparams(STUDY, 'averagechan','off'); 
[STUDY erpdata erptimes pgroup pcond pinter] = std_erpplot(STUDY,ALLEEG,'channels',{'Fp1','Fz','F3','F7','FT9','FC5','FC1','C3','T7','CP5','CP1','Pz','P3','P7','O1','O2','P4','P8','CP6','CP2','Cz','C4','TP8','FT10','FC6','FC2','F4','F8','Fp2'}, 'design', 3);
CORR_GRAMpval_exact = pcond % Modify alpha: STUDY = pop_statparams(STUDY, 'fieldtripalpha',0.05); Exact pvalue that I will not save because I don't need it for the grid

save CORR_GRAMpval_exact CORR_GRAMpval_exact
%% CORR vs SYN - ERPs

STUDY = std_selectdesign(STUDY, ALLEEG, 4);

%logical pvalue (aplha = 0.05), 10000 perm
STUDY = pop_statparams(STUDY, 'effect','main','groupstats','off','mode','fieldtrip','fieldtripmethod','montecarlo','fieldtripmcorrect','cluster','fieldtripclusterparam','''clusterstatistic'',''maxsum''');
STUDY = pop_statparams(STUDY, 'fieldtripnaccu',10000);
STUDY = pop_erpparams(STUDY, 'averagechan','off'); 
[STUDY erpdata erptimes pgroup pcond pinter] = std_erpplot(STUDY,ALLEEG,'channels',{'Fp1','Fz','F3','F7','FT9','FC5','FC1','C3','T7','CP5','CP1','Pz','P3','P7','O1','O2','P4','P8','CP6','CP2','Cz','C4','TP8','FT10','FC6','FC2','F4','F8','Fp2'}, 'design', 4);
CORR_SYNpval_exact = pcond % Modify alpha: STUDY = pop_statparams(STUDY, 'fieldtripalpha',0.05); Exact pvalue that I will not save because I don't need it for the grid

save CORR_SYNpval_exact CORR_SYNpval_exact
%% SEM vs GRAM - ERPs

STUDY = std_selectdesign(STUDY, ALLEEG, 5);

%logical pvalue (aplha = 0.05), 10000 perm
STUDY = pop_statparams(STUDY, 'effect','main','groupstats','off','mode','fieldtrip','fieldtripmethod','montecarlo','fieldtripmcorrect','cluster','fieldtripclusterparam','''clusterstatistic'',''maxsum''');
STUDY = pop_statparams(STUDY, 'fieldtripnaccu',10000);
STUDY = pop_erpparams(STUDY, 'averagechan','off'); 
[STUDY erpdata erptimes pgroup pcond pinter] = std_erpplot(STUDY,ALLEEG,'channels',{'Fp1','Fz','F3','F7','FT9','FC5','FC1','C3','T7','CP5','CP1','Pz','P3','P7','O1','O2','P4','P8','CP6','CP2','Cz','C4','TP8','FT10','FC6','FC2','F4','F8','Fp2'}, 'design', 5);
SEM_GRAMpval_exact = pcond % Modify alpha: STUDY = pop_statparams(STUDY, 'fieldtripalpha',0.05); Exact pvalue that I will not save because I don't need it for the grid


save SEM_GRAMpval_exact SEM_GRAMpval_exact

%% SEM vs SYN - ERPs

STUDY = std_selectdesign(STUDY, ALLEEG, 6);

%logical pvalue (aplha = 0.05), 10000 perm
STUDY = pop_statparams(STUDY, 'effect','main','groupstats','off','mode','fieldtrip','fieldtripmethod','montecarlo','fieldtripmcorrect','cluster','fieldtripclusterparam','''clusterstatistic'',''maxsum''');
STUDY = pop_statparams(STUDY, 'fieldtripnaccu',10000);
STUDY = pop_erpparams(STUDY, 'averagechan','off'); 
[STUDY erpdata erptimes pgroup pcond pinter] = std_erpplot(STUDY,ALLEEG,'channels',{'Fp1','Fz','F3','F7','FT9','FC5','FC1','C3','T7','CP5','CP1','Pz','P3','P7','O1','O2','P4','P8','CP6','CP2','Cz','C4','TP8','FT10','FC6','FC2','F4','F8','Fp2'}, 'design', 6);
SEM_SYNpval_exact = pcond % Modify alpha: STUDY = pop_statparams(STUDY, 'fieldtripalpha',0.05); Exact pvalue that I will not save because I don't need it for the grid

save SEM_SYNpval_exact SEM_SYNpval_exact
%% GRAM vs SYN - ERPs
STUDY = std_selectdesign(STUDY, ALLEEG, 7);

%logical pvalue (aplha = 0.05), 10000 perm
STUDY = pop_statparams(STUDY, 'effect','main','groupstats','off','mode','fieldtrip','fieldtripmethod','montecarlo','fieldtripmcorrect','cluster','fieldtripclusterparam','''clusterstatistic'',''maxsum''');
STUDY = pop_statparams(STUDY, 'fieldtripnaccu',10000);
STUDY = pop_erpparams(STUDY, 'averagechan','off'); 
[STUDY erpdata erptimes pgroup pcond pinter] = std_erpplot(STUDY,ALLEEG,'channels',{'Fp1','Fz','F3','F7','FT9','FC5','FC1','C3','T7','CP5','CP1','Pz','P3','P7','O1','O2','P4','P8','CP6','CP2','Cz','C4','TP8','FT10','FC6','FC2','F4','F8','Fp2'}, 'design', 7);
GRAM_SYNpval_exact = pcond 

save GRAM_SYNpval_exact GRAM_SYNpval_exact