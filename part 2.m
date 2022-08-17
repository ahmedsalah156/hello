clc;
clear all;
% time axix
fm=400;
fs=150*fm;
ts=1/fs;
t=-2.5*10^-3:ts:2.5*10^-3;

% the messsage signal in time domain
ym=2*sinc(200*t).^2+sinc(400*t).^2;
figure(1);
plot(t,ym);

% frequency domain
ym_f=fft(ym)*ts;
ym_f=fftshift(ym_f);

%calculating the frequency axix
n= length(t);
if rem(n,2)
f= fs/n* ( -(n-1)/2 : (n-1)/2 );
else
f= fs/n* ( -(n/2) : (n/2 - 1) );
end

%ploting message in freq domain
figure(2);
xlabel('fre')
plot(f,abs(ym_f));

% carrier
yc=cos(20000*2*pi*t);
yc_f=fft(yc)*ts;
yc_f=fftshift(yc_f);
figure(3);
plot(f,abs(yc_f));

%modulation

y_am=(1+0.75*ym).*yc;
y1_am=(1+0.75*ym);
figure(4);
hold on;
plot(t,y_am);
plot(t,y1_am);
hold on;

%spectrum of AM
y_f_am=fft(y_am).*ts;
y_f_am=fftshift(y_f_am);
figure(5);
plot(f,abs(y_f_am));

%spectrogram
figure(6);
specgram(y_am);

%spectrum od DSB-SC
y=(0.75*ym).*yc;
y1=(0.75*ym);
figure(7);
hold on;
plot(t,y);
plot(t,y1);
hold on;
y_f=fft(y).*ts;
y_f=fftshift(y_f);
figure(8);
xlabel('fre');
plot(f,abs(y_f));

%spectrogram os DSB-SC
figure(9);
specgram(y);

