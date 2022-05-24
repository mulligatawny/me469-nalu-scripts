###############################################################################
# DATA PROBES FOR PERIODIC HILL FLOW AT RE 10595 IN NALUCFD                   #
# Generate probes to average over lines or rings. The output is to be placed  #
# under "solution_options" in the Nalu input file                             #
###############################################################################

import numpy as np

probe = 'line'
num_probes = 96
a = np.linspace(1, num_probes, num_probes)
a = a.astype(int)
x = np.linspace(0.0, 3.14, num_probes)
x = np.round(x,4)

if probe == 'line':
    for i in range(num_probes):
        print('''
        - name: probe''' + str(a[i]) +'''
          from_target_part: SOLID

          line_of_site_specifications:
            - name: probe''' + str(a[i]) +'''
              number_of_points: 1024
              tip_coordinates: [3.0, 0.0,''',x[i],''']
              tail_coordinates: [3.0, 1.0,''',x[i],''']

          output_variables:
            - field_name: velocity_ra_one
              field_size: 3
            - field_name: reynolds_stress
              field_size: 6
            - field_name: resolved_stress
              field_size: 6
            - field_name: sfs_stress
              field_size: 6
        ''')

elif probe == 'ring':
    for i in range(num_probes):
        print('''
        - name:''',a[i],'''
          from_target_part: coflow-HEX

          ring_specifications:

            - name:''',a[i],'''
              number_of_points: 128
              number_of_line_points: 512
              unit_normal: [1.0, 0.0, 0.0]
              origin_coordinates: [''',x[i],''', 0.0, 0.0]
              tip_coordinates: [''',x[i],''', 0.0, 0.0]
              tail_coordinates: [''',x[i],''', 0.265, 0.0]

          output_variables:

            - field_name: mixture_fraction_fa_one
              field_size: 1
            - field_name: velocity_fa_one
              field_size: 3
            - field_name: reynolds_stress_fa_one
              field_size: 6
        ''')
