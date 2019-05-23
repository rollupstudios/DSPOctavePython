% multi sine wave generator
% vasantha kumar
% 23-May-2019

% Function to generate multi sinewaves and plots
% Inputs :  Signal Frequency, Sampling Frequency, DC Offset
%           Amplitude, Phase Shift, No of cycles
% Outputs : Signal Plotting
% return value : 1

function return_val = mFsine(f, fs, dcoffset, amplitude, phaseshift, nc)

  % creates the time stamps
  t = 0:1/fs:nc*1/f(1);
  x = 0;

  % adds the signals to create a single signal
  for i=1:numel(f)
    x = x + (sin(2*pi*f(i)*t)/numel(f));
  endfor

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