import neuralnetworkQ as nn
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import copy

#plt.ion()

print( '\n------------------------------------------------------------')
print( "Reinforcement Learning Example: Dynamic Marble on a Track")

# Define the problem

def reinforcement(s,s1):
    #goal = 2
    #return 0 if abs(s1[1]-s[1]) < 1 else -1
    return -1 if(s1[2] > s[2]) else 0
      #return 0
    #else: return -1

def initialState():
    #return np.array([4*np.random.random_sample(), 0.0])
    #return np.array([np.random.randint(1,5), 1.0])
    position = np.random.randint(1,5)
    processing = np.random.randint(0,2)
    energy_units = 1
    return np.array([position, processing, energy_units])

def nextState(s,a):
    s = copy.copy(s)   # s[0] is position, s[1] is velocity. a is -1, 0 or 1
    #deltaT = 0.1                           # Euler integration time step
    #s[0] += 1                  # Update position
    #s[1] += 1  # Update velocity. Includes friction
    s[2] = np.random.randint(1,5)
    if (s[1] == 0) :        # Bound next position. If at limits, set velocity to 0.
        s[1] = 1
    elif (s[1] == 1) :
        s[1] = 0
    return s

validActions = (-1,1)

# training Loop
gamma = 0.1
nh = 5
nTrials = 500
nStepsPerTrial = 1000
nSCGIterations = 10
finalEpsilon = 0.01
epsilonDecay = np.exp(np.log(finalEpsilon)/(nTrials)) # to produce this final value

nnet = nn.NeuralNetworkQ(4,nh,1,((0,4), (1,2), (1,5), (-1,1)))
epsilon = 1
epsilonTrace = np.zeros(nTrials)
rtrace = np.zeros(nTrials)
for trial in range(nTrials):
    # Collect nStepsPerRep samples of X, R, Qn, and Q, and update epsilon
    X,R,Qn,Q,epsilon = nnet.makeSamples(initialState,nextState,reinforcement,
                                        validActions,nStepsPerTrial,epsilon)
    # Update the Q neural network.
    nnet.train(X,R,Qn,Q,gamma=gamma, nIterations=nSCGIterations) #  weightPrecision=1e-8, errorPrecision=1e-10)
    epsilon *= epsilonDecay
    # Rest is for plotting
    epsilonTrace[trial] = epsilon
    #rtrace[trial] = np.mean(R)
    rtrace[trial] = np.mean(R)
    #print('Trial',trial,'mean R',np.mean(R))
    print('Trial',trial,'mean R',R[trial])

##  Plotting functions

def plotStatus(net,trial,epsilonTrace,rtrace):
    g=5
    
    g = 5
    qs = net.use(np.array([[s,0,g,a] for a in validActions for s in range(11)]))
    #print np.hstack((qs,-1+np.argmax(qs,axis=1).reshape((-1,1))))
    

    plt.subplot(2,2,1)
    n = 5
    positions = np.linspace(0,5,n)
    velocities = np.linspace(0,4,n)
    #velocities =  np.linspace(-5,5,n)
    xs,ys = np.meshgrid(positions,velocities)
    #states = np.vstack((xs.flat,ys.flat)).T
    #qs = [net.use(np.hstack((states,np.ones((states.shape[0],1))*act))) for act in actions]
    xsflat = xs.flat
    ysflat = ys.flat
    qs = net.use(np.array([[xsflat[i],ysflat[i],g,a] for a in validActions for i in range(len(xsflat))]))
    #qs = np.array(qs).squeeze().T
    qs = qs.reshape((len(validActions),-1)).T
    qsmax = np.max(qs,axis=1).reshape(xs.shape)
    cs = plt.contourf(xs,ys,qsmax)
    plt.colorbar(cs)
    plt.xlabel("$x$")
    plt.ylabel("$\dot{x}$")
    plt.title("Max Q")
    plt.subplot(2,2,2)
    acts = np.array(validActions)[np.argmax(qs,axis=1)].reshape(xs.shape)
    cs = plt.contourf(xs,ys,acts,[-2, -0.5, 0.5, 2])
    plt.colorbar(cs)
    plt.xlabel("$x$")
    plt.ylabel("$\dot{x}$")
    plt.title("Actions")

    s = plt.subplot(2,2,3)
    rect = s.get_position()
    ax = Axes3D(plt.gcf(),rect=rect)
    ax.plot_surface(xs,ys,qsmax,cstride=1,rstride=1,cmap=cm.jet,linewidth=0)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$\dot{x}$")
    #ax.set_zlabel("Max Q")
    plt.title("Max Q")

    s = plt.subplot(2,2,4)
    rect = s.get_position()
    ax = Axes3D(plt.gcf(),rect=rect)
    ax.plot_surface(xs,ys,acts,cstride=1,rstride=1,cmap=cm.jet,linewidth=0)
    ax.set_xlabel("$x$")
    ax.set_ylabel("$\dot{x}$")
    #ax.set_zlabel("Action")
    plt.title("Action")
    plt.savefig('reinforcement.png')
def testIt(Qnet,nTrials,nStepsPerTrial):
    xs = np.linspace(0,5,nTrials)
    plt.subplot(4,3,12)
    g = 5
    for x in xs:
        s = [x,0,g] ## 0 velocity
        xtrace = np.zeros((nStepsPerTrial,3))
        for step in range(nStepsPerTrial):
            a,_ = Qnet.epsilonGreedy(s,validActions,0.0) # epsilon = 0
            s = nextState(s,a)
            xtrace[step,:] = s
        plt.plot(xtrace[:,0],xtrace[:,1])
        plt.xlim(-1,11)
        plt.ylim(-5,5)
        plt.plot([2,2],[-5,5],'--',alpha=0.5,lw=5)
        plt.ylabel('$\dot{x}$')
        plt.xlabel('$x$')
        plt.title('State Trajectories for $\epsilon=0$')



plotStatus(nnet,nTrials,epsilonTrace,rtrace)
#testIt(nnet,10,500)

plt.show()
#plt.savefig('reinforcement.png')
