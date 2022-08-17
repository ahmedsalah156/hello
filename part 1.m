% time axix
fm=400;
fs=150*fm;
ts=1/fs;
t=-2.5*10^-3:ts:2.5*10^-3;

% the messsage signal
ym=2*sinc(200*t).^2+sinc(400*t).^2;
figure(1);
plot(t,ym);

% frequency domain
ym_f=fft(ym)*ts;
ym_f=fftshift(ym_f);
n= length(t);
if rem(n,2)
f= fs/n* ( -(n-1)/2 : (n-1)/2 );
else
f= fs/n* ( -(n/2) : (n/2 - 1) );
end
figure(2);
%xlabel('fre')
plot(f,abs(ym_f));

% carrier
yc=cos(20000*2*pi*t);
yc_f=fft(yc)*ts;
yc_f=fftshift(yc_f);
figure(3);
plot(f,abs(yc_f));

%modulation

y=(1+.75*ym).*yc;
y1=(1+.75*ym);
hold on;
plot(t,y);
plot(t,y1);
hold on;
y_f=fft(y).*ts;
y_f=fftshift(y_f);
figure(4);
xlabel('fre');
plot(f,abs(y_f));
figure(5);
specgram(y);
