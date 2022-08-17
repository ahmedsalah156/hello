clc;
clear all;


% time
f=4000;
fs=100*f;
ts=1/fs;
t=-2.5*10^-4:ts:2.5*10^-4;
taw=-5*10^-4:ts:5*10^-4;

%definition of reandom variable and process
theta=2*pi*rand(1000,1);
theta1=2*pi*rand(1,1);          %%for omly ome sample  
x=cos(2*pi*f*t + theta);
x1=cos(2*pi*f*t + theta1);
%1)
%figure(1);
%plot(t,x);

 
%2)
figure(1);
%subplot(4,1,1);  %%for each time you run it gives you a different sample to see them on the same figure just change the third numbue in subplot from 1->4
%plot(t,x1);


%3)
z=1/(2*pi)*quad(1/(2*pi)*x,0,2*pi); 
figure(2);
subplot(4,1,1);
plot(t,z);

%4)
y=mean(x1);     %%we use X1 to get the mean of only one cosine
figure(2);
subplot(4,1,3);
plot(t,y);

%5)
autocorrelation=0.5*cos(2*pi*f*taw);
%figure(3);
%lot(taw,autocorrelation);

