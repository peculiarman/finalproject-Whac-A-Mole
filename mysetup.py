# mysetup.py
from distutils.core import setup
import py2exe
 
setup(console=["C:\Users\Etfl\Desktop\homework\main.py"],
      data_files=[("gif",
                   ['C:\Users\Etfl\Desktop\homework\gif\mice_1.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\mice_2.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\mice_3.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\mice_1_x.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\mice_2_x.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\mice_3_x.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\mouse_1.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\mouse_2.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\mouse_3.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\mouse_1_x.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\mouse_2_x.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\mouse_3_x.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\mm_1.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\mm_2.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\mm_3.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\mm_1_x.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\mm_2_x.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\mm_3_x.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\\nomouse.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\\bg.gif',
                    'C:\Users\Etfl\Desktop\homework\gif\\help.gif'])])
