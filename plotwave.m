% plots the time and frequency data of a chosen wave file
% vasantha kumar
% 23-May-2019

% Function to plot the time and frequency data of a chosen wave file
% Inputs :  Chosen wave file name
% Outputs : plots the time and frequency data of a chosen wave file
% return value : 1

function return_val = plotwave(wavefilename)

  % reads the input wave file and extract required data
  [x, fs, nbits] = wavread(wavefilename);  
  dt = 1/fs;  
  t = 0:dt:(length(x)*dt)-dt;
  
  % plotting the signal in time domain  
  subplot(211)
  plot(t,x); 
  xlabel('Time (s)'); 
  ylabel('Amplitude'); 
  title('Signal Time Domain Plot');
  grid on;
  
   % calculates the spectrum of the signal  
  N = 1024;
  X = fft(x, N);
  Px = X .* conj(X) / (N * length(x));
  fvals = fs * (0:1:N/2-1) / N;

  % plotting the signal in frequency domain
  subplot(212);
  plot(fvals, Px(1:N/2))
  title('Signal Frequency Domain Plot');
  ylabel('PSD');
  xlabel('Frequency(Hz)');
  grid on;  
  
  % assigns return value
  return_val = 1;

endfunction