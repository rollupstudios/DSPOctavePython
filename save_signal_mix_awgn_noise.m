% applies a awgn noise on chosen wave file and save
% vasantha kumar
% 23-May-2019

% Function to apply a awgn noise on chosen wave file and save
% Inputs :  input wave file,SNR in dB
% Outputs : Save noise added signal as wave file
% return value : 1

function return_val = save_signal_mix_awgn_noise(wavefilename, snr)

  % loads necessary package
  pkg load communications;
  
  % reads the input wave file and extract required data
  [x, fs, nbits] = wavread(wavefilename);
  dt = 1/fs;
  t = 0:dt:(length(x)*dt)-dt;
 
  % applies noise on signal
  y = awgn(x, snr);  

  % assigns the output file name
  filename = ["awgn_mixed_wave.wav"]
  
  % saves the filtered signal as a wave file
  wavwrite(y, fs, filename);
  
  % assigns return value  
  return_val = 1;
  
endfunction