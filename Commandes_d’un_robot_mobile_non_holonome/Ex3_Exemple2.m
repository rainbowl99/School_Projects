function Ex3_2
 
% Ralliement de points de passage

% fonction d'etat : x etant l'etat et u le vecteur de commande
   
    function xpoint=f(x,u)
        theta=x(3);
        xpoint=[u(1)*cos(theta);u(1)*sin(theta);u(2)];
    end
%
    function y = g(x,a,b,c)
        y = -a/b * x - c/b;
    end


%%
clear all;

% x,y,theta (conditions initiales en position x,y et orientation theta)
X = [2;5;-pi/2];  

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
k = 0.1;

% lx
lx = 0.1;

% vitessse u
u = 1;

% Les parametres d'equation
a = 1;
b = 2;
c = 1;
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
    
    drawnow();
    
%     pause(0.1);

    theta0 = atan(-a/b);
    theta_e = X(3) - theta0;

    %Tracer le chemin de reference
    s = u*t;
    Xr = [s*sin(theta0);-c/b+s*cos(theta0)];
    plot(Xr(2),Xr(1),'ro');

    % Calcul des parametres d'erreurs
    P = [X(1)+lx*cos(X(3)),X(2)+lx*sin(X(3))];
    d = abs(a*P(1) + b*P(2) + c) / sqrt(a^2 + b^2);
    
    
    
    % calcul des commandes u et omega
    
    omega = -1*u*sin(theta_e)/(lx * cos(theta_e)) - u*k*d; 
    U(1) = u;
    U(2) = omega;
    
    %positions enregistres
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




end

