#this will delete all words 3 letters or shorter
def remove_small(list):
    new_list = []
    for i in list:
        if (len(i) > 3):
            new_list.append(i)
    return new_list

rName = input('Enter the resume file name: ')

#below is a failsafe incase the file is not saved properly
try:
    rHand = open(rName)
except:
    print('File cannot be opened:', rName)
    exit();

jName = input('Enter the job file name: ')

#below is a failsafe incase the file is not saved properly
try:
    jHand = open(jName)
except:
    print('File cannot be opened:', jName)
    exit();


#below code compiles an array of words from job post and deletes duplicates
job_list = []
for line in jHand:
    words = line.split()
    for word in words:
        if word in job_list:
            continue
        job_list.append(word)

#below code compiles an array of words from resume and deletes duplicates
resume_list = []
for line in rHand:
    words = line.split()
    for word in words:
        if word in resume_list:
            continue
        resume_list.append(word)
#this code uses set and intersection to create a unique list of the two lists
list_matches = set(resume_list).intersection(job_list)

#this passes the unique list to function remove_small
new_list = remove_small(list_matches)
print(new_list)
#prints number of matches between job post and resume
print(len(new_list))
