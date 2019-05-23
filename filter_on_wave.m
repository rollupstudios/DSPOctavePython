% apply the filter on chosen wave file and plot
% vasantha kumar
% 23-May-2019

% Function to apply filtering and plot the filtered signal
% Inputs :  input wave file, pass band frequency, stop band frequency,
%           stop band attenuation in dB, filter type, edge frequencies
%           for band pass and band stop filters
% Outputs : Plots the filtered signal
% return value : 1

function ret = filter_on_wave(wavefilename, fpass, fstop, stopband_attn, filter_type, f1, f2)

  % loads necessary packages
  pkg load communications;
  pkg load signal;

  % reads the input wave file and extract required data
  [x, fs, nbits] = wavread(wavefilename);
  dt = 1/fs;
  t = 0:dt:(length(x)*dt)-dt;

  % plotting the signal in time domain
  ax(1) = subplot (321);
  set (ax(1), "tag", "1");
  plot(t,x);
  title (["Signal Time Domain plot with fs = ", num2str(fs)]);
  xlabel "Time(s)";
  ylabel "Amplitude";
  
  % calculates the spectrum of the signal
  N = 1024;
  X = fft(x, N);
  Px = X .* conj(X) / (N * length(x));
  fvalsx = fs * (0:1:N/2-1) / N;

  % plotting the signal in frequency domain
  ax(2) = subplot (322);
  set (ax(2), "tag", "2");
  plot(fvalsx, Px(1:N/2));
  title (["Signal Frequency Domain plot with fs = ", num2str(fs)]);
  xlabel "Frequency(Hz)";
  ylabel "PSD";  
  
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
  ax(3) = subplot (323);
  set (ax(3), "tag", "3");
  plot((-0.5:1/4096:0.5-1/4096)*fs,20*log10(abs(fftshift(fft(hc,4096)))));
  axis([0 fs/2 -60 20]);
  title('Filter Frequency Response');
  grid on;
  
  % applies the FCs on chosen wave file
  xf = filter(hc,1,x);
  
  % plotting the signal in time domain
  ax(5) = subplot (325);
  set (ax(5), "tag", "5");
  plot(t, xf);
  title('Filtered Signal');
  xlabel "Time (s)";
  ylabel "Amplitude"; 
  

  % calculates the spectrum of the filtered signal
  N = 1024;
  XF = fft(xf, N);
  Px = XF .* conj(XF) / (N * length(xf));
  fvalsxf = fs * (0:1:N/2-1) / N;

  % plotting the signal in frequency domain
  ax(6) = subplot (326);
  set (ax(6), "tag", "6");
  plot(fvalsxf, Px(1:N/2));
  title (["Filtered Signal Frequency Domain plot with fs = ", num2str(fs)]);
  xlabel "Frequency(Hz)";
  ylabel "PSD";  
  
  % assigns return value
  ret = 1;

endfunction

