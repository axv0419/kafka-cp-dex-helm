import sys

san_names = sys.argv[1].split(',')
domain_suffix = sys.argv[2]
san_list= [f'{subject_alternate_name}.{domain_suffix}' for subject_alternate_name in san_names]
print (''.join(['{', ','.join(san_list),'}']))

