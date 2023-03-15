function Ex2
 
% Ralliement de points de passage

% fonction d'etat : x etant l'etat et u le vecteur de commande
    

    function xpoint=f(X,U)
        theta=X(3);
        xpoint=[U(1)*cos(theta);U(1)*sin(theta);U(2)];
    end

%% Équation de la trajectoire en ligne droite xr et xd=d(xr)/dt
    function xr=h(t)
        xr=[2*t;2*t];
    end

    function xd = g(t)
        xd = [2;2];
    end

%% Équation de l'erreur e, v=[v1,v2], U=[u,omega]
    function  e = error(P,xr)
        e = [xr(1)-P(1);xr(2)-P(2)];
    end

    function v = control(xd,e,kx,ky)
        v = [xd(1) + kx*e(1);xd(2) + ky*e(2)];
    end
    
    function U = change(lx,X,v)
        M = [cos(X(3)),-lx*sin(X(3));
            sin(X(3)),lx*cos(X(3))];
        U = inv(M)*v;
    end
%% La trajectoire est une droite
clear all;


% x,y,theta (conditions initiales en position x,y et orientation theta)
X=[0;0;0];
% pas de discretisation du temps
dt=0.1;

% Temps final de simulation
Tfinal = 10;

% Le nb des points passes
N = Tfinal/dt + 1;

% La list des vitesses des roues
phi_point = zeros(3,N);

% Une serie de points de passage
pointspassage = zeros(3,N);
% les gains de commande

% Gains de la commande
kx = 0.1;
ky = 0.1;
lx = 0.5;

clf(); 
hold on; axis([-25 25 -25 25]); axis square;

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

    % Calcul du point P et Xr
    P = [X(1)+lx*cos(X(3)),X(2)+lx*sin(X(3))];
    xr = h(t);
    
    % Tracer le chemin de reference
    plot(xr(2),xr(1),'ro');

    % Calcul des parametres d'erreurs
    e = error(P,xr);
    

    % calcul des commandes u et omega
 
    xd = g(t);  
    v = control(xd,e,kx,ky);
    U = change(lx,X,v);
    
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
 
    X = X + f(X,U)*dt;

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

