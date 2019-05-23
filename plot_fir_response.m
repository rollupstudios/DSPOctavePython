% finds filter coefficients and plots the frequency response
% vasantha kumar
% 23-May-2019

% Function to apply filtering and plot the filtered signal
% Inputs :  pass band frequency, stop band frequency,
%           stop band attenuation in dB, filter type, edge frequencies
%           for band pass and band stop filters
% Outputs : Plots the frequnecy response
% return value : 1

function return_val = plot_fir_response(fpass, fstop, fs, stopband_attn, filter_type, f1, f2)

  % loads necessary packages
  pkg load signal;
  pkg load communications;

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
  
  % plotting the frequency response of the filter
  plot((-0.5:1/4096:0.5-1/4096)*fs,20*log10(abs(fftshift(fft(hc,4096)))));
  axis([0 fs/2 -60 20])
  title('Filter Frequency Response')
  grid on

  % assigns return value
  return_val = 1;
  
endfunction

