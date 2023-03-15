function trace_robot(x,couleur,taille) 
   if (exist('taille')==0), taille=1; end;
   
   % suivie de points derivant la geometrie du robot exprime dans le
   % repere du robot
    
   M = taille*...
      [  1 -1  0  0 -1 -1 0 0 -1 1 0 0 3    3    0; 
	    -2 -2 -2 -1 -1  1 1 2  2 2 2 1 0.5 -0.5 -1]; 
    
   % en coordonnes homogenes
    M=[M;ones(1,length(M))]; 
      
   % Transformation homogene
    TH=[cos(x(3)),-sin(x(3)),x(1);...
        sin(x(3)),cos(x(3)),x(2);...
        0 0 1];
    
   % coordonnes des points dans le repere sol
   M =TH*M;
   
   %trace robot
   plot(M(1,:),M(2,:),couleur,'LineWidth',2);       
end

