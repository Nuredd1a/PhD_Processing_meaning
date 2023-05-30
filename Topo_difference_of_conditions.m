
clear all
clc
eeglab
%% load STUDY
[STUDY ALLEEG] = pop_loadstudy('filename', 'KW_030223.study', 'filepath', 'C:\Users\clara\OneDrive\Escritorio\EEG ES\Analysis\EEG\DATA\Studies\KW_34_suj_clean\KW_ERP_070223\');
CURRENTSTUDY = 1; EEG = ALLEEG; CURRENTSET = [1:length(EEG)];
eeglab redraw;
%% Precompute channel measures
%[STUDY, ALLEEG] = std_precomp(STUDY, ALLEEG, {},'savetrials','on','interp','on','recompute','on','erp','on','erpparams',{'rmbase',[-100 0] });
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
%% CORR-SEM erpdata difference
%CORRECT erpdata
STUDY = std_selectdesign(STUDY, ALLEEG, 8);
STUDY = pop_erpparams(STUDY, 'averagechan','off'); 
%extrec erpdata de condició CORR
[STUDY erpdata] = std_erpplot(STUDY,ALLEEG,'channels',{'Fp1','Fz','F3','F7','FT9','FC5','FC1','C3','T7','CP5','CP1','Pz','P3','P7','O1','Eye','O2','P4','P8','CP6','CP2','Cz','C4','TP8','FT10','FC6','FC2','F4','F8','Fp2'}, 'design', 8);
CORR_ERPdata = erpdata{1};
%grandaverage
grand_averageCorrect = mean(CORR_ERPdata, 3);

%SEMANTIC erpdata
STUDY = std_selectdesign(STUDY, ALLEEG, 9);
STUDY = pop_erpparams(STUDY, 'averagechan','off'); 
%extrec erpdata de condició SEM
[STUDY erpdata] = std_erpplot(STUDY,ALLEEG,'channels',{'Fp1','Fz','F3','F7','FT9','FC5','FC1','C3','T7','CP5','CP1','Pz','P3','P7','O1','Eye','O2','P4','P8','CP6','CP2','Cz','C4','TP8','FT10','FC6','FC2','F4','F8','Fp2'}, 'design', 9);
SEM_ERPdata = erpdata{1};
grand_averageSEM = mean(SEM_ERPdata, 3);

%DIFERENCE
Diff_CORR_SEM = grand_averageCorrect - grand_averageSEM;
Diff_SEM_CORR = grand_averageSEM - grand_averageCorrect
save Diff_CORR_SEM Diff_CORR_SEM
save Diff_SEM_CORR Diff_SEM_CORR
%% CORR - GRAM ERP data difference
%GRAM erpdata
STUDY = std_selectdesign(STUDY, ALLEEG, 10);
STUDY = pop_erpparams(STUDY, 'averagechan','off'); 
%extrec erpdata de condició GRAM
[STUDY erpdata] = std_erpplot(STUDY,ALLEEG,'channels',{'Fp1','Fz','F3','F7','FT9','FC5','FC1','C3','T7','CP5','CP1','Pz','P3','P7','O1','Eye','O2','P4','P8','CP6','CP2','Cz','C4','TP8','FT10','FC6','FC2','F4','F8','Fp2'}, 'design', 10);
GRAM_ERPdata = erpdata{1};
grand_averageGRAM = mean(GRAM_ERPdata, 3);

Diff_CORR_GRAM = grand_averageCorrect - grand_averageGRAM;
Diff_GRAM_CORR = grand_averageGRAM - grand_averageCorrect
save Diff_CORR_GRAM Diff_CORR_GRAM
save Diff_GRAM_CORR Diff_GRAM_CORR
%% CORR - SYN ERP data diference

%SYN erpdata
STUDY = std_selectdesign(STUDY, ALLEEG, 11);
STUDY = pop_erpparams(STUDY, 'averagechan','off'); 
%extrec erpdata de condició GRAM
[STUDY erpdata] = std_erpplot(STUDY,ALLEEG,'channels',{'Fp1','Fz','F3','F7','FT9','FC5','FC1','C3','T7','CP5','CP1','Pz','P3','P7','O1','Eye','O2','P4','P8','CP6','CP2','Cz','C4','TP8','FT10','FC6','FC2','F4','F8','Fp2'}, 'design', 11);
SYN_ERPdata = erpdata{1};
grand_averageSYN = mean(SYN_ERPdata, 3);

Diff_CORR_SYN = grand_averageCorrect -  grand_averageSYN;
Diff_SYN_CORR = grand_averageSYN -  grand_averageCorrect
save Diff_CORR_SYN Diff_CORR_SYN
save Diff_SYN_CORR Diff_SYN_CORR
%% SEM-GRAM, SEM-SYN, GRAM-SYN Differences

Diff_SEM_GRAM = grand_averageSEM - grand_averageGRAM
Diff_SEM_GRAM = Diff_SEM_GRAM;
save Diff_SEM_GRAM Diff_SEM_GRAM


%% Load Diff datasets

load Diff_SEM_CORR
load Diff_GRAM_CORR
load Diff_SYN_CORR
load Diff_SEM_GRAM

%% Topography
erp_data = Diff_SEM_GRAM


t_start = 0.350 % start time in seconds
t_end = 0.550 % end time in seconds

% Get the indices (finding time range in the corresponding samples)
start_idx = t_start * 250 + 1;
end_idx = t_end * 250;

% Remove baseline (from 1 to 25 saples)
erp_data = erp_data(25:end,:);

% single vector of electrode values for the selected time range
data_topo = mean(erp_data(start_idx:end_idx,:), 1)
data_topo = data_topo'

% Plot the scalp topography
figure;
topoplot( data_topo, 'templete_chanloc.ced', 'maplimits', 'maxmin', 'electrodes', 'labels')%?
colormap(jet); % Set the colormap (jet is a commonly used colormap)
colorbar; % Add the colorbar to the plot
caxis([-3 3]); % Set the color axis limits (you can adjust this based on your data)
title('Lexical-Grammatical (350-550 ms)'); % Add a title to the plot

%figure;
%topoplot( data_topo, 'templete_chanloc.ced', 'style', 'contour', 'style', 'blank', 'electrodes', 'labels', 'electrodes', 'ptslabels')%?
%title('Montage'); % Add a title to the plot

