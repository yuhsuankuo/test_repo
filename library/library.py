#python 2.7
#by Beryl Yu-Hsuan Kuo
#camera transmission curve & QE curve library


import numpy as np
import matplotlib.pyplot as plt

a = np.load('10D.npz')
b = np.load('20D.npz')
c = np.load('filterforcanon.npz')
d = np.load('ICR650.npz')
e = np.load('ACS.npz')
f = np.load('CAT-C.npz')
g = np.load('Hubble.npz')
h = np.load('LBL.npz')
i = np.load('MAT.npz')
j = np.load('MIT-LL.npz')

name = input('\n\n\n-----CAMERA TRANSMISSION CURVE-----\n1=10D\n2=20D\n3=filterforcanon\n4=ICR650\n-----QE CURVE-----\n5=ACS\n6=CAT-C\n7=Hubble\n8=LBL\n9=MAT\n10=MIT-LL\ntype:')

print('\n\n')


if name == 1:
    print 'name = 10D','\n\nwavelength =\n',a['x'],'\n\npercent transmittance =\n',a['y'],'\n\n'
    plt.plot(a['x'],a['y'],'g')
    plt.xlabel('Wavelengh (nm)')
    plt.ylabel('Transmittance (%)')
    plt.title('10D')
    plt.grid(True)
    plt.show()


if name == 2:
    print 'name = 20D','\n\nwavelength =\n',b['x'],'\n\npercent transmittance =\n',b['y'],'\n\n'
    plt.plot(b['x'],b['y'],'g')
    plt.xlabel('Wavelengh (nm)')
    plt.ylabel('Transmittance (%)')
    plt.title('20D')
    plt.grid(True)
    plt.show()


if name == 3:
    print 'name = filter for Canon','\n\nwavelength =\n',c['x'],'\n\npercent transmittance =\n',c['y'],'\n\n'
    plt.plot(c['x'],c['y'],'g')
    plt.xlabel('Wavelengh (nm)')
    plt.ylabel('Transmittance (%)')
    plt.title('filter for Canon')
    plt.grid(True)
    plt.show()


if name == 4:
    print 'name = ICR650','\n\nwavelength =\n',d['x'],'\n\npercent transmittance =\n',d['y'],'\n\n'
    plt.plot(d['x'],d['y'],'g')
    plt.xlabel('Wavelengh (nm)')
    plt.ylabel('Transmittance (%)')
    plt.title('ICR650')
    plt.grid(True)
    plt.show()


if name == 5:
    print 'name = ACS','\n\nwavelength =\n',e['x'],'\n\nquantum efficiency =\n',e['y'],'\n\n'
    plt.plot(e['x'],e['y'],'g')
    plt.xlabel('Wavelengh (nm)')
    plt.ylabel('QE (%)')
    plt.title('ACS')
    plt.grid(True)
    plt.show()


if name == 6:
    print 'name = CAT-C','\n\nwavelength =\n',f['x'],'\n\nquantum efficiency =\n',f['y'],'\n\n'
    plt.plot(f['x'],f['y'],'g')
    plt.xlabel('Wavelengh (nm)')
    plt.ylabel('QE (%)')
    plt.title('CAT-C')
    plt.grid(True)
    plt.show()


if name == 7:
    print 'name = Hubble','\n\nwavelength =\n',g['x'],'\n\nquantum efficiency =\n',g['y'],'\n\n'
    plt.plot(g['x'],g['y'],'g')
    plt.xlabel('Wavelengh (nm)')
    plt.ylabel('QE (%)')
    plt.title('Hubble')
    plt.grid(True)
    plt.show()


if name == 8:
    print 'name = LBL','\n\nwavelength =\n',h['x'],'\n\nquantum efficiency =\n',h['y'],'\n\n'
    plt.plot(h['x'],h['y'],'g')
    plt.xlabel('Wavelengh (nm)')
    plt.ylabel('QE (%)')
    plt.title('LBL')
    plt.grid(True)
    plt.show()


if name == 9:
    print 'name = MAT','\n\nwavelength =\n',i['x'],'\n\nquantum efficiency =\n',i['y'],'\n\n'
    plt.plot(i['x'],i['y'],'g')
    plt.xlabel('Wavelengh (nm)')
    plt.ylabel('QE (%)')
    plt.title('MAT')
    plt.grid(True)
    plt.show()


if name == 10:
    print 'name = MIT-LL','\n\nwavelength =\n',j['x'],'\n\nquantum efficiency =\n',j['y'],'\n\n'
    plt.plot(j['x'],j['y'],'g')
    plt.xlabel('Wavelengh (nm)')
    plt.ylabel('QE (%)')
    plt.title('MIT-LL')
    plt.grid(True)
    plt.show()


if name >= 11:
    print '\n\n----------no data----------\n\n'
