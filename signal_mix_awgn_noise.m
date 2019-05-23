% applies a awgn noise on chosen wave file
% vasantha kumar
% 23-May-2019

% Function to apply a awgn noise on chosen wave file
% Inputs :  input wave file,SNR in dB
% Outputs : plots the awgn noise applied wave
% return value : 1

function return_val = signal_mix_awgn_noise(wavefilename, snr)

  % loads necessary package
  pkg load communications;
  
  % reads the input wave file and extract required data
  [x, fs, nbits] = wavread(wavefilename);
  dt = 1/fs;
  t = 0:dt:(length(x)*dt)-dt;

  % calculates the spectrum of the signal
  N = 1024;
  X = fft(x, N);
  Px = X .* conj(X) / (N * length(x));
  fvalsx = fs * (0:1:N/2-1) / N;
  
  % applies noise on signal
  y = awgn(x, snr);  

  % calculates the spectrum of the noise added signal  
  N = 1024;
  Y = fft(y, N);
  Py = Y .* conj(Y) / (N * length(y));
  fvalsy = fs * (0:1:N/2-1) / N;
  
  % plotting the signal in time domain
  ax(1) = subplot (221);
  set (ax(1), "tag", "1");
  plot(t,x);
  title (["Signal Time Domain plot with fs = ", num2str(fs)]);
  xlabel "Time(s)";
  ylabel "Amplitude";
 
  % plotting the signal in frequnecy domain
  ax(2) = subplot (222);
  set (ax(2), "tag", "2");
  plot(fvalsx, Px(1:N/2));
  title (["Signal Frequency Domain plot with fs = ", num2str(fs)]);
  xlabel "Frequency(Hz)";
  ylabel "PSD";

  % plotting the noisy signal in time domain
  ax(2) = subplot (223);
  set (ax(2), "tag", "2");
  plot(t,y);
  title (["Noisy Signal Time Domain plot with fs = ", num2str(fs), " snr = ", num2str(snr)]);
  xlabel "Time(s)";
  ylabel "Amplitude";

  % plotting the noisy signal in frequnecy domain
  ax(2) = subplot (224);
  set (ax(2), "tag", "2");
  plot(fvalsy, Py(1:N/2))
  title (["Noisy Signal Frequency Domain plot with fs = ", num2str(fs), " snr = ", num2str(snr)]);
  xlabel "Frequency(Hz)";
  ylabel "PSD";
  
  % assigns return value
  return_val = 1;
  
endfunction