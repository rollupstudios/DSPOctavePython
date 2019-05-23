% sine wave generator
% vasantha kumar
% 23-May-2019

% Function to generate a sinewave
% Inputs :  Signal Frequency, Sampling Frequency, DC Offset
%           Amplitude, Phase Shift, No of cycles
% Outputs : Signal Plotting
% return value : 1

function return_val = Fsine(f, fs, dcoffset, amplitude, phaseshift, nc)

  % creates the time stamps
  t = 0:1/fs:nc*1/f;

  % generates the sine signal vector
  x = dcoffset + (amplitude * sin(2*pi*f*t + phaseshift));

  % plotting the signal in time domain
  figure;
  subplot(211);
  plot(t, x);
  title(['Signal Time Domain Plot with f = ', num2str(f) , ' and fs = ' , num2str(fs)]);
  ylabel('Amplitude');
  xlabel('Time (s)');
  grid on;

  % calculates the spectrum of the signal
  N = 1024;
  X = fft(x, N);
  Px = X .* conj(X) / (N * length(x));
  fvals = fs * (0:1:N/2-1) / N;

  % plotting the signal in frequency domain
  subplot(212);
  plot(fvals, Px(1:N/2))
  title(['Signal Frequency Domain Plot with f = ' , num2str(f) , ' and fs = ' , num2str(fs)]);
  ylabel('PSD');
  xlabel('Frequency(Hz)');
  grid on;

  % assigns return value
  return_val = 1;

endfunction