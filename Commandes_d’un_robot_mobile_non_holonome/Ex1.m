function Ex1
 
% Ralliement de points de passage

% fonction d'etat : x etant l'etat et u le vecteur de commande
   
    function xpoint=f(x,u)
        theta=x(3);
        xpoint=[u(1)*cos(theta);u(1)*sin(theta);u(2)];
    end


clear all;

% point but final et orientation final desiree
D=[25;6]; betad=0;

% x,y,theta (conditions initiales en position x,y et orientation theta)
X=[-20;-10;-pi/2];  

% pas de discretisation du temps
dt=0.1;

% Temps final de simulation
Tfinal = 20;

% Le nb des points passes
N = Tfinal/dt + 1;

% La list des vitesses des roues
phi_point = zeros(3,N);

% Une serie de points de passage
pointspassage = zeros(3,N);
% les gains de commande
krho = 1;
kalpha= 5;
kbeta= -10;

% decommenter ces deux lignes si vous voulez superposer les poses du robot

clf(); 
hold on; axis([-30 30 -30 30]); axis square;

ite = 0;
for t=0:dt:Tfinal

    % commenter ces deux lignes si vous voulez superposer les poses du
    % robot
%     clf(); 
%     hold on; axis([-30 30 -30 30]); axis square;
    
    % La serie de points de passage dans lesquels des angles
%     pointspassage(:,(t+dt)/dt) = X(1:2)

    % d'orientation desires sont associees.
    

    % Tracer la nouvelle position du robot
    trace_robot(X,'blue'); 
    
    % Tracer la pose finale desiree du robot
    plot(D(1),D(2),'ro'); 
    
    drawnow();
    
    %pause(0.1);

    % Calcul des parametres d'erreurs
    rho = sqrt((D(1)-X(1))^2 + (D(2)-X(2))^2);
    beta= atan2(D(2)-X(2),D(1)-X(1));
    alpha=beta-X(3);
   

    % arret de la boucle si le point D est atteint
    if (rho < 0.1) break; end
    
    % calcul des commandes u et omega
    
    U(1)=krho*rho;
    U(2)=kalpha*alpha+kbeta*(betad-beta);  

    % positions enregistres
    ite = ite + 1;
    pointspassage(:,ite) = X;

    % Calcul des vitesses des roues
    r = 0.4;
    w = 1;
    phi_point(1,ite) = t;
    phi_p = 1/r * [1 w;1 -w] * [U(1);U(2)];
    phi_point(2,ite) = phi_p(1);
    phi_point(3,ite) = phi_p(2);

    %integrer l'equation d'etat (determiner le nouveau etat) par un simple
    %schema d'Euler explicite 
    
    X=X+f(X,U)*dt;
    

end

phi_point = phi_point(:,1:ite);
figure(2)
plot(phi_point(1,:),phi_point(2,:),'LineWidth',1.5)
hold on
plot(phi_point(1,:),phi_point(3,:),'LineWidth',1.5)
xlabel('temps') 
ylabel('vitesses des roues') 
legend({'roue droite','roue gauche'},'Location','northeast')



% Quelque exemples de parcours
Pointsdesires = [0 10 25 ; 0 -10 12 ]; betad_P = 0;X=[-20;-10;-pi/2];
for i = 1:3 
    P = Pointsdesires(:,i);
    figure(3)
%     clf(); 
    hold on; axis([-30 30 -30 30]); axis square;
    for t=0:dt:Tfinal

    % commenter ces deux lignes si vous voulez superposer les poses du
    % robot
%     clf(); 
%     hold on; axis([-30 30 -30 30]); axis square;
    
    % La serie de points de passage dans lesquels des angles
%     pointspassage(:,(t+dt)/dt) = X(1:2)

    % d'orientation desires sont associees.
    

    % Tracer la nouvelle position du robot
    trace_robot(X,'blue'); 
    
    % Tracer la pose finale desiree du robot
    plot(P(1),P(2),'ro'); 

    drawnow();
    
    %pause(0.1);

    % Calcul des parametres d'erreurs
    rho = sqrt((P(1)-X(1))^2 + (P(2)-X(2))^2);
    beta= atan2(P(2)-X(2),P(1)-X(1));
    alpha=beta-X(3);
   

    % arret de la boucle si le point D est atteint
    if (rho < 0.1) break; end
    
    % calcul des commandes u et omega
    U(1)=krho*rho;
    U(2)=kalpha*alpha+kbeta*(betad_P-beta);   

    %integrer l'equation d'etat (determiner le nouveau etat) par un simple
    %schema d'Euler explicite 
    
    X=X+f(X,U)*dt;
    end
end
end

