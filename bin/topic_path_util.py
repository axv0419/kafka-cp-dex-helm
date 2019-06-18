import sys

topic_names = sys.argv[1].split(',')
allow_topic_list = 'true' in  sys.argv[2]
topic_paths=  [f'/topics/{topic}\$' for topic in topic_names]
topic_paths += ['/\$']
if allow_topic_list:
        topic_paths += ['/topics\$']
print (''.join(['{', ','.join(topic_paths),'}']))

