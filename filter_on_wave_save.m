% apply the filter on chosen wave file and save
% vasantha kumar
% 23-May-2019

% Function to apply filtering and save the filtered signal
% Inputs :  input wave file, pass band frequency, stop band frequency,
%           stop band attenuation in dB, filter type, edge frequencies
%           for band pass and band stop filters
% Outputs : Save filtered signal as wave file
% return value : 1

function ret = filter_on_wave_save(wavefilename, fpass, fstop, stopband_attn, filter_type, f1, f2)

  % loads necessary packages
  pkg load communications;
  pkg load signal;

  % reads the input wave file and extract required data
  [x, fs, nbits] = wavread(wavefilename);

  % based on the user given filter type, calculates the filter co-efficients
  switch (filter_type)
    case "low"
      delta_f = fstop-fpass;
      N = stopband_attn * fs/(22*delta_f);    
      
      f =  fpass/(fs/2);
      hc = fir1(round(N)-1, f, filter_type);    
    case "high"
      delta_f = fstop-fpass;
      N = stopband_attn * fs/(22*delta_f);    
      
      f =  fpass/(fs/2);
      hc = fir1(round(N)-1, f, filter_type);      
    case "pass"
      delta_f = f2-f1;
      N = stopband_attn * fs/(22*delta_f);    
      
      fa = f1/(fs/2);
      fb = f2/(fs/2);        
      hc = fir1(round(N)-1, [fa, fb], filter_type);
    case "stop"
      delta_f = f2 - f1;
      N = stopband_attn * fs/(22*delta_f);
      
      fa = f1/(fs/2);
      fb = f2/(fs/2);    
      hc = fir1(round(N)-1, [fa, fb], filter_type);
  endswitch 

  % applies the FCs on chosen wave file
  xf = filter(hc,1,x);
  
  % assigns the output file name
  filename = ["filter_applied_wave.wav"];
  
  % saves the filtered signal as a wave file
  wavwrite(xf, fs, filename);

  % assigns return value  
  ret = 1;

endfunction

