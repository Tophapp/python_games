import numpy as np
print("Hi, I Am Kevin 1.0")
print()
words = [".","hi","i","like","not","you","how","do","in","it","if","bob","so","for","apple","eat","are","what","am","the","robot","pie","one","two","three","to","yes","no","some","tim","good","bad","store","house","a","went"]
small = 100
ans = np.array([['.'], ['bob'], ['do'], ['you'], ['like'], ['the'], ['bad'], ['robot'], ['.'], ['if'], ['you'], ['do'], ['like'], ['the'], ['bad'], ['robot'], ['eat'], ['apple'], ['.'], ['hi'], ['apple'], ['pie'], ['for'], ['bob'], ['good']])
que = np.array([['bob'], ['do'], ['you'], ['like'], ['the'], ['bad'], ['robot'], ['.'], ['if'], ['you'], ['do'], ['like'], ['the'], ['bad'], ['robot'], ['eat'], ['apple'], ['.'], ['hi'], ['apple'], ['pie'], ['for'], ['bob'], ['good'], ['.']])

def encode(array):
    newarray = np.array([[1/small]])
    for x in array:
        for g in x:
            if g in words:
                newarray2 = np.concatenate((newarray,np.array([[(words.index(x[0])+1)/small]])),axis=0)
                newarray = newarray2
            else:
                print(f"Kevin Does Not Know This Word: '{x[0]}'")
    newarray2 = np.delete(newarray, [0]) 
    newarray = np.array(np.split(newarray2, np.arange(1, len(newarray2))))
    return newarray

def decode(array):
    newarray = np.array([[""]])
    for x in array:
        newarray2 = np.concatenate((newarray,np.array([[(words[round(x[0]*100-1)])]])),axis=0)
        newarray = newarray2
    newarray2 = np.delete(newarray, [0]) 
    newarray = np.array(np.split(newarray2, np.arange(1, len(newarray2))))
    return newarray

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
            if cycle % 100000 == 0:
                print("Cycle: " + str(cycle))

inputs = encode(que)
answers = encode(ans)
net = network(inp=1,hid=100,out=1)
net.train(inputs,answers,100000,0.1)
print(decode(net.predict(encode(np.array([["hi"]])))))
print(decode(net.predict(net.predict(encode(np.array([["hi"]]))))))
print(decode(net.predict(net.predict(net.predict(encode(np.array([["hi"]])))))))
