clear all
load Plus1_GRAM_SYNpval_grid
load chanord_noeye
%load chan_ord
%chanord_noeye = chan_ord(1:15);
%chanord_noeye(16:29) = chan_ord(17:30);
%save chanord_noeye chanord_noeye
%% 

data = Plus1_GRAM_SYNpval_grid{1};
data = data'

imagesc(data); % plot the matrix as an image
colormap([0 0 1; 1 1 0]); % yellow and blue colors
axis equal;
axis tight;
set(gca,'DataAspectRatio',[1 0.1 1]); % set the aspect ratio to 1:0.1:1
yticklabels(gca,chanord_noeye); % set the y-axis labels
set(gca,'YTick',1:length(chanord_noeye)); % set the y-axis tick locations
xticklabels(gca,-100:50:1100); % set the x-axis labels
set(gca,'XTick',0:50*275/1100:275); % set the x-axis tick locations
xlabel('Time (ms)');
ylabel('Electrodes');

ax = gca; % get the current axes
xlim = get(ax,'XLim'); % get the x-axis limits
ylim = get(ax,'YLim'); % get the y-axis limits
text(xlim(2)-diff(xlim)*0.001, mean([ylim(1),15]), ' Left Hemisphere', 'VerticalAlignment','middle');
text(xlim(2)-diff(xlim)*0.001, mean([ylim(1),45]), ' Right Hemisphere', 'VerticalAlignment','middle');
title('Grammatical - Syntactic')
hold on; % keep the current plot
x = [25 25]; % x-coordinates of the line
y = get(gca,'YLim'); % y-coordinates of the line
line(x,y,'Color','k','LineStyle','--'); % draw the line
hold off; % release the plot


hold on; % keep the current plot
x = get(gca,'XLim'); % x-coordinates of the line
y = [15.5 15.5]; % y-coordinates of the line
line(x,y,'Color','k','LineStyle','--'); % draw the line
hold off; % release the plot

