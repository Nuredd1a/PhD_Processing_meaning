clear all
clc
eeglab
%% load STUDY
[STUDY ALLEEG] = pop_loadstudy('filename', 'KW_030223.study', 'filepath', 'C:\Users\clara\OneDrive\Escritorio\EEG ES\Analysis\EEG\DATA\Studies\KW_34_suj_clean\KW_ERP_070223\');
CURRENTSTUDY = 1; EEG = ALLEEG; CURRENTSET = [1:length(EEG)];
eeglab redraw;
%% Make study designs
STUDY = std_makedesign(STUDY, ALLEEG, 1, 'name','STUDY.design 1','delfiles','off','defaultdesign','off','variable1','condition','values1',{'CORR','GRAM','SEM','SYN'},'vartype1','categorical','subjselect',{'S01','S02','S03','S04','S05','S06','S07','S08','S09','S10','S11','S12','S15','S16','S17','S18','S19','S20','S22','S23','S24','S25','S26','S28','S29','S30','S31','S32','S33'});
STUDY = std_makedesign(STUDY, ALLEEG, 2, 'name','Corr_Sem','delfiles','off','defaultdesign','off','variable1','condition','values1',{'CORR','SEM'},'vartype1','categorical','subjselect',{'S01','S02','S03','S04','S05','S06','S07','S08','S09','S10','S11','S12','S15','S16','S17','S18','S19','S20','S22','S23','S24','S25','S26','S28','S29','S30','S31','S32','S33'});
STUDY = std_makedesign(STUDY, ALLEEG, 3, 'name','Corr_Gram','delfiles','off','defaultdesign','off','variable1','condition','values1',{'CORR','GRAM'},'vartype1','categorical','subjselect',{'S01','S02','S03','S04','S05','S06','S07','S08','S09','S10','S11','S12','S15','S16','S17','S18','S19','S20','S22','S23','S24','S25','S26','S28','S29','S30','S31','S32','S33'});
STUDY = std_makedesign(STUDY, ALLEEG, 4, 'name','Corr_Syn','delfiles','off','defaultdesign','off','variable1','condition','values1',{'CORR','SYN'},'vartype1','categorical','subjselect',{'S01','S02','S03','S04','S05','S06','S07','S08','S09','S10','S11','S12','S15','S16','S17','S18','S19','S20','S22','S23','S24','S25','S26','S28','S29','S30','S31','S32','S33'});
STUDY = std_makedesign(STUDY, ALLEEG, 5, 'name','Sem_Gram','delfiles','off','defaultdesign','off','variable1','condition','values1',{'SEM','GRAM'},'vartype1','categorical','subjselect',{'S01','S02','S03','S04','S05','S06','S07','S08','S09','S10','S11','S12','S15','S16','S17','S18','S19','S20','S22','S23','S24','S25','S26','S28','S29','S30','S31','S32','S33'});
STUDY = std_makedesign(STUDY, ALLEEG, 6, 'name','Sem_Syn','delfiles','off','defaultdesign','off','variable1','condition','values1',{'SEM','SYN'},'vartype1','categorical','subjselect',{'S01','S02','S03','S04','S05','S06','S07','S08','S09','S10','S11','S12','S15','S16','S17','S18','S19','S20','S22','S23','S24','S25','S26','S28','S29','S30','S31','S32','S33'});
STUDY = std_makedesign(STUDY, ALLEEG, 7, 'name','Gram_Syn','delfiles','off','defaultdesign','off','variable1','condition','values1',{'GRAM','SYN'},'vartype1','categorical','subjselect',{'S01','S02','S03','S04','S05','S06','S07','S08','S09','S10','S11','S12','S15','S16','S17','S18','S19','S20','S22','S23','S24','S25','S26','S28','S29','S30','S31','S32','S33'});

% Single conditions stored as designs to later substract the topographies
STUDY = std_makedesign(STUDY, ALLEEG, 8, 'name','Correct','delfiles','off','defaultdesign','off','variable1','condition','values1',{'CORR'},'vartype1','categorical','subjselect',{'S01','S02','S03','S04','S05','S06','S07','S08','S09','S10','S11','S12','S15','S16','S17','S18','S19','S20','S22','S23','S24','S25','S26','S28','S29','S30','S31','S32','S33'});
STUDY = std_makedesign(STUDY, ALLEEG, 9, 'name','Semantic','delfiles','off','defaultdesign','off','variable1','condition','values1',{'SEM'},'vartype1','categorical','subjselect',{'S01','S02','S03','S04','S05','S06','S07','S08','S09','S10','S11','S12','S15','S16','S17','S18','S19','S20','S22','S23','S24','S25','S26','S28','S29','S30','S31','S32','S33'});
STUDY = std_makedesign(STUDY, ALLEEG, 10, 'name','Grammatical','delfiles','off','defaultdesign','off','variable1','condition','values1',{'GRAM'},'vartype1','categorical','subjselect',{'S01','S02','S03','S04','S05','S06','S07','S08','S09','S10','S11','S12','S15','S16','S17','S18','S19','S20','S22','S23','S24','S25','S26','S28','S29','S30','S31','S32','S33'});
STUDY = std_makedesign(STUDY, ALLEEG, 11, 'name','Syntactic','delfiles','off','defaultdesign','off','variable1','condition','values1',{'SYN'},'vartype1','categorical','subjselect',{'S01','S02','S03','S04','S05','S06','S07','S08','S09','S10','S11','S12','S15','S16','S17','S18','S19','S20','S22','S23','S24','S25','S26','S28','S29','S30','S31','S32','S33'});
[STUDY EEG] = pop_savestudy( STUDY, EEG, 'savemode','resave'); 
%% Precompute channel measures
%[STUDY, ALLEEG] = std_precomp(STUDY, ALLEEG, {},'savetrials','on','interp','on','recompute','on','erp','on','erpparams',{'rmbase',[-100 0] });
%% General ERP plot all channels 4 conditions
STUDY = std_selectdesign(STUDY, ALLEEG, 1);
STUDY = pop_erpparams(STUDY, 'averagechan','off'); 
[STUDY erpdata] = std_erpplot(STUDY,ALLEEG,'channels',{'Fp1','Fz','F3','F7','FT9','FC5','FC1','C3','T7','CP5','CP1','Pz','P3','P7','O1','Eye','O2','P4','P8','CP6','CP2','Cz','C4','TP8','FT10','FC6','FC2','F4','F8','Fp2'}, 'design', 1);

%9 Region plots 4 conditions
STUDY = pop_erpparams(STUDY, 'averagechan','on'); 
[STUDY] = std_erpplot(STUDY, ALLEEG, 'channels', {'Fp1', 'Fp2', 'Fz'}, 'design', 1);
[STUDY] = std_erpplot(STUDY, ALLEEG, 'channels', {'F7', 'FC5'}, 'design', 1);
[STUDY] = std_erpplot(STUDY, ALLEEG, 'channels', {'F8', 'FC6'}, 'design', 1);
[STUDY] = std_erpplot(STUDY, ALLEEG, 'channels', {'F3', 'FC1', 'C3'}, 'design', 1);
[STUDY] = std_erpplot(STUDY, ALLEEG, 'channels', {'Cz', 'CP1', 'Pz', 'CP2'}, 'design', 1);
[STUDY] = std_erpplot(STUDY, ALLEEG, 'channels', {'F4', 'FC2', 'C4'}, 'design', 1);
[STUDY] = std_erpplot(STUDY, ALLEEG, 'channels', {'CP5', 'P7', 'P3'}, 'design', 1);
[STUDY] = std_erpplot(STUDY, ALLEEG, 'channels', {'O1', 'O2'}, 'design', 1);
[STUDY] = std_erpplot(STUDY, ALLEEG, 'channels', {'CP6', 'P4', 'P8'}, 'design', 1);

eeglab redraw;
% General plot per sections? 
%% CORR vs SEM -ERPs
STUDY = std_selectdesign(STUDY, ALLEEG, 2);

%logical pvalue (aplha = 0.05), 10000 perm
STUDY = pop_statparams(STUDY, 'effect','main','groupstats','off','mode','fieldtrip','fieldtripmethod','montecarlo','fieldtripmcorrect','cluster','fieldtripclusterparam','''clusterstatistic'',''maxsum''');
STUDY = pop_statparams(STUDY, 'fieldtripnaccu',10000,'fieldtripalpha',0.05);
STUDY = pop_erpparams(STUDY, 'averagechan','off'); 
[STUDY erpdata erptimes pgroup pcond pinter] = std_erpplot(STUDY,ALLEEG,'channels',{'Fp1','Fz','F3','F7','FT9','FC5','FC1','C3','T7','CP5','CP1','Pz','P3','P7','O1','O2','P4','P8','CP6','CP2','Cz','C4','TP8','FT10','FC6','FC2','F4','F8','Fp2'}, 'design', 2);
%CORR_SEMpval_exact = pcond % Modify alpha: STUDY = pop_statparams(STUDY, 'fieldtripalpha',0.05); Exact pvalue that I will not save because I don't need it for the grid
CORR_SEMpval_grid = pcond 

%retrieve t
[stats] = statcond(erpdata)
T_Corr_Sem = stats

save CORR_SEMpval_grid CORR_SEMpval_grid
save T_Corr_Sem T_Corr_Sem
%% CORR v GRAM - ERPs

STUDY = std_selectdesign(STUDY, ALLEEG, 3);

%logical pvalue (aplha = 0.05), 10000 perm
STUDY = pop_statparams(STUDY, 'effect','main','groupstats','off','mode','fieldtrip','fieldtripmethod','montecarlo','fieldtripmcorrect','cluster','fieldtripclusterparam','''clusterstatistic'',''maxsum''');
STUDY = pop_statparams(STUDY, 'fieldtripnaccu',10000,'fieldtripalpha',0.05);
STUDY = pop_erpparams(STUDY, 'averagechan','off'); 
[STUDY erpdata erptimes pgroup pcond pinter] = std_erpplot(STUDY,ALLEEG,'channels',{'Fp1','Fz','F3','F7','FT9','FC5','FC1','C3','T7','CP5','CP1','Pz','P3','P7','O1','O2','P4','P8','CP6','CP2','Cz','C4','TP8','FT10','FC6','FC2','F4','F8','Fp2'}, 'design', 3);
%CORR_SEMpval_exact = pcond % Modify alpha: STUDY = pop_statparams(STUDY, 'fieldtripalpha',0.05); Exact pvalue that I will not save because I don't need it for the grid
CORR_GRAMpval_grid = pcond 

%retrieve t
[stats] = statcond(erpdata)
T_Corr_GRAM = stats

save CORR_GRAMpval_grid CORR_GRAMpval_grid
save T_Corr_GRAM T_Corr_GRAM
%% CORR vs SYN - ERPs

STUDY = std_selectdesign(STUDY, ALLEEG, 4);

%logical pvalue (aplha = 0.05), 10000 perm
STUDY = pop_statparams(STUDY, 'effect','main','groupstats','off','mode','fieldtrip','fieldtripmethod','montecarlo','fieldtripmcorrect','cluster','fieldtripclusterparam','''clusterstatistic'',''maxsum''');
STUDY = pop_statparams(STUDY, 'fieldtripnaccu',10000,'fieldtripalpha',0.05);
STUDY = pop_erpparams(STUDY, 'averagechan','off'); 
[STUDY erpdata erptimes pgroup pcond pinter] = std_erpplot(STUDY,ALLEEG,'channels',{'Fp1','Fz','F3','F7','FT9','FC5','FC1','C3','T7','CP5','CP1','Pz','P3','P7','O1','O2','P4','P8','CP6','CP2','Cz','C4','TP8','FT10','FC6','FC2','F4','F8','Fp2'}, 'design', 4);
%CORR_SYNpval_exact = pcond % Modify alpha: STUDY = pop_statparams(STUDY, 'fieldtripalpha',0.05); Exact pvalue that I will not save because I don't need it for the grid
CORR_SYNpval_grid = pcond 

%retrieve t
[stats] = statcond(erpdata);
T_Corr_SYN = stats
save CORR_SYNpval_grid CORR_SYNpval_grid
save T_Corr_SYN T_Corr_SYN
%% SEM vs GRAM - ERPs

STUDY = std_selectdesign(STUDY, ALLEEG, 5);

%logical pvalue (aplha = 0.05), 10000 perm
STUDY = pop_statparams(STUDY, 'effect','main','groupstats','off','mode','fieldtrip','fieldtripmethod','montecarlo','fieldtripmcorrect','cluster','fieldtripclusterparam','''clusterstatistic'',''maxsum''');
STUDY = pop_statparams(STUDY, 'fieldtripnaccu',10000,'fieldtripalpha',0.05);
STUDY = pop_erpparams(STUDY, 'averagechan','off'); 
[STUDY erpdata erptimes pgroup pcond pinter] = std_erpplot(STUDY,ALLEEG,'channels',{'Fp1','Fz','F3','F7','FT9','FC5','FC1','C3','T7','CP5','CP1','Pz','P3','P7','O1','O2','P4','P8','CP6','CP2','Cz','C4','TP8','FT10','FC6','FC2','F4','F8','Fp2'}, 'design', 5);
%SEM_GRAMpval_exact = pcond % Modify alpha: STUDY = pop_statparams(STUDY, 'fieldtripalpha',0.05); Exact pvalue that I will not save because I don't need it for the grid
SEM_GRAMpval_grid = pcond 

%retrieve t
[stats] = statcond(erpdata);
T_SEM_GRAM = stats
save SEM_GRAMpval_grid SEM_GRAMpval_grid
save T_SEM_GRAM T_SEM_GRAM

%% SEM vs SYN - ERPs

STUDY = std_selectdesign(STUDY, ALLEEG, 6);

%logical pvalue (aplha = 0.05), 10000 perm
STUDY = pop_statparams(STUDY, 'effect','main','groupstats','off','mode','fieldtrip','fieldtripmethod','montecarlo','fieldtripmcorrect','cluster','fieldtripclusterparam','''clusterstatistic'',''maxsum''');
STUDY = pop_statparams(STUDY, 'fieldtripnaccu',10000,'fieldtripalpha',0.05);
STUDY = pop_erpparams(STUDY, 'averagechan','off'); 
[STUDY erpdata erptimes pgroup pcond pinter] = std_erpplot(STUDY,ALLEEG,'channels',{'Fp1','Fz','F3','F7','FT9','FC5','FC1','C3','T7','CP5','CP1','Pz','P3','P7','O1','O2','P4','P8','CP6','CP2','Cz','C4','TP8','FT10','FC6','FC2','F4','F8','Fp2'}, 'design', 6);
%SEM_SYNpval_exact = pcond % Modify alpha: STUDY = pop_statparams(STUDY, 'fieldtripalpha',0.05); Exact pvalue that I will not save because I don't need it for the grid
SEM_SYNpval_grid = pcond 

%retrieve t
[stats] = statcond(erpdata)
T_SEM_SYN = stats
save SEM_SYNpval_grid SEM_SYNpval_grid
save T_SEM_SYN T_SEM_SYN

%% GRAM vs SYN - ERPs
STUDY = std_selectdesign(STUDY, ALLEEG, 7);

%logical pvalue (aplha = 0.05), 10000 perm
STUDY = pop_statparams(STUDY, 'effect','main','groupstats','off','mode','fieldtrip','fieldtripmethod','montecarlo','fieldtripmcorrect','cluster','fieldtripclusterparam','''clusterstatistic'',''maxsum''');
STUDY = pop_statparams(STUDY, 'fieldtripnaccu',10000,'fieldtripalpha',0.05);
STUDY = pop_erpparams(STUDY, 'averagechan','off'); 
[STUDY erpdata erptimes pgroup pcond pinter] = std_erpplot(STUDY,ALLEEG,'channels',{'Fp1','Fz','F3','F7','FT9','FC5','FC1','C3','T7','CP5','CP1','Pz','P3','P7','O1','O2','P4','P8','CP6','CP2','Cz','C4','TP8','FT10','FC6','FC2','F4','F8','Fp2'}, 'design', 7);
%GRAM_SYNpval_exact = pcond % Modify alpha: STUDY = pop_statparams(STUDY, 'fieldtripalpha',0.05); Exact pvalue that I will not save because I don't need it for the grid
GRAM_SYNpval_grid = pcond 

%retrieve t
%[stats] = statcond(erpdata)
T_GRAM_SYN = stats
save GRAM_SYNpval_grid GRAM_SYNpval_grid
save T_GRAM_SYN T_GRAM_SYN
%% Cluster_grid
load 'cluster_grid.m'
%% T_obs and cluster size
load T_obs_and_cluster_size.m
%% Exact p values of clusters
load exact_pvalue.m
%% Substraction topographies - new scrpt 
load Topo_difference_of_conditions.m


