clc
clear all
load END_GRAM_SYNpval_grid
load T_END_GRAM_SYN

%load CORR_GRAMpval_grid
%load CORR_SYNpval_grid
%load SEM_GRAMpval_grid
%load SEM_SYNpval_grid
%load GRAM_SYNpval_grid

%load T_Corr_GRAM
%load T_Corr_SYN
%load T_SEM_GRAM
%load T_SEM_SYN
%load T_GRAM_SYN


%% T_obs


% Logical matrix indicating significant clusters
sig_clusters = END_GRAM_SYNpval_grid{1};

% Matrix of t-values
t_vals = T_END_GRAM_SYN;

% Identify and label the connected components in the significant clusters
CC = bwconncomp(sig_clusters);

% Initialize a vector to store the T_obs values for each significant cluster
T_obs = zeros(CC.NumObjects, 1);

% Loop over the significant clusters
for i = 1:CC.NumObjects
    % Get the linear indices for the current cluster
    lin_indices = CC.PixelIdxList{i};
    
    % Get the t-values for the current cluster
    t_vals_cluster = t_vals(lin_indices);
    
    % Find the sum of the t-values for the current cluster
    T_obs(i) = sum(t_vals_cluster(:));
end
%% Cluster size

cluster_sizes = cellfun(@numel, CC.PixelIdxList);
