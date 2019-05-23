% multi sine wave generator and saves as a single wave
% vasantha kumar
% 23-May-2019

% Function to generate multi sinewaves and saves as a single wave
% Inputs :  Signal Frequency, Sampling Frequency, DC Offset
%           Amplitude, Phase Shift, No of cycles
% Outputs : generate multi sinewaves and saves as a single wave
% return value : 1

function return_val = mwriteWave(f, fs, dcoffset, amplitude, phaseshift, nc)

  % creates the time stamps
  t = 0:1/fs:nc*1/f(1);
  x = 0;

  % adds the signals to create a single signal
  for i=1:numel(f)  
    x = x + (sin(2*pi*f(i)*t) / numel(f));  
  endfor

  % assigns the output file name
  filename = ["mwave_multi_sine.wav"]
  
  % saves the signal as a wave file
  wavwrite(x, fs, filename)

  % assigns return value  
  return_val = 1;

endfunction