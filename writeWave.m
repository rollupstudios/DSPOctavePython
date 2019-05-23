% sine wave generator and saves as a single wave
% vasantha kumar
% 23-May-2019

% Function to generate sinewave and saves as a single wave
% Inputs :  Signal Frequency, Sampling Frequency, DC Offset
%           Amplitude, Phase Shift, No of cycles
% Outputs : generate multi sinewaves and saves as a single wave
% return value : 1

function return_val = writeWave(f, fs, dcoffset, amplitude, phaseshift, nc)

  % creates the time stamps
  t = 0:1/fs:nc*1/f;
  
  % generates the sine signal vector
  x = dcoffset + (amplitude * sin(2*pi*f*t + phaseshift));

  % assigns the output file name
  filename = ["wave_", num2str(f), "_", num2str(fs), ".wav"]
  
  % saves the signal as a wave file
  wavwrite(x, fs, filename)

  % assigns return value
  return_val = 1
  
endfunction