import numpy as np

class network():
    def __init__(self,inp,out,hid):
        self.hid = hid
        self.out = out
        self.inp = inp

        self.whid = np.random.randn(self.inp, self.hid)
        self.wout = np.random.randn(self.hid, self.out)

        self.bhid = np.zeros((1, self.hid))
        self.bout = np.zeros((1, self.out))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def derivitive(self, x):
        return x * (1 - x)
    
    def predict(self,inp):
        self.rhid = np.dot(inp, self.whid) + self.bhid
        self.rhid = self.sigmoid(self.rhid)

        self.rout = np.dot(self.rhid, self.wout) + self.bout
        self.rout = self.sigmoid(self.rout)

        return self.rout

    def learn(self,inp,expect,rate):
        eout = expect-self.rout
        eout = eout*self.derivitive(self.rout)
        ehid = np.dot(eout, self.wout.T)
        ehid = ehid * self.derivitive(self.rhid)

        self.wout += np.dot(self.rhid.T, eout) * rate
        self.bout += np.sum(eout, axis=0, keepdims=True) * rate
        self.whid += np.dot(inp.T, ehid) * rate
        self.bhid += np.sum(ehid, axis=0, keepdims=True) * rate

    def train(self,input2,correct,cycles,rate):
        for cycle in range(cycles):
            output = self.predict(input2)
            self.learn(input2,correct,rate)
            if cycle % 4000 == 0:
                print(f"Cycle {cycle}")

inputs = np.array([[0, 0, 1, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 1, 1, 0], [1, 0, 1, 1, 0, 0, 0, 1], [1, 0, 1, 1, 1, 0, 0, 1], [1, 0, 1, 0, 0, 1, 1, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 1], [1, 1, 0, 1, 1, 0, 1, 1], [0, 1, 0, 1, 1, 0, 1, 1], [1, 0, 0, 1, 0, 1, 1, 0], [0, 0, 0, 1, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1, 0, 1], [0, 0, 1, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 1, 1, 1, 0, 0, 1, 1], [1, 1, 1, 0, 1, 1, 0, 0], [0, 1, 1, 1, 1, 0, 0, 1], [0, 1, 1, 1, 0, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 1, 1], [0, 1, 0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0, 1, 0], [0, 0, 1, 0, 1, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 1, 1, 1, 1], [1, 0, 0, 1, 0, 1, 1, 1], [1, 1, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 0, 1, 1, 0], [1, 1, 0, 1, 1, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 0], [1, 1, 0, 0, 1, 1, 1, 1], [1, 0, 1, 1, 0, 1, 1, 1], [1, 1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 0, 1, 1, 1], [1, 0, 1, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0, 0, 1], [1, 0, 0, 1, 0, 0, 0, 0], [1, 0, 1, 1, 0, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1, 0], [0, 1, 1, 0, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 0, 0, 1], [1, 0, 1, 1, 0, 1, 1, 1]])
answers = np.array([[0.8], [1], [0.6], [0.6], [0.8], [0.8], [0.8], [0.8], [0.8], [1], [1], [1], [1], [1], [0.6], [0.8], [0.6], [0.6], [0.8], [0.4], [1], [1], [0.2], [1], [0.6], [0.8], [0.8], [0.6], [0.6], [0.8], [1], [1], [1], [0.6], [0.6], [1], [0.6], [0.6], [0.8], [0.8], [1], [0.6], [1], [1], [0.6], [0.2], [1], [1], [1], [0.4]])
net = network(inp=8,hid=2000,out=1)
net.train(inputs,answers,10000,0.1)

userinput = np.array([[0, 0, 0, 0, 0, 0, 1, 1]])
answer = -np.sort(-net.predict(userinput)).copy()
answer2 = net.predict(userinput).copy()
#answer = answer[0,0]
answer = answer[0,0]
'''
answer3 = np.where(answer2==answer)[1][0]+1
print(answer3)
print()
print(net.predict(userinput))

print(net.whid,net.wout,net.bhid,net.bout)'''
print(answer)